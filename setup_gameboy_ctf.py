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
    set_config("ctf_name", "RETRO GAME BOY CTF")
    set_config("ctf_description", "Monochrome 8-Bit Cyber Security Competition")
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
    index_html = """
<div class="row justify-content-center">
  <div class="col-md-10 text-center py-4">
    <div class="arcade-monitor-frame mb-4">
      <div class="monitor-header">
        <span class="monitor-dot"></span>
        <span class="monitor-title">SYSTEM READY // INSERT COIN</span>
        <span class="monitor-dot"></span>
      </div>
      <div class="py-4">
        <h1 style="font-size: 32px; letter-spacing: 4px; margin-bottom: 20px;">★ GAME BOY CTF 1989 ★</h1>
        <p style="font-size: 24px; color: var(--gb-darkest); max-width: 700px; margin: 0 auto 24px;">
          WELCOME TO THE 8-BIT MONOCHROME CYBER ARENA. CHOOSE YOUR CHALLENGES, SUBMIT FLAGS, AND CLIMB TO THE TOP OF THE HIGH SCORES!
        </p>
        <div class="d-flex justify-content-center gap-3 flex-wrap">
          <a href="/challenges" class="btn btn-primary" style="font-size: 14px; padding: 14px 24px;">
            ▶ START GAME
          </a>
          <a href="/scoreboard" class="btn btn-outline-primary" style="font-size: 14px; padding: 14px 24px;">
            ★ HIGH SCORES
          </a>
        </div>
      </div>
    </div>
  </div>
</div>
"""
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
