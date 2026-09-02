/* Ledger theme · runtime: theme toggle, keyboard, year counts, TOC, reading stats, code blocks, git meta */
(function () {
  'use strict';

  var root = document.documentElement;
  var STORAGE_KEY = 'theme';

  function isDark() {
    var explicit = root.getAttribute('data-theme');
    if (explicit === 'dark' || explicit === 'light') return explicit === 'dark';
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  }

  function syncThemeIcon() {
    var mode = isDark() ? 'dark' : 'light';
    document.querySelectorAll('.theme-btn').forEach(function (button) { button.setAttribute('data-mode', mode); });
  }

  function toggleTheme() {
    var next = isDark() ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem(STORAGE_KEY, next); } catch (error) { /* storage unavailable */ }
    syncThemeIcon();
  }

  syncThemeIcon();
  var scheme = window.matchMedia('(prefers-color-scheme: dark)');
  if (scheme.addEventListener) scheme.addEventListener('change', syncThemeIcon);

  function openSearch() {
    if (window.ledgerSearch) window.ledgerSearch.open();
  }

  function isTypingTarget(target) {
    return target && (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA' || target.isContentEditable);
  }

  document.addEventListener('keydown', function (event) {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
      event.preventDefault();
      openSearch();
      return;
    }
    if (isTypingTarget(event.target) || event.metaKey || event.ctrlKey || event.altKey) return;
    if (event.key === 't') toggleTheme();
    if (event.key === '/') {
      event.preventDefault();
      openSearch();
    }
  });

  document.querySelectorAll('[data-action="theme"]').forEach(function (button) {
    button.addEventListener('click', toggleTheme);
  });
  document.querySelectorAll('[data-action="search"]').forEach(function (button) {
    button.addEventListener('click', openSearch);
  });
  document.querySelectorAll('[data-year]').forEach(function (node) {
    node.textContent = String(new Date().getFullYear());
  });

  /* year group counts */
  document.querySelectorAll('.year-group').forEach(function (group) {
    var count = group.querySelectorAll('.row').length;
    var target = group.querySelector('[data-count]');
    if (target) target.textContent = count + ' posts';
  });

  /* post page */
  var content = document.querySelector('.post-content');
  if (content) {
    buildToc(content);
    fillReadingStats(content);
    decorateCodeBlocks(content);
  }

  loadGitMeta();
  loadPostIndex();

  function slugify(text, used) {
    var base = text.trim().toLowerCase().replace(/[^\p{L}\p{N}]+/gu, '-').replace(/^-+|-+$/g, '') || 'section';
    var slug = base;
    var index = 2;
    while (used[slug]) { slug = base + '-' + index; index += 1; }
    used[slug] = true;
    return slug;
  }

  function buildToc(container) {
    var toc = document.getElementById('toc');
    if (!toc) return;
    var headings = Array.prototype.slice.call(container.querySelectorAll('h2, h3'));
    if (headings.length < 2) { toc.hidden = true; return; }
    var list = toc.querySelector('ol');
    var used = {};
    headings.forEach(function (heading, index) {
      if (!heading.id) heading.id = slugify(heading.textContent, used);
      var rest = headings.slice(index + 1);
      var moreTopLevel = rest.some(function (node) { return node.tagName === 'H2'; });
      var prefix;
      if (heading.tagName === 'H3') {
        var nextIsSibling = rest.length > 0 && rest[0].tagName === 'H3';
        prefix = (moreTopLevel ? '│  ' : '   ') + (nextIsSibling ? '├─ ' : '└─ ');
      } else {
        prefix = moreTopLevel ? '├─ ' : '└─ ';
      }
      var item = document.createElement('li');
      item.className = heading.tagName.toLowerCase();
      var link = document.createElement('a');
      link.href = '#' + heading.id;
      link.textContent = prefix + heading.textContent;
      item.appendChild(link);
      list.appendChild(item);
    });
    var details = toc.querySelector('details');
    if (details) details.open = window.matchMedia('(min-width: 901px)').matches;
    toc.hidden = false;
    trackActiveHeading(headings, list);
  }

  function trackActiveHeading(headings, list) {
    if (!('IntersectionObserver' in window)) return;
    var items = list.querySelectorAll('li');
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var index = headings.indexOf(entry.target);
        items.forEach(function (item, i) { item.classList.toggle('on', i === index); });
      });
    }, { rootMargin: '0px 0px -70% 0px' });
    headings.forEach(function (heading) { observer.observe(heading); });
  }

  function fillReadingStats(container) {
    var text = container.textContent || '';
    var words = text.trim() ? text.trim().split(/\s+/).length : 0;
    var characters = text.replace(/\s/g, '').length;
    var minutes = Math.max(1, Math.ceil(characters / 600));
    setText('[data-words]', String(words));
    setText('[data-read]', String(minutes));
  }

  function setText(selector, value) {
    document.querySelectorAll(selector).forEach(function (node) { node.textContent = value; });
  }

  function languageOf(code) {
    var match = /(?:^|\s)language-([\w+-]+)/.exec(code.className || '');
    return match ? match[1] : 'text';
  }

  function decorateCodeBlocks(container) {
    container.querySelectorAll('pre > code').forEach(function (code) {
      var pre = code.parentNode;
      if (window.hljs && typeof window.hljs.highlightElement === 'function') {
        try { window.hljs.highlightElement(code); } catch (error) { /* keep plain text */ }
      }
      var lines = code.textContent.replace(/\n$/, '').split('\n').length;

      var wrapper = document.createElement('div');
      wrapper.className = 'code';

      var header = document.createElement('div');
      header.className = 'code-h';
      var label = document.createElement('span');
      label.textContent = languageOf(code);
      var copy = document.createElement('button');
      copy.type = 'button';
      copy.textContent = 'copy';
      copy.addEventListener('click', function () { copyCode(code, copy); });
      header.appendChild(label);
      header.appendChild(copy);

      var body = document.createElement('div');
      body.className = 'code-body';
      var gutter = document.createElement('div');
      gutter.className = 'code-gutter';
      gutter.setAttribute('aria-hidden', 'true');
      for (var i = 1; i <= lines; i += 1) {
        var number = document.createElement('span');
        number.textContent = String(i);
        gutter.appendChild(number);
      }

      pre.parentNode.insertBefore(wrapper, pre);
      body.appendChild(gutter);
      body.appendChild(pre);
      wrapper.appendChild(header);
      wrapper.appendChild(body);
    });
  }

  function copyCode(code, button) {
    var text = code.textContent;
    var done = function () { button.textContent = 'copied'; setTimeout(function () { button.textContent = 'copy'; }, 1500); };
    var fail = function () { button.textContent = 'failed'; setTimeout(function () { button.textContent = 'copy'; }, 1500); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, fail);
      return;
    }
    fail();
  }

  function loadGitMeta() {
    var changelog = document.querySelector('[data-changelog]');
    var history = document.querySelector('[data-history]');
    var commits = document.querySelector('[data-commits]');
    if (!changelog && !history && !commits) return;
    if (!window.fetch) return;
    fetch('/meta/git.json', { cache: 'no-cache' })
      .then(function (response) { if (!response.ok) throw new Error('git.json ' + response.status); return response.json(); })
      .then(function (meta) {
        if (commits && typeof meta.total_commits === 'number' && meta.total_commits > 0) {
          commits.textContent = String(meta.total_commits);
        }
        if (changelog) renderCommits(changelog, meta.changelog || []);
        if (history) {
          var article = document.querySelector('article[data-slug]');
          var slug = article ? article.getAttribute('data-slug') : '';
          var posts = meta.posts || {};
          renderCommits(history, slug && posts[slug] ? posts[slug] : []);
        }
      })
      .catch(function () { /* meta is optional; sections stay hidden */ });
  }

  function loadPostIndex() {
    var nav = document.querySelector('[data-pn]');
    var article = document.querySelector('article[data-slug]');
    if (!nav || !article || !window.fetch) return;
    var slug = article.getAttribute('data-slug');
    fetch('/meta/posts.json', { cache: 'force-cache' })
      .then(function (response) { if (!response.ok) throw new Error('posts.json ' + response.status); return response.json(); })
      .then(function (rows) {
        var index = -1;
        for (var i = 0; i < rows.length; i += 1) { if (rows[i][0] === slug) { index = i; break; } }
        if (index < 0) return;
        /* rows are newest first: next = newer (index - 1), prev = older (index + 1) */
        fillNeighbor(nav.querySelector('[data-pn-next]'), rows[index - 1]);
        fillNeighbor(nav.querySelector('[data-pn-prev]'), rows[index + 1]);
        nav.hidden = !(rows[index - 1] || rows[index + 1]);
      })
      .catch(function () { /* optional navigation */ });
  }

  function fillNeighbor(link, row) {
    if (!link || !row) return;
    link.href = row[2];
    link.querySelector('b').textContent = row[1];
    link.title = row[3] + ' · ' + row[1];
    link.hidden = false;
  }

  function renderCommits(section, rows) {
    if (!rows.length) { section.hidden = true; return; }
    var target = section.querySelector('.cl-rows') || section;
    rows.forEach(function (row) {
      var line = document.createElement('a');
      line.className = 'cl-row';
      line.href = 'https://github.com/AhnSeongHyun/ahnseonghyun.github.io/commit/' + encodeURIComponent(row.hash);
      line.rel = 'noopener';
      line.target = '_blank';
      var hash = document.createElement('code');
      hash.textContent = row.hash;
      var date = document.createElement('span');
      date.textContent = row.date;
      var message = document.createElement('em');
      message.textContent = row.message;
      message.title = row.message;
      line.appendChild(hash);
      line.appendChild(date);
      line.appendChild(message);
      target.appendChild(line);
    });
    section.hidden = false;
  }
})();
