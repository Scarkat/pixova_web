const hamMenu = document.querySelector('.fa-reorder');
const offScreenMenu = document.querySelector('.off-screen-menu');

hamMenu.addEventListener('click', (event) => {
    event.preventDefault();
    offScreenMenu.classList.toggle('active')
})