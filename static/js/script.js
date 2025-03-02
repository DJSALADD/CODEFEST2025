console.log("Script loaded successfully!");

chat_box = document.getElementById('chat-box');
button = document.getElementById('button');
const darkModeButton = document.getElementById('dark-mode-button');
const mascotContainer = document.getElementById('mascot-container');

function onButtonClick() {
    const question = document.getElementById('input').value;

    fetch('/generate', {
        method: 'POST',  
        headers: {
          'Content-Type': 'application/json',  // Indicate we are sending JSON
        },
        body: JSON.stringify({ topic: question }),  // Convert data to JSON and send it
      })
      .then(response => response.json())  // Parse JSON response from Flask
.then(data => {
    const response = data['topic']
    const receivedMessage = document.createElement('div');
    receivedMessage.innerHTML = `<p>${question}</p>`;
    receivedMessage.classList.add('message', 'sent');
    chat_box.appendChild(receivedMessage);

    const sentMessage = document.createElement('div');
    sentMessage.innerHTML = `<p>${response}</p>`;
    sentMessage.classList.add('message', 'received');
    chat_box.appendChild(sentMessage);

    const mascot = document.getElementById('mascot')
    
    const images = ['confused.png', 'curious.png', 'happy.png', 'neutral.png', 'wave.png', 'wave2.png'];
    const randomIndex = Math.floor(Math.random() * images.length);
    const randomImage = images[randomIndex];
 
    mascot.src = `../static/images/scrubby/${randomImage}`;


    document.getElementById('input').value = '';
   
    bounceAnimation(mascotContainer);
})
      .catch(error => {
        console.error('Error:', error);  // Handle any errors
      });
    }
    
function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-mode');
}

function spinAnimation() {
    mascot.classList.add('spin-animation');
    setTimeout(() => {
        mascot.classList.remove('spin-animation');
    }, 600);
}

function bounceAnimation(element) {
    mascot.classList.add('bounce-animation');
    setTimeout(() => {
        mascot.classList.remove('bounce-animation');
    }, 400);
}

button.addEventListener('click', onButtonClick);
darkModeButton.addEventListener('click', toggleDarkMode);

mascotContainer.addEventListener('click', spinAnimation);

// Get the modal
var quizModal = document.getElementById("myModal");

// Get the button that opens the modal
var quizButton = document.getElementById("quiz-button");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
quizButton.onclick = function() {
  quizModal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  quizModal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == quizModal) {
    quizModal.style.display = "none";
  }
}
generate_question = document.getElementById("questionBtn")
generate_question.addEventListener('click', sendData);
   function sendData() {
      const input = document.getElementById('topic').value;  // Get the input value
      fetch('/calculate', {
        method: 'POST',  
        headers: {
          'Content-Type': 'application/json',  // Indicate we are sending JSON
        },
        body: JSON.stringify({ topic: input }),  // Convert data to JSON and send it
      })
      .then(response => response.json())  // Parse JSON response from Flask

.then(data => {
    const buttons = document.getElementsByClassName('answer-button');  // Get all buttons
    const choices = ['A', 'B', 'C', 'D'];  // Define choice labels
    let j = 0;
    const quiz_question = document.getElementById('question');  // Get the question element
    quiz_question.textContent = data[0]['question'];  // Set the question text

    // Ensure you have 4 buttons and data.choices contains A, B, C, D keys
    for (let i = 0; i < buttons.length; i++) {
        const choiceKey = choices[j];  // Get the current choice key (e.g., 'A', 'B', etc.)
        const choice = data[0]['choices'][choiceKey];  // Get the choice text for the button
        
        // Set the button text to the choice
        buttons[i].textContent = choice;

        // Attach an event listener to each button
        buttons[i].onclick = (function(choiceKey) {
            return function() {
                if (choiceKey === data[0]['correct_answer']) {
                    alert('Correct!');
                } else {
                    alert('Incorrect!');
                }
            };
        })(choiceKey); // Immediately invoke the function with the current choiceKey

        // Move to the next choice for the next button
        j++;
    }
})
      .catch(error => {
        console.error('Error:', error);  // Handle any errors
      });
    }