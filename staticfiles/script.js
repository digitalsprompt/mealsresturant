
const hamburger = document.getElementById('hamburger-menu');
const navLinks = document.getElementById('nav-links');
hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('nav-active');
        hamburger.classList.toggle('toggle');
});