import os, shutil

SRC = "index.html"
BAK = "index-before-rsv6.html"
S = '<style id="rsv4">'
J = '<script id="rsv4js">'

html = open(SRC, encoding="utf-8").read()

if 'id="rsv6"' in html:
    print("Already applied. Nothing changed.")
    raise SystemExit(0)
if os.path.exists(BAK):
    print(BAK + " already exists. Move it first. Nothing changed.")
    raise SystemExit(1)
if html.count(S) != 1 or html.count(J) != 1:
    print("Anchor not found exactly once. Nothing changed.")
    raise SystemExit(1)

a = html.index(S)
j = html.index(J)
if a > j:
    print("Anchors out of order. Nothing changed.")
    raise SystemExit(1)
end = html.index("</script>", j) + len("</script>")

NEW = r'''<style id="rsv6">
#adm-tab-results>div:first-child{display:none!important}
#rv6-tabs{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border:1px solid #E0E1E6;border-radius:14px;background:#fff;overflow:hidden;margin:0 0 18px}
.rv6-tab{border:none;border-left:1px solid #E0E1E6;background:transparent;padding:14px 4px;font-size:13px;line-height:1.25;color:#64748b;font-weight:500;text-align:center;cursor:pointer}
.rv6-tab:first-child{border-left:none}
.rv6-tab.on{background:#e6efe8;color:#3d5a4c;font-weight:600}
.rs2-hide{display:none!important}
.rv6-bar{display:flex;gap:10px;align-items:center;margin:0 0 18px}
.rv6-sw{flex:1;min-width:0;height:48px;display:flex;align-items:center;gap:10px;border:1px solid #E0E1E6;border-radius:12px;padding:0 14px;background:#fff}
.rv6-search{flex:1;min-width:0;border:none;outline:none;font-size:15px;background:transparent;color:#1e293b}
.rv6-fbtn{height:48px;display:flex;align-items:center;gap:8px;border:1px solid #E0E1E6;background:#fff;border-radius:12px;padding:0 14px;font-weight:600;font-size:15px;color:#1e293b;white-space:nowrap}
.rv6-panel{border:1px solid #E0E1E6;border-radius:12px;padding:12px 14px;margin:0 0 16px;background:#fff}
.rv6-plab{font-size:11px;font-weight:700;letter-spacing:.06em;color:#60646C;margin:0 0 8px}
.rv6-lr{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:12px 16px;margin:0 0 22px}
.rv6-grp{display:flex;align-items:center;flex-wrap:wrap;gap:6px}
.rv6-lab{font-size:14px;color:#64748b;margin-right:4px;white-space:nowrap}
.rv6-chip{height:36px;min-width:36px;padding:0 10px;border:1px solid #E0E1E6;background:#fff;border-radius:10px;font-size:14px;color:#1e293b}
.rv6-chip.on{background:#e6efe8;border-color:#cfe0d5;color:#3d5a4c;font-weight:600}
.rv6-lvl{font-size:16px;font-weight:700;margin:0 0 10px;color:#1e293b}
.rv6-card{border:1px solid #E0E1E6;border-radius:14px;background:#fff;overflow:hidden;margin:0 0 14px}
.rv6-cols,.rv6-row{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr) 60px 50px;gap:10px;align-items:center;padding:0 16px}
.rv6-cols{height:46px;font-size:12px;font-weight:600;letter-spacing:.06em;color:#60646C;border-bottom:1px solid #EBEBEF}
.rv6-row{min-height:58px;padding-top:12px;padding-bottom:12px;border-top:1px solid #EBEBEF;cursor:pointer}
.rv6-r{text-align:right;justify-self:end}
.rv6-n{font-size:15px;font-weight:500;color:#1e293b;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rv6-u{font-size:14px;color:#60646C;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rv6-sc{font-size:15px;font-weight:600;color:#1e293b}
.rv6-g{font-size:15px;font-weight:700;color:#3d5a4c}
.rv6-g.f{color:#1e293b}
.rv6-export{display:block;margin:0 0 24px auto;border:1px solid #E0E1E6;background:#fff;border-radius:10px;padding:8px 12px;font-size:14px;color:#1e293b}
.rv6-empty{padding:24px;text-align:center;color:#60646C}
</style>
<script id="rsv6js">
(function(){
var TABS=[['res','Scores & Grades'],['att','Active Attempts'],['flags','Flagged Questions'],['reviews','Candidate Reviews']];
var data=[],umap={},lv='ALL',sort='recent',sem='ALL',q='',show=false,loaded=false,profLoaded=false,active='res';
var I_SEARCH='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>';
var I_FILTER='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1e293b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>';
function el(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!==undefined)e.textContent=x;return e;}
function pct(r){return r.total?Math.round((r.score/r.total)*100):0;}
function grade(p){try{return app.utils.computeGrade(p).grade;}catch(e){return '';}}
function uname(r){return r.username||r.cand_username||umap[r.cand_id]||umap[r.candidate]||'-';}
function when(r){var v=r.submitted_at||r.finished_at||r.created_at;var d=v?new Date(v):null;return d&&!isNaN(d.getTime())?d.getTime():0;}
function chip(t,on,fn){var b=el('button','rv6-chip'+(on?' on':''),t);b.type='button';b.onclick=fn;return b;}

function tabs(){
  var host=document.getElementById('adm-tab-results');if(!host)return;
  var w=document.getElementById('rv6-tabs');
  if(!w){w=el('div');w.id='rv6-tabs';host.insertBefore(w,host.children[1]||null);}
  w.innerHTML='';
  TABS.forEach(function(t){
    var b=el('button','rv6-tab'+(active===t[0]?' on':''),t[1]);b.type='button';
    b.onclick=function(){app.admin.resTab(t[0],null);};
    w.appendChild(b);
  });
}
function mount(){
  var h=document.getElementById('adm-res-res');if(!h)return null;
  var m=document.getElementById('rv6-root');
  if(!m){m=el('div');m.id='rv6-root';h.insertBefore(m,h.firstChild);}
  Array.prototype.forEach.call(h.children,function(c){if(c!==m)c.classList.add('rs2-hide');});
  return m;
}
function draw(){
  var m=mount();if(!m)return;m.innerHTML='';
  var bar=el('div','rv6-bar');
  var sw=el('div','rv6-sw');sw.innerHTML=I_SEARCH;
  var inp=el('input','rv6-search');inp.placeholder='Search by name';inp.value=q;
  inp.oninput=function(){q=inp.value;drawList();};
  sw.appendChild(inp);
  var fb=el('button','rv6-fbtn');fb.type='button';fb.innerHTML=I_FILTER+'<span>Filter</span>';
  fb.onclick=function(){show=!show;draw();};
  bar.appendChild(sw);bar.appendChild(fb);m.appendChild(bar);
  if(show){
    var p=el('div','rv6-panel');
    p.appendChild(el('div','rv6-plab','SEMESTER'));
    var w=el('div','rv6-grp');
    [['ALL','All'],['First Semester','First'],['Second Semester','Second']].forEach(function(o){
      w.appendChild(chip(o[1],sem===o[0],function(){sem=o[0];draw();}));});
    p.appendChild(w);m.appendChild(p);
  }
  var lr=el('div','rv6-lr');
  var g1=el('div','rv6-grp');g1.appendChild(el('span','rv6-lab','Level'));
  [['ALL','All'],['100','100'],['200','200'],['300','300'],['400','400']].forEach(function(o){
    g1.appendChild(chip(o[1],lv===o[0],function(){lv=o[0];draw();}));});
  var g2=el('div','rv6-grp');g2.appendChild(el('span','rv6-lab','Sort:'));
  [['recent','Recent'],['az','A-Z']].forEach(function(o){
    g2.appendChild(chip(o[1],sort===o[0],function(){sort=o[0];draw();}));});
  lr.appendChild(g1);lr.appendChild(g2);m.appendChild(lr);
  var list=el('div');list.id='rv6-list';m.appendChild(list);
  var ex=el('button','rv6-export','Export CSV');ex.type='button';
  ex.onclick=function(){app.admin.exportResults();};
  m.appendChild(ex);
  drawList();
}
function drawList(){
  var box=document.getElementById('rv6-list');if(!box)return;
  box.innerHTML='';
  var rows=data.slice();
  if(lv!=='ALL')rows=rows.filter(function(r){return String(r.cand_level)===lv;});
  if(sem!=='ALL')rows=rows.filter(function(r){return r.semester===sem;});
  if(q){var s=q.toLowerCase();rows=rows.filter(function(r){return String(r.candidate||'').toLowerCase().indexOf(s)>=0;});}
  if(sort==='az')rows.sort(function(a,b){return String(a.candidate||'').localeCompare(String(b.candidate||''));});
  else rows.sort(function(a,b){return when(b)-when(a);});
  if(!rows.length){box.appendChild(el('div','rv6-empty',loaded?'No results match this filter.':'Loading...'));return;}
  var groups={};
  rows.forEach(function(r){var L=String(r.cand_level||'Other');(groups[L]=groups[L]||[]).push(r);});
  Object.keys(groups).sort().forEach(function(L){
    box.appendChild(el('div','rv6-lvl',L+' Level'));
    var card=el('div','rv6-card');
    var hd=el('div','rv6-cols');
    hd.appendChild(el('span','','NAME'));
    hd.appendChild(el('span','','USERNAME'));
    hd.appendChild(el('span','rv6-r','SCORE'));
    hd.appendChild(el('span','rv6-r','GRADE'));
    card.appendChild(hd);
    groups[L].forEach(function(r){
      var row=el('div','rv6-row');
      row.appendChild(el('span','rv6-n',r.candidate||''));
      row.appendChild(el('span','rv6-u',uname(r)));
      var p=pct(r),gr=grade(p);
      row.appendChild(el('span','rv6-sc rv6-r',String(p)));
      row.appendChild(el('span','rv6-g rv6-r'+(gr==='F'?' f':''),gr));
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
if(app.admin&&app.admin.resTab&&!app.admin.resTab.__rv6){
  var origTab=app.admin.resTab;
  var wt=function(sec,btn){active=sec;var r=origTab.call(this,sec,btn);tabs();return r;};
  wt.__rv6=true;app.admin.resTab=wt;
}
if(app.admin&&app.admin.loadScores&&!app.admin.loadScores.__rv6){
  var origLoad=app.admin.loadScores;
  var wl=function(){
    var p=origLoad.apply(this,arguments);
    return Promise.resolve(p).then(function(){refresh();});
  };
  wl.__rv6=true;app.admin.loadScores=wl;
}
setInterval(function(){
  if(!document.getElementById('rv6-tabs'))tabs();
  if(document.getElementById('adm-res-res')&&!document.getElementById('rv6-root'))draw();
},800);
setTimeout(function(){tabs();refresh();},600);
})();
</script>
'''

shutil.copy2(SRC, BAK)
out = html[:a] + NEW + html[end:]
open(SRC, "w", encoding="utf-8").write(out)
print("Done. Backup saved as " + BAK)
