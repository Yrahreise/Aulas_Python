import os
import subprocess
import sys
import time
from datetime import datetime


"""
Auto Sync para repositório Git

Funciona assim:
- Observa mudanças em arquivos aula*.py neste diretório.
- Quando não há alterações por QUIET_SECONDS, faz git add/commit e tenta git push.
- Se estiver sem internet ou remoto indisponível, mantém apenas o commit local e tenta novamente na próxima alteração.

Personalização via variáveis (opcional):
- QUIET_SECONDS: segundos de inatividade antes do commit (default 20)
- CHECK_INTERVAL: intervalo de verificação em segundos (default 2)
"""


WATCH_DIR = os.path.abspath(os.path.dirname(__file__))
FILE_PREFIX = "aula"
FILE_SUFFIX = ".py"
QUIET_SECONDS = int(os.getenv("QUIET_SECONDS", "20"))
CHECK_INTERVAL = float(os.getenv("CHECK_INTERVAL", "2"))
PUSH_POLL_SECONDS = int(os.getenv("PUSH_POLL_SECONDS", "60"))


def run(cmd, cwd=None, check=False, capture=True):
    if isinstance(cmd, str):
        shell = True
    else:
        shell = False
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd or WATCH_DIR,
            shell=shell,
            check=check,
            stdout=subprocess.PIPE if capture else None,
            stderr=subprocess.STDOUT if capture else None,
            text=True,
        )
        return result.returncode, (result.stdout or "").strip()
    except subprocess.CalledProcessError as e:
        return e.returncode, (e.stdout or str(e)).strip()


def is_git_repo() -> bool:
    code, out = run(["git", "rev-parse", "--is-inside-work-tree"]) 
    return code == 0 and out.strip() == "true"


def repo_has_changes() -> bool:
    code, out = run(["git", "status", "--porcelain"]) 
    return code == 0 and bool(out.strip())


def add_changes():
    # Adiciona apenas arquivos de aula por padrão, mas se nada for capturado,
    # ainda assim tentará adicionar tudo para não perder alterações relacionadas.
    # Primeiro tenta por padrão: aula*.py
    code, _ = run(["git", "add", f"{FILE_PREFIX}*{FILE_SUFFIX}"])
    if code != 0:
        # fallback: adiciona tudo
        run(["git", "add", "."])


def commit_changes():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Auto: atualiza aulas ({now})"
    code, out = run(["git", "commit", "-m", message])
    if code == 0:
        log(f"Commit criado: {message}")
        return True
    if "nothing to commit" in out.lower():
        return False
    log(f"Falha ao commitar: {out}")
    return False


def push_changes():
    # Primeiro teste leve para checar conexão com o remoto
    code, _ = run(["git", "ls-remote", "--heads", "origin"], capture=True)
    if code != 0:
        log("Remoto indisponível agora (offline?). Mantendo commit local.")
        return False
    code, out = run(["git", "push"]) 
    if code == 0:
        log("Push concluído.")
        return True
    log(f"Falha no push: {out}")
    return False


def has_unpushed_commits() -> bool:
    # Conta commits à frente do remoto
    code, out = run(["git", "rev-list", "--count", "@{u}..HEAD"]) 
    if code != 0:
        return False
    try:
        ahead = int(out.strip())
        return ahead > 0
    except ValueError:
        return False


def list_aula_files():
    return [
        os.path.join(WATCH_DIR, f)
        for f in os.listdir(WATCH_DIR)
        if f.startswith(FILE_PREFIX) and f.endswith(FILE_SUFFIX)
    ]


def current_snapshot():
    snap = {}
    for path in list_aula_files():
        try:
            snap[path] = os.path.getmtime(path)
        except FileNotFoundError:
            continue
    return snap


def diff_snapshots(prev, curr):
    changed = set()
    # novos ou modificados
    for p, mtime in curr.items():
        if p not in prev or prev[p] != mtime:
            changed.add(p)
    # removidos
    for p in prev:
        if p not in curr:
            changed.add(p)
    return changed


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}")
    sys.stdout.flush()


def main():
    if not is_git_repo():
        print("Este diretório não é um repositório Git. Saindo.")
        sys.exit(1)

    log("Auto-sync iniciado. Observando arquivos aula*.py…")
    prev = current_snapshot()
    last_change = None

    last_push_check = 0.0
    while True:
        time.sleep(CHECK_INTERVAL)
        curr = current_snapshot()
        changed = diff_snapshots(prev, curr)
        if changed:
            last_change = time.time()
            log(f"Mudanças detectadas ({len(changed)} arquivo(s)). Aguardando inatividade…")
            prev = curr
            continue

        if last_change is not None and (time.time() - last_change) >= QUIET_SECONDS:
            # tempo de inatividade atingido
            last_change = None

            if not repo_has_changes():
                continue

            add_changes()
            # Após add, verifique novamente se há algo a commitar
            code, _ = run(["git", "diff", "--cached", "--quiet"], capture=False)
            # git diff --quiet retorna 1 se há mudanças, 0 se não há
            if code == 0:
                continue

            if commit_changes():
                push_changes()

        # Tentativa periódica de push caso existam commits não enviados
        now = time.time()
        if now - last_push_check >= PUSH_POLL_SECONDS:
            last_push_check = now
            if has_unpushed_commits():
                push_changes()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Auto-sync interrompido pelo usuário.")
        sys.exit(0)
