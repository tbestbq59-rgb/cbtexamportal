import shutil, sys

path = "index.html"
src = open(path, encoding="utf-8").read()

if "/*usern1*/" in src:
    print("Nothing changed: usern1 is already in index.html.")
    sys.exit(0)

pairs = [
    ("window.sbClient.from('profiles').select('id,full_name,username').then(function(res){if(res.error){profLoaded=false;app.ui.toast('Usernames: '+res.error.message,true);return;}\n      (res.data||[]).forEach(function(p){",
     "/*usern1*/app.api.rpc('admin_profile_names').then(function(rows){\n      (rows||[]).forEach(function(p){"),
    ("      drawList();\n    },function(){});",
     "      drawList();\n    },function(e){profLoaded=false;app.ui.toast('Usernames: '+((e&&e.message)||'failed'),true);});"),
]

for old, new in pairs:
    n = src.count(old)
    if n != 1:
        print("Nothing changed: an anchor was found %d times instead of once. Stopped." % n)
        sys.exit(1)

shutil.copy(path, "index-before-usern1.html")
for old, new in pairs:
    src = src.replace(old, new, 1)
open(path, "w", encoding="utf-8").write(src)
print("Done: USERNAME now reads admin_profile_names. Backup: index-before-usern1.html")
