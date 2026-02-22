// ============================================================
// Module d'authentification — Vibe Lab
// JWT + API REST backend
// ============================================================

const Auth = (() => {
  const TOKEN_KEY = 'vl_token';
  let currentUser = null;
  let onAuthChange = null;

  function getToken() {
    return localStorage.getItem(TOKEN_KEY);
  }

  // Vérifier le token stocké au chargement
  async function init() {
    const token = getToken();
    if (!token) return;

    try {
      const res = await fetch(API_BASE_URL + '/api/auth/me', {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      if (res.ok) {
        currentUser = await res.json();
        if (onAuthChange) onAuthChange(true);
      } else {
        localStorage.removeItem(TOKEN_KEY);
      }
    } catch (e) {
      console.error('Auth check failed:', e);
    }
  }

  // Login via API
  async function login(email, password) {
    const res = await fetch(API_BASE_URL + '/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.error || 'Identifiants incorrects');
    }
    localStorage.setItem(TOKEN_KEY, data.token);
    currentUser = data.user;
    if (onAuthChange) onAuthChange(true);
    return currentUser;
  }

  // Logout (JWT stateless — on supprime le token local)
  function logout() {
    currentUser = null;
    localStorage.removeItem(TOKEN_KEY);
    if (onAuthChange) onAuthChange(false);
  }

  function isAuthenticated() {
    return currentUser !== null;
  }

  function getUser() {
    return currentUser;
  }

  function subscribe(callback) {
    onAuthChange = callback;
  }

  return { init, login, logout, isAuthenticated, getUser, getToken, subscribe };
})();
