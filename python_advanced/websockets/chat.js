const form = document.getElementById("chat-form");
const message = document.getElementById("message");
const chathistory = document.getElementById("history");
const onlineList = document.getElementById("online-list");
const socket = new WebSocket("ws://127.0.0.1:8000/ws");
const username = "Guest-" + Math.floor(Math.random() * 10000);
const myName = document.getElementById("my-name");
myName.textContent = "Vous êtes " + username;

socket.onopen = () => {
    socket.send(JSON.stringify({ type: "join", username: username }));
};

form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (message.value.trim() === "") {
       return;
    }
    socket.send(JSON.stringify({
        type: "message",
        username: username,
        timestamp: new Date().toISOString(),
        text: message.value
    }));
    message.value = "";
});

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);

    if (data.type === "users") {
        onlineList.innerHTML = "";
        data.users.forEach((name) => {
            const item = document.createElement("li");
            item.textContent = name;
            onlineList.appendChild(item);
        });
        return;
    }
    if (data.type !== "message") {
        return;
    }

    const article = document.createElement("article");
    article.className = "message";

    if (data.username === username) {
        article.classList.add("mine");
    } else {
        article.classList.add("other");
    }

    const meta = document.createElement("p");
    meta.className = "meta";
    meta.textContent = data.username + " - " + new Date(data.timestamp).toLocaleString("fr-FR");

    const text = document.createElement("p");
    text.className = "text";
    text.textContent = data.text;

    article.appendChild(meta);
    article.appendChild(text);
    chathistory.appendChild(article);
    chathistory.scrollTop = chathistory.scrollHeight;
};