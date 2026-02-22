// ============================================================
// Module principal — Vibe Lab
// Orchestration auth, navigation, initialisation
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

  // --- Navigation onglets ---
  function initTabs() {
    const tabs = document.querySelectorAll('.fr-tabs__tab');
    const panels = document.querySelectorAll('.fr-tabs__panel');

    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        // Désactiver tous
        tabs.forEach(t => {
          t.setAttribute('aria-selected', 'false');
          t.setAttribute('tabindex', '-1');
        });
        panels.forEach(p => p.classList.remove('fr-tabs__panel--selected'));

        // Activer le cliqué
        tab.setAttribute('aria-selected', 'true');
        tab.setAttribute('tabindex', '0');
        const panelId = tab.getAttribute('aria-controls');
        const panel = document.getElementById(panelId);
        if (panel) {
          panel.classList.add('fr-tabs__panel--selected');
        }

        // Init Kanban si besoin
        if (panelId === 'panel-kanban') {
          Kanban.init();
        }

        // Sauvegarder onglet actif
        localStorage.setItem('vl_active_tab', tab.id);
      });
    });

    // Restaurer onglet actif
    const savedTab = localStorage.getItem('vl_active_tab');
    if (savedTab) {
      const tab = document.getElementById(savedTab);
      if (tab) tab.click();
    }
  }

  // --- Keyboard navigation ---
  function initKeyboard() {
    // Enter sur les champs login
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

    // Init navigation
    initTabs();
    initKeyboard();
  }

  // Lancer quand le DOM est prêt
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
