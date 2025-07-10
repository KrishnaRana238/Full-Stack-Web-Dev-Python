// Show/Hide Password Toggle
document.addEventListener('DOMContentLoaded', function () {
  const togglePassword = document.getElementById('togglePassword');
  const passwordInput = document.getElementById('password');

  if (togglePassword && passwordInput) {
    togglePassword.addEventListener('click', function () {
      const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
      passwordInput.setAttribute('type', type);
      togglePassword.textContent = type === 'password' ? '👁️' : '🙈';
    });
  }

  // Form Validation
  const form = document.getElementById('stripe-login');
  if (form) {
    form.addEventListener('submit', function (e) {
      const email = document.querySelector('input[name="email"]').value;
      const password = document.querySelector('input[name="password"]').value;
      const formContainer = document.querySelector('.formbg');

      if (!email || !password) {
        if (formContainer) {
          formContainer.classList.add('shake');
          setTimeout(() => formContainer.classList.remove('shake'), 300);
        }
        alert("Please fill out both email and password fields.");
        e.preventDefault();
        return;
      }

      const emailRegex = /\S+@\S+\.\S+/;
      if (!emailRegex.test(email)) {
        if (formContainer) {
          formContainer.classList.add('shake');
          setTimeout(() => formContainer.classList.remove('shake'), 300);
        }
        alert("Please enter a valid email address.");
        e.preventDefault();
      }
    });
  }

  // Typing Animation in Heading
  const heading = document.getElementById("typingHeading");
  const headingText = "Welcome to Stackfindover";
  if (heading) {
    let i = 0;
    function typeEffect() {
      if (i < headingText.length) {
        heading.innerHTML += headingText.charAt(i);
        i++;
        setTimeout(typeEffect, 100);
      }
    }
    typeEffect();
  }

  // Dark/Light Mode Toggle
  const themeToggleBtn = document.getElementById('themeToggle');
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', function () {
      document.body.classList.toggle("dark-mode");
    });
  }
});
