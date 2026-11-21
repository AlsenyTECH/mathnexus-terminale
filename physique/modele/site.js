
(function(){
  var lessons = Array.prototype.slice.call(document.querySelectorAll('.lesson'));
  var ids = lessons.map(function(s){ return s.id; });
  var KEY = PARCOURS_KEY;
  var done = {};
  try { done = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch(e){ done = {}; }
  function save(){ try { localStorage.setItem(KEY, JSON.stringify(done)); } catch(e){} }

  // ----- sommaire -----
  var nav = document.getElementById('nav'), html = '', part = null, n = 0;
  lessons.forEach(function(s){
    var p = s.dataset.part || '';
    if (p !== part){ if (part !== null) html += '</ol>'; html += (p ? '<p class="nav-part">' + p + '</p>' : '') + '<ol class="nav-list">'; part = p; }
    var num = s.id === 'accueil' ? 'i' : String(++n);
    html += '<li><a href="#' + s.id + '" data-id="' + s.id + '"><span class="nav-n">' + num + '</span><span>' + s.dataset.title + '</span></a></li>';
  });
  nav.innerHTML = html + '</ol>';
  var links = Array.prototype.slice.call(nav.querySelectorAll('a'));
  var total = ids.length - 1;

  links.forEach(function(a){ a.dataset.num = a.querySelector('.nav-n').textContent; });
  var resetBtn = document.getElementById('reset');

  function refreshProgress(){
    var c = 0;
    links.forEach(function(a){
      var d = !!done[a.dataset.id] && a.dataset.id !== 'accueil';
      a.classList.toggle('done', d);
      a.querySelector('.nav-n').textContent = d ? '✓' : a.dataset.num;
      if (d) c++;
    });
    document.getElementById('prog-fill').style.width = (100 * c / total) + '%';
    document.getElementById('prog-txt').textContent = c + ' étape' + (c > 1 ? 's' : '') + ' validée' + (c > 1 ? 's' : '') + ' sur ' + total;
    document.getElementById('mini-prog').textContent = c + ' / ' + total;
    resetBtn.hidden = c === 0;
    disarmReset();
  }

  // remise à zéro : deux appuis, sans fenêtre de confirmation
  var armed = false, armTimer = null;
  function disarmReset(){ armed = false; clearTimeout(armTimer); resetBtn.textContent = 'Remettre ma progression à zéro'; resetBtn.classList.remove('warn'); }
  resetBtn.addEventListener('click', function(){
    if (!armed){ armed = true; resetBtn.textContent = 'Appuie encore pour tout effacer'; resetBtn.classList.add('warn'); armTimer = setTimeout(disarmReset, 5000); return; }
    done = {}; save(); refreshProgress(); refreshDone();
  });

  // ----- formules : rendues à l'ouverture de l'étape -----
  var typeset = {};
  function renderMath(el){
    if (typeset[el.id] || !window.MathJax || !MathJax.typesetPromise) return;
    typeset[el.id] = true;
    MathJax.typesetPromise([el]).catch(function(){ typeset[el.id] = false; });
  }

  var side = document.getElementById('side'), scrim = document.getElementById('scrim'), menuBtn = document.getElementById('menu-btn');
  function closeMenu(){ side.classList.remove('open'); scrim.hidden = true; menuBtn.setAttribute('aria-expanded','false'); }
  menuBtn.addEventListener('click', function(){
    var o = !side.classList.contains('open');
    side.classList.toggle('open', o); scrim.hidden = !o; menuBtn.setAttribute('aria-expanded', String(o));
  });
  scrim.addEventListener('click', closeMenu);

  var prev = document.getElementById('prev'), next = document.getElementById('next'), doneNote = document.getElementById('done-note'), undo = document.getElementById('undo');
  var current = 0;
  function refreshDone(){ var d = !!done[ids[current]] && current > 0; doneNote.hidden = !d; undo.hidden = !d; }
  undo.addEventListener('click', function(){ delete done[ids[current]]; save(); refreshProgress(); refreshDone(); });
  function show(id, scroll){
    var i = ids.indexOf(id); if (i < 0) i = 0;
    current = i;
    document.querySelectorAll('video').forEach(function(v){ try { v.pause(); } catch(e){} });
    lessons.forEach(function(s, k){ s.hidden = k !== i; });
    links.forEach(function(a){ if (a.dataset.id === ids[i]) a.setAttribute('aria-current','page'); else a.removeAttribute('aria-current'); });
    renderMath(lessons[i]);
    prev.hidden = i === 0;
    if (i > 0) prev.setAttribute('href', '#' + ids[i-1]);
    var last = i === ids.length - 1;
    next.setAttribute('href', last ? '#accueil' : '#' + ids[i+1]);
    next.textContent = i === 0 ? 'Commencer le parcours →' : (last ? 'Valider et revenir au début' : "J'ai compris, étape suivante →");
    refreshDone();
    closeMenu();
    if (scroll) window.scrollTo(0, 0);
  }
  next.addEventListener('click', function(){ if (current > 0){ done[ids[current]] = true; save(); refreshProgress(); } });
  window.addEventListener('hashchange', function(){ show(location.hash.slice(1), true); });

  // ----- chronomètres : calculés sur l'heure réelle, donc justes même si l'onglet passe en arrière-plan -----
  document.querySelectorAll('.chrono').forEach(function(c){
    var totalS = (+c.dataset.min || 15) * 60, left = totalS, timer = null, endAt = 0;
    var t = c.querySelector('.chrono-t'), b = c.querySelector('.c-start'), r = c.querySelector('.c-reset'), end = c.querySelector('.chrono-end');
    function draw(){ var m = Math.floor(left / 60), s = left % 60; t.textContent = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s; }
    function stop(){ clearInterval(timer); timer = null; b.textContent = left === totalS ? 'Démarrer' : 'Reprendre'; }
    function tick(){
      left = Math.max(0, Math.ceil((endAt - Date.now()) / 1000)); draw();
      if (left <= 0){ stop(); b.textContent = 'Terminé'; end.hidden = false; }
    }
    b.addEventListener('click', function(){
      if (timer){ tick(); if (timer) stop(); return; }
      if (left === 0) return;
      end.hidden = true; b.textContent = 'Pause';
      endAt = Date.now() + left * 1000;
      timer = setInterval(tick, 250);
    });
    r.addEventListener('click', function(){ clearInterval(timer); timer = null; left = totalS; draw(); b.textContent = 'Démarrer'; end.hidden = true; });
    document.addEventListener('visibilitychange', function(){ if (timer && !document.hidden) tick(); });
  });

  // corrections : formules rendues à l'ouverture
  document.querySelectorAll('.exo details').forEach(function(d){
    d.addEventListener('toggle', function(){
      if (!d.open || !d.classList.contains('tex2jax_ignore')) return;
      d.classList.remove('tex2jax_ignore');
      if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([d]).catch(function(){});
    });
  });

  // notes des évaluations
  document.querySelectorAll('.score').forEach(function(inp){
    var msg = inp.closest('.note').querySelector('.note-msg'), tot = +inp.dataset.tot;
    var sk = KEY + ':' + inp.closest('.lesson').id;
    try { var old = localStorage.getItem(sk); if (old !== null) inp.value = old; } catch(e){}
    function upd(){
      var v = parseFloat(String(inp.value).replace(',', '.'));
      if (isNaN(v)){ msg.textContent = ''; msg.className = 'note-msg'; return; }
      try { localStorage.setItem(sk, String(v)); } catch(e){}
      if (v >= 0.6 * tot){ msg.textContent = 'Partie comprise : tu peux passer à la suite.'; msg.className = 'note-msg ok'; }
      else { msg.textContent = 'Pas encore : refais les exercices des étapes de cette partie, puis recommence l\u2019évaluation.'; msg.className = 'note-msg ko'; }
    }
    inp.addEventListener('input', upd); upd();
  });

  if (lessons.length < 2){ document.querySelector('.pager').hidden = true; document.querySelector('.prog').hidden = true; }
  refreshProgress();
  show(location.hash.slice(1) || 'accueil', true);
  // si MathJax arrive après le premier affichage
  var tries = 0, wait = setInterval(function(){
    if (window.MathJax && MathJax.typesetPromise){ clearInterval(wait); renderMath(lessons[current]); }
    else if (++tries > 100) clearInterval(wait);
  }, 150);
})();
