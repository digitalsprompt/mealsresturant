
const hamburger = document.getElementById('hamburger-menu');
const navLinks = document.getElementById('nav-links');

if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('nav-active');
    hamburger.classList.toggle('toggle');
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const foodPage = document.querySelector('.food-page');
  const modeSwitch = document.querySelector('.mode-switch');
  const foodCards = document.querySelectorAll('.food-card');

  if (foodPage && modeSwitch) {
    modeSwitch.addEventListener('click', () => {
      foodPage.classList.toggle('theme-light');
      modeSwitch.classList.toggle('active');
    });
  }

  if (foodCards.length && window.VanillaTilt) {
    VanillaTilt.init(foodCards, {
      max: 15,
      speed: 300,
      easing: 'cubic-bezier(.03,.98,.52,.99)',
      scale: 1.03,
      glare: true,
      'max-glare': 0.14,
    });
  }
});
