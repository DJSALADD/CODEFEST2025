console.log("Script loaded successfully!");

chat_box = document.getElementById('chat-box');
button = document.getElementById('button');

function onButtonClick() {
    const question = document.getElementById('input').value;
    const response = "Testing a response";
    
    const receivedMessage = document.createElement('div');
    receivedMessage.innerHTML = `<p>${question}</p>`;
    receivedMessage.classList.add('message', 'received');
    chat_box.appendChild(receivedMessage);

    const sentMessage = document.createElement('div');
    sentMessage.innerHTML = `<p>${response}</p>`;
    sentMessage.classList.add('message', 'sent');
    chat_box.appendChild(sentMessage);
}

button.addEventListener('click', onButtonClick);
