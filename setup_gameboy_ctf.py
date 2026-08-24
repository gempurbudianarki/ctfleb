import os
import sys
from CTFd import create_app
from CTFd.models import db, Admins, Users, Pages, Challenges, Flags, Hints, Solves
from CTFd.utils import set_config, get_config
from CTFd.cache import clear_config, clear_challenges, clear_pages, clear_standings

app = create_app()

with app.app_context():
    print("[*] Initializing CTFd with Retro Game Boy configuration...")
    
    # 1. CTF General Config
    set_config("ctf_name", "CYBERSECURITY COMMUNITY OF ACEH")
    set_config("ctf_description", "Organized by Cybersecurity Community of Aceh (CCA)")
    set_config("ctf_logo", "img/logo_cca.png")
    set_config("user_mode", "users")
    set_config("ctf_theme", "gameboy-retro")
    set_config("theme_header", "")
    set_config("theme_settings", None)
    
    # 2. Visibilities
    set_config("challenge_visibility", "public")
    set_config("account_visibility", "public")
    set_config("score_visibility", "public")
    set_config("registration_visibility", "public")
    set_config("verify_emails", False)
    set_config("setup", True)
    
    # 3. Create Admin Account if not exists
    admin = Admins.query.filter_by(name="admin").first()
    if not admin:
        admin = Admins(
            name="admin",
            email="admin@ctf.local",
            password="admin",
            type="admin",
            hidden=True
        )
        db.session.add(admin)
        db.session.commit()
        print("[+] Created Admin: admin / admin")
    else:
        print("[*] Admin user already exists.")

    # 4. Create Home Index Page
    page = Pages.query.filter_by(route="index").first()
    index_html = """<div class="row justify-content-center">
  <div class="col-lg-11 col-md-12 text-center py-2">

    <!-- Cyber Hero Jumbotron -->
    <div class="jumbotron py-5 px-4 mb-4 position-relative overflow-hidden" style="border-radius: 20px;">
      <div class="d-inline-flex align-items-center gap-2 mb-3 flex-wrap justify-content-center">
        <span class="badge" style="background: var(--pop-blue); color: #fff; font-size: 0.85rem; font-weight: 800; padding: 7px 18px; border-radius: 9999px; border: var(--pop-border-thin); box-shadow: var(--pop-shadow-sm);">🏛️ ORGANIZER: CCA</span>
        <span class="badge" style="background: var(--pop-pink); color: #fff; font-size: 0.85rem; font-weight: 800; padding: 7px 18px; border-radius: 9999px; border: var(--pop-border-thin); box-shadow: var(--pop-shadow-sm);"><i class="fas fa-bolt me-1"></i> LIVE COMPETITION</span>
        <span class="badge" style="background: var(--pop-yellow); color: #12162a; font-size: 0.85rem; font-weight: 800; padding: 7px 18px; border-radius: 9999px; border: var(--pop-border-thin); box-shadow: var(--pop-shadow-sm);">🎮 NEO ARCADE</span>
      </div>

      <h1 class="display-4 fw-bold mb-3" style="font-family: var(--font-heading); color: var(--ink-dark); font-size: 3.1rem; letter-spacing: -1px; line-height: 1.15;">
        CYBERSECURITY COMMUNITY <br class="d-none d-md-block"><span style="color: var(--pop-blue);">OF ACEH (CCA)</span>
      </h1>

      <p class="lead mx-auto mb-4" style="max-width: 760px; font-size: 1.2rem; color: var(--ink-secondary); font-weight: 500; line-height: 1.6;">
        Selamat datang di arena kompetisi Capture The Flag resmi diselenggarakan oleh <strong>Cybersecurity Community of Aceh</strong>. Pecahkan teka-teki keamanan siber, submit flag, dan rebut posisi puncak leaderboard!
      </p>

      <div class="d-flex justify-content-center gap-3 flex-wrap mb-4">
        <a href="/challenges" class="btn btn-primary btn-lg px-4 py-3 fw-bold" style="border-radius: 12px; font-size: 1.05rem;">
          <i class="fas fa-play me-2"></i> MULAI TANTANGAN (CHALLENGES)
        </a>
        <a href="/scoreboard" class="btn btn-outline-primary btn-lg px-4 py-3 fw-bold" style="border-radius: 12px; font-size: 1.05rem; background: var(--card-bg);">
          <i class="fas fa-trophy me-2"></i> LEADERBOARD REAL-TIME
        </a>
      </div>

      <!-- Quick Ticker Stats Bar -->
      <div class="row g-2 justify-content-center pt-2">
        <div class="col-6 col-md-3">
          <div class="p-3 bg-white border rounded-3" style="border: var(--pop-border-thin) !important; box-shadow: var(--pop-shadow-sm);">
            <div style="font-size: 1.4rem; font-weight: 900; color: var(--pop-blue); font-family: var(--font-mono);">7</div>
            <div style="font-size: 0.78rem; font-weight: 700; color: var(--ink-muted); text-transform: uppercase;">Kategori Soal</div>
          </div>
        </div>
        <div class="col-6 col-md-3">
          <div class="p-3 bg-white border rounded-3" style="border: var(--pop-border-thin) !important; box-shadow: var(--pop-shadow-sm);">
            <div style="font-size: 1.4rem; font-weight: 900; color: var(--pop-pink); font-family: var(--font-mono);">1,000+</div>
            <div style="font-size: 0.78rem; font-weight: 700; color: var(--ink-muted); text-transform: uppercase;">Total Poin</div>
          </div>
        </div>
        <div class="col-6 col-md-3">
          <div class="p-3 bg-white border rounded-3" style="border: var(--pop-border-thin) !important; box-shadow: var(--pop-shadow-sm);">
            <div style="font-size: 1.4rem; font-weight: 900; color: var(--pop-teal); font-family: var(--font-mono);">LIVE</div>
            <div style="font-size: 0.78rem; font-weight: 700; color: var(--ink-muted); text-transform: uppercase;">SSE Telemetry</div>
          </div>
        </div>
        <div class="col-6 col-md-3">
          <div class="p-3 bg-white border rounded-3" style="border: var(--pop-border-thin) !important; box-shadow: var(--pop-shadow-sm);">
            <div style="font-size: 1.4rem; font-weight: 900; color: var(--pop-yellow); font-family: var(--font-mono);">CTF{...}</div>
            <div style="font-size: 0.78rem; font-weight: 700; color: var(--ink-muted); text-transform: uppercase;">Format Flag</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Category Highlights Grid -->
    <div class="row g-4 text-start mb-5">
      <div class="col-md-4">
        <div class="card h-100 p-4" style="border-left: 6px solid var(--cat-web); border-radius: 16px;">
          <div class="d-flex align-items-center gap-3 mb-2">
            <div style="background: rgba(37, 99, 235, 0.12); width: 46px; height: 46px; border-radius: 12px; display: flex; align-items: center; justify-content: center; border: var(--pop-border-thin); font-size: 1.3rem;">🌐</div>
            <h4 class="mb-0 fw-bold" style="font-family: var(--font-heading);">Web Exploitation</h4>
          </div>
          <p class="text-muted mb-0" style="font-size: 0.95rem;">Uji kerentanan web security, SQL injection, XSS, SSRF, authentication bypass, dan API security.</p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card h-100 p-4" style="border-left: 6px solid var(--cat-crypto); border-radius: 16px;">
          <div class="d-flex align-items-center gap-3 mb-2">
            <div style="background: rgba(124, 58, 237, 0.12); width: 46px; height: 46px; border-radius: 12px; display: flex; align-items: center; justify-content: center; border: var(--pop-border-thin); font-size: 1.3rem;">🔐</div>
            <h4 class="mb-0 fw-bold" style="font-family: var(--font-heading);">Cryptography</h4>
          </div>
          <p class="text-muted mb-0" style="font-size: 0.95rem;">Pecahkan sandi klasik, enkripsi modern, RSA, AES, modulo arithmetic, dan algoritma hash custom.</p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card h-100 p-4" style="border-left: 6px solid var(--cat-reverse); border-radius: 16px;">
          <div class="d-flex align-items-center gap-3 mb-2">
            <div style="background: rgba(219, 39, 119, 0.12); width: 46px; height: 46px; border-radius: 12px; display: flex; align-items: center; justify-content: center; border: var(--pop-border-thin); font-size: 1.3rem;">⚡</div>
            <h4 class="mb-0 fw-bold" style="font-family: var(--font-heading);">Reverse Engineering</h4>
          </div>
          <p class="text-muted mb-0" style="font-size: 0.95rem;">Dekompresi binary, analisis instruksi assembly, decompile bytecode, dan bongkar logika verifikasi ROM.</p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card h-100 p-4" style="border-left: 6px solid var(--cat-pwn); border-radius: 16px;">
          <div class="d-flex align-items-center gap-3 mb-2">
            <div style="background: rgba(220, 38, 38, 0.12); width: 46px; height: 46px; border-radius: 12px; display: flex; align-items: center; justify-content: center; border: var(--pop-border-thin); font-size: 1.3rem;">💥</div>
            <h4 class="mb-0 fw-bold" style="font-family: var(--font-heading);">Binary Exploitation</h4>
          </div>
          <p class="text-muted mb-0" style="font-size: 0.95rem;">Buffer overflow, format string exploit, ROP chain, dan manipulasi alur eksekusi memori.</p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card h-100 p-4" style="border-left: 6px solid var(--cat-forensics); border-radius: 16px;">
          <div class="d-flex align-items-center gap-3 mb-2">
            <div style="background: rgba(5, 150, 105, 0.12); width: 46px; height: 46px; border-radius: 12px; display: flex; align-items: center; justify-content: center; border: var(--pop-border-thin); font-size: 1.3rem;">🔍</div>
            <h4 class="mb-0 fw-bold" style="font-family: var(--font-heading);">Digital Forensics</h4>
          </div>
          <p class="text-muted mb-0" style="font-size: 0.95rem;">Analisis packet PCAP, ekstraksi artefak memori dump, steganografi gambar, dan rekonstruksi file.</p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card h-100 p-4" style="border-left: 6px solid var(--cat-osint); border-radius: 16px;">
          <div class="d-flex align-items-center gap-3 mb-2">
            <div style="background: rgba(217, 119, 6, 0.12); width: 46px; height: 46px; border-radius: 12px; display: flex; align-items: center; justify-content: center; border: var(--pop-border-thin); font-size: 1.3rem;">🛰️</div>
            <h4 class="mb-0 fw-bold" style="font-family: var(--font-heading);">OSINT & Misc</h4>
          </div>
          <p class="text-muted mb-0" style="font-size: 0.95rem;">Investigasi jejak digital sumber terbuka, geolokasi satelit, metadata rahasia, dan teka-teki logika.</p>
        </div>
      </div>
    </div>

    <!-- Cyber Terminal Command Snippet -->
    <div class="card p-0 text-start shadow-sm mb-4" style="border-radius: 16px; border: var(--pop-border); overflow: hidden; background: #0f172a; color: #f8fafc;">
      <div class="p-3 d-flex align-items-center justify-content-between" style="background: #1e293b; border-bottom: 1.5px solid #334155;">
        <div class="d-flex align-items-center gap-2">
          <span style="width: 12px; height: 12px; border-radius: 50%; background: #ef4444; display: inline-block;"></span>
          <span style="width: 12px; height: 12px; border-radius: 50%; background: #f59e0b; display: inline-block;"></span>
          <span style="width: 12px; height: 12px; border-radius: 50%; background: #10b981; display: inline-block;"></span>
          <span class="ms-2 fw-bold" style="font-family: var(--font-mono); font-size: 0.85rem; color: #94a3b8;">bash - terminal@cca-ctf</span>
        </div>
        <span class="badge" style="background: #334155; color: #38bdf8; font-family: var(--font-mono); font-size: 0.75rem;">RULES & PROTOCOL</span>
      </div>
      <div class="p-4" style="font-family: var(--font-mono); font-size: 0.95rem; line-height: 1.7;">
        <div style="color: #38bdf8;">root@cca-ctf:~# ./rules_and_protocol.sh</div>
        <div style="color: #94a3b8;" class="mt-2">> 1. Format Flag: <span style="color: #facc15; font-weight: 700;">CTF{string_jawaban}</span> atau <span style="color: #facc15; font-weight: 700;">CCA{...}</span></div>
        <div style="color: #94a3b8;">> 2. Dilarang melakukan serangan DoS / Brute-force terhadap server infrastruktur platform.</div>
        <div style="color: #94a3b8;">> 3. Dilarang membagikan jawaban/flag ke peserta lain selama kompetisi aktif.</div>
        <div style="color: #34d399;" class="mt-2">> [STATUS] System ready. Happy Hacking and Good Luck! 🚀</div>
      </div>
    </div>

  </div>
</div>"""
    if not page:
        page = Pages(title="Home", route="index", content=index_html, draft=False)
        db.session.add(page)
    else:
        page.content = index_html
    db.session.commit()
    print("[+] Configured Index Page.")

    # 5. Create Sample Challenges for Demonstration if empty
    if Challenges.query.count() == 0:
        sample_chals = [
            ("Pocket Inspector", "Web", 100, "Inspect the retro cartridge source code to find the hidden flag token in the header.", "CTF{w3b_1nsp3ct0r_8b1t}"),
            ("Caesar 1989", "Crypto", 100, "Decrypt this ancient Game Boy shift cipher message: `FWI{u3wu0_g4m3b0b_1989}`.", "CTF{r3tr0_g4m3b0y_1989}"),
            ("Chiptune Keygen", "Reverse", 200, "Decompile the ROM binary and reverse-engineer the passcode validation logic.", "CTF{r0m_d3c0mp1l3d_succ3ss}"),
            ("Buffer Overbite", "Pwn", 300, "Overflow the high score stack buffer to overwrite the instruction pointer.", "CTF{st4ck_0v3rfl0w_m4st3r}"),
            ("Pixel Memory Dump", "Forensics", 150, "Analyze the extracted VRAM framebuffer dump to recover the deleted sprite flag.", "CTF{vr4m_m3m0ry_r3c0v3r}"),
            ("Arcade Cartridge Geolocation", "OSINT", 100, "Find the exact arcade museum location where this prototype DMG-01 was photographed.", "CTF{4rc4d3_mus3um_k0t4}"),
            ("Secret Cheat Code", "Misc", 50, "Enter the classic Konami code: UP UP DOWN DOWN LEFT RIGHT LEFT RIGHT B A.", "CTF{k0n4m1_c0d3_unl0ck3d}")
        ]

        for name, cat, val, desc, flag_val in sample_chals:
            chal = Challenges(
                name=name,
                category=cat,
                description=desc,
                value=val,
                state="visible",
                type="standard"
            )
            db.session.add(chal)
            db.session.commit()

            flag = Flags(
                challenge_id=chal.id,
                type="static",
                content=flag_val
            )
            db.session.add(flag)
            db.session.commit()
        print(f"[+] Created {len(sample_chals)} sample retro challenges.")

        # Create 3 sample demo players for scoreboard
        demo_players = [
            ("PIXEL_HERO", "pixel@ctf.local", "password"),
            ("RETRO_GHOST", "ghost@ctf.local", "password"),
            ("CHIP_WARRIOR", "chip@ctf.local", "password"),
        ]
        for pname, pemail, ppass in demo_players:
            puser = Users(name=pname, email=pemail, password=ppass, verified=True)
            db.session.add(puser)
            db.session.commit()

            # Award solves to create a live High Score ranking
            all_chals = Challenges.query.all()
            if pname == "PIXEL_HERO":
                for c in all_chals[:4]:
                    db.session.add(Solves(user_id=puser.id, challenge_id=c.id, ip="127.0.0.1"))
            elif pname == "RETRO_GHOST":
                for c in all_chals[:2]:
                    db.session.add(Solves(user_id=puser.id, challenge_id=c.id, ip="127.0.0.1"))
            elif pname == "CHIP_WARRIOR":
                for c in all_chals[:1]:
                    db.session.add(Solves(user_id=puser.id, challenge_id=c.id, ip="127.0.0.1"))
            db.session.commit()
        print("[+] Created sample scoreboard players & solve records.")

    # 6. Clear all caches
    clear_config()
    clear_challenges()
    clear_pages()
    clear_standings()
    print("[*] Setup complete! Theme active: gameboy-retro")
