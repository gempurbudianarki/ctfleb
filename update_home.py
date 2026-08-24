from CTFd import create_app
from CTFd.models import db, Pages
from CTFd.cache import clear_pages, clear_config, clear_challenges

app = create_app()
with app.app_context():
    Pages.query.filter_by(route='index').delete()
    db.session.commit()
    
    advanced_html = """<div class="row justify-content-center">
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
        <div col="col-6 col-md-3" class="col-6 col-md-3">
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
    
    p = Pages(title='Home', route='index', content=advanced_html, draft=False, format='html')
    db.session.add(p)
    db.session.commit()
    clear_pages()
    clear_config()
    print("[+] Advanced High-Tech Cyber Homepage created successfully!")
