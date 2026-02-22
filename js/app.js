// ============================================================
// Module principal — Vibe Lab
// Auth, navigation, réalisations
// ============================================================

(function () {
  'use strict';

  const loginPage = document.getElementById('login-page');
  const mainApp = document.getElementById('main-app');
  const loginBtn = document.getElementById('login-btn');
  const logoutBtn = document.getElementById('logout-btn');
  const loginEmail = document.getElementById('login-email');
  const loginPassword = document.getElementById('login-password');
  const loginError = document.getElementById('login-error');
  const loginErrorMsg = document.getElementById('login-error-msg');
  const userDisplay = document.getElementById('user-display');

  // --- Affichage conditionnel ---
  function showLogin() {
    loginPage.classList.remove('vl-hidden');
    mainApp.classList.add('vl-hidden');
    loginEmail.value = '';
    loginPassword.value = '';
    loginError.classList.add('vl-hidden');
    loginEmail.focus();
  }

  function showApp() {
    loginPage.classList.add('vl-hidden');
    mainApp.classList.remove('vl-hidden');
    const user = Auth.getUser();
    if (user) {
      userDisplay.textContent = user.email;
    }
    // Charger les réalisations sur la page d'accueil
    loadRealisations();
    // Notifier les scripts de page (ex: kanban.init)
    document.dispatchEvent(new Event('vl:app-shown'));
  }

  // --- Login handler ---
  async function handleLogin() {
    const email = loginEmail.value.trim();
    const password = loginPassword.value;

    if (!email || !password) {
      showError('Veuillez remplir tous les champs.');
      return;
    }

    loginBtn.disabled = true;
    loginBtn.textContent = 'Connexion...';

    try {
      await Auth.login(email, password);
      showApp();
    } catch (err) {
      showError(err.message || 'Identifiants incorrects.');
    } finally {
      loginBtn.disabled = false;
      loginBtn.textContent = 'Se connecter';
    }
  }

  function showError(msg) {
    loginErrorMsg.textContent = msg;
    loginError.classList.remove('vl-hidden');
  }

  // --- Réalisations (accueil) ---
  async function loadRealisations() {
    const container = document.getElementById('realisations-container');
    if (!container) return;

    const token = Auth.getToken();
    if (!token) return;

    try {
      const res = await fetch(API_BASE_URL + '/api/kanban/cards', {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      if (!res.ok) return;
      const data = await res.json();
      const realisations = (data.cards || []).filter(c =>
        ['test', 'candidat', 'deploye'].includes(c.column_name)
      );

      if (realisations.length === 0) {
        container.innerHTML = '';
        return;
      }

      const statusLabels = {
        test: { label: 'En test', badge: 'fr-badge--yellow-tournesol' },
        candidat: { label: 'Candidat', badge: 'fr-badge--green-emeraude' },
        deploye: { label: 'Déployé', badge: 'fr-badge--purple-glycine' }
      };

      let html = '<h3 class="fr-mb-2w">Réalisations</h3>';
      html += '<div class="fr-grid-row fr-grid-row--gutters">';

      realisations.forEach(card => {
        const status = statusLabels[card.column_name] || { label: card.column_name, badge: '' };
        const titleHtml = `<a href="/projet/${card.id}">${escapeHtml(card.title)}</a>`;

        let footerLinks = '';
        if (card.repo_url || card.prod_url) {
          footerLinks = '<div class="fr-card__footer"><ul class="fr-links-group">';
          if (card.prod_url) {
            footerLinks += `<li><a class="fr-link fr-link--sm" href="${escapeAttr(card.prod_url)}" target="_blank" rel="noopener">Accéder</a></li>`;
          }
          if (card.repo_url) {
            footerLinks += `<li><a class="fr-link fr-link--sm" href="${escapeAttr(card.repo_url)}" target="_blank" rel="noopener">Code source</a></li>`;
          }
          footerLinks += '</ul></div>';
        }

        html += `
          <div class="fr-col-12 fr-col-md-4">
            <div class="fr-card fr-card--shadow">
              <div class="fr-card__body">
                <div class="fr-card__content">
                  <h4 class="fr-card__title">${titleHtml}</h4>
                  <p class="fr-card__detail">
                    <span class="fr-badge fr-badge--sm fr-badge--no-icon ${status.badge}">${status.label}</span>
                    ${card.category ? `<span class="fr-tag fr-tag--sm fr-ml-1w">${escapeHtml(card.category)}</span>` : ''}
                  </p>
                  ${card.description ? `<p class="fr-card__desc">${escapeHtml(card.description)}</p>` : ''}
                </div>
                ${footerLinks}
              </div>
            </div>
          </div>`;
      });

      html += '</div>';
      container.innerHTML = html;
    } catch (e) {
      console.error('Erreur chargement réalisations:', e);
    }
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  function escapeAttr(text) {
    return text.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  // --- Keyboard navigation ---
  function initKeyboard() {
    loginEmail.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') loginPassword.focus();
    });
    loginPassword.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') handleLogin();
    });
  }

  // --- Init ---
  async function init() {
    // Souscrire aux changements d'auth
    Auth.subscribe((isAuth) => {
      if (isAuth) showApp();
      else showLogin();
    });

    // Initialiser auth (async — vérifie le token avec le serveur)
    await Auth.init();

    // Si déjà authentifié
    if (Auth.isAuthenticated()) {
      showApp();
    } else {
      showLogin();
    }

    // Event listeners
    loginBtn.addEventListener('click', handleLogin);
    logoutBtn.addEventListener('click', () => Auth.logout());

    // Init clavier
    initKeyboard();
  }

  // Lancer quand le DOM est prêt
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
