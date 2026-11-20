import os, sys, shutil

SRC = "index.html"
BAK = "index-before-rsv4.html"
START = '<style id="rsv3">'
END = '</body>'
MARK = 'id="rsv4"'

html = open(SRC, encoding="utf-8").read()

if MARK in html:
    print("Patch already applied. Nothing changed.")
    sys.exit(0)
if os.path.exists(BAK):
    print(BAK + " already exists. Rename it first. Nothing changed.")
    sys.exit(1)
if html.count(START) != 1 or html.count(END) != 1:
    print("Anchor not found exactly once. Nothing changed.")
    sys.exit(1)

a = html.index(START)
b = html.index(END)
if a > b:
    print("Anchors out of order. Nothing changed.")
    sys.exit(1)

NEW = r'''<style id="rsv4">
.rs2-hide{display:none!important}
#adm-res-level-tabs{display:none!important}
#adm-tab-results>div:first-child{display:block!important;margin-bottom:0!important}
#adm-tab-results>div:first-child>div:first-child{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr));gap:0;border:1px solid #E0E1E6;border-radius:12px;background:#fff;padding:0;margin:0 0 18px!important;overflow:hidden}
#adm-tab-results>div:first-child>div:first-child>button{border:none!important;border-left:1px solid #E0E1E6!important;border-bottom:none!important;border-radius:0!important;background:transparent!important;padding:14px 4px!important;font-size:12px!important;line-height:1.25;color:#64748b!important;text-align:center;justify-content:center;white-space:normal;box-shadow:none!important;font-weight:500}
#adm-tab-results>div:first-child>div:first-child>button:first-child{border-left:none!important}
#adm-tab-results>div:first-child>div:first-child>button .ico{display:none!important}
#adm-tab-results>div:first-child>div:first-child>button.text-g{background:#e6efe8!important;color:#3d5a4c!important;font-weight:600}
#rv4-head{display:flex;align-items:center;gap:18px;margin:4px 0 22px}
#rv4-head h2{font-size:22px;font-weight:600;color:#1e293b;margin:0;line-height:1.2}
.rv4-bar{display:flex;gap:10px;align-items:center;margin:0 0 18px}
.rv4-sw{flex:1;min-width:0;height:48px;display:flex;align-items:center;gap:10px;border:1px solid #E0E1E6;border-radius:12px;padding:0 14px;background:#fff}
.rv4-search{flex:1;min-width:0;border:none;outline:none;font-size:15px;background:transparent;color:#1e293b}
.rv4-fbtn{height:48px;display:flex;align-items:center;gap:8px;border:1px solid #E0E1E6;background:#fff;border-radius:12px;padding:0 14px;font-weight:600;font-size:15px;color:#1e293b;white-space:nowrap}
.rv4-panel{border:1px solid #E0E1E6;border-radius:12px;padding:12px 14px;margin:0 0 16px;background:#fff}
.rv4-plab{font-size:11px;font-weight:700;letter-spacing:.06em;color:#60646C;margin:0 0 8px}
.rv4-lr{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px 14px;margin:0 0 22px}
.rv4-grp{display:flex;align-items:center;flex-wrap:wrap;gap:6px}
.rv4-lab{font-size:14px;color:#64748b;margin-right:4px;white-space:nowrap}
.rv4-chip{height:36px;min-width:36px;padding:0 10px;border:1px solid #E0E1E6;background:#fff;border-radius:10px;font-size:14px;color:#1e293b;white-space:nowrap}
.rv4-chip.on{background:#e6efe8;border-color:#cfe0d5;color:#3d5a4c;font-weight:600}
.rv4-lvl{font-size:15px;font-weight:700;margin:0 0 10px;color:#1e293b}
.rv4-card{background:#fff;border:1px solid #E0E1E6;border-radius:14px;overflow:hidden;margin:0 0 22px}
.rv4-cols,.rv4-row{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr) 56px 44px;gap:10px;align-items:center;padding:0 18px}
.rv4-cols{height:46px;font-size:12px;font-weight:600;letter-spacing:.06em;color:#60646C;border-bottom:1px solid #EBEBEF}
.rv4-row{min-height:58px;border-top:1px solid #EBEBEF;cursor:pointer;padding-top:12px;padding-bottom:12px}
.rv4-row:first-of-type{border-top:none}
.rv4-r{text-align:right;justify-self:end}
.rv4-n{font-size:15px;font-weight:500;color:#1e293b;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rv4-u{font-size:14px;color:#60646C;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rv4-sc{font-size:15px;font-weight:600;color:#1e293b}
.rv4-gl{font-size:15px;font-weight:700;color:#3d5a4c}
.rv4-empty{padding:24px;text-align:center;color:#60646C}
</style>
<script id="rsv4js">
(function(){
var data=[],umap={},lv='ALL',sort='recent',sem='ALL',q='',show=false,loaded=false,profLoaded=false;
var ICON_FILTER='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1e293b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>';
var ICON_SEARCH='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#60646C" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>';
var ICON_MENU='<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1e293b" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';
function el(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!==undefined)e.textContent=x;return e;}
function pct(r){return r.total?Math.round((r.score/r.total)*100):0;}
function grade(p){try{return app.utils.computeGrade(p).grade;}catch(e){return '';}}
function uname(r){return r.username||r.cand_username||umap[r.cand_id]||umap[r.candidate]||'-';}
function when(r){var v=r.submitted_at||r.finished_at||r.created_at;var d=v?new Date(v):null;return d&&!isNaN(d.getTime())?d.getTime():0;}
function chip(t,on,fn){var b=el('button','rv4-chip'+(on?' on':''),t);b.type='button';b.onclick=fn;return b;}
function head(){
  var tabs=document.getElementById('adm-tab-results');if(!tabs)return;
  if(document.getElementById('rv4-head'))return;
  var h=el('div');h.id='rv4-head';
  h.innerHTML=ICON_MENU+'<h2>Results &amp; Attempts</h2>';
  tabs.insertBefore(h,tabs.firstChild);
}
function mount(){
  var h=document.getElementById('adm-res-res');if(!h)return null;
  head();
  var m=document.getElementById('rv4-root');
  if(!m){m=el('div');m.id='rv4-root';h.insertBefore(m,h.firstChild);}
  Array.prototype.forEach.call(h.children,function(c){if(c!==m)c.classList.add('rs2-hide');});
  return m;
}
function draw(){
  var m=mount();if(!m)return;m.innerHTML='';
  var bar=el('div','rv4-bar');
  var sw=el('div','rv4-sw');sw.innerHTML=ICON_SEARCH;
  var inp=el('input','rv4-search');inp.placeholder='Search by name';inp.value=q;
  inp.oninput=function(){q=inp.value;drawList();};
  sw.appendChild(inp);
  var fb=el('button','rv4-fbtn');fb.type='button';fb.innerHTML=ICON_FILTER+'<span>Filter</span>';
  fb.onclick=function(){show=!show;draw();};
  bar.appendChild(sw);bar.appendChild(fb);m.appendChild(bar);
  if(show){
    var p=el('div','rv4-panel');
    p.appendChild(el('div','rv4-plab','SEMESTER'));
    var w=el('div','rv4-grp');
    [['ALL','All'],['First Semester','First'],['Second Semester','Second']].forEach(function(o){
      w.appendChild(chip(o[1],sem===o[0],function(){sem=o[0];draw();}));});
    p.appendChild(w);m.appendChild(p);
  }
  var lr=el('div','rv4-lr');
  var g1=el('div','rv4-grp');g1.appendChild(el('span','rv4-lab','Level'));
  [['ALL','All'],['100','100'],['200','200'],['300','300'],['400','400']].forEach(function(o){
    g1.appendChild(chip(o[1],lv===o[0],function(){lv=o[0];draw();}));});
  var g2=el('div','rv4-grp');g2.appendChild(el('span','rv4-lab','Sort:'));
  [['recent','Recent'],['az','A-Z']].forEach(function(o){
    g2.appendChild(chip(o[1],sort===o[0],function(){sort=o[0];draw();}));});
  lr.appendChild(g1);lr.appendChild(g2);m.appendChild(lr);
  var list=el('div');list.id='rv4-list';m.appendChild(list);
  drawList();
}
function drawList(){
  var box=document.getElementById('rv4-list');if(!box)return;
  box.innerHTML='';
  var rows=data.slice();
  if(lv!=='ALL')rows=rows.filter(function(r){return String(r.cand_level)===lv;});
  if(sem!=='ALL')rows=rows.filter(function(r){return r.semester===sem;});
  if(q){var s=q.toLowerCase();rows=rows.filter(function(r){return String(r.candidate||'').toLowerCase().indexOf(s)>=0;});}
  if(sort==='az')rows.sort(function(a,b){return String(a.candidate||'').localeCompare(String(b.candidate||''));});
  else rows.sort(function(a,b){return when(b)-when(a);});
  if(!rows.length){box.appendChild(el('div','rv4-empty',loaded?'No results match this filter.':'Loading...'));return;}
  var groups={};
  rows.forEach(function(r){var L=String(r.cand_level||'Other');(groups[L]=groups[L]||[]).push(r);});
  Object.keys(groups).sort().forEach(function(L){
    box.appendChild(el('div','rv4-lvl',L+' Level'));
    var card=el('div','rv4-card');
    var hd=el('div','rv4-cols');
    hd.appendChild(el('span','','NAME'));
    hd.appendChild(el('span','','USERNAME'));
    hd.appendChild(el('span','rv4-r','SCORE'));
    hd.appendChild(el('span','rv4-r','GRADE'));
    card.appendChild(hd);
    groups[L].forEach(function(r){
      var row=el('div','rv4-row');
      row.appendChild(el('span','rv4-n',r.candidate||''));
      row.appendChild(el('span','rv4-u',uname(r)));
      var p=pct(r);
      row.appendChild(el('span','rv4-sc rv4-r',String(p)));
      row.appendChild(el('span','rv4-gl rv4-r',grade(p)));
      row.onclick=function(){app.admin.viewAttempt(r.id);};
      card.appendChild(row);
    });
    box.appendChild(card);
  });
}
function refresh(){
  app.api.rpc('admin_results').then(function(d){
    data=Array.isArray(d)?d:[];loaded=true;draw();
  },function(){loaded=true;draw();});
  if(!profLoaded){
    profLoaded=true;
    window.sbClient.from('profiles').select('*').then(function(res){
      (res.data||[]).forEach(function(p){
        var u=p.username||'';
        [p.id,p.user_id,p.full_name].forEach(function(k){if(k)umap[k]=u;});
      });
      drawList();
    },function(){});
  }
}
if(app.admin&&app.admin.loadScores&&!app.admin.loadScores.__rv4){
  var orig=app.admin.loadScores;
  var wrapped=function(){
    var p=orig.apply(this,arguments);
    return Promise.resolve(p).then(function(){refresh();});
  };
  wrapped.__rv4=true;
  app.admin.loadScores=wrapped;
}
setInterval(function(){
  if(document.getElementById('adm-res-res')&&!document.getElementById('rv4-root'))draw();
},800);
setTimeout(function(){refresh();},600);
})();
</script>
'''

out = html[:a] + NEW + html[b:]
shutil.copy2(SRC, BAK)
open(SRC, "w", encoding="utf-8").write(out)
print("Done. Backup saved as " + BAK)
