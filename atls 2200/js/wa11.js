const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Declaring the array of image filenames */
const imgArray = ['pig1.jpg','pig2.jpg','goat1.jpg','goat2.jpg','goat3.jpg'];

/* Declaring the alternative text for each image file */
var altDict = {
    'pig1.jpg': 'petting a pig',
    'pig2.jpg': 'face of a pig',
    'goat1.jpg': 'a brown goats face',
    'goat2.jpg': 'close up of the brown goats face',
    'goat3.jpg': 'side profile of a black goats face',
}
/* Looping through images */
for(img of imgArray){
    const newImage = document.createElement('img');
    // use setAttribute to connect src to images
    newImage.setAttribute('src', `../img/images/${img}`);

    // use setAttribute to connect alt text to the images
    newImage.setAttribute('alt', altDict[img]);

    thumbBar.appendChild(newImage);

    newImage.addEventListener('click', e => {
        displayedImage.src = e.target.src;
        displayedImage.alt = e.target.alt;
    })
}

/* Wiring up the Darken/Lighten button */
btn.addEventListener('click', () => {

    if (btn.getAttribute('class') === 'dark'){
        btn.setAttribute("class", 'light');
        btn.textContent = "Lighten";
        overlay.style.backgroundColor = "rgba(0,0,0,0.5)";
    }

    else{
        btn.setAttribute("class", 'dark');
        btn.textContent = "Darken";
        overlay.style.backgroundColor = "rgba(0,0,0,0)"; 
    }
})
// if else statement for on-click
// if button is dark change to light and change class and vice versa