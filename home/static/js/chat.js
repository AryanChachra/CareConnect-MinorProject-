function toggleChat() {
    const chatPopup = document.getElementById("chatPopup");
    chatPopup.style.display = chatPopup.style.display === "block" ? "none" : "block";
  }
  
  function sendMessage() {
    const messageInput = document.getElementById("messageInput");
    const chatBody = document.getElementById("chatBody");
  
    const message = messageInput.value.trim();
    if (message !== "") {
      const messageElement = document.createElement("div");
      messageElement.classList.add("message");
      messageElement.textContent = message;
      chatBody.appendChild(messageElement);
  
      messageInput.value = "";
    }
  }
  