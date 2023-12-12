// there are 10 boxes in the middle of the screen
// they all start with a zero in them
// when clicked they go up a digit uptil 9 when it resets to 0
document.addEventListener('DOMContentLoaded', function () {
  const boxes = document.querySelectorAll('.box');
  let animationInterval;

  // resets all numbers to 0
  const clearNumbers = () => {
    boxes.forEach(box => {
      box.textContent = '0';
      box.style.transform = 'none'; // Reset the transform property
    });
  };

  // Function to show popup
  const submitScreen = () => {
    alert('Thanks for submitting you number! Please never come back :)');
  };

  // use "click" event listener for clear button
  document.getElementById('clearButton').addEventListener('click', clearNumbers);

  // use "click" event listener for submit button
  document.getElementById('submitButton').addEventListener('click', submitScreen);

  // use "click" event listener for each box to change value to random number
  boxes.forEach((box, index) => {
    let value = Math.floor(Math.random() * 10);
  
    box.addEventListener('click', function () {
      const randomNumber = Math.floor(Math.random() * 10);
      box.textContent = randomNumber;

    });
  });
});



