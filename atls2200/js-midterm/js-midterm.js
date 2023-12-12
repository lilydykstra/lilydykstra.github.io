// there are 10 boxes in the middle of the screen
// they all start with a zero in them
// when clicked they go up a digit uptil 9 when it resets to 0

document.addEventListener('DOMContentLoaded', function() {
  const boxes = document.querySelectorAll('.box');

  boxes.forEach((box, index) => {
    box.addEventListener('click', function() {
      // Generate a random number between 0 and 9
      const randomNumber = Math.floor(Math.random() * 10);
      box.textContent = randomNumber;
    });
  });
});


// if clear button gets clicked
//   all number reset to 0

// if submit button is clicked
//   popup with "you submited you number"
