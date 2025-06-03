const hamMenu = document.querySelector('.fa-reorder');
const offScreenMenu = document.querySelector('.off-screen-menu');

hamMenu.addEventListener('click', (event) => {
    event.preventDefault();
    offScreenMenu.classList.toggle('active')
})

document.querySelectorAll('.fade-in').forEach(el => {
  el.classList.remove('visible');
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.2 });

document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));