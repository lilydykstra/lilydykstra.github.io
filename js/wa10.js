
// creating variables that correspond with elements in our html
const customName = document.getElementById('customname');
const randomize = document.querySelector('.randomize');
const story = document.querySelector('.story');

// function that picks a random number from the length of given array, then uses that index to pick an irem from the array
function randomValueFromArray(array){
  const random = Math.floor(Math.random()*array.length);
  return array[random];
}

// defiing variables 
var storyText = "It was 94 fahrenheit outside, so :insertx: went for a walk. When they got to :inserty:, they stared in horror for a few moments, then :insertz:. Bob saw the whole thing, but was not surprised — :insertx: weighs 300 pounds, and it was a hot day.";
var insertX = ["a guinea pig", "a lone wolf", "Satan"];
var insertY = ["the alley behind the hospital","Antarctica","CVS pharmacy"];
var insertZ = ["jumped off a clif", "called his mom crying", "watched Harry Potter for 10 hours straight"];


randomize.addEventListener('click', result);

function result() {
    var newStory = storyText;
    const xItem = randomValueFromArray(insertX);
    const yItem = randomValueFromArray(insertY);
    const zItem = randomValueFromArray(insertZ);

    newStory = newStory.replaceAll(':insertx:', xItem);
    newStory = newStory.replace(':inserty:', yItem);
    newStory = newStory.replace(':insertz:', zItem);

  if(customName.value !== '') {
    const name = customName.value;
    newStory = newStory.replace('Bob', name);

  }

  if(document.getElementById("uk").checked) {
    const weight = `${Math.round(300*0.0714286)} stones`;
    const temperature = `${Math.round((94-32)*(5/9))} centigrade`;
    newStory = newStory.replace('300 pounds', weight);
    newStory = newStory.replace('94 fahrenheit', temperature);
  }

  story.textContent = newStory;
  story.style.visibility = 'visible';
}