/*Add your JavaScript here*/
var folkloreScore = 0;
var evermoreScore = 0;
var questionCount = 0;

// storing html elements using the dom for accessing buttons later 
const q1a1 = document.getElementById("q1a1");
const q1a2 = document.getElementById("q1a2");

const q2a1 = document.getElementById("q2a1");
const q2a2 = document.getElementById("q2a2");

const q3a1 = document.getElementById("q3a1");
const q3a2 = document.getElementById("q3a2");

const result = document.getElementById("result");
const restart = document.getElementById("restart");

// selecting all answer buttons (all buttons excluding restart button)
const buttons = document.querySelectorAll("div button");
// selecting question pair buttons using qselector and css selector [attribute^=""] which selects elements if the att. value starts with the string
const q1Buttons = document.querySelectorAll(`[id^="q1"]`);
const q2Buttons = document.querySelectorAll(`[id^="q2"]`);
const q3Buttons = document.querySelectorAll(`[id^="q3"]`);

// event listeners
q1a1.addEventListener("click", evermore);
q1a2.addEventListener("click", folklore);

q2a1.addEventListener("click", evermore);
q2a2.addEventListener("click", folklore);

q3a1.addEventListener("click", folklore);
q3a2.addEventListener("click", evermore);

restart.addEventListener("click", resetGame);
// functions
function evermore() {
  evermoreScore++;
  questionCount++;

  if (questionCount === 3) {
    updateResult()
}
}

function folklore() {
  folkloreScore++;
  questionCount++;

  if (questionCount === 3) {
    updateResult()
}
}

function updateResult() {
  if (folkloreScore >= 2) {
    result.innerHTML = "You are  <i>folklore!</i>";
  } else if (evermoreScore >= 2) {
    result.innerHTML = "You are <i>evermore!</i>";
  }
}

function resetGame() {
  folkloreScore = 0;
  evermoreScore = 0;
  questionCount = 0;
  result.innerHTML = "Your result is..."
  buttons.forEach(button => {
    button.disabled = false;
  })
  // console.log(folkloreScore, evermoreScore, questionCount)
}

// for each of the first pair of buttons, add an event listener 
q1Buttons.forEach(button => {
  button.addEventListener("click", () => {
    // for each of the buttons, disable the button
    q1Buttons.forEach(button => {
      button.disabled = true;
    })
  })
})

q2Buttons.forEach(button => {
  button.addEventListener("click", () => {
    q2Buttons.forEach(button => {
      button.disabled = true;
    })
  })
})

q3Buttons.forEach(button => {
  button.addEventListener("click", () => {
    q3Buttons.forEach(button => {
      button.disabled = true;
    })
  })
})
