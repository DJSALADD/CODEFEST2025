console.log("Script loaded successfully!");

chat_box = document.getElementById('chat-box');
button = document.getElementById('button');

function onButtonClick() {
    const question = document.getElementById('input').value;
    const response = "Testing a response";
    
    const sentMessage = document.createElement('div');
    sentMessage.innerHTML = `<p>${response}</p>`;
    sentMessage.classList.add('message', 'sent');
    chat_box.appendChild(sentMessage);

    const receivedMessage = document.createElement('div');
    receivedMessage.innerHTML = `<p>${question}</p>`;
    receivedMessage.classList.add('message', 'received');
    chat_box.appendChild(receivedMessage);
}

button.addEventListener('click', onButtonClick);

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
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
    const buttons = document.getElementsByClassName('button-class'); // Assuming 'button-class' is the class name of your buttons
    const choices = ['A', 'B', 'C', 'D'];
    let j = 0;

    // Ensure you have 4 buttons and data.choices contains A, B, C, D keys
    for (let i = 0; i < buttons.length; i++) {
        // Set the button's label (text) to the corresponding choice
        buttons[i].textContent = data['choices'][choices[j]];

        // Attach an event listener to each button
        buttons[i].onclick = function() {
            if (choices[j] === data['correct_answer']) {
                alert('Correct!');
            } else {
                alert('Incorrect!');
            }
        };

        // Move to the next choice for the next button
        j++;
    }
})

      .catch(error => {
        console.error('Error:', error);  // Handle any errors
      });
    }