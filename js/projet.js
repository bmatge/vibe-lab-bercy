// ============================================================
// Module Fiche Projet — Vibe Lab
// Affichage détaillé, édition inline, GitHub proxy, screenshots
// ============================================================

const Projet = (() => {
  let card = null;
  let cardId = null;

  // --- Helpers ---
  function apiHeaders() {
    return {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + Auth.getToken()
    };
  }

  function handleAuthError(res) {
    if (res.status === 401) Auth.logout();
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text || '';
    return div.innerHTML;
  }

  function escapeAttr(text) {
    return (text || '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  // --- Chargement ---
  async function loadCard() {
    try {
      const res = await fetch(API_BASE_URL + '/api/kanban/cards/' + cardId, {
        headers: apiHeaders()
      });
      if (!res.ok) {
        handleAuthError(res);
        showError(res.status === 404 ? 'Projet non trouvé.' : 'Erreur de chargement.');
        return;
      }
      card = (await res.json()).card;
      renderCard();
    } catch (e) {
      console.error('Load card error:', e);
      showError('Erreur de connexion.');
    }
  }

  function showError(msg) {
    document.getElementById('projet-loading').classList.add('vl-hidden');
    document.getElementById('projet-error-msg').textContent = msg;
    document.getElementById('projet-error').classList.remove('vl-hidden');
  }

  // --- Rendu principal ---
  function renderCard() {
    document.getElementById('projet-loading').classList.add('vl-hidden');
    const content = document.getElementById('projet-content');
    content.classList.remove('vl-hidden');
    content.setAttribute('data-mode', 'view');

    document.getElementById('projet-title').textContent = card.title;
    document.title = card.title + ' — Vibe Lab';

    renderBadges();

    const descEl = document.getElementById('projet-description');
    descEl.textContent = card.description || 'Aucune description.';

    renderInfoTable();
    renderLinks();
    renderStack();
    renderMetrics();
    renderNotes();
    renderScreenshots();

    // GitHub section
    const ghSection = document.getElementById('projet-github-section');
    if (card.repo_url && card.repo_url.includes('github.com')) {
      ghSection.classList.remove('vl-hidden');
    } else {
      ghSection.classList.add('vl-hidden');
    }
  }

  // --- Badges ---
  function renderBadges() {
    const container = document.getElementById('projet-badges');
    const statusLabels = {
      propose: { label: 'Proposé', badge: '' },
      roadmap: { label: 'Dans roadmap', badge: 'fr-badge--blue-france' },
      developpement: { label: 'En cours', badge: 'fr-badge--blue-ecume' },
      test: { label: 'En test', badge: 'fr-badge--yellow-tournesol' },
      candidat: { label: 'Candidat', badge: 'fr-badge--green-emeraude' },
      deploye: { label: 'Déployé', badge: 'fr-badge--purple-glycine' }
    };
    const priorityClass = {
      haute: 'fr-badge--error',
      moyenne: 'fr-badge--warning',
      basse: 'fr-badge--success'
    }[card.priority] || '';

    const status = statusLabels[card.column_name] || { label: card.column_name, badge: '' };

    let html = `<span class="fr-badge fr-badge--sm fr-badge--no-icon ${status.badge}">${status.label}</span>`;
    html += ` <span class="fr-badge fr-badge--sm fr-badge--no-icon ${priorityClass}">Priorité ${card.priority}</span>`;
    if (card.category) {
      html += ` <span class="fr-tag fr-tag--sm">${escapeHtml(card.category)}</span>`;
    }
    container.innerHTML = html;
  }

  // --- Tableau d'infos ---
  function renderInfoTable() {
    const tbody = document.getElementById('projet-info-tbody');
    const rows = [
      { label: 'Sponsor', value: card.sponsor },
      { label: 'Publics ciblés', value: card.target_audience },
      { label: 'Utilisateurs potentiels', value: card.potential_users },
      { label: 'Durée estimée (J/H presta.)', value: card.dev_duration },
      { label: 'Durée réelle (vibe coding)', value: card.dev_duration_real },
      { label: 'Catégorie', value: card.category },
      { label: 'Créé le', value: card.created_at },
      { label: 'Mis à jour le', value: card.updated_at },
    ];

    const filledRows = rows.filter(r => r.value);
    if (filledRows.length === 0) {
      document.getElementById('projet-info-table').classList.add('vl-hidden');
      return;
    }
    document.getElementById('projet-info-table').classList.remove('vl-hidden');

    tbody.innerHTML = filledRows.map(r =>
      `<tr><td style="font-weight:600; width:40%">${escapeHtml(r.label)}</td><td>${escapeHtml(r.value)}</td></tr>`
    ).join('');
  }

  // --- Liens ---
  function renderLinks() {
    const container = document.getElementById('projet-links');
    if (!card.repo_url && !card.prod_url) {
      container.innerHTML = '';
      return;
    }
    let html = '';
    if (card.prod_url) {
      html += `<a class="fr-link fr-link--icon-right fr-icon-external-link-line fr-mr-3w" href="${escapeAttr(card.prod_url)}" target="_blank" rel="noopener">URL de production</a>`;
    }
    if (card.repo_url) {
      html += `<a class="fr-link fr-link--icon-right fr-icon-git-branch-line fr-mr-3w" href="${escapeAttr(card.repo_url)}" target="_blank" rel="noopener">Dépôt Git</a>`;
    }
    container.innerHTML = html;
  }

  // --- Stack technique ---
  function renderStack() {
    const container = document.getElementById('projet-stack');
    const empty = document.getElementById('projet-stack-empty');
    if (!card.stack) {
      container.innerHTML = '';
      empty.classList.remove('vl-hidden');
      return;
    }
    empty.classList.add('vl-hidden');
    const tags = card.stack.split(',').map(t => t.trim()).filter(Boolean);
    container.innerHTML = tags.map(t =>
      `<span class="fr-tag fr-tag--sm">${escapeHtml(t)}</span>`
    ).join(' ');
  }

  // --- Métriques ---
  function renderMetrics() {
    const container = document.getElementById('projet-metrics');
    const empty = document.getElementById('projet-metrics-empty');
    const metrics = [
      { value: card.loc, label: 'Lignes de code', suffix: '' },
      { value: card.test_coverage, label: 'Couverture tests', suffix: '%' },
      { value: card.file_count, label: 'Fichiers', suffix: '' },
      { value: card.commit_count, label: 'Commits', suffix: '' },
    ];

    const filled = metrics.filter(m => m.value != null);
    if (filled.length === 0) {
      container.innerHTML = '';
      empty.classList.remove('vl-hidden');
      return;
    }
    empty.classList.add('vl-hidden');
    container.innerHTML = filled.map(m => `
      <div class="fr-col-${Math.max(4, Math.floor(12 / filled.length))}">
        <div class="vl-kpi" style="padding:0.75rem 0.5rem">
          <span class="vl-kpi__value" style="font-size:1.25rem">${m.value}${m.suffix}</span>
          <span class="vl-kpi__label">${escapeHtml(m.label)}</span>
        </div>
      </div>
    `).join('');
  }

  // --- Notes ---
  function renderNotes() {
    const display = document.getElementById('projet-notes');
    if (card.notes) {
      display.textContent = card.notes;
      display.style.color = '';
    } else {
      display.textContent = 'Aucune note.';
      display.style.color = 'var(--text-mention-grey)';
    }
  }

  // --- Screenshots ---
  function renderScreenshots() {
    const container = document.getElementById('projet-screenshots');
    const empty = document.getElementById('projet-screenshots-empty');
    const screenshots = card.screenshots || [];

    if (screenshots.length === 0) {
      container.innerHTML = '';
      empty.classList.remove('vl-hidden');
      return;
    }
    empty.classList.add('vl-hidden');

    container.innerHTML = screenshots.map(s => `
      <div class="vl-projet-screenshot" data-id="${s.id}">
        <img src="/data/screenshots/${escapeAttr(s.filename)}" alt="${escapeAttr(s.original_name || 'Capture')}" loading="lazy">
        <button class="vl-projet-screenshot-delete" data-screenshot-id="${s.id}" title="Supprimer">
          <span class="fr-icon-delete-line fr-icon--sm" aria-hidden="true"></span>
        </button>
      </div>
    `).join('');

    container.querySelectorAll('.vl-projet-screenshot-delete').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        deleteScreenshot(btn.dataset.screenshotId);
      });
    });

    container.querySelectorAll('.vl-projet-screenshot img').forEach(img => {
      img.addEventListener('click', () => openLightbox(img.src));
    });
  }

  async function uploadScreenshot(file) {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await fetch(API_BASE_URL + '/api/kanban/cards/' + cardId + '/screenshots', {
        method: 'POST',
        headers: { 'Authorization': 'Bearer ' + Auth.getToken() },
        body: formData
      });
      if (res.ok) {
        const data = await res.json();
        if (!card.screenshots) card.screenshots = [];
        card.screenshots.push(data.screenshot);
        renderScreenshots();
      } else {
        handleAuthError(res);
        const err = await res.json().catch(() => ({}));
        alert(err.error || 'Erreur lors de l\'upload');
      }
    } catch (e) {
      console.error('Upload error:', e);
    }
  }

  async function deleteScreenshot(screenshotId) {
    if (!confirm('Supprimer cette capture ?')) return;
    try {
      const res = await fetch(
        API_BASE_URL + '/api/kanban/cards/' + cardId + '/screenshots/' + screenshotId,
        { method: 'DELETE', headers: apiHeaders() }
      );
      if (res.ok) {
        card.screenshots = (card.screenshots || []).filter(s => s.id !== screenshotId);
        renderScreenshots();
      } else {
        handleAuthError(res);
      }
    } catch (e) {
      console.error('Delete screenshot error:', e);
    }
  }

  // --- Lightbox ---
  function openLightbox(src) {
    const overlay = document.createElement('div');
    overlay.className = 'vl-lightbox';
    overlay.innerHTML = `<img src="${escapeAttr(src)}" alt="Capture d'écran">`;
    overlay.addEventListener('click', () => overlay.remove());
    document.body.appendChild(overlay);
  }

  // --- Mode édition inline ---
  function startEdit() {
    document.getElementById('projet-content').setAttribute('data-mode', 'edit');

    document.getElementById('pm-title').value = card.title || '';
    document.getElementById('pm-description').value = card.description || '';
    document.getElementById('pm-priority').value = card.priority || 'moyenne';
    document.getElementById('pm-category').value = card.category || '';
    document.getElementById('pm-column').value = card.column_name || 'propose';
    document.getElementById('pm-sponsor').value = card.sponsor || '';
    document.getElementById('pm-target-audience').value = card.target_audience || '';
    document.getElementById('pm-potential-users').value = card.potential_users || '';
    document.getElementById('pm-stack').value = card.stack || '';
    document.getElementById('pm-dev-duration').value = card.dev_duration || '';
    document.getElementById('pm-dev-duration-real').value = card.dev_duration_real || '';
    document.getElementById('pm-loc').value = card.loc != null ? card.loc : '';
    document.getElementById('pm-test-coverage').value = card.test_coverage != null ? card.test_coverage : '';
    document.getElementById('pm-file-count').value = card.file_count != null ? card.file_count : '';
    document.getElementById('pm-commit-count').value = card.commit_count != null ? card.commit_count : '';
    document.getElementById('pm-repo-url').value = card.repo_url || '';
    document.getElementById('pm-prod-url').value = card.prod_url || '';
    document.getElementById('pm-notes').value = card.notes || '';

    document.getElementById('pm-title').focus();
  }

  function cancelEdit() {
    document.getElementById('projet-content').setAttribute('data-mode', 'view');
  }

  async function saveEdit() {
    const title = document.getElementById('pm-title').value.trim();
    if (!title) { document.getElementById('pm-title').focus(); return; }

    const locVal = document.getElementById('pm-loc').value;
    const coverageVal = document.getElementById('pm-test-coverage').value;
    const fileCountVal = document.getElementById('pm-file-count').value;

    const updates = {
      title,
      description: document.getElementById('pm-description').value.trim(),
      priority: document.getElementById('pm-priority').value,
      category: document.getElementById('pm-category').value.trim(),
      column_name: document.getElementById('pm-column').value,
      sponsor: document.getElementById('pm-sponsor').value.trim(),
      target_audience: document.getElementById('pm-target-audience').value.trim(),
      potential_users: document.getElementById('pm-potential-users').value.trim(),
      stack: document.getElementById('pm-stack').value.trim(),
      dev_duration: document.getElementById('pm-dev-duration').value.trim(),
      dev_duration_real: document.getElementById('pm-dev-duration-real').value.trim(),
      loc: locVal ? parseInt(locVal, 10) : null,
      test_coverage: coverageVal ? parseFloat(coverageVal) : null,
      file_count: fileCountVal ? parseInt(fileCountVal, 10) : null,
      commit_count: (() => { const v = document.getElementById('pm-commit-count').value; return v ? parseInt(v, 10) : null; })(),
      repo_url: document.getElementById('pm-repo-url').value.trim(),
      prod_url: document.getElementById('pm-prod-url').value.trim(),
      notes: document.getElementById('pm-notes').value,
    };

    document.getElementById('projet-content').setAttribute('data-mode', 'view');
    await updateCard(updates);
  }

  // --- GitHub via proxy serveur ---
  async function fetchGitHubData() {
    const match = (card.repo_url || '').match(/github\.com\/([^\/]+\/[^\/\?#]+)/);
    if (!match) return;
    const repoPath = match[1].replace(/\.git$/, '');

    const statusEl = document.getElementById('projet-github-status');
    const btn = document.getElementById('projet-github-fetch');
    statusEl.textContent = 'Chargement…';
    btn.disabled = true;

    try {
      const [langRes, repoRes, commitsRes] = await Promise.all([
        fetch(API_BASE_URL + '/api/github-proxy/' + repoPath + '/languages', {
          headers: apiHeaders()
        }),
        fetch(API_BASE_URL + '/api/github-proxy/' + repoPath, {
          headers: apiHeaders()
        }),
        fetch(API_BASE_URL + '/api/github-proxy/' + repoPath + '/contributors?per_page=100', {
          headers: apiHeaders()
        })
      ]);

      if (!langRes.ok || !repoRes.ok) {
        const errData = await (langRes.ok ? repoRes : langRes).json().catch(() => ({}));
        throw new Error(errData.error || 'Erreur GitHub (code ' + (langRes.ok ? repoRes.status : langRes.status) + ')');
      }

      const languages = await langRes.json();
      const repoInfo = await repoRes.json();
      const updates = {};

      // Top 5 langages
      const topLangs = Object.entries(languages)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5)
        .map(([lang]) => lang);
      if (topLangs.length > 0) {
        updates.stack = topLangs.join(', ');
      }

      // Estimation LOC depuis les bytes de code
      const totalBytes = Object.values(languages).reduce((sum, b) => sum + b, 0);
      if (totalBytes > 0) {
        updates.loc = Math.round(totalBytes / 40);
      }

      // Nombre de commits (via liste des contributeurs)
      if (commitsRes.ok) {
        const contributors = await commitsRes.json();
        if (Array.isArray(contributors)) {
          updates.commit_count = contributors.reduce((sum, c) => sum + (c.contributions || 0), 0);
        }
      }

      if (Object.keys(updates).length > 0) {
        await updateCard(updates);
      }

      statusEl.textContent = 'Mis à jour (' + new Date().toLocaleTimeString('fr-FR') + ')';
    } catch (e) {
      console.error('GitHub fetch error:', e);
      statusEl.textContent = 'Erreur : ' + e.message;
    } finally {
      btn.disabled = false;
    }
  }

  // --- Mise à jour carte ---
  async function updateCard(updates) {
    try {
      const res = await fetch(API_BASE_URL + '/api/kanban/cards/' + cardId, {
        method: 'PUT',
        headers: apiHeaders(),
        body: JSON.stringify(updates)
      });
      if (res.ok) {
        const data = await res.json();
        const screenshots = card.screenshots;
        card = data.card;
        card.screenshots = screenshots;
        renderCard();
      } else {
        handleAuthError(res);
      }
    } catch (e) {
      console.error('Update card error:', e);
    }
  }

  // --- Init ---
  async function init(id) {
    cardId = id;
    await loadCard();

    // Boutons édition
    document.getElementById('projet-edit-btn').addEventListener('click', startEdit);
    document.getElementById('projet-save-btn').addEventListener('click', saveEdit);
    document.getElementById('projet-cancel-btn').addEventListener('click', cancelEdit);

    // GitHub
    const ghBtn = document.getElementById('projet-github-fetch');
    if (ghBtn) ghBtn.addEventListener('click', fetchGitHubData);

    // Screenshot upload
    document.getElementById('projet-screenshot-upload').addEventListener('change', (e) => {
      if (e.target.files[0]) {
        uploadScreenshot(e.target.files[0]);
        e.target.value = '';
      }
    });
  }

  return { init };
})();
