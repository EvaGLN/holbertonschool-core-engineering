const form = document.getElementById("chat-form");
const message = document.getElementById("message");
const chathistory = document.getElementById("history");
const onlineList = document.getElementById("online-list");
const socket = new WebSocket("ws://127.0.0.1:8000/ws");
const username = "Guest-" + Math.floor(Math.random() * 10000);
const myName = document.getElementById("my-name");
myName.textContent = "Vous êtes " + username;
const inputWrap = document.getElementById("input-wrap");
const emojiButton = document.getElementById("emoji-button");
const emojiPanel = document.getElementById("emoji-panel");
const emojis = [
    "😀", "😂", "😍", "🥰", "😎", "🤔", "😢", "😡",
    "👍", "👎", "👏", "🙏", "💪", "🎉", "❤️", "🔥",
    "🦄", "🌈", "✨", "⭐", "🌸", "🍕", "☕", "🎶"
];
const sparkleColors = ["#ffd54a", "#ff8fcf", "#b79cff", "#7fe3ff", "#ffffff"];
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
let lastSparkle = 0;

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

emojis.forEach((emoji) => {
    const choice = document.createElement("button");
    choice.type = "button";
    choice.textContent = emoji;
    choice.addEventListener("click", () => {
        message.value += emoji;
        message.focus();
    });
    emojiPanel.appendChild(choice);
});

emojiButton.addEventListener("click", () => {
    emojiPanel.hidden = !emojiPanel.hidden;
});

document.addEventListener("click", (event) => {
    if (!inputWrap.contains(event.target)) {
        emojiPanel.hidden = true;
    }
});

document.addEventListener("mousemove", (event) => {
    if (reduceMotion) {
        return;
    }
    const now = Date.now();
    if (now - lastSparkle < 30) {
        return;
    }
    lastSparkle = now;

    const sparkle = document.createElement("span");
    sparkle.className = "sparkle";
    sparkle.textContent = "✦";
    sparkle.style.left = (event.clientX + 7) + "px";
    sparkle.style.top = (event.clientY + 12) + "px";
    sparkle.style.fontSize = (8 + Math.random() * 12) + "px";
    sparkle.style.color = sparkleColors[Math.floor(Math.random() * sparkleColors.length)];
    sparkle.style.setProperty("--dx", (Math.random() * 30 - 15) + "px");
    sparkle.style.setProperty("--dy", (Math.random() * 30 + 5) + "px");
    document.body.appendChild(sparkle);

    sparkle.addEventListener("animationend", () => {
        sparkle.remove();
    });
});