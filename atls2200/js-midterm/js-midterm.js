// there are 10 boxes in the middle of the screen
// they all start with a zero in them
// when clicked they go up a digit uptil 9 when it resets to 0

document.addEventListener('DOMContentLoaded', function () {
  const boxes = document.querySelectorAll('.box');

// Toggle the moving class on box click
boxes.forEach(box => {
  box.addEventListener('click', function () {
    // Remove the 'moving' class from all boxes
    boxes.forEach(otherBox => {
      otherBox.classList.remove('moving');
    });

    // Add the 'moving' class to the clicked box
    box.classList.toggle('moving');

    // Adjust the animation duration for each box
    const duration = Math.random() * 2 + 0.3; 
    box.style.animationDuration = `${duration}s`;
  });
});

  // resets all numbers to 0
  const clearNumbers = () => {
    boxes.forEach(box => {
      box.textContent = '0';
      box.style.transform = 'none';
      box.classList.remove('moving'); // Stop the animation
    });
  };

  // Function to show popup
  const submitScreen = () => {
    alert('Thanks for submitting your number! Please never come back :)');
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