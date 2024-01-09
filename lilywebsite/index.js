// Add this to your existing JavaScript file or create a new one
const carouselContainer = document.querySelector('.carousel-container');

// Set up event listeners for smooth scrolling
carouselContainer.addEventListener('wheel', (e) => {
    e.preventDefault();
    carouselContainer.scrollLeft += e.deltaY;
});