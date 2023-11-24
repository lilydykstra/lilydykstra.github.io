document.addEventListener('DOMContentLoaded', function() {
    const newBtn = document.querySelector('#js-new-photo').addEventListener('click',getDog);
    const dogPhoto = document.querySelector('#js-dog-photo');
    const loadingBar = document.querySelector('#loading-bar');

    const endpoint = 'https://dog.ceo/api/breeds/image/random';

    async function getDog() {
        try{
            // Show loading bar and text
            loadingBar.style.width = '100%';

            const response = await fetch(endpoint);
            if (!response.ok){
                throw Error(response.statusText);
            }
            const json = await response.json();

            await delay(1000);

            displayDog(json['message']);

        }
        catch(err){
            console.log(err);
            alert('Failed to fetch new dog')
        }
        finally {
            // Hide loading bar and text
            loadingBar.style.width = '0';
        }
    }

    function displayDog(imageUrl) {
        dogPhoto.src = imageUrl;
    }
    function delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    getDog();

});