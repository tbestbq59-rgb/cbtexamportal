import os, sys, shutil

SRC = "index.html"
BAK = "index-before-rsv3.html"
START = '<script id="rs2b">'
END = '</body>'
MARK = 'id="rsv3"'

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

NEW = r'''<style id="rsv3">
.rs2-hide{display:none!important}
#adm-res-level-tabs{display:none!important}
#adm-tab-results>div:first-child>div:first-child{flex-wrap:nowrap!important;overflow-x:auto;border-bottom:1px solid #e2e8f0!important;gap:6px!important;padding-bottom:0!important}
#adm-tab-results>div:first-child>div:first-child>button{white-space:nowrap;flex-shrink:0;border-radius:10px!important;padding:8px 12px!important;font-size:13px;color:#64748b!important;background:transparent!important}
#adm-tab-results>div:first-child>div:first-child>button.text-g{background:#e6efe8!important;color:#3d5a4c!important;border-color:transparent!important}
.rv3-bar{display:flex;gap:8px;align-items:center;margin:0 0 12px}
.rv3-search{flex:1;min-width:0;height:44px;border:1px solid #E0E1E6;border-radius:12px;padding:0 14px;font-size:14px;background:#fff}
.rv3-fbtn{height:44px;border:1px solid #E0E1E6;background:#fff;border-radius:12px;padding:0 14px;font-weight:600;color:#1e293b;white-space:nowrap}
.rv3-panel{border:1px solid #E0E1E6;border-radius:12px;padding:10px 12px;margin:0 0 12px;background:#fff}
.rv3-plab{font-size:11px;font-weight:700;letter-spacing:.06em;color:#60646C;margin:4px 0 8px}
.rv3-chips{display:flex;flex-wrap:wrap;gap:6px}
.rv3-row2{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin:4px 0 14px}
.rv3-seg{display:inline-flex;background:#fff;border:1px solid #E0E1E6;border-radius:12px;padding:4px;gap:4px}
.rv3-chip{height:32px;padding:0 12px;border:1px solid transparent;background:transparent;border-radius:9px;font-size:13px;font-weight:600;color:#60646C;white-space:nowrap}
.rv3-chip.on{background:#e6efe8;color:#3d5a4c;border-color:#3d5a4c}
.rv3-lvl{font-size:15px;font-weight:700;margin:18px 0 8px;color:#1e293b}
.rv3-card{background:#fff;border:1px solid #E0E1E6;border-radius:14px;overflow:hidden}
.rv3-cols,.rv3-row{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr) 76px 34px;gap:10px;align-items:center}
.rv3-cols{padding:12px 16px;font-size:11px;font-weight:700;letter-spacing:.06em;color:#60646C;background:#F9F9FB}
.rv3-row{padding:14px 16px;border-top:1px solid #EBEBEF;cursor:pointer}
.rv3-n{font-size:15px;font-weight:600;color:#1e293b;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rv3-u{font-size:14px;color:#60646C;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rv3-sc{font-weight:700;color:#1e293b}
.rv3-gl{font-weight:700;color:#3d5a4c}
.rv3-gb{width:30px;height:30px;border:1px solid #E0E1E6;background:#fff;border-radius:8px;font-size:16px;font-weight:700;color:#3d5a4c;padding:0}
.rv3-empty{padding:24px;text-align:center;color:#60646C}
</style>
<script id="rsv3js">
(function(){
var data=[],umap={},lv='ALL',sort='recent',sem='ALL',q='',show=false,loaded=false,profLoaded=false;
function el(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!==undefined)e.textContent=x;return e;}
function esc(s){return app.ui.esc(s==null?'':String(s));}
function pct(r){return r.total?Math.round((r.score/r.total)*100):0;}
function grade(p){try{return app.utils.computeGrade(p).grade;}catch(e){return '';}}
function uname(r){var v=r.username||r.cand_username||umap[r.cand_id]||'';return v||'-';}
function when(r){var v=r.submitted_at||r.finished_at||r.created_at;var d=v?new Date(v):null;return d&&!isNaN(d.getTime())?d.getTime():0;}
function chip(t,on,fn){var b=el('button','rv3-chip'+(on?' on':''),t);b.type='button';b.onclick=fn;return b;}
function mount(){
  var h=document.getElementById('adm-res-res');if(!h)return null;
  var m=document.getElementById('rv3-root');
  if(!m){m=el('div');m.id='rv3-root';h.insertBefore(m,h.firstChild);}
  Array.prototype.forEach.call(h.children,function(c){if(c!==m)c.classList.add('rs2-hide');});
  return m;
}
function setLevel(v){
  lv=v;
  try{app.admin.setResLevelFilter(v,null);}catch(e){}
  draw();
}
function draw(){
  var m=mount();if(!m)return;m.innerHTML='';
  var bar=el('div','rv3-bar');
  var inp=el('input','rv3-search');inp.placeholder='Search by name';inp.value=q;
  inp.oninput=function(){q=inp.value;drawList();};
  var fb=el('button','rv3-fbtn','Filter');fb.type='button';
  fb.onclick=function(){show=!show;draw();};
  bar.appendChild(inp);bar.appendChild(fb);m.appendChild(bar);
  if(show){
    var p=el('div','rv3-panel');
    p.appendChild(el('div','rv3-plab','SEMESTER'));
    var w=el('div','rv3-chips');
    [['ALL','All'],['First Semester','First'],['Second Semester','Second']].forEach(function(o){
      w.appendChild(chip(o[1],sem===o[0],function(){sem=o[0];draw();}));});
    p.appendChild(w);m.appendChild(p);
  }
  var row=el('div','rv3-row2');
  var lw=el('div','rv3-seg');
  [['ALL','All'],['100','100'],['200','200'],['300','300'],['400','400']].forEach(function(o){
    lw.appendChild(chip(o[1],lv===o[0],function(){setLevel(o[0]);}));});
  var sw=el('div','rv3-seg');
  [['recent','Recent'],['az','A-Z']].forEach(function(o){
    sw.appendChild(chip(o[1],sort===o[0],function(){sort=o[0];draw();}));});
  row.appendChild(lw);row.appendChild(sw);m.appendChild(row);
  m.appendChild(el('div','','')).id='rv3-list';
  drawList();
}
function drawList(){
  var box=document.getElementById('rv3-list');if(!box)return;
  box.innerHTML='';
  var rows=data.slice();
  if(lv!=='ALL')rows=rows.filter(function(r){return String(r.cand_level)===lv;});
  if(sem!=='ALL')rows=rows.filter(function(r){return r.semester===sem;});
  if(q){var s=q.toLowerCase();rows=rows.filter(function(r){return String(r.candidate||'').toLowerCase().indexOf(s)>=0;});}
  if(sort==='az')rows.sort(function(a,b){return String(a.candidate||'').localeCompare(String(b.candidate||''));});
  else rows.sort(function(a,b){return when(b)-when(a);});
  if(!rows.length){box.appendChild(el('div','rv3-empty',loaded?'No results match this filter.':'Loading...'));return;}
  var groups={};
  rows.forEach(function(r){var L=String(r.cand_level||'Other');(groups[L]=groups[L]||[]).push(r);});
  Object.keys(groups).sort().forEach(function(L){
    box.appendChild(el('div','rv3-lvl',L+' Level'));
    var card=el('div','rv3-card');
    var hd=el('div','rv3-cols');
    ['NAME','USERNAME','GRADE',''].forEach(function(x){hd.appendChild(el('span','',x));});
    card.appendChild(hd);
    groups[L].forEach(function(r){
      var row=el('div','rv3-row');
      row.appendChild(el('span','rv3-n',r.candidate||''));
      row.appendChild(el('span','rv3-u',uname(r)));
      var p=pct(r);var g=el('span');
      g.innerHTML='<span class="rv3-sc">'+p+'</span> <span style="color:#9ca3af">&middot;</span> <span class="rv3-gl">'+esc(grade(p))+'</span>';
      row.appendChild(g);
      var gb=el('button','rv3-gb','+');gb.type='button';gb.title='Grant attempt';
      gb.onclick=function(e){e.stopPropagation();
        try{app.admin.modals.openGrantAttempt(r.cand_id,r.candidate,r.exam_id);}
        catch(err){app.ui.toast('Could not open grant.',true);}};
      row.appendChild(gb);
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
    window.sbClient.from('profiles').select('id,username').then(function(res){
      profLoaded=true;
      (res.data||[]).forEach(function(p){umap[p.id]=p.username||'';});
      drawList();
    },function(){profLoaded=true;});
  }
}
if(app.admin&&app.admin.loadScores&&!app.admin.loadScores.__rv3){
  var orig=app.admin.loadScores;
  var wrapped=function(){
    var p=orig.apply(this,arguments);
    return Promise.resolve(p).then(function(){refresh();});
  };
  wrapped.__rv3=true;
  app.admin.loadScores=wrapped;
}
setInterval(function(){
  if(document.getElementById('adm-res-res')&&!document.getElementById('rv3-root'))draw();
},800);
setTimeout(function(){refresh();},600);
})();
</script>
'''

out = html[:a] + NEW + html[b:]
shutil.copy2(SRC, BAK)
open(SRC, "w", encoding="utf-8").write(out)
print("Done. Backup saved as " + BAK)

