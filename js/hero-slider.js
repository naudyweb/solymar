/**
 * Hero slideshows: each .hero-slider cross-fades its photos every 5 seconds.
 * When a page has several (the homepage pair), each one starts a bit later so
 * they don't change at the same time. The fade/blur/zoom effect lives in
 * src/input.css (.hero-slide).
 */
(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  document.querySelectorAll('.hero-slider').forEach(function (slider, index) {
    var slides = slider.querySelectorAll('.hero-slide');
    if (slides.length < 2) return;

    var current = 0;
    setTimeout(function () {
      setInterval(function () {
        slides[current].classList.remove('is-active');
        current = (current + 1) % slides.length;
        slides[current].classList.add('is-active');
      }, 5000);
    }, index * 2500);
  });
})();
