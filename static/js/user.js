// static/js/user.js
document.addEventListener("DOMContentLoaded", function () {
  const root = document.documentElement;
  const themeToggle = document.getElementById('tzh-theme-toggle');
  const themeIcon = document.getElementById('tzh-theme-icon');

  // --- restore theme
  const savedTheme = localStorage.getItem('tzhTheme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  setThemeIcon(savedTheme);

  // --- restore accent
  const savedAccent = localStorage.getItem('tzhAccent');
  if (savedAccent) {
    root.style.setProperty('--tzh-primary', savedAccent);
  }

  // --- add form-control to inputs inside .tzh-form (helps without changing forms)
  document.querySelectorAll('.tzh-form').forEach(form => {
    form.querySelectorAll('input, select, textarea').forEach(el => {
      // skip buttons
      if (el.tagName.toLowerCase() === 'input' && (el.type === 'submit' || el.type === 'button' || el.type === 'hidden')) return;
      if (!el.classList.contains('form-control')) el.classList.add('form-control','mb-2');
    });
  });

  // theme toggle handler
  function setThemeIcon(theme) {
    if (!themeIcon) return;
    if (theme === 'dark') {
      themeIcon.classList.remove('fa-moon');
      themeIcon.classList.add('fa-sun');
    } else {
      themeIcon.classList.remove('fa-sun');
      themeIcon.classList.add('fa-moon');
    }
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      const current = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('tzhTheme', next);
      setThemeIcon(next);
    });
  }

  // Accent color picker
  document.querySelectorAll('.tzh-accent-option').forEach(btn => {
    btn.addEventListener('click', function (e) {
      const color = this.getAttribute('data-accent');
      if (color) {
        root.style.setProperty('--tzh-primary', color);
        localStorage.setItem('tzhAccent', color);
      }
      // close dropdown (bootstrap)
      const dropdown = bootstrap.Dropdown.getInstance(this.closest('.dropdown'));
      if (dropdown) dropdown.hide();
    });
  });

  // bootstrap tooltips if present
  if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
    document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
      new bootstrap.Tooltip(el);
    });
  }
});

// End of document ready