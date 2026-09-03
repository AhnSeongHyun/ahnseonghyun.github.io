/* Ledger theme · search overlay backed by pagefind (static index built at `make build`) */
window.ledgerSearch = (function () {
  'use strict';

  var overlay = document.getElementById('search');
  if (!overlay) return { open: function () {}, close: function () {} };

  var input = overlay.querySelector('input');
  var list = overlay.querySelector('.sq-list');
  var status = overlay.querySelector('.sq-empty');
  var pagefind = null;
  var loadFailed = false;
  var selected = -1;
  var timer = null;
  var lastQuery = '';

  function setStatus(text) {
    status.textContent = text;
    status.hidden = !text;
  }

  function loadPagefind() {
    if (pagefind) return Promise.resolve(pagefind);
    if (loadFailed) return Promise.reject(new Error('pagefind unavailable'));
    return import('/pagefind/pagefind.js')
      .then(function (module) {
        return module.options({ excerptLength: 30 }).then(function () {
          pagefind = module;
          return module;
        });
      })
      .catch(function (error) {
        loadFailed = true;
        throw error;
      });
  }

  function clearResults() {
    while (list.firstChild) list.removeChild(list.firstChild);
    selected = -1;
  }

  function appendExcerpt(target, excerpt) {
    /* pagefind excerpts are HTML with <mark>; rebuild with text nodes so no markup is injected */
    var parts = String(excerpt || '').split(/<\/?mark>/);
    parts.forEach(function (part, index) {
      var text = part.replace(/<[^>]*>/g, '');
      if (!text) return;
      if (index % 2 === 1) {
        var mark = document.createElement('mark');
        mark.textContent = decodeEntities(text);
        target.appendChild(mark);
      } else {
        target.appendChild(document.createTextNode(decodeEntities(text)));
      }
    });
  }

  function decodeEntities(text) {
    var area = document.createElement('textarea');
    area.innerHTML = text;
    return area.value;
  }

  function render(results) {
    clearResults();
    if (!results.length) { setStatus('결과 없음'); return; }
    setStatus('');
    results.forEach(function (result) {
      var item = document.createElement('a');
      item.className = 'sq-item';
      item.href = result.url;
      item.setAttribute('role', 'option');
      var title = document.createElement('div');
      title.className = 't';
      title.textContent = (result.meta && result.meta.title) || result.url;
      var url = document.createElement('div');
      url.className = 'u';
      url.textContent = result.url;
      var excerpt = document.createElement('div');
      excerpt.className = 'x';
      appendExcerpt(excerpt, result.excerpt);
      item.appendChild(title);
      item.appendChild(url);
      item.appendChild(excerpt);
      list.appendChild(item);
    });
    select(0);
  }

  function select(index) {
    var items = list.querySelectorAll('.sq-item');
    if (!items.length) { selected = -1; return; }
    selected = (index + items.length) % items.length;
    items.forEach(function (item, i) {
      item.setAttribute('aria-selected', i === selected ? 'true' : 'false');
    });
    items[selected].scrollIntoView({ block: 'nearest' });
  }

  function run(query) {
    lastQuery = query;
    if (!query.trim()) { clearResults(); setStatus('검색어를 입력하세요'); return; }
    setStatus('검색 중…');
    loadPagefind()
      .then(function (module) { return module.search(query); })
      .then(function (response) {
        if (query !== lastQuery) return null;
        return Promise.all(response.results.slice(0, 12).map(function (result) { return result.data(); }));
      })
      .then(function (data) { if (data) render(data); })
      .catch(function () {
        clearResults();
        setStatus('검색 인덱스가 없습니다. make build 후 다시 시도하세요.');
      });
  }

  function onInput() {
    clearTimeout(timer);
    var value = input.value;
    timer = setTimeout(function () { run(value); }, 150);
  }

  function onKey(event) {
    if (event.key === 'Escape') { event.preventDefault(); close(); return; }
    if (event.key === 'ArrowDown') { event.preventDefault(); select(selected + 1); return; }
    if (event.key === 'ArrowUp') { event.preventDefault(); select(selected - 1); return; }
    if (event.key === 'Enter') {
      var items = list.querySelectorAll('.sq-item');
      if (selected >= 0 && items[selected]) { event.preventDefault(); window.location.href = items[selected].href; }
    }
  }

  function open() {
    overlay.hidden = false;
    document.body.style.overflow = 'hidden';
    input.focus();
    input.select();
    if (!input.value) setStatus('검색어를 입력하세요');
  }

  function close() {
    overlay.hidden = true;
    document.body.style.overflow = '';
  }

  input.addEventListener('input', onInput);
  overlay.addEventListener('keydown', onKey);
  /* input[type=search]'s native Escape-to-clear can swallow the keydown before it bubbles
     to the overlay in some browsers; a capture-phase fallback on document guarantees close(). */
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && !overlay.hidden) { event.preventDefault(); close(); }
  }, true);
  overlay.addEventListener('click', function (event) { if (event.target === overlay) close(); });
  overlay.querySelectorAll('[data-action="close"]').forEach(function (button) {
    button.addEventListener('click', close);
  });

  return { open: open, close: close };
})();
