document.addEventListener("DOMContentLoaded", function() {
    var images = document.querySelectorAll('img');

    var colors = ['#f8d3fe', '#98e6cd', '#adc8fe', '#fee2a1', '#cebefe']; // Array of 5 different color choices

    images.forEach(function(image) {
        var randomColorIndex = Math.floor(Math.random() * colors.length); // Generate a random index to pick a color
        var randomColor = colors[randomColorIndex]; // Get the random color from the array
        image.style.border = '5px solid ' + randomColor; // Apply the random color as the border
    });
});