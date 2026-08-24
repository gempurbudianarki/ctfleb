import os
import sqlite3
from PIL import Image
from CTFd import create_app
from CTFd.models import db, Pages
from CTFd.utils import set_config
from CTFd.cache import clear_pages, clear_config

# 1. Optimize and create lightweight logo
print("[*] Optimizing organization logo...")
src_logo = "logo/logokomunitas.png"
dst_dir = "CTFd/themes/gameboy-retro/static/img"
os.makedirs(dst_dir, exist_ok=True)

if os.path.exists(src_logo):
    img = Image.open(src_logo)
    
    # Calculate aspect ratio for height 90px (high-DPI for 45px navbar)
    target_height = 90
    aspect_ratio = img.width / img.height
    target_width = int(target_height * aspect_ratio)
    
    resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    # Save optimized PNG with maximum compression
    dst_path = os.path.join(dst_dir, "logo_cca.png")
    dst_logo_default = os.path.join(dst_dir, "logo.png")
    
    resized_img.save(dst_path, "PNG", optimize=True)
    resized_img.save(dst_logo_default, "PNG", optimize=True)
    
    orig_kb = os.path.getsize(src_logo) / 1024
    new_kb = os.path.getsize(dst_path) / 1024
    print(f"[+] Logo optimized: {orig_kb:.1f} KB -> {new_kb:.1f} KB (Reduced by {(1 - new_kb/orig_kb)*100:.1f}%)")

# 2. Optimize SQLite Database Performance (WAL Mode + Fast Pragma)
print("[*] Optimizing SQLite database performance...")
db_path = "CTFd/ctfd.db"
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("PRAGMA journal_mode=WAL;")
    cursor.execute("PRAGMA synchronous=NORMAL;")
    cursor.execute("PRAGMA cache_size=10000;")
    cursor.execute("PRAGMA temp_store=MEMORY;")
    conn.commit()
    conn.close()
    print("[+] SQLite configured with WAL mode & high-speed memory cache.")

# 3. Update CTFd configs with Organization Info
app = create_app()
with app.app_context():
    set_config("ctf_name", "CYBERSECURITY COMMUNITY OF ACEH")
    set_config("ctf_description", "Organized by Cybersecurity Community of Aceh (CCA)")
    set_config("ctf_logo", "img/logo_cca.png")
    
    # Update Homepage to feature CCA Branding
    page = Pages.query.filter_by(route="index").first()
    if page:
        home_html = """<div class="row justify-content-center">
<div class="col-lg-10 col-md-12 text-center py-2">
<div class="jumbotron py-5 px-4 mb-4">
<div class="d-inline-flex align-items-center gap-2 mb-3 flex-wrap justify-content-center">
<span class="badge" style="background: var(--pop-blue); color: #fff; font-size: 0.85rem; font-weight: 800; padding: 6px 16px; border-radius: 9999px; border: var(--pop-border-thin); box-shadow: var(--pop-shadow-sm);">🏛️ ORGANIZER: CCA</span>
<span class="badge" style="background: var(--pop-pink); color: #fff; font-size: 0.85rem; font-weight: 800; padding: 6px 16px; border-radius: 9999px; border: var(--pop-border-thin); box-shadow: var(--pop-shadow-sm);">⚡ LIVE COMPETITION</span>
<span class="badge" style="background: var(--pop-yellow); color: #12162a; font-size: 0.85rem; font-weight: 800; padding: 6px 16px; border-radius: 9999px; border: var(--pop-border-thin); box-shadow: var(--pop-shadow-sm);">🎮 NEO ARCADE</span>
</div>
<h1 class="display-4 fw-bold mb-2" style="font-family: var(--font-heading); color: var(--ink-dark); font-size: 2.8rem; letter-spacing: -1px;">
CYBERSECURITY COMMUNITY OF ACEH
</h1>
<p class="lead mx-auto mb-4" style="max-width: 720px; font-size: 1.2rem; color: var(--ink-secondary); font-weight: 500;">
Selamat datang di arena kompetisi CTF resmi diselenggarakan oleh <strong>Cybersecurity Community of Aceh (CCA)</strong>. Pecahkan tantangan, submit flag, dan buktikan keahlian siber Anda!
</p>
<div class="d-flex justify-content-center gap-3 flex-wrap">
<a href="/challenges" class="btn btn-primary btn-lg px-4 py-3" style="border-radius: 12px; font-size: 1.05rem;"><i class="fas fa-play"></i> MULAI TANTANGAN (CHALLENGES)</a>
<a href="/scoreboard" class="btn btn-outline-primary btn-lg px-4 py-3" style="border-radius: 12px; font-size: 1.05rem; background: #fff;"><i class="fas fa-trophy"></i> LEADERBOARD</a>
</div>
</div>

<div class="row g-4 text-start">
<div class="col-md-4">
<div class="card h-100 p-4" style="border-left: 6px solid var(--cat-web);">
<div class="d-flex align-items-center gap-3 mb-2">
<div style="background: #e0e7ff; width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; border: var(--pop-border-thin);"><i class="fas fa-globe" style="color: var(--cat-web); font-size: 1.25rem;"></i></div>
<h4 class="mb-0 fw-bold">Web Exploitation</h4>
</div>
<p class="text-muted mb-0">Uji keamanan web, SQL injection, XSS, dan API hacking.</p>
</div>
</div>
<div class="col-md-4">
<div class="card h-100 p-4" style="border-left: 6px solid var(--cat-crypto);">
<div class="d-flex align-items-center gap-3 mb-2">
<div style="background: #ede9fe; width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; border: var(--pop-border-thin);"><i class="fas fa-key" style="color: var(--cat-crypto); font-size: 1.25rem;"></i></div>
<h4 class="mb-0 fw-bold">Cryptography</h4>
</div>
<p class="text-muted mb-0">Pecahkan cipher klasik hingga modern cryptography.</p>
</div>
</div>
<div class="col-md-4">
<div class="card h-100 p-4" style="border-left: 6px solid var(--cat-reverse);">
<div class="d-flex align-items-center gap-3 mb-2">
<div style="background: #fce7f3; width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; border: var(--pop-border-thin);"><i class="fas fa-microchip" style="color: var(--cat-reverse); font-size: 1.25rem;"></i></div>
<h4 class="mb-0 fw-bold">Reverse Engineering</h4>
</div>
<p class="text-muted mb-0">Bongkar binary, assembly code, dan logic target.</p>
</div>
</div>
</div>
</div>
</div>"""
        page.content = home_html
        db.session.commit()
    
    clear_pages()
    clear_config()
    print("[+] CTFd configured with CCA organization name, logo, and fast cached database.")
