from CTFd import create_app
from CTFd.models import db, Pages
from CTFd.cache import clear_pages, clear_config, clear_challenges

app = create_app()
with app.app_context():
    Pages.query.filter_by(route='index').delete()
    db.session.commit()
    
    clean_html = """<div class="row justify-content-center">
<div class="col-lg-10 col-md-12 text-center py-2">
<div class="jumbotron py-5 px-4 mb-4">
<div class="d-inline-flex align-items-center gap-2 mb-3">
<span class="badge" style="background: var(--pop-pink); color: #fff; font-size: 0.85rem; font-weight: 800; padding: 6px 16px; border-radius: 9999px; border: var(--pop-border-thin); box-shadow: var(--pop-shadow-sm);">⚡ LIVE COMPETITION</span>
<span class="badge" style="background: var(--pop-yellow); color: #12162a; font-size: 0.85rem; font-weight: 800; padding: 6px 16px; border-radius: 9999px; border: var(--pop-border-thin); box-shadow: var(--pop-shadow-sm);">🎮 NEO ARCADE</span>
</div>
<h1 class="display-4 fw-bold mb-3" style="font-family: var(--font-heading); color: var(--ink-dark); font-size: 3rem; letter-spacing: -1.5px;">WELCOME TO <span style="color: var(--pop-blue);">CTF ARENA</span></h1>
<p class="lead mx-auto mb-4" style="max-width: 680px; font-size: 1.2rem; color: var(--ink-secondary); font-weight: 500;">Pecahkan tantangan keamanan siber, temukan flag tersembunyi, kumpulkan poin, dan raih posisi puncak di leaderboard!</p>
<div class="d-flex justify-content-center gap-3 flex-wrap">
<a href="/challenges" class="btn btn-primary btn-lg px-4 py-3" style="border-radius: 12px; font-size: 1.05rem;"><i class="fas fa-play"></i> MULAI MAIN (CHALLENGES)</a>
<a href="/scoreboard" class="btn btn-outline-primary btn-lg px-4 py-3" style="border-radius: 12px; font-size: 1.05rem; background: #fff;"><i class="fas fa-trophy"></i> LEADERBOARD</a>
</div>
</div>
</div>
</div>"""
    
    p = Pages(title='Home', route='index', content=clean_html, draft=False)
    db.session.add(p)
    db.session.commit()
    clear_pages()
    clear_config()
    print("Recreated index page successfully!")
