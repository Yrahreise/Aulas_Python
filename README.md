# 🐍 Aulas de Python

Repositório com scripts das aulas de Python. Cada arquivo `aulaX.py` contém exemplos e exercícios do curso, cobrindo fundamentos da linguagem.

## Estrutura
- `aula001.py` ... `aula032.py`: Exemplos progressivos.
- `.gitignore`: Arquivos e pastas ignorados no controle de versão.

## Índice das Aulas
- [Aula 001](./aula001.py)
- [Aula 002](./aula002.py)
- [Aula 003](./aula003.py)
- [Aula 004](./aula004.py)
- [Aula 005](./aula005.py)
- [Aula 006](./aula006.py)
- [Aula 007](./aula007.py)
- [Aula 008](./aula008.py)
- [Aula 009](./aula009.py)
- [Aula 010](./aula010.py)
- [Aula 011](./aula011.py)
- [Aula 012](./aula012.py)
- [Aula 013](./aula013.py)
- [Aula 014](./aula014.py)
- [Aula 015](./aula015.py)
- [Aula 016](./aula016.py)
- [Aula 017](./aula017.py)
- [Aula 018](./aula018.py)
- [Aula 019](./aula019.py)
- [Aula 020](./aula020.py)
- [Aula 021](./aula021.py)
- [Aula 022](./aula022.py)
- [Aula 023](./aula023.py)
- [Aula 024](./aula024.py)
- [Aula 025](./aula025.py)
- [Aula 026](./aula026.py)
- [Aula 027](./aula027.py)
- [Aula 028](./aula028.py)
- [Aula 029](./aula029.py)
- [Aula 030](./aula030.py)
- [Aula 031](./aula031.py)
- [Aula 032](./aula032.py)

## Como executar
No PowerShell dentro da pasta do projeto:

```pwsh
python aula001.py
```

Substitua `aula001.py` pelo arquivo da aula desejada.

## 📁 Estrutura do Repositório

```
Aulas_Python/
├── aula001.py
├── aula002.py
├── ...
├── aula032.py
├── auto_sync.py
├── README.md
└── .gitignore
```

## 🔄 Auto-sync com Git (opcional)

O arquivo `auto_sync.py` observa mudanças em arquivos `aula*.py` e sincroniza automaticamente com o GitHub:

- Quando ficar sem alterações por alguns segundos, faz `git add` + `commit` e tenta `git push`.
- Se estiver offline, o commit é feito localmente; quando a conexão voltar, ele tenta enviar periodicamente.

Como iniciar pelo VS Code:
1. Abra o menu "Terminal" > "Run Task…"
2. Escolha "Auto Sync: Git aulas". Isso abrirá um terminal rodando em background.
3. Para parar, feche o terminal desta tarefa ou pressione `Ctrl+C` nele.

Ajustes rápidos (opcionais):
- No arquivo `.vscode/tasks.json`, você pode alterar variáveis de ambiente:
	- `QUIET_SECONDS` (padrão 30): tempo de inatividade antes de commitar.
	- `CHECK_INTERVAL` (padrão 2): frequência de verificação.
	- `PUSH_POLL_SECONDS` (padrão 60): frequência de tentativas de push pendentes.

Observação: o script só considera arquivos que começam com `aula` e terminam com `.py`.
