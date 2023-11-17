const newBtn = document.querySelector('#js-new-photo').addEventListener('click',getDog);
const dogPhoto = document.querySelector('#js-dog-photo');


const endpoint = 'https://dog.ceo/api/breeds/image/random';

async function getDog() {
    try{
        const response = await fetch(endpoint);
        if (!response.ok){
            throw Error(response.statusText);
        }
        const json = await response.json();
            displayDog(json['message']);

    }
    catch(err){
        console.log(err);
        alert('Failed to fetch new dog')
    }
}

function displayDog(imageUrl) {
    dogPhoto.src = imageUrl;
}

getDog();

