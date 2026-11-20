import shutil, sys

P = "index.html"
BAK = "index-before-rsv7.html"

h = open(P, encoding="utf-8").read()

if "/*rsv7*/" in h:
    print("Already applied. Nothing changed.")
    sys.exit(0)

reps = [
    (
        "function uname(r){return r.username||r.cand_username||umap[r.cand_id]||umap[r.candidate]||'-';}",
        "function uname(r){var k='name:'+String(r.candidate||'').trim().toLowerCase();return r.username||r.cand_username||umap[String(r.cand_id)]||umap[k]||'-';}/*rsv7*/",
    ),
    (
        "window.sbClient.from('profiles').select('*').then(function(res){",
        "window.sbClient.from('profiles').select('id,full_name,username').then(function(res){if(res.error){profLoaded=false;app.ui.toast('Usernames: '+res.error.message,true);return;}",
    ),
    (
        "[p.id,p.user_id,p.full_name].forEach(function(k){if(k)umap[k]=u;});",
        "if(p.id)umap[String(p.id)]=u;if(p.full_name)umap['name:'+String(p.full_name).trim().toLowerCase()]=u;",
    ),
]

for old, new in reps:
    if h.count(old) != 1:
        print("Anchor not found exactly once. Nothing changed:")
        print(old[:60])
        sys.exit(1)

shutil.copy2(P, BAK)
for old, new in reps:
    h = h.replace(old, new)
open(P, "w", encoding="utf-8").write(h)
print("Done. Backup saved as " + BAK)
