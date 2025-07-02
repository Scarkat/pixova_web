let currentIndex = 0;
const images = document.querySelectorAll('#carouselImages img');
const totalImages = images.length;
document.getElementById('carouselImages').style.width = `${1200 * totalImages}px`;

function showSlide(index) {
    const carouselImages = document.getElementById('carouselImages');
    carouselImages.style.transform = `translateX(-${index * 1200}px)`;

    images.forEach(img => img.classList.remove('active'));
    images[index].classList.add('active');
}

showSlide(currentIndex);

function nextSlide() {
    currentIndex = (currentIndex + 1) % totalImages;
    showSlide(currentIndex);
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + totalImages) % totalImages;
    showSlide(currentIndex);
}