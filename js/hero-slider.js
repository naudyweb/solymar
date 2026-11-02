/**
 * Hero slideshows: each .hero-slider cross-fades its photos every 5 seconds.
 * Secondary slides stay unrendered until after window.load so they never
 * compete with the LCP hero image during initial page load.
 */
(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  function initSliders() {
    document.querySelectorAll('.hero-slider').forEach(function (slider, index) {
      if (slider.offsetParent === null) return;
      var slides = slider.querySelectorAll('.hero-slide');
      if (slides.length < 2) return;

      slider.classList.add('is-ready');
      var current = 0;
      setTimeout(function () {
        setInterval(function () {
          slides[current].classList.remove('is-active');
          current = (current + 1) % slides.length;
          slides[current].classList.add('is-active');
        }, 5000);
      }, index * 2500);
    });
  }

  if (document.readyState === 'complete') {
    setTimeout(initSliders, 1500);
  } else {
    window.addEventListener('load', function () {
      setTimeout(initSliders, 1500);
    }, { once: true });
  }
})();
