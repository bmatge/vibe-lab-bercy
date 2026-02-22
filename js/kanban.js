// ============================================================
// Module Kanban — Vibe Lab
// SortableJS drag & drop + persistance API REST / SQLite
// ============================================================

const Kanban = (() => {
  const COLUMNS = ['propose', 'roadmap', 'developpement', 'test', 'candidat', 'deploye'];
  let cards = [];
  let sortables = [];
  let initialized = false;

  // --- Helpers API ---
  function apiHeaders() {
    return {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + Auth.getToken()
    };
  }

  function handleAuthError(res) {
    if (res.status === 401) {
      Auth.logout();
    }
  }

  // --- Persistance ---
  async function loadCards() {
    try {
      const res = await fetch(API_BASE_URL + '/api/kanban/cards', {
        headers: apiHeaders()
      });
      if (!res.ok) { handleAuthError(res); return; }
      const data = await res.json();
      cards = data.cards || [];
    } catch (e) {
      console.error('Load cards error:', e);
      cards = [];
    }
  }

  async function saveCard(card) {
    try {
      if (card.id && !card.id.startsWith('temp-')) {
        // Update
        const res = await fetch(API_BASE_URL + '/api/kanban/cards/' + card.id, {
          method: 'PUT',
          headers: apiHeaders(),
          body: JSON.stringify({
            title: card.title,
            description: card.description,
            priority: card.priority,
            category: card.category,
            column_name: card.column_name,
            position: card.position,
            repo_url: card.repo_url || '',
            prod_url: card.prod_url || ''
          })
        });
        if (!res.ok) handleAuthError(res);
      } else {
        // Create
        const res = await fetch(API_BASE_URL + '/api/kanban/cards', {
          method: 'POST',
          headers: apiHeaders(),
          body: JSON.stringify({
            title: card.title,
            description: card.description,
            priority: card.priority,
            category: card.category,
            column_name: card.column_name,
            position: card.position,
            repo_url: card.repo_url || '',
            prod_url: card.prod_url || ''
          })
        });
        if (res.ok) {
          const data = await res.json();
          const idx = cards.findIndex(c => c.id === card.id);
          if (idx >= 0) cards[idx].id = data.card.id;
        } else {
          handleAuthError(res);
        }
      }
    } catch (e) {
      console.error('Save card error:', e);
    }
  }

  async function deleteCardFromDB(cardId) {
    try {
      const res = await fetch(API_BASE_URL + '/api/kanban/cards/' + cardId, {
        method: 'DELETE',
        headers: apiHeaders()
      });
      if (!res.ok) handleAuthError(res);
    } catch (e) {
      console.error('Delete card error:', e);
    }
    cards = cards.filter(c => c.id !== cardId);
  }

  // --- Rendu ---
  function renderCards() {
    COLUMNS.forEach(col => {
      const container = document.getElementById('sortable-' + col);
      if (!container) return;
      container.innerHTML = '';
      const colCards = cards.filter(c => c.column_name === col).sort((a, b) => a.position - b.position);
      colCards.forEach(card => {
        container.appendChild(createCardElement(card));
      });
      // Mise à jour compteur
      const badge = document.querySelector(`.vl-count[data-column="${col}"]`);
      if (badge) badge.textContent = colCards.length;
    });
  }

  function createCardElement(card) {
    const el = document.createElement('div');
    el.className = 'vl-kanban-card';
    el.dataset.cardId = card.id;

    const priorityClass = {
      haute: 'fr-badge--error',
      moyenne: 'fr-badge--warning',
      basse: 'fr-badge--success'
    }[card.priority] || 'fr-badge--info';

    // Liens repo / prod
    let linksHtml = '';
    if (card.repo_url || card.prod_url) {
      linksHtml = '<div class="vl-kanban-card-links">';
      if (card.prod_url) {
        linksHtml += `<a href="${escapeAttr(card.prod_url)}" target="_blank" rel="noopener" title="Production">Prod</a>`;
      }
      if (card.repo_url) {
        linksHtml += `<a href="${escapeAttr(card.repo_url)}" target="_blank" rel="noopener" title="Dépôt Git">Git</a>`;
      }
      linksHtml += '</div>';
    }

    el.innerHTML = `
      <div class="vl-kanban-card-top">
        <span class="vl-kanban-card-title">${escapeHtml(card.title)}</span>
        <div class="vl-kanban-card-actions">
          <button class="vl-card-btn" data-action="edit" data-id="${card.id}" title="Modifier">
            <span class="fr-icon-edit-line fr-icon--sm" aria-hidden="true"></span>
          </button>
          <button class="vl-card-btn vl-card-btn--delete" data-action="delete" data-id="${card.id}" title="Supprimer">
            <span class="fr-icon-delete-line fr-icon--sm" aria-hidden="true"></span>
          </button>
        </div>
      </div>
      ${card.description ? `<p class="vl-kanban-card-desc">${escapeHtml(card.description)}</p>` : ''}
      <div class="vl-kanban-card-footer">
        <span class="fr-badge fr-badge--sm fr-badge--no-icon ${priorityClass}">${card.priority}</span>
        ${card.category ? `<span class="fr-tag fr-tag--sm">${escapeHtml(card.category)}</span>` : ''}
      </div>
      ${linksHtml}
    `;

    // Event listeners
    el.querySelector('[data-action="edit"]').addEventListener('click', (e) => {
      e.stopPropagation();
      openModal(card);
    });
    el.querySelector('[data-action="delete"]').addEventListener('click', (e) => {
      e.stopPropagation();
      if (confirm('Supprimer ce projet ?')) {
        deleteCardFromDB(card.id).then(() => renderCards());
      }
    });

    return el;
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  function escapeAttr(text) {
    return (text || '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  // --- Modal ---
  function openModal(card) {
    const modal = document.getElementById('kanban-modal');
    const title = document.getElementById('kanban-modal-title');
    const idInput = document.getElementById('card-id');
    const titleInput = document.getElementById('card-title');
    const descInput = document.getElementById('card-description');
    const prioInput = document.getElementById('card-priority');
    const catInput = document.getElementById('card-category');
    const colInput = document.getElementById('card-column');
    const repoInput = document.getElementById('card-repo-url');
    const prodInput = document.getElementById('card-prod-url');

    if (card) {
      title.textContent = 'Modifier le projet';
      idInput.value = card.id;
      titleInput.value = card.title;
      descInput.value = card.description || '';
      prioInput.value = card.priority;
      catInput.value = card.category || '';
      colInput.value = card.column_name;
      repoInput.value = card.repo_url || '';
      prodInput.value = card.prod_url || '';
    } else {
      title.textContent = 'Nouveau projet';
      idInput.value = '';
      titleInput.value = '';
      descInput.value = '';
      prioInput.value = 'moyenne';
      catInput.value = '';
      colInput.value = 'propose';
      repoInput.value = '';
      prodInput.value = '';
    }

    modal.showModal ? modal.showModal() : modal.setAttribute('open', '');
    modal.classList.add('fr-modal--opened');
    titleInput.focus();
  }

  function closeModal() {
    const modal = document.getElementById('kanban-modal');
    modal.close ? modal.close() : modal.removeAttribute('open');
    modal.classList.remove('fr-modal--opened');
  }

  function handleSave() {
    const titleInput = document.getElementById('card-title');
    const title = titleInput.value.trim();
    if (!title) { titleInput.focus(); return; }

    const id = document.getElementById('card-id').value;
    const description = document.getElementById('card-description').value.trim();
    const priority = document.getElementById('card-priority').value;
    const category = document.getElementById('card-category').value.trim();
    const column_name = document.getElementById('card-column').value;
    const repo_url = document.getElementById('card-repo-url').value.trim();
    const prod_url = document.getElementById('card-prod-url').value.trim();

    if (id) {
      // Édition
      const card = cards.find(c => c.id === id);
      if (card) {
        card.title = title;
        card.description = description;
        card.priority = priority;
        card.category = category;
        card.repo_url = repo_url;
        card.prod_url = prod_url;
        saveCard(card);
      }
    } else {
      // Nouveau
      const colCards = cards.filter(c => c.column_name === column_name);
      const newCard = {
        id: 'temp-' + Date.now(),
        title, description, priority, category, column_name,
        position: colCards.length,
        repo_url, prod_url
      };
      cards.push(newCard);
      saveCard(newCard);
    }

    closeModal();
    renderCards();
  }

  // --- Export CSV ---
  function exportCSV() {
    if (cards.length === 0) return;

    const headers = ['Titre', 'Description', 'Priorité', 'Catégorie', 'Colonne', 'Dépôt Git', 'URL Production', 'Créé le', 'Mis à jour le'];
    const rows = cards.map(c => [
      c.title, c.description || '', c.priority, c.category || '',
      c.column_name, c.repo_url || '', c.prod_url || '',
      c.created_at || '', c.updated_at || ''
    ]);

    const csvContent = [headers, ...rows]
      .map(row => row.map(cell => '"' + String(cell).replace(/"/g, '""') + '"').join(','))
      .join('\n');

    const blob = new Blob(['\uFEFF' + csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    const date = new Date().toISOString().slice(0, 10);
    a.href = url;
    a.download = `vibelab-kanban-${date}.csv`;
    a.click();
    URL.revokeObjectURL(url);
  }

  // --- SortableJS ---
  function initSortable() {
    sortables.forEach(s => s.destroy());
    sortables = [];

    COLUMNS.forEach(col => {
      const el = document.getElementById('sortable-' + col);
      if (!el) return;
      const s = Sortable.create(el, {
        group: 'kanban',
        animation: 150,
        ghostClass: 'vl-kanban-card--ghost',
        dragClass: 'vl-kanban-card--drag',
        onEnd(evt) {
          const cardId = evt.item.dataset.cardId;
          const newCol = evt.to.id.replace('sortable-', '');
          const card = cards.find(c => c.id === cardId);
          if (!card) return;

          card.column_name = newCol;
          card.position = evt.newIndex;

          // Recalculer positions de la colonne cible
          const targetContainer = evt.to;
          Array.from(targetContainer.children).forEach((child, idx) => {
            const cid = child.dataset.cardId;
            const c = cards.find(x => x.id === cid);
            if (c) {
              c.position = idx;
              saveCard(c);
            }
          });

          renderCards();
        }
      });
      sortables.push(s);
    });
  }

  // --- Init public ---
  async function init() {
    if (initialized) {
      renderCards();
      return;
    }

    await loadCards();
    renderCards();
    initSortable();

    // Bouton ajouter
    document.getElementById('kanban-add-btn').addEventListener('click', () => openModal(null));

    // Bouton export CSV
    document.getElementById('kanban-export-btn').addEventListener('click', exportCSV);

    // Boutons modal
    document.getElementById('modal-save-btn').addEventListener('click', handleSave);
    document.getElementById('modal-cancel-btn').addEventListener('click', closeModal);
    document.getElementById('modal-close-btn').addEventListener('click', closeModal);

    // Fermer au clic hors modal
    document.getElementById('kanban-modal').addEventListener('click', (e) => {
      if (e.target === e.currentTarget) closeModal();
    });

    // Enter pour sauvegarder
    document.getElementById('card-title').addEventListener('keydown', (e) => {
      if (e.key === 'Enter') handleSave();
    });

    initialized = true;
  }

  return { init, renderCards, openModal, closeModal };
})();
