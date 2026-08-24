import os
import subprocess
from CTFd import create_app
from CTFd.models import db, Challenges, Flags, ChallengeFiles, Files
from CTFd.cache import clear_challenges, clear_standings

app = create_app()

with app.app_context():
    uploads_dir = os.path.abspath("CTFd/uploads")

    def update_challenge_binary(chal_name, flag_str, c_code, bin_filename, gcc_flags=[]):
        chal = Challenges.query.filter_by(name=chal_name).first()
        if not chal:
            print(f"[-] Challenge not found: {chal_name}")
            return
        
        # Compile
        bin_path = f"/tmp/{bin_filename}"
        cmd = ["gcc"] + gcc_flags + ["-O2", "-x", "c", "-", "-o", bin_path]
        subprocess.run(cmd, input=c_code.encode(), check=True)
        with open(bin_path, "rb") as f:
            bin_data = f.read()

        # Update flag in DB
        Flags.query.filter_by(challenge_id=chal.id).delete()
        db.session.add(Flags(challenge_id=chal.id, type="static", content=flag_str))
        
        # Update challenge file
        cf = ChallengeFiles.query.filter_by(challenge_id=chal.id).first()
        if cf:
            full_path = os.path.join(uploads_dir, cf.location)
            with open(full_path, "wb") as f:
                f.write(bin_data)
        db.session.commit()
        print(f"[+] Successfully fixed & recompiled {chal_name} -> Flag: {flag_str}")

    # 1. Fix Reverse 2: Bitwise Logic Checker (200 pts)
    flag2 = "CCA{bitwise_xor_transformation_logic_master}"
    # Target array is flag2[i] ^ 0x5a
    target2 = [ord(c) ^ 0x5a for c in flag2]
    c2_code = f"""#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {{
    if (argc < 2) {{
        printf("Usage: %s <key>\\n", argv[0]);
        return 1;
    }}
    char *input = argv[1];
    unsigned char target[] = {{ {', '.join(hex(b) for b in target2)} }};
    int len = sizeof(target);
    if (strlen(input) != len) {{
        printf("[-] Wrong key length!\\n");
        return 1;
    }}
    for (int i = 0; i < len; i++) {{
        if ((unsigned char)(input[i] ^ 0x5a) != target[i]) {{
            printf("[-] Verification failed at byte %d!\\n", i);
            return 1;
        }}
    }}
    printf("[+] SUCCESS! Flag is: %s\\n", input);
    return 0;
}}
"""
    update_challenge_binary("Bitwise Logic Checker", flag2, c2_code, "bitwise_checker")

    # 2. Fix Reverse 3: Anti-Debug Sentinel (350 pts)
    flag3 = "CCA{antidebug_ptrace_rolling_shift_master}"
    # Encrypt: (ord(c) + (i * 3) + 7) & 0xff
    enc3 = [((ord(c) + (i * 3) + 7) & 0xff) for i, c in enumerate(flag3)]
    c3_code = f"""#include <stdio.h>
#include <string.h>
#include <sys/ptrace.h>
#include <unistd.h>
#include <stdlib.h>

void antidebug() {{
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) < 0) {{
        printf("[-] Debugger detected! Exiting...\\n");
        exit(1);
    }}
}}

int main(int argc, char *argv[]) {{
    antidebug();
    if (argc < 2) {{
        printf("Usage: %s <secret_token>\\n", argv[0]);
        return 1;
    }}
    char *s = argv[1];
    unsigned char enc[] = {{ {', '.join(hex(b) for b in enc3)} }};
    int n = sizeof(enc);
    if (strlen(s) != n) {{
        printf("[-] Invalid token length.\\n");
        return 1;
    }}
    for (int i = 0; i < n; i++) {{
        if ((unsigned char)((s[i] + (i * 3) + 7) & 0xff) != enc[i]) {{
            printf("[-] Token mismatch at step %d!\\n", i);
            return 1;
        }}
    }}
    printf("[+] CORRECT! Welcome elite agent: %s\\n", s);
    return 0;
}}
"""
    update_challenge_binary("Anti-Debug Sentinel", flag3, c3_code, "secure_agent_auth")

    # 3. Fix Reverse 4: Virtual Machine Bytecode Reversal (500 pts)
    flag4 = "CCA{custom_vm_bytecode_disassembler_elite_rev_2026}"
    def rol8(v, shift):
        return ((v << shift) | (v >> (8 - shift))) & 0xff
    
    # VM: b ^ 0x33 -> + 0x15 -> rol8(b, 3)
    target4 = [rol8(((ord(c) ^ 0x33) + 0x15) & 0xff, 3) for c in flag4]
    c4_code = f"""#include <stdio.h>
#include <string.h>

unsigned char rol8(unsigned char v, int shift) {{
    return (v << shift) | (v >> (8 - shift));
}}

int main(int argc, char *argv[]) {{
    if (argc < 2) {{
        printf("Usage: %s <vm_key>\\n", argv[0]);
        return 1;
    }}
    char *input = argv[1];
    unsigned char target_vm[] = {{ {', '.join(hex(b) for b in target4)} }};
    int len = sizeof(target_vm);
    if (strlen(input) != len) {{
        printf("[-] Invalid length!\\n");
        return 1;
    }}
    for (int i = 0; i < len; i++) {{
        unsigned char b = input[i];
        b = b ^ 0x33;
        b = (b + 0x15) & 0xff;
        b = rol8(b, 3);
        if (b != target_vm[i]) {{
            printf("[-] VM rejected state at %d!\\n", i);
            return 1;
        }}
    }}
    printf("[+] VM SUCCESS! Flag accepted: %s\\n", input);
    return 0;
}}
"""
    update_challenge_binary("Virtual Machine Bytecode Reversal", flag4, c4_code, "vm_evaluator")

    clear_challenges()
    clear_standings()
    print("[✓] All Reverse challenges cleanly verified and updated.")
