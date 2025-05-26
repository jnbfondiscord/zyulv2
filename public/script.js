// script.js
window.addEventListener('DOMContentLoaded', () => {
  const msg = document.getElementById('message');
  // Overwrite the default for real browsers
  msg.innerHTML = `
    <h1>Hello, Web Browser!</h1>
    <p>You are viewing this via a browser with JS enabled.</p>
  `;
});
