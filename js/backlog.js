// ============================================================
// Module Backlog — Vibe Lab
// Comité d'évaluation : tableau backlog, scoring, saisie
// ============================================================

const Backlog = (() => {
  let cards = [];
  let selectedCardId = null;
  let sortColumn = 'score_total';
  let sortAsc = false;

  const COLUMNS_LABELS = {
    propose: 'Proposé', roadmap: 'Roadmap', developpement: 'En cours',
    test: 'En test', candidat: 'Candidat', deploye: 'Déployé'
  };

  const ENTRY_FIELDS = [
    { key: 'entry_sponsor', label: 'Sponsor métier identifié' },
    { key: 'entry_besoin', label: 'Besoin exprimé clairement' },
    { key: 'entry_donnees', label: 'Données publiques ou agrégées' },
    { key: 'entry_hors_bercyhub', label: 'Hors périmètre BercyHub' },
    { key: 'entry_pas_existant', label: 'Pas de solution existante' },
    { key: 'entry_prototypable', label: 'Prototypable en 2 semaines' }
  ];

  const SCORE_FIELDS = [
    { key: 'score_impact', label: 'Impact utilisateur', weight: 3, hint: 'Combien d\'agents concernés ? Gain de temps ?' },
    { key: 'score_urgence', label: 'Urgence métier', weight: 2, hint: 'Échéance, obligation réglementaire ?' },
    { key: 'score_donnees', label: 'Disponibilité données', weight: 2, hint: 'API ou export immédiatement accessible ?' },
    { key: 'score_visibilite', label: 'Visibilité / démonstration', weight: 1, hint: 'Valeur vitrine pour le Lab ?' },
    { key: 'score_complexite', label: 'Complexité technique (inv.)', weight: 1, hint: 'Plus c\'est simple, plus la note est haute' },
    { key: 'score_reutilisabilite', label: 'Réutilisabilité', weight: 1, hint: 'Composants réutilisables ?' }
  ];

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

  function formatDate(iso) {
    if (!iso) return '—';
    const d = new Date(iso + 'Z');
    return d.toLocaleDateString('fr-FR', { day: '2-digit', month: '2-digit', year: 'numeric' });
  }

  // --- Data ---
  async function loadCards() {
    try {
      const res = await fetch(API_BASE_URL + '/api/backlog/cards', { headers: apiHeaders() });
      if (!res.ok) { handleAuthError(res); return; }
      const data = await res.json();
      cards = data.cards || [];
    } catch (e) {
      console.error('Backlog load error:', e);
      cards = [];
    }
  }

  // ================================================================
  // TAB 1 : BACKLOG TABLE
  // ================================================================

  function renderTable() {
    const container = document.getElementById('backlog-table-container');
    if (!container) return;

    const sorted = [...cards].sort((a, b) => {
      let va = a[sortColumn], vb = b[sortColumn];
      // Null values at the bottom
      if (va == null && vb == null) return 0;
      if (va == null) return 1;
      if (vb == null) return -1;
      if (typeof va === 'string') va = va.toLowerCase();
      if (typeof vb === 'string') vb = vb.toLowerCase();
      if (va < vb) return sortAsc ? -1 : 1;
      if (va > vb) return sortAsc ? 1 : -1;
      return 0;
    });

    const scored = cards.filter(c => c.score_total != null);
    const avgScore = scored.length ? Math.round(scored.reduce((s, c) => s + c.score_total, 0) / scored.length) : null;

    let html = `
      <div class="fr-table">
        <div class="fr-table__wrapper"><div class="fr-table__container"><div class="fr-table__content">
          <table>
            <caption class="fr-sr-only">Backlog des projets</caption>
            <thead><tr>
              ${tableHeader('title', 'Projet')}
              ${tableHeader('sponsor', 'Sponsor')}
              ${tableHeader('category', 'Catégorie')}
              <th scope="col">Critères</th>
              ${tableHeader('score_total', 'Score')}
              ${tableHeader('column_name', 'Statut')}
              ${tableHeader('created_at', 'Date')}
              <th scope="col">Actions</th>
            </tr></thead>
            <tbody>`;

    if (sorted.length === 0) {
      html += '<tr><td colspan="8" style="text-align:center;padding:2rem">Aucun projet dans le backlog</td></tr>';
    }

    for (const card of sorted) {
      const ec = entryCriteriaCount(card);
      const ecClass = ec.met === 6 ? 'fr-badge--success' : (ec.filled > 0 ? 'fr-badge--warning' : '');
      const scoreBadge = scoreBadgeHtml(card.score_total);
      const statusBadge = `<span class="fr-badge fr-badge--sm fr-badge--no-icon">${escapeHtml(COLUMNS_LABELS[card.column_name] || card.column_name)}</span>`;

      html += `<tr>
        <td><a href="/projet/${card.id}">${escapeHtml(card.title)}</a></td>
        <td>${escapeHtml(card.sponsor) || '—'}</td>
        <td>${card.category ? `<span class="fr-tag fr-tag--sm">${escapeHtml(card.category)}</span>` : '—'}</td>
        <td><span class="fr-badge fr-badge--sm fr-badge--no-icon ${ecClass}">${ec.met}/6</span></td>
        <td>${scoreBadge}</td>
        <td>${statusBadge}</td>
        <td>${formatDate(card.created_at)}</td>
        <td><button class="fr-btn fr-btn--sm fr-btn--tertiary" data-eval-id="${card.id}">Évaluer</button></td>
      </tr>`;
    }

    html += `</tbody></table>
        </div></div></div>
      </div>
      <p class="fr-text--sm fr-mt-2w" style="color:var(--text-mention-grey)">
        ${cards.length} projet${cards.length > 1 ? 's' : ''}${avgScore != null ? ` · Score moyen : ${avgScore}/50` : ''}
        · ${scored.length} évalué${scored.length > 1 ? 's' : ''}
      </p>`;

    container.innerHTML = html;

    // Bind sort headers
    container.querySelectorAll('[data-sort]').forEach(th => {
      th.addEventListener('click', () => handleSort(th.dataset.sort));
    });

    // Bind "Évaluer" buttons
    container.querySelectorAll('[data-eval-id]').forEach(btn => {
      btn.addEventListener('click', () => navigateToEvaluation(btn.dataset.evalId));
    });
  }

  function tableHeader(col, label) {
    const arrow = sortColumn === col ? (sortAsc ? ' ▲' : ' ▼') : '';
    return `<th scope="col" class="vl-sortable-header" data-sort="${col}">${label}<span class="vl-sort-indicator">${arrow}</span></th>`;
  }

  function handleSort(column) {
    if (sortColumn === column) { sortAsc = !sortAsc; }
    else { sortColumn = column; sortAsc = column === 'title'; }
    renderTable();
  }

  function entryCriteriaCount(card) {
    let met = 0, filled = 0;
    for (const f of ENTRY_FIELDS) {
      if (card[f.key] != null) { filled++; if (card[f.key] === 1) met++; }
    }
    return { met, filled };
  }

  function scoreBadgeHtml(score) {
    if (score == null) return '<span class="fr-badge fr-badge--sm fr-badge--no-icon" style="opacity:.5">—</span>';
    let cls = 'fr-badge--error';
    if (score >= 25) cls = 'fr-badge--success';
    else if (score >= 15) cls = 'fr-badge--warning';
    return `<span class="fr-badge fr-badge--sm fr-badge--no-icon ${cls}">${score}/50</span>`;
  }

  // ================================================================
  // TAB 2 : ÉVALUER UN PROJET
  // ================================================================

  function renderEvaluation(cardId) {
    selectedCardId = cardId;
    const container = document.getElementById('backlog-eval-container');
    if (!container) return;

    // Project selector
    let html = `
      <div class="fr-select-group fr-mb-3w">
        <label class="fr-label" for="eval-select">Projet à évaluer</label>
        <select class="fr-select" id="eval-select">
          <option value="">— Sélectionner un projet —</option>
          ${cards.map(c => `<option value="${c.id}"${c.id === cardId ? ' selected' : ''}>${escapeHtml(c.title)}${c.score_total != null ? ` (${c.score_total}/50)` : ''}</option>`).join('')}
        </select>
      </div>`;

    const card = cards.find(c => c.id === cardId);
    if (!card) {
      html += '<p class="fr-text--sm" style="color:var(--text-mention-grey)">Sélectionnez un projet pour l\'évaluer.</p>';
      container.innerHTML = html;
      container.querySelector('#eval-select').addEventListener('change', onSelectChange);
      return;
    }

    // Entry criteria
    html += `
      <h3 class="fr-mb-2w">Critères d'entrée</h3>
      <p class="fr-text--sm fr-mb-2w">Tous les critères doivent être remplis pour qu'un projet soit éligible.</p>
      <div class="vl-entry-criteria fr-mb-2w">
        ${ENTRY_FIELDS.map(f => `
          <div class="fr-checkbox-group">
            <input type="checkbox" id="eval-${f.key}" name="${f.key}" ${card[f.key] === 1 ? 'checked' : ''}>
            <label class="fr-label" for="eval-${f.key}">${f.label}</label>
          </div>
        `).join('')}
      </div>
      <div id="eval-entry-result" class="fr-mb-4w"></div>`;

    // Scoring grid
    html += `
      <h3 class="fr-mb-2w">Scoring de priorisation</h3>
      <div class="fr-table fr-mb-2w">
        <div class="fr-table__wrapper"><div class="fr-table__container"><div class="fr-table__content">
          <table class="vl-eval-grid">
            <thead><tr>
              <th scope="col">Critère</th>
              <th scope="col" style="width:4rem;text-align:center">Poids</th>
              <th scope="col" style="width:8rem">Note (1-5)</th>
              <th scope="col" style="width:5rem;text-align:center">Pondéré</th>
              <th scope="col">Question clé</th>
            </tr></thead>
            <tbody>
              ${SCORE_FIELDS.map(f => {
                const val = card[f.key];
                const weighted = val != null ? val * f.weight : '';
                return `<tr>
                  <td><strong>${f.label}</strong></td>
                  <td style="text-align:center">×${f.weight}</td>
                  <td>
                    <select class="fr-select fr-select--sm" id="eval-${f.key}" name="${f.key}" style="width:100%">
                      <option value="">—</option>
                      ${[1,2,3,4,5].map(n => `<option value="${n}"${val === n ? ' selected' : ''}>${n}</option>`).join('')}
                    </select>
                  </td>
                  <td class="vl-eval-weighted" id="weighted-${f.key}">${weighted}</td>
                  <td class="fr-text--sm" style="color:var(--text-mention-grey)">${f.hint}</td>
                </tr>`;
              }).join('')}
            </tbody>
          </table>
        </div></div></div>
      </div>

      <div class="fr-grid-row fr-grid-row--gutters fr-mb-4w" style="align-items:center">
        <div class="fr-col-auto">
          <div class="vl-backlog-score" id="eval-total">—</div>
          <div class="vl-backlog-threshold">/ 50 · Seuil recommandé : ≥ 25</div>
        </div>
        <div class="fr-col-auto" id="eval-threshold-badge"></div>
      </div>

      <div class="fr-input-group fr-mb-3w">
        <label class="fr-label" for="eval-notes">Notes d'évaluation</label>
        <textarea class="fr-input" id="eval-notes" rows="3">${escapeHtml(card.evaluation_notes || '')}</textarea>
      </div>

      <div style="display:flex;gap:1rem;align-items:center">
        <button class="fr-btn" id="eval-save-btn">Enregistrer l'évaluation</button>
        <span id="eval-save-status"></span>
      </div>`;

    container.innerHTML = html;

    // Bind events
    container.querySelector('#eval-select').addEventListener('change', onSelectChange);

    // Entry criteria live update
    ENTRY_FIELDS.forEach(f => {
      container.querySelector(`#eval-${f.key}`).addEventListener('change', updateEntryResult);
    });
    updateEntryResult();

    // Score live update
    SCORE_FIELDS.forEach(f => {
      container.querySelector(`#eval-${f.key}`).addEventListener('change', updateScoreTotal);
    });
    updateScoreTotal();

    // Save
    container.querySelector('#eval-save-btn').addEventListener('click', handleSaveEvaluation);
  }

  function onSelectChange(e) {
    renderEvaluation(e.target.value || null);
  }

  function updateEntryResult() {
    let met = 0;
    ENTRY_FIELDS.forEach(f => {
      if (document.getElementById(`eval-${f.key}`).checked) met++;
    });
    const el = document.getElementById('eval-entry-result');
    if (met === 6) {
      el.innerHTML = '<div class="vl-entry-result vl-entry-result--pass">Critères d\'entrée : VALIDÉS (6/6)</div>';
    } else {
      el.innerHTML = `<div class="vl-entry-result vl-entry-result--fail">Critères d'entrée : NON VALIDÉS (${met}/6)</div>`;
    }
  }

  function updateScoreTotal() {
    let total = 0;
    let allFilled = true;
    SCORE_FIELDS.forEach(f => {
      const sel = document.getElementById(`eval-${f.key}`);
      const val = sel.value ? parseInt(sel.value) : null;
      const weightedEl = document.getElementById(`weighted-${f.key}`);
      if (val != null) {
        const w = val * f.weight;
        weightedEl.textContent = w;
        total += w;
      } else {
        weightedEl.textContent = '';
        allFilled = false;
      }
    });

    const totalEl = document.getElementById('eval-total');
    const badgeEl = document.getElementById('eval-threshold-badge');

    if (!allFilled && total === 0) {
      totalEl.textContent = '—';
      totalEl.className = 'vl-backlog-score';
      badgeEl.innerHTML = '';
    } else {
      totalEl.textContent = total;
      if (total >= 25) {
        totalEl.className = 'vl-backlog-score vl-backlog-score--pass';
        badgeEl.innerHTML = '<span class="fr-badge fr-badge--success fr-badge--no-icon">Au-dessus du seuil</span>';
      } else {
        totalEl.className = 'vl-backlog-score vl-backlog-score--fail';
        badgeEl.innerHTML = '<span class="fr-badge fr-badge--error fr-badge--no-icon">Sous le seuil</span>';
      }
    }
  }

  async function handleSaveEvaluation() {
    if (!selectedCardId) return;
    const statusEl = document.getElementById('eval-save-status');
    statusEl.textContent = 'Enregistrement…';

    const payload = { evaluation_notes: document.getElementById('eval-notes').value };

    // Entry criteria
    ENTRY_FIELDS.forEach(f => {
      payload[f.key] = document.getElementById(`eval-${f.key}`).checked ? 1 : 0;
    });

    // Scores
    SCORE_FIELDS.forEach(f => {
      const val = document.getElementById(`eval-${f.key}`).value;
      payload[f.key] = val ? parseInt(val) : null;
    });

    try {
      const res = await fetch(API_BASE_URL + '/api/kanban/cards/' + selectedCardId + '/evaluate', {
        method: 'PUT',
        headers: apiHeaders(),
        body: JSON.stringify(payload)
      });
      if (!res.ok) { handleAuthError(res); statusEl.textContent = 'Erreur'; return; }
      const data = await res.json();

      // Update local card data
      const idx = cards.findIndex(c => c.id === selectedCardId);
      if (idx >= 0) cards[idx] = data.card;

      statusEl.innerHTML = '<span class="fr-badge fr-badge--success fr-badge--no-icon">Enregistré</span>';
      setTimeout(() => { statusEl.textContent = ''; }, 3000);

      // Refresh table
      renderTable();
    } catch (e) {
      console.error('Save evaluation error:', e);
      statusEl.textContent = 'Erreur réseau';
    }
  }

  // ================================================================
  // TAB 3 : SAISIR UN PROJET
  // ================================================================

  function renderForm() {
    const container = document.getElementById('backlog-form-container');
    if (!container) return;

    container.innerHTML = `
      <h3 class="fr-mb-2w">Proposer un nouveau projet</h3>
      <p class="fr-text--sm fr-mb-3w" style="color:var(--text-mention-grey)">Le projet sera ajouté dans la colonne « Proposé » du kanban.</p>

      <div id="form-alert"></div>

      <div class="fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-12 fr-col-md-8">
          <div class="fr-input-group">
            <label class="fr-label" for="form-title">Titre du projet *</label>
            <input class="fr-input" type="text" id="form-title" required>
          </div>
        </div>
        <div class="fr-col-12 fr-col-md-4">
          <div class="fr-select-group">
            <label class="fr-label" for="form-priority">Priorité</label>
            <select class="fr-select" id="form-priority">
              <option value="moyenne" selected>Moyenne</option>
              <option value="haute">Haute</option>
              <option value="basse">Basse</option>
            </select>
          </div>
        </div>
      </div>

      <div class="fr-input-group">
        <label class="fr-label" for="form-description">Description du besoin</label>
        <textarea class="fr-input" id="form-description" rows="3"></textarea>
      </div>

      <div class="fr-grid-row fr-grid-row--gutters">
        <div class="fr-col-12 fr-col-md-4">
          <div class="fr-input-group">
            <label class="fr-label" for="form-sponsor">Sponsor métier</label>
            <input class="fr-input" type="text" id="form-sponsor">
          </div>
        </div>
        <div class="fr-col-12 fr-col-md-4">
          <div class="fr-input-group">
            <label class="fr-label" for="form-target">Publics ciblés</label>
            <input class="fr-input" type="text" id="form-target" placeholder="Ex: Agents MEF, DIRCOM…">
          </div>
        </div>
        <div class="fr-col-12 fr-col-md-4">
          <div class="fr-input-group">
            <label class="fr-label" for="form-category">Catégorie</label>
            <input class="fr-input" type="text" id="form-category" placeholder="Ex: Outils, Pilotage…">
          </div>
        </div>
      </div>

      <button class="fr-btn fr-mt-2w" id="form-submit-btn">Ajouter au backlog</button>
    `;

    container.querySelector('#form-submit-btn').addEventListener('click', handleSubmitProject);
  }

  async function handleSubmitProject() {
    const title = document.getElementById('form-title').value.trim();
    if (!title) {
      showFormAlert('Veuillez saisir un titre.', 'error');
      return;
    }

    const payload = {
      title,
      description: document.getElementById('form-description').value.trim(),
      priority: document.getElementById('form-priority').value,
      category: document.getElementById('form-category').value.trim(),
      sponsor: document.getElementById('form-sponsor').value.trim(),
      target_audience: document.getElementById('form-target').value.trim(),
      column_name: 'propose'
    };

    try {
      const res = await fetch(API_BASE_URL + '/api/kanban/cards', {
        method: 'POST',
        headers: apiHeaders(),
        body: JSON.stringify(payload)
      });
      if (!res.ok) { handleAuthError(res); showFormAlert('Erreur lors de la création.', 'error'); return; }

      const data = await res.json();

      // Update sponsor/target if set (create doesn't include these)
      if (payload.sponsor || payload.target_audience) {
        await fetch(API_BASE_URL + '/api/kanban/cards/' + data.card.id, {
          method: 'PUT',
          headers: apiHeaders(),
          body: JSON.stringify({ sponsor: payload.sponsor, target_audience: payload.target_audience })
        });
      }

      showFormAlert(`Projet « ${escapeHtml(title)} » ajouté au backlog.`, 'success');

      // Clear form
      document.getElementById('form-title').value = '';
      document.getElementById('form-description').value = '';
      document.getElementById('form-sponsor').value = '';
      document.getElementById('form-target').value = '';
      document.getElementById('form-category').value = '';
      document.getElementById('form-priority').value = 'moyenne';

      // Reload
      await loadCards();
      renderTable();
    } catch (e) {
      console.error('Create project error:', e);
      showFormAlert('Erreur réseau.', 'error');
    }
  }

  function showFormAlert(msg, type) {
    const el = document.getElementById('form-alert');
    const cls = type === 'success' ? 'fr-alert--success' : 'fr-alert--error';
    el.innerHTML = `<div class="fr-alert ${cls} fr-alert--sm fr-mb-2w"><p>${msg}</p></div>`;
    if (type === 'success') setTimeout(() => { el.innerHTML = ''; }, 5000);
  }

  // ================================================================
  // NAVIGATION INTER-ONGLETS
  // ================================================================

  function navigateToEvaluation(cardId) {
    selectedCardId = cardId;
    // Activate the "Évaluer" tab via DSFR
    const tabBtn = document.getElementById('tabpanel-evaluer-tab');
    if (tabBtn) tabBtn.click();
    // Render after a short delay to let DSFR show the panel
    setTimeout(() => renderEvaluation(cardId), 50);
  }

  // ================================================================
  // INIT
  // ================================================================

  async function init() {
    await loadCards();
    renderTable();
    renderForm();
    renderEvaluation(null);
  }

  return { init, navigateToEvaluation };
})();
