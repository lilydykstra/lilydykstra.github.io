// there are 10 boxes in the middle of the screen
// they all start with a zero in them
// when clicked they go up a digit uptil 9 when it resets to 0

document.addEventListener('DOMContentLoaded', function() {
    const boxes = document.querySelectorAll('.box');

    boxes.forEach((box, index) => {
      let value = 0;

      box.addEventListener('click', function() {
        value = (value + 1) % 10;
        box.textContent = value;
      });
    });
  });