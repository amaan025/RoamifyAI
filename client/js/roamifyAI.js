// chat.js
document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chatMessages');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');

    // Auto-resize textarea
    userInput.addEventListener('input', () => {
        userInput.style.height = 'auto';
        userInput.style.height = `${userInput.scrollHeight}px`;
    });

    // Message handling
    function handleSendMessage() {
        const message = userInput.value.trim();
        if (message) {
            addMessage(message, 'user');
            simulateBotResponse(message);
            userInput.value = '';
            resetInputHeight();
        }
    }

    // Add new message
    function addMessage(content, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        messageDiv.innerHTML = `<p>${content}</p>`;
        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }

    // Simulate bot response
    function simulateBotResponse(userMessage) {
        const loadingMessage = addMessage('Typing...', 'bot');
        
        setTimeout(() => {
            chatMessages.removeChild(loadingMessage);
            const response = generateMockResponse(userMessage);
            addMessage(response, 'bot');
        }, 1500);
    }

    // Generate mock response
    function generateMockResponse(message) {
        const responses = {
            'hello': 'Hello! How can I assist with your travel plans?',
            'default': `I received: "${message}". This is a mock response. Implement API for real answers.`
        };
        return responses[message.toLowerCase()] || responses['default'];
    }

    // Utility functions
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function resetInputHeight() {
        userInput.style.height = 'auto';
    }

    // Event listeners
    sendButton.addEventListener('click', handleSendMessage);
    
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    });
});