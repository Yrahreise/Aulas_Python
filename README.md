# 🐍 Aulas de Python

Repositório contendo scripts progressivos das aulas de Python, cobrindo desde fundamentos até conceitos avançados.

## 📚 Índice das Aulas

| Aula | Link |
|------|------|
| Aula 001 | [aula001.py](./aula001.py) |
| Aula 002 | [aula002.py](./aula002.py) |
| Aula 003 | [aula003.py](./aula003.py) |
| Aula 004 | [aula004.py](./aula004.py) |
| Aula 005 | [aula005.py](./aula005.py) |
| Aula 006 | [aula006.py](./aula006.py) |
| Aula 007 | [aula007.py](./aula007.py) |
| Aula 008 | [aula008.py](./aula008.py) |
| Aula 009 | [aula009.py](./aula009.py) |
| Aula 010 | [aula010.py](./aula010.py) |
| Aula 011 | [aula011.py](./aula011.py) |
| Aula 012 | [aula012.py](./aula012.py) |
| Aula 013 | [aula013.py](./aula013.py) |
| Aula 014 | [aula014.py](./aula014.py) |
| Aula 015 | [aula015.py](./aula015.py) |
| Aula 016 | [aula016.py](./aula016.py) |
| Aula 017 | [aula017.py](./aula017.py) |
| Aula 018 | [aula018.py](./aula018.py) |
| Aula 019 | [aula019.py](./aula019.py) |
| Aula 020 | [aula020.py](./aula020.py) |
| Aula 021 | [aula021.py](./aula021.py) |
| Aula 022 | [aula022.py](./aula022.py) |
| Aula 023 | [aula023.py](./aula023.py) |
| Aula 024 | [aula024.py](./aula024.py) |
| Aula 025 | [aula025.py](./aula025.py) |
| Aula 026 | [aula026.py](./aula026.py) |
| Aula 027 | [aula027.py](./aula027.py) |
| Aula 028 | [aula028.py](./aula028.py) |
| Aula 029 | [aula029.py](./aula029.py) |
| Aula 030 | [aula030.py](./aula030.py) |
| Aula 031 | [aula031.py](./aula031.py) |
| Aula 032 | [aula032.py](./aula032.py) |

## 🚀 Como Executar

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

Para usar:
```pwsh
python auto_sync.py
```

Variáveis de ambiente opcionais:
- `QUIET_SECONDS` (padrão 20): tempo de inatividade antes de commitar
- `CHECK_INTERVAL` (padrão 2): frequência de verificação
- `PUSH_POLL_SECONDS` (padrão 60): frequência de tentativas de push pendentes

## 👨‍💻 Autor

Hary Fernando Herdt
