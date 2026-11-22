import shutil, sys

path = "index.html"
src = open(path, encoding="utf-8").read()

if "/*aa1*/" in src:
    print("Nothing changed: aa1 is already in index.html.")
    sys.exit(0)

anchor = "</body>"
n = src.count(anchor)
if n != 1:
    print("Nothing changed: </body> found %d times instead of once. Stopped." % n)
    sys.exit(1)

css = r'''
.aa-wrap{max-width:100%;overflow-x:hidden;}
.aa-card{background:#fff;border:1px solid #E0E1E6;border-radius:12px;padding:16px;margin-bottom:16px;}
.aa-card h4{margin:0 0 12px;font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:#64748b;font-weight:600;}
.aa-table{background:#fff;border:1px solid #E0E1E6;border-radius:12px;overflow:hidden;}
.aa-head,.aa-row{display:grid;grid-template-columns:1.3fr .8fr 1fr 1fr;align-items:center;gap:8px;padding:14px 16px;font-size:14px;color:#1e293b;}
.aa-head{font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:#64748b;border-bottom:1px solid #E0E1E6;}
.aa-row{border-bottom:1px solid #E0E1E6;}
.aa-row:last-child{border-bottom:none;}
.aa-link{background:none;border:none;padding:0;font:inherit;font-weight:600;color:#3d5a4c;text-decoration:underline;text-underline-offset:3px;cursor:pointer;}
.aa-num{text-align:center;}
.aa-page-head{display:flex;align-items:center;gap:12px;margin:0 0 16px;}
.aa-back{width:40px;height:40px;border:1px solid #E0E1E6;background:#fff;border-radius:10px;display:flex;align-items:center;justify-content:center;cursor:pointer;flex:none;}
.aa-title{font-size:18px;font-weight:700;color:#1e293b;margin:0;}
.aa-sub{font-size:13px;color:#64748b;margin:2px 0 0;}
.aa-kv{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.aa-kv span{display:block;font-size:12px;color:#64748b;}
.aa-kv b{font-size:15px;color:#1e293b;font-weight:600;}
.aa-badge{display:inline-block;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:600;background:#e6efe8;color:#3d5a4c;}
.aa-badge.paused{background:#fff;border:1px solid #3d5a4c;}
.aa-badge.closed{background:#f1f5f9;color:#475569;}
.aa-list-row{display:grid;grid-template-columns:1.2fr 1fr .8fr;align-items:center;gap:8px;padding:12px 16px;border-bottom:1px solid #E0E1E6;font-size:14px;color:#1e293b;}
.aa-list-row:last-child{border-bottom:none;}
.aa-student{display:grid;grid-template-columns:1fr auto;align-items:center;gap:12px;padding:12px 16px;border-bottom:1px solid #E0E1E6;}
.aa-student:last-child{border-bottom:none;}
.aa-name{font-weight:600;color:#1e293b;font-size:14px;overflow-wrap:anywhere;}
.aa-user{font-size:12px;color:#64748b;overflow-wrap:anywhere;}
.aa-btn{height:36px;min-width:84px;padding:0 14px;border-radius:8px;border:1px solid #E0E1E6;background:#fff;color:#1e293b;font-size:13px;font-weight:600;cursor:pointer;}
.aa-btn.primary{background:#3d5a4c;border-color:#3d5a4c;color:#fff;}
.aa-btn.danger{color:#b91c1c;border-color:#fecaca;}
.aa-btn:disabled{opacity:.5;cursor:not-allowed;}
.aa-stop{width:100%;height:48px;margin-top:8px;}
.aa-confirm{background:#fff;border:1px solid #E0E1E6;border-radius:12px;padding:16px;margin-top:12px;}
.aa-confirm p{margin:0 0 14px;font-size:14px;color:#1e293b;line-height:1.5;}
.aa-actions{display:flex;gap:10px;}
.aa-actions .aa-btn{flex:1;}
.aa-empty{padding:24px 16px;text-align:center;color:#64748b;font-size:14px;}
.aa-notice{padding:12px 14px;border:1px solid #E0E1E6;border-left:3px solid #3d5a4c;border-radius:10px;background:#fff;font-size:14px;color:#1e293b;line-height:1.5;margin:12px 0;}
.aa-closed-msg{text-align:center;padding:32px 16px;font-size:16px;font-weight:600;color:#1e293b;}
@media (max-width:480px){
  .aa-head,.aa-row{grid-template-columns:1.2fr .7fr 1fr 1fr;font-size:13px;padding:12px;gap:6px;}
  .aa-head{font-size:11px;}
  .aa-kv{grid-template-columns:1fr;}
  .aa-list-row{grid-template-columns:1fr .9fr;font-size:13px;padding:12px;}
  .aa-title{font-size:16px;}
}
'''

block = '<style id="aa1">/*aa1*/' + css + '</style>\n'

shutil.copy(path, "index-before-aa1.html")
src = src.replace(anchor, block + anchor, 1)
open(path, "w", encoding="utf-8").write(src)
print("Done: Active Attempts styles added. Backup: index-before-aa1.html")
