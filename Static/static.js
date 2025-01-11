document.getElementById("chatForm").onsubmit = async function (event) {
    event.preventDefault();
    const prompt = document.getElementById("userPrompt").value;
    const chatBox = document.getElementById("chatBox");

    // Display user message
    const userMessage = document.createElement("div");
    userMessage.textContent = "You: " + prompt;
    chatBox.appendChild(userMessage);

    // Send the data to the Django backend
    const response = await fetch('/generate/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ prompt: prompt })
    });

    const data = await response.json();

    // Display the AI's response
    const aiMessage = document.createElement("div");
    aiMessage.textContent = "AI: " + data.response;
    chatBox.appendChild(aiMessage);

    document.getElementById("userPrompt").value = ""; // Clear input
};

// CSRF Token handler for Django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        cookies.forEach(cookie => {
            if (cookie.trim().startsWith(name + '=')) {
                cookieValue = cookie.split('=')[1];
            }
        });
    }
    return cookieValue;
}
