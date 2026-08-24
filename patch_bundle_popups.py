import os

files_to_patch = [
    "CTFd/themes/gameboy-retro/static/assets/index.94b01c79.js",
    "CTFd/themes/core/static/assets/index.94b01c79.js"
]

for file_path in files_to_patch:
    if not os.path.exists(file_path):
        print(f"[-] File not found: {file_path}")
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace displayUnlock
    old_unlock = 'displayUnlock(e){return confirm("Are you sure you\'d like to unlock this hint?")}'
    new_unlock = 'displayUnlock(e){return window.showCyberConfirm?window.showCyberConfirm({title:"Buka Petunjuk (Unlock Hint)",text:"Apakah Anda yakin ingin membuka petunjuk untuk tantangan ini?",highlight:"<i class=\\"fas fa-exclamation-circle text-warning me-1\\"></i> Poin Anda akan dikurangi untuk membuka petunjuk.",confirmText:"Buka Sekarang",cancelText:"Batal",icon:\'<i class="fas fa-lightbulb text-warning"></i>\'}):confirm("Are you sure you\'d like to unlock this hint?")}'

    # 2. Replace displayHintUnlock
    old_hint_unlock = 'displayHintUnlock(e){return confirm("Are you sure you\'d like to unlock this hint?")}'
    new_hint_unlock = 'displayHintUnlock(e){return window.showCyberConfirm?window.showCyberConfirm({title:"Buka Petunjuk (Unlock Hint)",text:"Apakah Anda yakin ingin membuka petunjuk untuk tantangan ini?",highlight:e&&e.cost?("<i class=\\"fas fa-exclamation-circle text-warning me-1\\"></i> Poin Anda akan dikurangi sebesar <strong>"+e.cost+" PTS</strong>."):"<i class=\\"fas fa-check-circle text-success me-1\\"></i> Petunjuk ini gratis (0 PTS).",confirmText:e&&e.cost?("Buka (-"+e.cost+" PTS)"):"Buka Petunjuk",cancelText:"Batal",icon:\'<i class="fas fa-lightbulb text-warning"></i>\'}):confirm("Are you sure you\'d like to unlock this hint?")}'

    # 3. Replace displaySolutionUnlock
    old_sol_unlock = 'displaySolutionUnlock(e){return confirm("Are you sure you\'d like to unlock this solution?")}'
    new_sol_unlock = 'displaySolutionUnlock(e){return window.showCyberConfirm?window.showCyberConfirm({title:"Buka Solusi (Writeup)",text:"Membuka kunci solusi akan menghentikan perolehan poin Anda untuk soal ini.",highlight:"<i class=\\"fas fa-exclamation-triangle text-danger me-1\\"></i> Tindakan ini permanen dan tidak dapat dibatalkan.",confirmText:"Ya, Buka Solusi",cancelText:"Batal",icon:\'<i class="fas fa-unlock text-primary"></i>\'}):confirm("Are you sure you\'d like to unlock this solution?")}'

    # 4. Replace displayHint alert
    old_hint = 'displayHint(e){alert(e.content)}'
    new_hint = 'displayHint(e){return window.showCyberAlert?window.showCyberAlert({title:"Petunjuk Tantangan",text:e.content||e.html||"",buttonText:"Tutup",icon:\'<i class="fas fa-lightbulb text-warning"></i>\'}):alert(e.content)}'

    # 5. Replace displayUnlockError
    old_err = 'displayUnlockError(e){const t=[];Object.keys(e.errors).map(r=>{t.push(e.errors[r])});const n=t.join(`\n`);alert(n)}'
    new_err = 'displayUnlockError(e){const t=[];if(e&&e.errors){Object.keys(e.errors).map(r=>{t.push(e.errors[r])});}const n=t.length?t.join("<br>"):"Gagal membuka petunjuk. Pastikan poin Anda mencukupi!";return window.showCyberAlert?window.showCyberAlert({title:"Gagal Membuka Kunci",text:n,buttonText:"Mengerti",icon:\'<i class="fas fa-times-circle text-danger"></i>\'}):alert(n)}'

    count = 0
    if old_unlock in content:
        content = content.replace(old_unlock, new_unlock)
        count += 1
    if old_hint_unlock in content:
        content = content.replace(old_hint_unlock, new_hint_unlock)
        count += 1
    if old_sol_unlock in content:
        content = content.replace(old_sol_unlock, new_sol_unlock)
        count += 1
    if old_hint in content:
        content = content.replace(old_hint, new_hint)
        count += 1
    if old_err in content:
        content = content.replace(old_err, new_err)
        count += 1

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[+] Patched {count} popup dialogs in {file_path}")
