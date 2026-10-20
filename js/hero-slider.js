/**
 * Hero slideshow: cross-fades the hero photos every 5 seconds.
 * The fade/blur/zoom effect lives in src/input.css (.hero-slide).
 */
(function () {
  var slides = document.querySelectorAll('#hero-slider .hero-slide');
  if (slides.length < 2 || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var current = 0;
  setInterval(function () {
    slides[current].classList.remove('is-active');
    current = (current + 1) % slides.length;
    slides[current].classList.add('is-active');
  }, 5000);
})();
