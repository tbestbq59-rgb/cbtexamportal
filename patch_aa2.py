import shutil, sys

path = "index.html"
src = open(path, encoding="utf-8").read()

if "/*aa2*/" in src:
    print("Nothing changed: aa2 is already in index.html.")
    sys.exit(0)

anchor = "</body>"
if src.count(anchor) != 1:
    print("Nothing changed: </body> not found exactly once. Stopped.")
    sys.exit(1)

js = r'''
(function(){
  var courses = [], students = [], cur = null;
  var ICON_BACK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1e293b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>';
  function root(){ return document.getElementById('adm-res-att'); }
  function E(s){ return app.ui.esc(s == null ? '' : String(s)); }
  function dur(s){ s = Math.max(0, Math.round(Number(s) || 0)); return Math.floor(s / 60) + 'm ' + (s % 60) + 's'; }
  function dt(v){ if(!v) return '-'; var d = new Date(v); return isNaN(d) ? '-' : d.toLocaleString(); }
  function setBox(html){ var r = root(); if(r) r.innerHTML = html; }
  function fail(e){ app.ui.toast((e && e.message) || 'Something went wrong.', true); }
  function head(title, sub){
    return '<div class="aa-page-head"><button class="aa-back" onclick="app.admin.aaCourses()">' + ICON_BACK + '</button><div><h3 class="aa-title">' + title + '</h3>' + (sub ? '<p class="aa-sub">' + sub + '</p>' : '') + '</div></div>';
  }

  app.admin.aaCourses = async function(){
    cur = null;
    setBox('<div class="aa-table"><div class="aa-empty">Loading...</div></div>');
    try{
      var all = await app.api.rpc('admin_course_counts');
      var lf = (typeof state !== 'undefined' && state.adminResLevelFilter) || 'ALL';
      courses = (all || []).filter(function(c){ return lf === 'ALL' || String(c.level) === String(lf); });
      var h = '<div class="aa-table"><div class="aa-head"><span>Course</span><span class="aa-num">Level</span><span class="aa-num">Active Students</span><span class="aa-num">Submitted</span></div>';
      if(!courses.length) h += '<div class="aa-empty">No live or submitted exams yet.</div>';
      courses.forEach(function(c, i){
        h += '<div class="aa-row"><span><button class="aa-link" onclick="app.admin.aaDetails(' + i + ')">' + E(c.code) + '</button></span>' +
             '<span class="aa-num">' + E(c.level) + '</span>' +
             '<span class="aa-num"><button class="aa-link" onclick="app.admin.aaStudents(' + i + ')">' + Number(c.active) + '</button></span>' +
             '<span class="aa-num"><button class="aa-link" onclick="app.admin.aaSubs(' + i + ')">' + Number(c.submitted) + '</button></span></div>';
      });
      setBox(h + '</div>');
    }catch(e){
      setBox('<div class="aa-table"><div class="aa-empty">Could not load attempts.</div></div>');
      fail(e);
    }
  };

  app.admin.loadAttempts = function(){ return app.admin.aaCourses(); };

  app.admin.aaDetails = function(i){
    var c = courses[i]; if(!c) return; cur = c;
    setBox(head(E(c.code), E(c.title) + ' · Level ' + E(c.level)) +
      '<div class="aa-card"><h4>Course information</h4><div class="aa-kv">' +
        '<div><span>Code</span><b>' + E(c.code) + '</b></div>' +
        '<div><span>Level</span><b>' + E(c.level) + '</b></div>' +
        '<div><span>Active students</span><b>' + Number(c.active) + '</b></div>' +
        '<div><span>Submitted</span><b>' + Number(c.submitted) + '</b></div>' +
      '</div></div>' +
      '<div class="aa-card"><h4>Stop all attempts</h4>' +
        '<p class="aa-sub" style="margin:0 0 4px">Closes every active and paused attempt in this course only. Answers are saved and scored.</p>' +
        '<button class="aa-btn danger aa-stop" onclick="app.admin.aaStopAll()">Stop All Attempts</button></div>' +
      '<div class="aa-card"><h4>Time slots and batches</h4><p class="aa-sub" style="margin:0">Coming in the next stage.</p></div>');
  };

  app.admin.aaStopAll = function(){
    if(!cur) return;
    var c = cur;
    app.ui.confirmModal('Stop all attempts?',
      'This closes every active and paused attempt in ' + E(c.code) + ' for all candidates. Answers are saved and scored. This cannot be undone.',
      async function(){
        try{
          var r = await app.api.rpc('admin_stop_all_attempts', { p_exam_id: c.exam_id });
          app.ui.toast('Closed ' + ((r && r.stopped) || 0) + ' attempt(s).');
          app.admin.aaCourses();
        }catch(e){ fail(e); }
      });
  };

  app.admin.aaStudents = async function(i){
    var c = courses[i]; if(!c) return; cur = c;
    setBox(head('Active Students', E(c.code) + ' — ' + Number(c.active) + ' candidate(s)') +
      '<div class="aa-table" id="aa-list"><div class="aa-empty">Loading...</div></div>');
    await drawStudents(c);
  };

  async function drawStudents(c){
    var box = document.getElementById('aa-list'); if(!box) return;
    try{
      students = (await app.api.rpc('admin_active_students', { p_exam_id: c.exam_id })) || [];
      if(!students.length){ box.innerHTML = '<div class="aa-empty">No active students right now.</div>'; return; }
      box.innerHTML = students.map(function(s, i){
        var paused = s.status === 'paused';
        return '<div class="aa-student"><div style="min-width:0"><div class="aa-name">' + E(s.full_name) + '</div>' +
          '<div class="aa-user">' + E(s.username) + (paused ? ' · <span class="aa-badge paused">Paused</span>' : '') + '</div></div>' +
          '<button class="aa-btn' + (paused ? ' primary' : '') + '" onclick="app.admin.aaToggle(' + i + ')">' + (paused ? 'Resume' : 'Pause') + '</button></div>';
      }).join('');
    }catch(e){
      box.innerHTML = '<div class="aa-empty">Could not load students.</div>';
      fail(e);
    }
  }

  app.admin.aaToggle = function(i){
    var s = students[i]; if(!s) return;
    var paused = s.status === 'paused';
    var go = async function(){
      try{
        await app.api.rpc(paused ? 'admin_resume_attempt' : 'admin_pause_attempt', { p_session_id: s.session_id });
        app.ui.toast(paused ? 'Attempt resumed.' : 'Attempt paused.');
        drawStudents(cur);
      }catch(e){ fail(e); }
    };
    if(paused) go();
    else app.ui.confirmModal('Pause attempt?', E(s.full_name) + ' will not be able to answer until you resume the attempt. The timer stops.', go);
  };

  app.admin.aaSubs = async function(i){
    var c = courses[i]; if(!c) return; cur = c;
    setBox(head('Submissions', E(c.code) + ' — ' + Number(c.submitted) + ' submission(s)') +
      '<div class="aa-table" id="aa-list"><div class="aa-empty">Loading...</div></div>');
    var box = document.getElementById('aa-list');
    try{
      var rows = (await app.api.rpc('admin_submissions', { p_exam_id: c.exam_id })) || [];
      if(!rows.length){ box.innerHTML = '<div class="aa-empty">No submissions yet.</div>'; return; }
      box.innerHTML = '<div class="aa-list-row aa-head"><span>Name</span><span>Username</span><span class="aa-num">Time used</span></div>' +
        rows.map(function(r){
          return '<div class="aa-list-row"><div style="min-width:0"><div class="aa-name">' + E(r.full_name) + '</div>' +
            '<div class="aa-user">Start ' + E(dt(r.started_at)) + '<br>Submitted ' + E(dt(r.submitted_at)) + '</div></div>' +
            '<span class="aa-user">' + E(r.username) + '</span>' +
            '<span class="aa-num">' + E(dur(r.time_used_seconds)) + '</span></div>';
        }).join('');
    }catch(e){
      box.innerHTML = '<div class="aa-empty">Could not load submissions.</div>';
      fail(e);
    }
  };

  setTimeout(function(){ if(root() && root().offsetParent !== null) app.admin.aaCourses(); }, 700);
})();
'''

shutil.copy(path, "index-before-aa2.html")
src = src.replace(anchor, '<script id="aa2js">/*aa2*/' + js + '</script>\n' + anchor, 1)
open(path, "w", encoding="utf-8").write(src)
print("Done: Active Attempts screens wired. Backup: index-before-aa2.html")
