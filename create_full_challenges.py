import os
import sys
import struct
import io
import zlib
import zipfile
import subprocess
import hashlib
from PIL import Image, PngImagePlugin, ExifTags

from CTFd import create_app
from CTFd.models import (
    db, Challenges, Flags, Hints, ChallengeFiles, Files, Solves, Fails, Users, Admins
)
from CTFd.cache import clear_challenges, clear_standings, clear_pages, clear_config

app = create_app()

with app.app_context():
    print("[*] 1. Resetting database: Cleaning old challenges, flags, files, solves, test users...")

    # Delete Solves & Fails
    Solves.query.delete()
    Fails.query.delete()

    # Delete Challenge Files
    ChallengeFiles.query.delete()
    Files.query.filter_by(type="challenge").delete()

    # Delete Hints, Flags, Challenges
    Hints.query.delete()
    Flags.query.delete()
    Challenges.query.delete()

    # Clean dummy users (keep admin)
    Users.query.filter(Users.type != "admin").delete()
    db.session.commit()
    print("[+] Old challenges and dummy solves cleared cleanly.")

    # Storage dir for uploaded CTFd challenge files
    uploads_dir = os.path.abspath("CTFd/uploads")
    os.makedirs(uploads_dir, exist_ok=True)

    def attach_file_to_challenge(chal, filename, file_bytes):
        # Calculate sha1
        sha1 = hashlib.sha1(file_bytes).hexdigest()
        # Create hashed folder like CTFd does
        folder_hash = hashlib.md5((chal.name + filename).encode()).hexdigest()
        folder_path = os.path.join(uploads_dir, folder_hash)
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "wb") as f:
            f.write(file_bytes)
        
        rel_location = f"{folder_hash}/{filename}"
        cf = ChallengeFiles(
            challenge_id=chal.id,
            type="challenge",
            location=rel_location,
            sha1sum=sha1
        )
        db.session.add(cf)
        db.session.commit()
        print(f"    [+] Attached file: {filename} -> {rel_location}")

    print("\n[*] 2. Creating New Progressive Challenge Suite...")

    # =========================================================================
    # CATEGORY: CRYPTOGRAPHY (4 Challenges: Easy -> Medium -> Hard -> Insane)
    # =========================================================================
    print("\n--- [CRYPTOGRAPHY] ---")

    # 1. Crypto Easy: Subtle Shift 1989 (50 pts)
    c1 = Challenges(
        name="Subtle Shift 1989",
        category="Crypto",
        value=50,
        description="""Seorang agen rahasia mengirimkan pesan terenkripsi menggunakan sandi substitusi geser kuno. Temukan kunci pergeserannya dan dapatkan kembali plaintext rahasianya!

**Ciphertext:**
`HHG{vxhvdu_vkliw_lv_wrr_hdvb_1989}`

**Format Flag:** `CCA{...}`""",
        state="visible",
        type="standard"
    )
    db.session.add(c1)
    db.session.commit()
    db.session.add(Flags(challenge_id=c1.id, type="static", content="CCA{caesar_shift_is_too_easy_1989}"))
    db.session.add(Hints(challenge_id=c1.id, content="Perhatikan huruf pertama 'H' bergeser dari 'C'. Hitung jarak alfabetnya (Shift = 5 atau ROT-21).", cost=10))
    db.session.commit()
    print("[+] Created Crypto: Subtle Shift 1989 (50 pts)")

    # 2. Crypto Medium: Vigenere Matrix (150 pts)
    c2 = Challenges(
        name="Vigenere Polyalphabetic Matrix",
        category="Crypto",
        value=150,
        description="""Komunikasi terenkripsi dicegat di stasiun transmisi radar. Algoritma yang digunakan adalah Vigenère Cipher dengan kata kunci rahasia bertema komunitas kita: `ACEH`.

**Ciphertext:**
`CEE{vmkgriii_pqsfaprxerilmg_qasxic_ocb}`

Pecahkan enkripsi di atas menggunakan key `ACEH` untuk membuka flag!""",
        state="visible",
        type="standard"
    )
    db.session.add(c2)
    db.session.commit()
    db.session.add(Flags(challenge_id=c2.id, type="static", content="CCA{vigenere_polyalphabetic_master_key}"))
    db.session.add(Hints(challenge_id=c2.id, content="Gunakan tabel Vigenere atau tools CyberChef dengan recipe 'Vigenère Decode' dan Key 'ACEH'.", cost=25))
    db.session.commit()
    print("[+] Created Crypto: Vigenere Matrix (150 pts)")

    # 3. Crypto Hard: Small Exponent RSA Attack (300 pts)
    # Flag: CCA{cube_root_rsa_small_e_attack}
    rsa_flag = b"CCA{cube_root_rsa_small_e_attack}"
    rsa_m = int.from_bytes(rsa_flag, "big")
    rsa_e = 3
    # N is much larger than m^3
    rsa_p = 104729
    rsa_q = 1299709
    # Choose big primes so N > m^3
    rsa_p_big = 2**512 + 75
    rsa_q_big = 2**512 + 151
    rsa_n = rsa_p_big * rsa_q_big
    rsa_c = pow(rsa_m, rsa_e, rsa_n) # m^3 < N because m^3 is ~ 256 bits, N is ~ 1024 bits!
    rsa_txt = f"""=== RSA PUBLIC TRANSMISSION INTERCEPT ===
Public Exponent (e): {rsa_e}
Modulus (N): {rsa_n}
Ciphertext (C): {rsa_c}

Hint: When e=3 and m^3 < N, is the modulo operation even necessary?
"""
    c3 = Challenges(
        name="Small Exponent RSA Attack",
        category="Crypto",
        value=300,
        description="""Sistem enkripsi kunci publik RSA yang dikonfigurasi secara buruk menggunakan public exponent $e = 3$ tanpa padding PKCS#1.

Download file transmisi terlampir, lakukan analisis matematis untuk mengekstrak pesan aslinya!""",
        state="visible",
        type="standard"
    )
    db.session.add(c3)
    db.session.commit()
    attach_file_to_challenge(c3, "rsa_challenge.txt", rsa_txt.encode())
    db.session.add(Flags(challenge_id=c3.id, type="static", content="CCA{cube_root_rsa_small_e_attack}"))
    db.session.add(Hints(challenge_id=c3.id, content="Karena $m^3 < N$, maka $C = m^3$. Anda cukup menghitung akar pangkat tiga bulat (integer cube root) dari $C$!", cost=50))
    db.session.commit()
    print("[+] Created Crypto: Small Exponent RSA Attack (300 pts)")

    # 4. Crypto Insane: Broken XOR Key Reuse Matrix (450 pts)
    # Two-time pad key reuse attack
    key_secret = b"K3yStR3am_AcEh_Cca_2026_S3cr3t!!"
    msg1 = b"The secret launch code is hidden inside the main mainframe core"
    msg2 = b"CCA{xor_key_reuse_cribdrag_pwned_all_stream_ciphers_broken_101}"
    
    # Encrypt with same XOR key
    def xor_bytes(k, m):
        return bytes([m[i] ^ k[i % len(k)] for i in range(len(m))])
    
    c_xor1 = xor_bytes(key_secret, msg1)
    c_xor2 = xor_bytes(key_secret, msg2)
    
    xor_file_content = f"""[STREAM CIPHER INTERCEPT DATA]
Stream 1 (Hex): {c_xor1.hex()}
Stream 2 (Hex): {c_xor2.hex()}

Known Info:
Both messages were encrypted using the EXACT same one-time pad keystream.
Stream 1 plaintext starts with: "The secret launch code is "
Stream 2 contains the coveted CTF Flag.
"""
    c4 = Challenges(
        name="Two-Time Pad Crib Drag",
        category="Crypto",
        value=450,
        description="""Operator telekomunikasi melakukan kesalahan fatal: menggunakan One-Time Pad / Keystream yang sama untuk mengenkripsi dua pesan berbeda (*Key Reuse*).

Analisis kedua ciphertext terlampir dengan teknik *Crib Dragging* untuk memulihkan kunci dan membaca flag!""",
        state="visible",
        type="standard"
    )
    db.session.add(c4)
    db.session.commit()
    attach_file_to_challenge(c4, "xor_streams.txt", xor_file_content.encode())
    db.session.add(Flags(challenge_id=c4.id, type="static", content="CCA{xor_key_reuse_cribdrag_pwned_all_stream_ciphers_broken_101}"))
    db.session.add(Hints(challenge_id=c4.id, content="$C_1 \oplus C_2 = M_1 \oplus M_2$. Lakukan XOR antara kedua ciphertext, lalu lakukan XOR dengan teks awal yang diketahui untuk mendapatkan potongan keystream!", cost=75))
    db.session.commit()
    print("[+] Created Crypto: Two-Time Pad Crib Drag (450 pts)")

    # =========================================================================
    # CATEGORY: REVERSE ENGINEERING (4 Challenges)
    # =========================================================================
    print("\n--- [REVERSE ENGINEERING] ---")

    # 1. Reverse Easy: String Vault 101 (75 pts)
    # Python script compiled or simple executable
    c_rev1_src = """# Embedded Vault Access
import sys

def verify_code(input_code):
    expected = [67, 67, 65, 123, 115, 105, 109, 112, 108, 101, 95, 115, 116, 114, 105, 110, 103, 115, 95, 97, 110, 100, 95, 100, 101, 99, 111, 109, 112, 105, 108, 97, 116, 105, 111, 110, 95, 49, 48, 49, 125]
    if len(input_code) != len(expected):
        return False
    return [ord(c) for c in input_code] == expected

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vault.py <passcode>")
        sys.exit(1)
    if verify_code(sys.argv[1]):
        print("[+] ACCESS GRANTED! Passcode is your flag.")
    else:
        print("[-] ACCESS DENIED.")
"""
    c_rev1 = Challenges(
        name="String Vault 101",
        category="Reverse",
        value=75,
        description="""Sebuah skrip verifikasi akses lemari besi digital berhasil diamankan. Analisis array kode verifikasi di dalam file untuk menemukan flag yang valid!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_rev1)
    db.session.commit()
    attach_file_to_challenge(c_rev1, "vault.py", c_rev1_src.encode())
    db.session.add(Flags(challenge_id=c_rev1.id, type="static", content="CCA{simple_strings_and_decompilation_101}"))
    db.session.add(Hints(challenge_id=c_rev1.id, content="Konversikan nilai ASCII array `expected` menjadi karakter string (`chr(x)`).", cost=15))
    db.session.commit()
    print("[+] Created Reverse: String Vault 101 (75 pts)")

    # 2. Reverse Medium: Bitwise Math Check (200 pts)
    # Compile a native C x86_64 binary
    c_rev2_c = """#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <key>\\n", argv[0]);
        return 1;
    }
    char *input = argv[1];
    unsigned char target[] = {
        0x19, 0x19, 0x1b, 0x21, 0x22, 0x62, 0x6e, 0x05, 0x3d, 0x33,
        0x29, 0x3b, 0x05, 0x2e, 0x28, 0x3b, 0x34, 0x29, 0x3c, 0x35,
        0x28, 0x37, 0x3b, 0x2e, 0x35, 0x3b, 0x05, 0x36, 0x35, 0x3d,
        0x33, 0x39, 0x27
    };
    int len = sizeof(target);
    if (strlen(input) != len) {
        printf("[-] Wrong key length!\\n");
        return 1;
    }
    for (int i = 0; i < len; i++) {
        if ((unsigned char)(input[i] ^ 0x5a) != target[i]) {
            printf("[-] Verification failed at byte %d!\\n", i);
            return 1;
        }
    }
    printf("[+] SUCCESS! Flag is: %s\\n", input);
    return 0;
}
"""
    # Compile with gcc
    subprocess.run(["gcc", "-O2", "-x", "c", "-", "-o", "/tmp/bitwise_checker"], input=c_rev2_c.encode(), check=True)
    with open("/tmp/bitwise_checker", "rb") as f:
        rev2_bin = f.read()

    c_rev2 = Challenges(
        name="Bitwise Logic Checker",
        category="Reverse",
        value=200,
        description="""Diberikan file ELF binary x86_64 `bitwise_checker`. Program ini memverifikasi kunci menggunakan transformasi bitwise sederhana.

Decompile binary ini menggunakan Ghidra, IDA Pro, atau GDB untuk merekonstruksi flag!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_rev2)
    db.session.commit()
    attach_file_to_challenge(c_rev2, "bitwise_checker", rev2_bin)
    # Flag is target ^ 0x5a
    # target = [0x19, 0x19, 0x1b, 0x21, 0x22, ...]
    # 0x19 ^ 0x5a = 'C', 0x19^0x5a='C', 0x1b^0x5a='A', 0x21^0x5a='{' ...
    flag_rev2 = "".join([chr(b ^ 0x5a) for b in [
        0x19, 0x19, 0x1b, 0x21, 0x22, 0x62, 0x6e, 0x05, 0x3d, 0x33,
        0x29, 0x3b, 0x05, 0x2e, 0x28, 0x3b, 0x34, 0x29, 0x3c, 0x35,
        0x28, 0x37, 0x3b, 0x2e, 0x35, 0x3b, 0x05, 0x36, 0x35, 0x3d,
        0x33, 0x39, 0x27
    ]])
    db.session.add(Flags(challenge_id=c_rev2.id, type="static", content=flag_rev2))
    db.session.add(Hints(challenge_id=c_rev2.id, content="Perhatikan operasi XOR `input[i] ^ 0x5a == target[i]`. Ekstrak array target dari binary dan XOR kembali dengan `0x5a`!", cost=35))
    db.session.commit()
    print(f"[+] Created Reverse: Bitwise Logic Checker (200 pts) -> Flag: {flag_rev2}")

    # 3. Reverse Hard: Anti-Debug & Rolling State (350 pts)
    c_rev3_c = """#include <stdio.h>
#include <string.h>
#include <sys/ptrace.h>
#include <unistd.h>
#include <stdlib.h>

void antidebug() {
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) < 0) {
        printf("[-] Debugger detected! Exiting...\\n");
        exit(1);
    }
}

int main(int argc, char *argv[]) {
    antidebug();
    if (argc < 2) {
        printf("Usage: %s <secret_token>\\n", argv[0]);
        return 1;
    }
    char *s = argv[1];
    unsigned char enc[] = {
        0x45, 0x47, 0x44, 0x7e, 0x76, 0x7f, 0x7c, 0x6b, 0x68, 0x6e, 
        0x6b, 0x64, 0x62, 0x72, 0x7c, 0x74, 0x79, 0x7a, 0x68, 0x65, 
        0x6b, 0x55, 0x57, 0x5a, 0x5d, 0x42, 0x49, 0x49, 0x47, 0x4b, 
        0x9a
    };
    int n = sizeof(enc);
    if (strlen(s) != n) {
        printf("[-] Invalid token length.\\n");
        return 1;
    }
    for (int i = 0; i < n; i++) {
        if ((unsigned char)(s[i] + (i * 2) + 2) != enc[i]) {
            printf("[-] Token mismatch at step %d!\\n", i);
            return 1;
        }
    }
    printf("[+] CORRECT! Welcome elite agent: %s\\n", s);
    return 0;
}
"""
    subprocess.run(["gcc", "-O2", "-x", "c", "-", "-o", "/tmp/secure_agent_auth"], input=c_rev3_c.encode(), check=True)
    with open("/tmp/secure_agent_auth", "rb") as f:
        rev3_bin = f.read()

    enc_bytes = [
        0x45, 0x47, 0x44, 0x7e, 0x76, 0x7f, 0x7c, 0x6b, 0x68, 0x6e, 
        0x6b, 0x64, 0x62, 0x72, 0x7c, 0x74, 0x79, 0x7a, 0x68, 0x65, 
        0x6b, 0x55, 0x57, 0x5a, 0x5d, 0x42, 0x49, 0x49, 0x47, 0x4b, 
        0x9a
    ]
    flag_rev3 = "".join([chr(enc_bytes[i] - (i * 2) - 2) for i in range(len(enc_bytes))])

    c_rev3 = Challenges(
        name="Anti-Debug Sentinel",
        category="Reverse",
        value=350,
        description="""Binary ini memiliki proteksi `ptrace` anti-debugging dan verifikasi algoritma *rolling state shift*.

Bypass mekanisme anti-debugnya atau lakukan reverse statis untuk mendapatkan flag yang tepat!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_rev3)
    db.session.commit()
    attach_file_to_challenge(c_rev3, "secure_agent_auth", rev3_bin)
    db.session.add(Flags(challenge_id=c_rev3.id, type="static", content=flag_rev3))
    db.session.add(Hints(challenge_id=c_rev3.id, content="Perhatikan loop pergeseran: `s[i] = enc[i] - (i * 2) - 2`.", cost=50))
    db.session.commit()
    print(f"[+] Created Reverse: Anti-Debug Sentinel (350 pts) -> Flag: {flag_rev3}")

    # 4. Reverse Insane: Custom 8-bit Bytecode VM (500 pts)
    c_rev4_c = """#include <stdio.h>
#include <string.h>

// Custom VM opcodes: 0x01=XOR, 0x02=ADD, 0x03=ROL, 0x04=CMP
unsigned char bytecode[] = {
    0x01, 0x33, // XOR with 0x33
    0x02, 0x15, // ADD 0x15
    0x03, 0x03, // ROL 3 bits
    0x04        // END & COMPARE
};

unsigned char target_vm[] = {
    0x1c, 0x1c, 0x3c, 0xf6, 0x56, 0x76, 0xd6, 0xb7, 0x97, 0x57,
    0xf7, 0x36, 0xd7, 0x97, 0xb7, 0x57, 0x77, 0x36, 0xf7, 0xd6,
    0x57, 0xf7, 0xb6, 0x37, 0x57, 0x36, 0xd7, 0xf7, 0x37, 0x77,
    0xb7, 0x16, 0x97, 0x37, 0x57, 0x36, 0xd7, 0x36, 0x97, 0x57,
    0x37, 0x76
};

unsigned char rol8(unsigned char v, int shift) {
    return (v << shift) | (v >> (8 - shift));
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <vm_key>\\n", argv[0]);
        return 1;
    }
    char *input = argv[1];
    int len = sizeof(target_vm);
    if (strlen(input) != len) {
        printf("[-] Invalid length!\\n");
        return 1;
    }
    for (int i = 0; i < len; i++) {
        unsigned char b = input[i];
        b = b ^ 0x33;
        b = (b + 0x15) & 0xff;
        b = rol8(b, 3);
        if (b != target_vm[i]) {
            printf("[-] VM rejected state at %d!\\n", i);
            return 1;
        }
    }
    printf("[+] VM SUCCESS! Flag accepted: %s\\n", input);
    return 0;
}
"""
    subprocess.run(["gcc", "-O2", "-x", "c", "-", "-o", "/tmp/vm_evaluator"], input=c_rev4_c.encode(), check=True)
    with open("/tmp/vm_evaluator", "rb") as f:
        rev4_bin = f.read()

    def ror8(v, shift):
        return ((v >> shift) | (v << (8 - shift))) & 0xff

    target_vm_bytes = [
        0x1c, 0x1c, 0x3c, 0xf6, 0x56, 0x76, 0xd6, 0xb7, 0x97, 0x57,
        0xf7, 0x36, 0xd7, 0x97, 0xb7, 0x57, 0x77, 0x36, 0xf7, 0xd6,
        0x57, 0xf7, 0xb6, 0x37, 0x57, 0x36, 0xd7, 0xf7, 0x37, 0x77,
        0xb7, 0x16, 0x97, 0x37, 0x57, 0x36, 0xd7, 0x36, 0x97, 0x57,
        0x37, 0x76
    ]
    # Invert VM: ror8(x, 3) -> subtract 0x15 -> xor 0x33
    flag_rev4 = "".join([chr(((ror8(b, 3) - 0x15) & 0xff) ^ 0x33) for b in target_vm_bytes])

    c_rev4 = Challenges(
        name="Virtual Machine Bytecode Reversal",
        category="Reverse",
        value=500,
        description="""Sebuah virtual machine kustom mengeksekusi urutan bytecode mini (XOR, ADD, Bitwise Rotation) pada input pengguna sebelum memeriksa kecocokan dengan register memori.

Disassemble binary `vm_evaluator` dan buat emulator pembalik (inverse VM solver) untuk mengekstrak flag!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_rev4)
    db.session.commit()
    attach_file_to_challenge(c_rev4, "vm_evaluator", rev4_bin)
    db.session.add(Flags(challenge_id=c_rev4.id, type="static", content=flag_rev4))
    db.session.add(Hints(challenge_id=c_rev4.id, content="Balikkan urutan operasi VM: 1) Rotate Right 3 bits, 2) Kurangi dengan 0x15 (modulo 256), 3) XOR dengan 0x33.", cost=100))
    db.session.commit()
    print(f"[+] Created Reverse: Custom VM (500 pts) -> Flag: {flag_rev4}")

    # =========================================================================
    # CATEGORY: BINARY EXPLOITATION / PWN (3 Challenges)
    # =========================================================================
    print("\n--- [BINARY EXPLOITATION / PWN] ---")

    # 1. Pwn Easy: Return to Win (100 pts)
    c_pwn1_c = """#include <stdio.h>
#include <stdlib.h>

void win() {
    printf("[+] Pwned! Flag: CCA{ret2win_buffer_overflow_rip_control}\\n");
    exit(0);
}

void vuln() {
    char buffer[64];
    printf("Enter payload buffer: ");
    gets(buffer); // Buffer overflow vulnerability
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
    printf("[-] Returned safely.\\n");
    return 0;
}
"""
    subprocess.run(["gcc", "-fno-stack-protector", "-no-pie", "-x", "c", "-", "-o", "/tmp/ret2win"], input=c_pwn1_c.encode(), check=True)
    with open("/tmp/ret2win", "rb") as f:
        pwn1_bin = f.read()

    c_pwn1 = Challenges(
        name="Classic ret2win",
        category="Pwn",
        value=100,
        description="""Diberikan binary ELF x86_64 yang dikompilasi tanpa *Stack Canary* dan tanpa *PIE*. Fungsi `vuln()` menggunakan `gets()` yang rentan terhadap Buffer Overflow.

Tujuan Anda: Temukan alamat fungsi `win()` dan manipulasi Saved Return Pointer (`$rip`) untuk memanggil `win()`!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_pwn1)
    db.session.commit()
    attach_file_to_challenge(c_pwn1, "ret2win", pwn1_bin)
    attach_file_to_challenge(c_pwn1, "ret2win.c", c_pwn1_c.encode())
    db.session.add(Flags(challenge_id=c_pwn1.id, type="static", content="CCA{ret2win_buffer_overflow_rip_control}"))
    db.session.add(Hints(challenge_id=c_pwn1.id, content="Gunakan GDB (`info address win`) atau `objdump -d ret2win | grep win` untuk mencari address fungsi target.", cost=20))
    db.session.commit()
    print("[+] Created Pwn: Classic ret2win (100 pts)")

    # 2. Pwn Medium: Format String Stack Leak (250 pts)
    c_pwn2_c = """#include <stdio.h>
#include <string.h>

int main() {
    char flag[] = "CCA{fmt_string_arbitrary_stack_leak_0x7f}";
    char user_input[128];
    
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("Send telemetry string: ");
    fgets(user_input, sizeof(user_input), stdin);
    
    // Vulnerable format string bug
    printf(user_input);
    return 0;
}
"""
    subprocess.run(["gcc", "-x", "c", "-", "-o", "/tmp/fmt_leak"], input=c_pwn2_c.encode(), check=True)
    with open("/tmp/fmt_leak", "rb") as f:
        pwn2_bin = f.read()

    c_pwn2 = Challenges(
        name="Format String Oracle",
        category="Pwn",
        value=250,
        description="""Aplikasi server mencetak input pengguna secara langsung menggunakan `printf(user_input)` tanpa format specifier yang aman.

Manfaatkan celah **Format String Vulnerability** (`%p`, `%x`, `%s`) untuk membocorkan isi data flag yang tersimpan di stack memory!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_pwn2)
    db.session.commit()
    attach_file_to_challenge(c_pwn2, "fmt_leak", pwn2_bin)
    db.session.add(Flags(challenge_id=c_pwn2.id, type="static", content="CCA{fmt_string_arbitrary_stack_leak_0x7f}"))
    db.session.add(Hints(challenge_id=c_pwn2.id, content="Kirimkan payload `%p.%p.%p.%p.%p.%p...` atau `%7$s` untuk membaca nilai pointer pada stack.", cost=40))
    db.session.commit()
    print("[+] Created Pwn: Format String Oracle (250 pts)")

    # 3. Pwn Hard: Executable Stack Shellcode Runner (400 pts)
    c_pwn3_c = """#include <stdio.h>
#include <string.h>

void execute_shellcode() {
    char buffer[256];
    printf("[*] Enter x86_64 raw shellcode: ");
    int bytes = read(0, buffer, 256);
    void (*func)() = (void (*)())buffer;
    func();
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    execute_shellcode();
    return 0;
}
"""
    subprocess.run(["gcc", "-z", "execstack", "-x", "c", "-", "-o", "/tmp/shell_runner"], input=c_pwn3_c.encode(), check=True)
    with open("/tmp/shell_runner", "rb") as f:
        pwn3_bin = f.read()

    c_pwn3 = Challenges(
        name="Shellcode Sandbox Execution",
        category="Pwn",
        value=400,
        description="""Binary `shell_runner` membaca byte shellcode dari stdin dan langsung mengeksekusi pointer buffer tersebut di stack (`-z execstack`).

Kompilasi shellcode x86_64 assembly untuk memanggil `sys_write` atau `execve` guna membaca flag server!

Flag format: `CCA{execstack_shellcode_payload_pwnage}`""",
        state="visible",
        type="standard"
    )
    db.session.add(c_pwn3)
    db.session.commit()
    attach_file_to_challenge(c_pwn3, "shell_runner", pwn3_bin)
    db.session.add(Flags(challenge_id=c_pwn3.id, type="static", content="CCA{execstack_shellcode_payload_pwnage}"))
    db.session.add(Hints(challenge_id=c_pwn3.id, content="Gunakan pwntools: `asm(shellcraft.sh())` untuk mengenerate x86_64 shellcode standard.", cost=60))
    db.session.commit()
    print("[+] Created Pwn: Shellcode Runner (400 pts)")

    # =========================================================================
    # CATEGORY: DIGITAL FORENSICS (4 Challenges)
    # =========================================================================
    print("\n--- [DIGITAL FORENSICS] ---")

    # 1. Forensics Easy: Drone Recon EXIF (75 pts)
    # Create valid JPEG with secret comment / EXIF
    img_recon = Image.new("RGB", (640, 480), color=(30, 41, 59))
    recon_buf = io.BytesIO()
    # Add EXIF UserComment
    exif_dict = {
        0x9286: b"CCA{exif_metadata_drone_recon_found}" # UserComment tag
    }
    img_recon.save(recon_buf, format="JPEG", quality=90, comment=b"Mission Drone Log: CCA{exif_metadata_drone_recon_found}")
    recon_bytes = recon_buf.getvalue()

    c_for1 = Challenges(
        name="Drone Recon EXIF Metadata",
        category="Forensics",
        value=75,
        description="""Drone pengintai mengunggah foto udara target sebelum hilang kontak. Analisis metadata file citra ini menggunakan `exiftool` atau `strings` untuk menemukan data intelijen rahasia!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_for1)
    db.session.commit()
    attach_file_to_challenge(c_for1, "drone_recon.jpg", recon_bytes)
    db.session.add(Flags(challenge_id=c_for1.id, type="static", content="CCA{exif_metadata_drone_recon_found}"))
    db.session.add(Hints(challenge_id=c_for1.id, content="Gunakan perintah terminal: `exiftool drone_recon.jpg` atau `strings drone_recon.jpg | grep CCA`.", cost=15))
    db.session.commit()
    print("[+] Created Forensics: Drone Recon EXIF (75 pts)")

    # 2. Forensics Medium: Embedded Stegocache (200 pts)
    # PNG with an appended ZIP archive (Polyglot / Binwalk carving)
    png_base = Image.new("RGBA", (400, 300), color=(15, 23, 42, 255))
    png_buf = io.BytesIO()
    png_base.save(png_buf, format="PNG")
    clean_png_bytes = png_buf.getvalue()

    # Create secret ZIP
    zip_buf = io.BytesIO()
    with zipfile.ZipFile(zip_buf, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("secret_flag.txt", "Selamat! Anda berhasil mengekstrak file arsip tersembunyi.\n\nFLAG: CCA{binwalk_and_hidden_zip_extracted}\n")
    zip_bytes = zip_buf.getvalue()

    # Combined Polyglot (PNG + ZIP)
    stego_png_bytes = clean_png_bytes + zip_bytes

    c_for2 = Challenges(
        name="Embedded Stegocache Fragment",
        category="Forensics",
        value=200,
        description="""Gambar PNG `corrupted_frame.png` tampak normal saat dibuka, namun ukuran filenya mencurigakan. Diduga ada arsip data lain yang disisipkan di akhir file (EOF Injection).

Lakukan ekstraksi file tersembunyi menggunakan `binwalk` atau `foremost`!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_for2)
    db.session.commit()
    attach_file_to_challenge(c_for2, "corrupted_frame.png", stego_png_bytes)
    db.session.add(Flags(challenge_id=c_for2.id, type="static", content="CCA{binwalk_and_hidden_zip_extracted}"))
    db.session.add(Hints(challenge_id=c_for2.id, content="Jalankan `binwalk -e corrupted_frame.png` atau buka langsung menggunakan 7-Zip / `unzip corrupted_frame.png`.", cost=30))
    db.session.commit()
    print("[+] Created Forensics: Embedded Stegocache (200 pts)")

    # 3. Forensics Hard: Wireshark Network PCAP Capture (350 pts)
    # Generate a genuine PCAP file with simulated HTTP stream containing flag
    pcap_buf = io.BytesIO()
    # PCAP Global Header
    pcap_buf.write(struct.pack('<IHHiIII', 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1)) # LinkType 1 = Ethernet
    
    # Packet 1: HTTP GET /api/v1/confidential_token
    # Ethernet Header (14 bytes) + IP Header (20 bytes) + TCP Header (20 bytes) + Payload
    eth = b'\x00\x0c\x29\x1f\x3b\x82\x00\x50\x56\xc0\x00\x08\x08\x00' # IPv4
    ip = b'\x45\x00\x00\x54\x00\x01\x00\x00\x40\x06\x7c\xcd\xc0\xa8\x01\x64\xc0\xa8\x01\x01' # 192.168.1.100 -> 192.168.1.1
    tcp = b'\xd4\x31\x00\x50\x00\x00\x00\x01\x00\x00\x00\x00\x50\x18\x01\x00\x00\x00\x00\x00'
    http_payload = b"GET /api/v1/auth/token HTTP/1.1\r\nHost: acehtanggap.cloud\r\nUser-Agent: SecretAgent/2.0\r\n\r\n"
    pkt1_data = eth + ip + tcp + http_payload
    # Packet Header: ts_sec, ts_usec, incl_len, orig_len
    pcap_buf.write(struct.pack('<IIII', 1724486400, 100000, len(pkt1_data), len(pkt1_data)))
    pcap_buf.write(pkt1_data)

    # Packet 2: HTTP 200 OK Response with Flag
    http_resp = b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"status\":\"success\",\"auth_token\":\"CCA{wireshark_pcap_stream_reassembly}\"}"
    pkt2_data = eth + ip + tcp + http_resp
    pcap_buf.write(struct.pack('<IIII', 1724486400, 250000, len(pkt2_data), len(pkt2_data)))
    pcap_buf.write(pkt2_data)

    c_for3 = Challenges(
        name="Network Incident PCAP Capture",
        category="Forensics",
        value=350,
        description="""Tim SOC berhasil menangkap rekaman lalu lintas jaringan (*Network Packet Capture*) saat terjadi kebocoran kredensial rahasia.

Buka file `traffic_incident.pcap` menggunakan **Wireshark**, ikuti TCP Stream komunikasi HTTP, dan temukan token otentikasi flag!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_for3)
    db.session.commit()
    attach_file_to_challenge(c_for3, "traffic_incident.pcap", pcap_buf.getvalue())
    db.session.add(Flags(challenge_id=c_for3.id, type="static", content="CCA{wireshark_pcap_stream_reassembly}"))
    db.session.add(Hints(challenge_id=c_for3.id, content="Filter `http` pada Wireshark, lalu klik kanan paket -> 'Follow' -> 'TCP Stream'.", cost=40))
    db.session.commit()
    print("[+] Created Forensics: Network Incident PCAP (350 pts)")

    # 4. Forensics Insane: Memory Dump Frame Carving (500 pts)
    # Raw memory blob with obfuscated strings and memory signature
    mem_buf = io.BytesIO()
    # Fill with 128KB dummy memory patterns
    mem_buf.write(os.urandom(32768))
    mem_buf.write(b"\x00\x00\xDE\xAD\xBE\xEF_VRAM_FRAME_BUFFER_DUMP_2026_\x00\x00")
    mem_buf.write(os.urandom(16384))
    mem_buf.write(b"FLAG_RECOVERED_SECTION: CCA{memory_forensics_vram_carving_pro}")
    mem_buf.write(os.urandom(49152))

    c_for4 = Challenges(
        name="VRAM Memory Dump Carving",
        category="Forensics",
        value=500,
        description="""Sebuah dump memori mentah (*raw memory dump*) berhasil di-ekstrak dari perangkat keras sesaat setelah shutdown darurat.

Lakukan teknik **Memory Carving** menggunakan Volatility, `strings`, atau hex editor untuk menemukan flag yang tersimpan pada segmen memori volatile!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_for4)
    db.session.commit()
    attach_file_to_challenge(c_for4, "memory.raw", mem_buf.getvalue())
    db.session.add(Flags(challenge_id=c_for4.id, type="static", content="CCA{memory_forensics_vram_carving_pro}"))
    db.session.add(Hints(challenge_id=c_for4.id, content="Jalankan `strings -a -t x memory.raw | grep CCA` untuk menemukan offset memori flag.", cost=60))
    db.session.commit()
    print("[+] Created Forensics: Memory Dump Carving (500 pts)")

    # =========================================================================
    # CATEGORY: OSINT (3 Challenges)
    # =========================================================================
    print("\n--- [OSINT] ---")

    # 1. OSINT Easy: Banda Aceh Landmark Recon (50 pts)
    img_osint1 = Image.new("RGB", (800, 600), color=(14, 116, 144))
    osint1_buf = io.BytesIO()
    img_osint1.save(osint1_buf, format="JPEG", comment=b"Banda Aceh Recon: Masjid Raya Baiturrahman (Coordinates: 5.5536, 95.3171)")

    c_osint1 = Challenges(
        name="Landmark Geolocation Alpha",
        category="OSINT",
        value=50,
        description="""Sebuah misi pengintaian memotret titik koordinat pusat landmark paling bersejarah di Kota Banda Aceh.

Berdasarkan koordinat latitude `5.5536` dan longitude `95.3171`, sebutkan nama landmark tersebut!

Format Flag: `CCA{nama_landmark_huruf_kecil_spasi_diganti_underscore}`  
Contoh: `CCA{masjid_raya_baiturrahman}`""",
        state="visible",
        type="standard"
    )
    db.session.add(c_osint1)
    db.session.commit()
    attach_file_to_challenge(c_osint1, "landmark_target.jpg", osint1_buf.getvalue())
    db.session.add(Flags(challenge_id=c_osint1.id, type="static", content="CCA{masjid_raya_baiturrahman}"))
    db.session.add(Hints(challenge_id=c_osint1.id, content="Buka Google Maps, masukkan koordinat `5.5536, 95.3171`.", cost=10))
    db.session.commit()
    print("[+] Created OSINT: Landmark Geolocation (50 pts)")

    # 2. OSINT Medium: Flight Radar & ICAO Route (200 pts)
    c_osint2 = Challenges(
        name="ADS-B Flight Radar Tracking",
        category="OSINT",
        value=200,
        description="""Laporan intelijen mencatat pergerakan penerbangan komersial dari Bandara Internasional Sultan Iskandar Muda (BTJ) menuju Bandara Internasional Soekarno-Hatta (CGK).

Kode ICAO untuk Bandara Sultan Iskandar Muda adalah `WITT` dan Soekarno-Hatta adalah `WIII`.

Jika format flag menggabungkan kode rute ICAO keberangkatan dan kedatangan:  
Format Flag: `CCA{WITT_to_WIII_flight_path}`""",
        state="visible",
        type="standard"
    )
    db.session.add(c_osint2)
    db.session.commit()
    db.session.add(Flags(challenge_id=c_osint2.id, type="static", content="CCA{WITT_to_WIII_flight_path}"))
    db.session.add(Hints(challenge_id=c_osint2.id, content="Periksa database bandara ICAO Indonesia untuk bandara Banda Aceh (BTJ) dan Jakarta (CGK).", cost=25))
    db.session.commit()
    print("[+] Created OSINT: Flight Radar (200 pts)")

    # 3. OSINT Hard: PGP Key & GitHub Commit Recon (350 pts)
    c_osint3 = Challenges(
        name="Undercover Cryptographic Footprint",
        category="OSINT",
        value=350,
        description="""Seorang developer anonim meninggalkan jejak digital berupa PGP Key Fingerprint di server kunci publik:
`E4B2 98F1 C3D0 7A9E 4120  558A 9921 B6E5 DB9B B6E5`

Pesan terakhir yang ditandatangani berbunyi:
`CCA{pgp_key_fingerprint_github_recon_mastered_2026}`

Submit flag tersebut untuk menyelesaikan investigasi digital!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_osint3)
    db.session.commit()
    db.session.add(Flags(challenge_id=c_osint3.id, type="static", content="CCA{pgp_key_fingerprint_github_recon_mastered_2026}"))
    db.session.add(Hints(challenge_id=c_osint3.id, content="Flag tertera langsung pada pesan bertandatangan digital di deskripsi.", cost=30))
    db.session.commit()
    print("[+] Created OSINT: PGP Key Recon (350 pts)")

    # =========================================================================
    # CATEGORY: MISCELLANEOUS (2 Challenges)
    # =========================================================================
    print("\n--- [MISCELLANEOUS] ---")

    # 1. Misc Easy: Sanity Check (50 pts)
    c_misc1 = Challenges(
        name="Sanity Check // Welcome Arena",
        category="Misc",
        value=50,
        description="""Selamat datang di kompetisi CTF resmi **Cybersecurity Community of Aceh (CCA)**!

Salin dan submit flag berikut untuk menguji sistem submission dan mendapatkan poin pertama Anda di leaderboard:

`CCA{welcome_to_cca_cyber_arena_2026}`""",
        state="visible",
        type="standard"
    )
    db.session.add(c_misc1)
    db.session.commit()
    db.session.add(Flags(challenge_id=c_misc1.id, type="static", content="CCA{welcome_to_cca_cyber_arena_2026}"))
    db.session.commit()
    print("[+] Created Misc: Sanity Check (50 pts)")

    # 2. Misc Medium: Base64 Multi-Layer Decoder (150 pts)
    # Multi encoded: Base64 -> Hex -> Rot13
    raw_flag = "CCA{multi_layer_encoding_pipeline_solved}"
    # Hex
    hex_str = raw_flag.encode().hex()
    # Base64
    import base64
    b64_str = base64.b64encode(hex_str.encode()).decode()
    # Rot13
    import codecs
    rot13_str = codecs.encode(b64_str, 'rot_13')

    c_misc2 = Challenges(
        name="Layered Cipher Encoding Pipeline",
        category="Misc",
        value=150,
        description=f"""Pesan ini di-enkode secara bertingkat menggunakan pipeline serial: **ROT13 -> Base64 -> Hex**.

**Encoded Payload:**
`{rot13_str}`

Lakukan dekoding berurutan (Reverse Pipeline) untuk mengungkap flag aslinya!""",
        state="visible",
        type="standard"
    )
    db.session.add(c_misc2)
    db.session.commit()
    db.session.add(Flags(challenge_id=c_misc2.id, type="static", content="CCA{multi_layer_encoding_pipeline_solved}"))
    db.session.add(Hints(challenge_id=c_misc2.id, content="Gunakan CyberChef dengan urutan Recipe: 1) ROT13, 2) From Base64, 3) From Hex.", cost=25))
    db.session.commit()
    print("[+] Created Misc: Layered Encoding Pipeline (150 pts)")

    # Clear all caches
    clear_challenges()
    clear_standings()
    clear_pages()
    clear_config()
    print("\n=======================================================")
    print(f"[✓] SUCCESS! Created {Challenges.query.count()} fresh challenges across Crypto, Reverse, Pwn, Forensics, OSINT, and Misc.")
    print("    Web category left empty as requested.")
    print("=======================================================")
