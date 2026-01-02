import math
import matplotlib.pyplot as plt

class SimulacaoFuelCell:
    """
    Simulação Eletroquímica de uma Célula a Combustível PEM de 50W,
    considerando perdas ambientais, pressões de gás e cargas parasitas.
    """
    def __init__(self):
        # --- Constantes Físicas ---
        self.R = 8.314  # Constante dos Gases Ideais [J/(mol.K)]
        self.F = 96485  # Constante de Faraday [C/mol]
        
        # --- Parâmetros do Usuário/Ambiente ---
        self.temp_amb_c = 25
        # Temperatura de Operação do Stack (Crucial para a eficiência)
        self.temp_stack_k = 273.15 + 55  # ~55°C é um valor comum para PEMFC
        self.temp_amb_k = 273.15 + self.temp_amb_c
        self.umidade_relativa = 0.70  # 70%
        self.pressao_atm = 101325  # Pressão atmosférica padrão [Pa]
        
        # --- Parâmetros do Tanque ---
        self.vol_tanque = 0.007  # 7 Litros em [m3]
        self.pressao_tanque_bar = 300
        self.pressao_regulada_bar = 0.6  # Pressão de entrada no anodo [bar]
        
        # --- Parâmetros do Stack (Estimativa) ---
        self.num_celulas = 18    # Células em série (para operar em ~12V)
        self.area_ativa = 15.0   # Área da célula [cm2]
        
        # Cargas Parasitas (2 Ventoinhas @ 12V, 0.12A cada)
        self.potencia_ventoinhas = 2 * (12.0 * 0.12) # ~2.88 Watts
        
        # --- Listas para Plotagem ---
        self.correntes = []
        self.tensoes = []
        self.potencias_liq = []
        
    def calcular_massa_h2(self):
        """
        Calcula a massa de H2 no tanque considerando o Fator de Compressibilidade Z
        para altas pressões (gás real).
        """
        # Z aproximado para H2 a 300 bar e 298K
        z_factor = 1.18 
        pressure_pa = self.pressao_tanque_bar * 100000
        
        # n = PV / (ZRT)
        mols = (pressure_pa * self.vol_tanque) / (z_factor * self.R * self.temp_amb_k)
        
        massa_molar_h2 = 2.016  # g/mol
        massa_total_g = mols * massa_molar_h2
        return massa_total_g

    def pressao_parcial_oxigenio(self):
        """
        Calcula a pressão parcial de O2 na entrada do Stack, descontando o vapor d'água.
        """
        # Pressão de saturação do vapor a 25C (Equação de Tetens simplificada)
        p_sat = 0.61078 * math.exp((17.27 * self.temp_amb_c) / (self.temp_amb_c + 237.3)) * 1000 # Em Pa
        
        p_vapor = self.umidade_relativa * p_sat
        p_ar_seco = self.pressao_atm - p_vapor
        
        # Ar é 21% Oxigênio
        p_o2 = 0.21 * p_ar_seco
        return p_o2

    def modelo_polarizacao(self, corrente_a):
        """
        Simula a tensão do Stack (VxI) considerando as três perdas principais:
        Ativação, Ôhmica e Concentração.
        """
        if corrente_a <= 0:
            return self.num_celulas * 0.96, 0.0

        densidade_corrente = corrente_a / self.area_ativa # A/cm2

        # 1. Tensão de Nernst (Teórica)
        e_nernst = 1.229 - (0.85e-3 * (self.temp_stack_k - 298.15))
        
        # 2. Perdas de Ativação (Tafel) - Perda logarítmica inicial
        # Parâmetro ajustado para 55°C
        v_act = 0.055 * math.log(densidade_corrente * 1000) if densidade_corrente > 0.001 else 0
        
        # 3. Perdas Ôhmicas - Perda linear (resistência interna da membrana)
        resistencia_interna = 0.25 # ohm.cm2 (valor típico)
        v_ohm = densidade_corrente * resistencia_interna
        
        # 4. Perdas de Concentração - Perda acentuada em alta carga
        v_conc = 0.0
        # A perda de concentração é mais sensível à densidade de corrente:
        if densidade_corrente > 0.6:
            v_conc = 0.05 * math.exp(3 * (densidade_corrente - 0.6))

        v_celula = e_nernst - v_act - v_ohm - v_conc
        
        v_stack = self.num_celulas * v_celula
        
        # Potência Bruta
        potencia_bruta = v_stack * corrente_a
        
        # Carga parasita só existe se houver eletricidade gerada
        carga_parasita = self.potencia_ventoinhas if corrente_a > 0.5 else 0
        potencia_liquida = potencia_bruta - carga_parasita
        
        return max(0, v_stack), max(0, potencia_liquida)

    def plotar_curvas(self):
        """
        Gera o gráfico de Polarização (VxI) e Potência (PxI) usando Matplotlib.
        """
        if not self.correntes:
            print("Nenhum dado para plotar. Execute a simulação primeiro.")
            return

        fig, ax1 = plt.subplots(figsize=(10, 6))

        # --- Plotagem da Curva de Polarização (VxI) no Eixo Esquerdo ---
        color = 'tab:blue'
        ax1.set_xlabel('Corrente (I) [A]')
        ax1.set_ylabel('Tensão (V) [V]', color=color)
        ax1.plot(self.correntes, self.tensoes, color=color, label='Tensão do Stack (V)')
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.grid(True, linestyle='--', alpha=0.6)
        
        # Adicionar o Ponto Nominal e Máximo na curva VxI
        v_max = max(self.tensoes)
        i_vmax = self.correntes[self.tensoes.index(v_max)]
        
        # --- Plotagem da Curva de Potência (PxI) no Eixo Direito ---
        ax2 = ax1.twinx()  
        color = 'tab:red'
        ax2.set_ylabel('Potência Líquida (P) [W]', color=color)  
        ax2.plot(self.correntes, self.potencias_liq, color=color, linestyle='-', label='Potência Líquida (W)')
        ax2.tick_params(axis='y', labelcolor=color)
        
        # Encontrar e marcar o Ponto de Máxima Potência (MPP)
        p_max = max(self.potencias_liq)
        i_mpp = self.correntes[self.potencias_liq.index(p_max)]
        v_mpp = self.tensoes[self.potencias_liq.index(p_max)]
        
        # Marcar o MPP
        ax2.plot(i_mpp, p_max, 'go', markersize=8, label=f'MPP ({p_max:.1f}W @ {i_mpp:.1f}A)')
        
        # Linhas de referência para o MPP
        ax1.axvline(x=i_mpp, color='gray', linestyle=':', linewidth=1)
        ax1.axhline(y=v_mpp, color='gray', linestyle=':', linewidth=1)
        ax2.axhline(y=p_max, color='gray', linestyle=':', linewidth=1)
        
        # Título e Legendas
        plt.title('Curvas de Polarização e Potência do Stack de 50W (18 Células)')
        fig.tight_layout()  # Ajusta o layout para não cortar rótulos
        
        # Adicionar legendas de ambos os eixos
        handles, labels = ax1.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(handles + handles2, labels + labels2, loc='lower left')
        
        plt.show()

    def executar(self):
        massa_h2 = self.calcular_massa_h2()
        
        print(f"--- Configuração Inicial ---")
        print(f"Tanque Tipo IV 7L @ 300 bar")
        print(f"Massa estimada de H2: {massa_h2:.2f} g")
        print(f"Umidade Relativa: {self.umidade_relativa*100}% | Temp: {self.temp_amb_c}°C")
        print(f"Carga Parasita (Ventoinhas): {self.potencia_ventoinhas:.2f} W")
        print("-" * 30)

        # Variável para rastrear o ponto nominal e o ponto máximo
        melhor_ponto_max = {'p': 0, 'v': 0, 'i': 0}
        ponto_nominal = {'p': 0, 'v': 0, 'i': 0} 
        
        # Varrer a corrente para gerar a curva
        step = 0.05
        current_scan = step
        while current_scan < 10.0: # Limite de 10A é seguro para um Stack de 50W
            volts, pot_liq = self.modelo_polarizacao(current_scan)
            
            # Critério de parada: Tensão por célula muito baixa (queda crítica)
            v_por_celula = volts / self.num_celulas
            if v_por_celula < 0.5:
                break
                
            self.correntes.append(current_scan)
            self.tensoes.append(volts)
            self.potencias_liq.append(pot_liq)
            
            # Rastrear Máximo
            if pot_liq > melhor_ponto_max['p']:
                melhor_ponto_max = {'p': pot_liq, 'v': volts, 'i': current_scan}
            
            # Rastrear Nominal (ponto mais próximo de 50W)
            if abs(pot_liq - 50.0) < abs(ponto_nominal['p'] - 50.0):
                ponto_nominal = {'p': pot_liq, 'v': volts, 'i': current_scan}
                
            current_scan += step

        # --- Impressão dos Resultados Finais ---
        print(f"\n--- Resultados da Simulação ---")
        
        print(f"\n[PONTO MÁXIMO (Pico Suportável - MPP)]")
        print(f"Potência Líquida Máxima: {melhor_ponto_max['p']:.2f} W")
        print(f"Tensão no Stack (Vmax):  {melhor_ponto_max['v']:.2f} V")
        print(f"Corrente Máxima (Imax):  {melhor_ponto_max['i']:.2f} A")

        print(f"\n[PONTO NOMINAL (Operação 50W)]")
        print(f"Potência Líquida: {ponto_nominal['p']:.2f} W")
        print(f"Tensão no Stack:  {ponto_nominal['v']:.2f} V")
        print(f"Corrente:         {ponto_nominal['i']:.2f} A")
        
        # Cálculo de Autonomia no regime Nominal
        energia_total_wh = massa_h2 * 33.3 # Energia específica H2 teórico
        energia_eletrica_disponivel = energia_total_wh * 0.5 # Assumindo 50% de eficiência
        
        tempo_horas = energia_eletrica_disponivel / ponto_nominal['p'] if ponto_nominal['p'] > 0 else 0
        
        print(f"\n--- Autonomia Estimada ---")
        print(f"Com carga constante no Ponto Nominal ({ponto_nominal['p']:.1f}W):")
        print(f"Tempo de uso: {tempo_horas:.1f} horas (aproximadamente)")
        
        # --- Geração do Gráfico ---
        self.plotar_curvas()

if __name__ == "__main__":
    # Certifique-se de que a variável global '__app_id' não está definida antes de rodar localmente
    # Este 'try-except' é apenas uma sugestão, mas o código acima é suficiente para VS Code.
    try:
        sim = SimulacaoFuelCell()
        sim.executar()
    except Exception as e:
        print(f"Ocorreu um erro durante a execução: {e}")