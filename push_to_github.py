import subprocess
import sys
import os

cwd = os.path.dirname(os.path.abspath(__file__))

commands = [
    ["git", "branch", "-M", "main"],
    ["git", "remote", "set-url", "origin", "https://github.com/gempurbudianarki/ctfleb.git"],
    ["git", "add", "."],
    ["git", "commit", "-m", "CCA ARENA CTFd - GameBoy Retro Neo-Arcade Theme, Super Mario BGM, SFX and Optimizations"],
    ["git", "push", "-u", "origin", "main"]
]

print(">>> Starting Git Push Workflow for ctfleb...", flush=True)

for cmd in commands:
    print(f"\n>>> Running: {' '.join(cmd)}", flush=True)
    try:
        res = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
        print("STDOUT:", res.stdout.strip())
        if res.stderr.strip():
            print("STDERR:", res.stderr.strip())
        if res.returncode != 0 and "set-url" in cmd:
            # Fallback to add remote if set-url failed
            print(">>> Remote not found, attempting git remote add origin...", flush=True)
            subprocess.run(["git", "remote", "add", "origin", "https://github.com/gempurbudianarki/ctfleb.git"], cwd=cwd)
    except Exception as e:
        print("Error executing command:", e, flush=True)

print("\n>>> Done!", flush=True)
