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