import shutil
import sys
from pathlib import Path

PATCH = r"""
<!-- RESULTS V2 START -->
<style>
#adm-tab-results .res-sec{display:none!important}
#adm-tab-results .res-sec.rv2-show{display:block!important;background:#fff;border:1px solid var(--border);border-radius:16px;padding:16px;overflow-x:auto}
#adm-tab-results .res-sec.rv2-show table{width:100%;border-collapse:collapse}
#adm-tab-results .res-sec.rv2-show th{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--text-light);font-weight:500;text-align:left;padding:10px 8px;border-bottom:1px solid var(--border)}
#adm-tab-results .res-sec.rv2-show td{padding:14px 8px;border-bottom:1px solid var(--border);font-size:15px}
.rv2-off{display:none!important}
#rv2{max-width:760px;margin:0 auto;font-family:var(--font);color:var(--text)}
#rv2 .rv2-tabs{display:flex;gap:0;padding:6px;border:1px solid var(--border);border-radius:14px;background:#fff;margin-bottom:22px;overflow-x:auto}
#rv2 .rv2-tabs button{flex:1 0 auto;border:0;border-right:1px solid var(--border);background:transparent;padding:14px 14px;font:500 14px var(--font);color:var(--text-light);cursor:pointer;white-space:nowrap}
#rv2 .rv2-tabs button:last-child{border-right:0}
#rv2 .rv2-tabs button.on{background:#e6efe8;color:var(--g);font-weight:600;border-radius:10px;border-right-color:transparent}
#rv2 .rv2-row{display:flex;gap:12px;margin-bottom:16px}
#rv2 .rv2-search{flex:1;display:flex;align-items:center;gap:10px;border:1px solid var(--border);border-radius:14px;background:#fff;padding:0 16px;height:52px}
#rv2 .rv2-search svg,#rv2 .rv2-fbtn svg{flex:none;color:var(--text-light)}
#rv2 .rv2-search input{border:0;outline:0;background:transparent;font:400 16px var(--font);width:100%;color:var(--text)}
#rv2 .rv2-fbtn{display:flex;align-items:center;gap:8px;border:1px solid var(--border);border-radius:14px;background:#fff;padding:0 18px;height:52px;font:500 15px var(--font);color:var(--text);cursor:pointer}
#rv2 .rv2-fpanel{border:1px solid var(--border);border-radius:14px;background:#fff;padding:14px;margin-bottom:16px;display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end}
#rv2 .rv2-fpanel label{display:block;font-size:12px;color:var(--text-light);margin-bottom:4px}
#rv2 .rv2-fpanel select{border:1px solid var(--border);border-radius:10px;padding:9px 10px;font:400 14px var(--font);background:#fff;min-width:150px}
#rv2 .rv2-chips{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:6px 0 22px}
#rv2 .rv2-lab{font-size:15px;color:var(--text-light);margin-right:2px}
#rv2 .rv2-sp{flex:1}
#rv2 .rv2-chip{border:1px solid var(--border);background:#fff;border-radius:12px;padding:9px 16px;font:500 15px var(--font);color:var(--text);cursor:pointer}
#rv2 .rv2-chip.on{background:#e6efe8;border-color:#b6cdbd;color:var(--g-dark)}
#rv2 .rv2-meta{display:flex;justify-content:space-between;align-items:center;font-size:13px;color:var(--text-light);margin-bottom:12px}
#rv2 .rv2-meta button{border:1px solid var(--border);background:#fff;border-radius:10px;padding:7px 12px;font:500 13px var(--font);color:var(--g);cursor:pointer}
#rv2 .rv2-glabel{font-weight:700;font-size:16px;margin:26px 0 14px}
#rv2 .rv2-card{border:1px solid var(--border);border-radius:18px;background:#fff;padding:6px 20px;margin-bottom:6px}
#rv2 .rv2-th,#rv2 .rv2-tr{display:grid;grid-template-columns:1.4fr 1fr auto;gap:12px;align-items:center}
#rv2 .rv2-th{padding:18px 0;border-bottom:1px solid var(--border);font-size:13px;letter-spacing:.06em;color:var(--text-light)}
#rv2 .rv2-th span:last-child,#rv2 .rv2-tr .rv2-r{text-align:right;justify-self:end}
#rv2 .rv2-tr{padding:20px 0;border-bottom:1px solid var(--border);cursor:pointer}
#rv2 .rv2-tr:last-child{border-bottom:0}
#rv2 .rv2-tr:active{background:#f6f9f7}
#rv2 .rv2-nm b{display:block;font-weight:500;font-size:18px;color:var(--text)}
#rv2 .rv2-nm small{display:block;font-size:12px;color:var(--text-light);margin-top:3px}
#rv2 .rv2-un{font-size:18px;color:var(--text-light)}
#rv2 .rv2-gr{font-size:20px;color:var(--text);white-space:nowrap}
#rv2 .rv2-gr i{font-style:normal;color:var(--text-light);margin:0 4px}
#rv2 .rv2-gr b{font-weight:600}
#rv2 .rv2-gr b.hi{color:var(--g)}
#rv2 .rv2-pill{display:inline-block;border-radius:999px;padding:5px 12px;font-size:13px;font-weight:600;background:#f1f5f9;color:var(--text-light)}
#rv2 .rv2-pill.live{background:#e6efe8;color:var(--g)}
#rv2 .rv2-stop{margin-left:8px;border:1px solid #fecaca;background:#fff;color:var(--red);border-radius:10px;padding:6px 12px;font:600 13px var(--font);cursor:pointer}
#rv2 .rv2-empty{border:1px dashed var(--border);border-radius:16px;padding:34px;text-align:center;color:var(--text-light);background:#fff}
@media(max-width:520px){#rv2 .rv2-nm b,#rv2 .rv2-un{font-size:16px}#rv2 .rv2-card{padding:4px 14px}}
</style>
<script>
(function(){
if(window.__rv2Loaded)return;window.__rv2Loaded=true;
var tries=0;
function boot(){
if(typeof app==='undefined'||!app||!app.admin||!app.ui||!app.api){if(++tries<60)setTimeout(boot,300);return;}
var root=document.getElementById('adm-tab-results');if(!root)return;
var A=app.admin;
var E=function(s){return app.ui.esc(s==null?'':String(s));};
var orig={flags:A.loadFlags,reviews:A.loadReviews};
var S={tab:'res',q:'',lvl:'ALL',sort:'recent',sem:'ALL',exam:'ALL',res:[],att:[],cur:[]};
var ob=root.querySelector('button[onclick^="app.admin.resTab"]');
if(ob&&ob.parentElement&&ob.parentElement!==root&&!ob.parentElement.querySelector('.res-sec'))ob.parentElement.classList.add('rv2-off');
var olv=document.getElementById('adm-res-level-tabs');if(olv)olv.classList.add('rv2-off');
var ICON_S='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>';
var ICON_F='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>';
var host=document.createElement('div');host.id='rv2';
host.innerHTML='<div class="rv2-tabs"><button data-t="res" class="on">Scores &amp; Grades</button><button data-t="att">Active Attempts</button><button data-t="flags">Flagged Questions</button><button data-t="reviews">Candidate Reviews</button></div>'
+'<div class="rv2-row" id="rv2-srow"><div class="rv2-search">'+ICON_S+'<input id="rv2-q" type="text" placeholder="Search by name" autocomplete="off"></div><button class="rv2-fbtn" id="rv2-fbtn" type="button">'+ICON_F+'Filter</button></div>'
+'<div class="rv2-fpanel rv2-off" id="rv2-fpanel"><div><label>Semester</label><select id="rv2-sem"><option value="ALL">All semesters</option><option value="First Semester">First Semester</option><option value="Second Semester">Second Semester</option></select></div><div><label>Course</label><select id="rv2-exam"><option value="ALL">All courses</option></select></div><button class="rv2-chip" id="rv2-reset" type="button">Reset</button></div>'
+'<div class="rv2-chips"><span class="rv2-lab">Level</span><button class="rv2-chip on" data-l="ALL">All</button><button class="rv2-chip" data-l="100">100</button><button class="rv2-chip" data-l="200">200</button><button class="rv2-chip" data-l="300">300</button><button class="rv2-chip" data-l="400">400</button><span class="rv2-sp"></span><span id="rv2-sortbox" style="display:contents"><span class="rv2-lab">Sort:</span><button class="rv2-chip on" data-s="recent">Recent</button><button class="rv2-chip" data-s="az">A-Z</button></span></div>'
+'<div class="rv2-meta" id="rv2-meta"><span>Graded on the 5.00 university scale</span><button type="button" id="rv2-exp">Export CSV</button></div>'
+'<div id="rv2-list"><div class="rv2-empty">Loading...</div></div>';
root.insertBefore(host,root.firstChild);
var $=function(id){return document.getElementById(id);};
function grade(p){return p>=70?'A':p>=60?'B':p>=50?'C':p>=45?'D':p>=40?'E':'F';}
function pct(r){var t=Number(r.total)||0;return t?Math.round(Number(r.score)/t*100):0;}
function matches(r,isRes){
if(S.lvl!=='ALL'&&String(r.cand_level)!==S.lvl)return false;
if(S.q){var h=((r.candidate||'')+' '+(r.username||'')).toLowerCase();if(h.indexOf(S.q)<0)return false;}
if(S.exam!=='ALL'&&r.exam!==S.exam)return false;
if(isRes&&S.sem!=='ALL'&&r.semester!==S.sem)return false;
return true;}
function fillExams(){
var seen={},opts='<option value="ALL">All courses</option>';
S.res.concat(S.att).forEach(function(r){if(r.exam&&!seen[r.exam]){seen[r.exam]=1;opts+='<option value="'+E(r.exam)+'">'+E(r.exam)+'</option>';}});
var sel=$('rv2-exam');sel.innerHTML=opts;sel.value=seen[S.exam]?S.exam:'ALL';if(!seen[S.exam])S.exam='ALL';}
function render(){
var el=$('rv2-list');
if(S.tab!=='res'&&S.tab!=='att'){el.innerHTML='';return;}
var isAtt=S.tab==='att';
var list=(isAtt?S.att:S.res).filter(function(r){return matches(r,!isAtt);});
S.cur=[];
if(!list.length){el.innerHTML='<div class="rv2-empty">'+(isAtt?'No attempts found.':'No results found.')+'</div>';return;}
var hasUser=list.some(function(r){return r.username;});
var map={};list.forEach(function(r){(map[r.cand_level]=map[r.cand_level]||[]).push(r);});
var out='';
Object.keys(map).sort(function(a,b){return a-b;}).forEach(function(k){
var rows=map[k];
if(S.sort==='az')rows=rows.slice().sort(function(a,b){return String(a.candidate).localeCompare(String(b.candidate));});
out+='<div class="rv2-glabel">'+E(k)+' Level</div><div class="rv2-card"><div class="rv2-th"><span>NAME</span><span>'+(hasUser?'USERNAME':(isAtt?'LEVEL':'SEMESTER'))+'</span><span>'+(isAtt?'STATUS':'GRADE')+'</span></div>';
rows.forEach(function(r){
var i=S.cur.push(r)-1;
var mid=hasUser?'@'+E(r.username):(isAtt?E(r.cand_level)+'L':E(r.semester));
if(isAtt){
var live=r.status==='in_progress';
out+='<div class="rv2-tr" style="cursor:default"><div class="rv2-nm"><b>'+E(r.candidate)+'</b><small>'+E(r.exam)+'</small></div><div class="rv2-un">'+mid+'</div><div class="rv2-r"><span class="rv2-pill'+(live?' live':'')+'">'+(live?'In progress':E(String(r.status||'').replace('_',' ')))+'</span>'+(live?'<button class="rv2-stop" type="button" onclick="event.stopPropagation();__rv2.stop('+i+')">Stop</button>':'')+'</div></div>';
}else{
var p=pct(r),g=grade(p);
out+='<div class="rv2-tr" onclick="__rv2.sheet('+i+')"><div class="rv2-nm"><b>'+E(r.candidate)+'</b><small>'+E(r.exam)+(r.attempt_no?' · Attempt '+E(r.attempt_no):'')+'</small></div><div class="rv2-un">'+mid+'</div><div class="rv2-r rv2-gr">'+p+'<i>·</i><b class="'+(g==='A'||g==='B'?'hi':'')+'">'+g+'</b></div></div>';
}});
out+='</div>';});
el.innerHTML=out;}
function secFor(sec){
if(sec==='flags'){var f=$('adm-res-flags-list');return f?f.closest('.res-sec'):null;}
if(sec==='reviews')return $('adm-res-reviews');
return null;}
function setTab(sec){
S.tab=sec;
host.querySelectorAll('.rv2-tabs button').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-t')===sec);});
var native=(sec==='flags'||sec==='reviews');
var target=secFor(sec);
root.querySelectorAll('.res-sec').forEach(function(s){var show=native&&s===target;s.classList.toggle('rv2-show',show);if(show)s.classList.remove('hidden');else s.classList.add('hidden');});
$('rv2-srow').classList.toggle('rv2-off',native);
$('rv2-sortbox').style.display=native?'none':'contents';
$('rv2-meta').classList.toggle('rv2-off',sec!=='res');
if(native)$('rv2-fpanel').classList.add('rv2-off');
$('rv2-list').innerHTML=native?'':'<div class="rv2-empty">Loading...</div>';
if(sec==='res')A.loadScores();
else if(sec==='att')A.loadAttempts();
else if(sec==='flags'&&orig.flags)orig.flags.call(A);
else if(sec==='reviews'&&orig.reviews)orig.reviews.call(A);}
function setLevel(l){
S.lvl=String(l);
try{state.adminResLevelFilter=S.lvl;}catch(e){}
host.querySelectorAll('.rv2-chip[data-l]').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-l')===S.lvl);});
if(S.tab==='flags'&&orig.flags)orig.flags.call(A);
else if(S.tab==='reviews'&&orig.reviews)orig.reviews.call(A);
else render();}
A.loadScores=async function(){try{var d=await app.api.rpc('admin_results');S.res=d||[];fillExams();if(S.tab==='res')render();}catch(e){app.ui.toast(e.message||'Could not load results.',true);}};
A.loadAttempts=async function(){try{var d=await app.api.rpc('admin_attempts');S.att=d||[];fillExams();if(S.tab==='att')render();}catch(e){app.ui.toast(e.message||'Could not load attempts.',true);}};
A.resTab=function(sec){setTab(sec||'res');};
A.setResLevelFilter=function(l){setLevel(l);};
window.__rv2={
sheet:function(i){var r=S.cur[i];if(!r)return;
app.ui.modal('<div class="modal-header"><h3 class="font-bold">'+E(r.candidate)+'</h3><button class="modal-close" onclick="app.ui.modal(false)">&times;</button></div><div class="modal-body flex-col gap-3"><p class="text-sm text-gray">'+E(r.exam)+' · '+E(r.score)+'/'+E(r.total)+'</p><button class="btn btn-primary w-full" onclick="__rv2.act('+i+',\'view\')">View / Mark</button><button class="btn btn-secondary w-full" onclick="__rv2.act('+i+',\'grant\')">Grant Attempts</button></div>');},
act:function(i,w){var r=S.cur[i];if(!r)return;app.ui.modal(false);
if(w==='view')A.viewAttempt(r.id);
else A.modals.openGrantAttempt(r.cand_id,r.candidate,r.exam_id);},
stop:function(i){var r=S.cur[i];if(!r)return;if(confirm('Stop this attempt for '+r.candidate+'?'))A.stopAttempt(r.id);}
};
host.querySelectorAll('.rv2-tabs button').forEach(function(b){b.addEventListener('click',function(){setTab(b.getAttribute('data-t'));});});
host.querySelectorAll('.rv2-chip[data-l]').forEach(function(b){b.addEventListener('click',function(){setLevel(b.getAttribute('data-l'));});});
host.querySelectorAll('.rv2-chip[data-s]').forEach(function(b){b.addEventListener('click',function(){S.sort=b.getAttribute('data-s');host.querySelectorAll('.rv2-chip[data-s]').forEach(function(x){x.classList.toggle('on',x===b);});render();});});
$('rv2-q').addEventListener('input',function(){S.q=this.value.trim().toLowerCase();render();});
$('rv2-fbtn').addEventListener('click',function(){$('rv2-fpanel').classList.toggle('rv2-off');});
$('rv2-sem').addEventListener('change',function(){S.sem=this.value;render();});
$('rv2-exam').addEventListener('change',function(){S.exam=this.value;render();});
$('rv2-reset').addEventListener('click',function(){S.sem='ALL';S.exam='ALL';$('rv2-sem').value='ALL';$('rv2-exam').value='ALL';render();});
$('rv2-exp').addEventListener('click',function(){A.exportResults();});
setTab('res');
}
boot();
})();
</script>
<!-- RESULTS V2 END -->
"""

target = Path("index.html")
if not target.exists():
    sys.exit("index.html not found. Run this inside ~/cbtexamportal")

src = target.read_text(encoding="utf-8")

if "RESULTS V2 START" in src:
    sys.exit("Patch already applied. Nothing changed.")

pos = src.rfind("</body>")
if pos == -1:
    sys.exit("No </body> tag found. Nothing changed.")

shutil.copy(target, "index-backup.html")
target.write_text(src[:pos] + PATCH + "\n" + src[pos:], encoding="utf-8")
print("Done. Backup saved as index-backup.html")
