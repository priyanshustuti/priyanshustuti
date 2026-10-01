/* Runs before first paint: marks the page as JS-enabled so reveal animations can hide/show.
   Kept as an external file (not inline) so the Content-Security-Policy can forbid inline scripts.
   Safety net: if main.js has not started within 4s (blocked/failed), drop the class so nothing stays hidden. */
document.documentElement.classList.add('js');
setTimeout(function () {
  if (!window.__usmsReady) document.documentElement.classList.remove('js');
}, 4000);
