<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Real-time communication with WebSockets

## Table of Contents :

  - [0. Server](#subparagraph0)
  - [1. Client](#subparagraph1)
  - [2. Validation](#subparagraph2)
  - [3. Unicast](#subparagraph3)
  - [4. Broadcast](#subparagraph4)
  - [5. ASGI Integration](#subparagraph5)
  - [6. Browser Client](#subparagraph6)
  - [7. Quiz](#subparagraph7)
## Introduction

Traditional HTTP communication follows a **request–response model**, where the client initiates every interaction and the server responds. This model is not suitable for applications that require continuous updates, such as chat systems, live dashboards, or collaborative tools.

WebSockets address this limitation by establishing a **persistent connection**. Once the connection is open, both the client and the server can send messages at any time without reopening the connection.

In this project, you will work with **WebSockets**, a communication protocol that enables **real-time, bidirectional data exchange** between a client and a server.

---

## Context

You will progressively implement:

* A WebSocket server
* Clients that communicate with the server
* Message exchange between multiple participants
* Basic message routing and validation
* Integration with a web-based client

Each step builds on previous behavior.

---

## Learning Objectives

By the end of this project, you should be able to:

* Implement a WebSocket server using asynchronous programming
* Handle multiple concurrent client connections
* Send and receive messages in real time
* Implement different message exchange patterns
* Enforce a defined message format when required

---

## Resources

**Intro Videos (must watch before starting):**
* [Be a Better Dev - API REST (HTTP) vs. Websockets](/rltoken/7UzYJKWSFygA4jCTY1TETQ) (7 mins)
* [FreeCodeCamp - A Beginner's Guide to WebSockets](/rltoken/yLpcjkkh1St0L37NEn17YA) (30 mins)

**Documentation:**
* [websockets documentation](/rltoken/7JyhjLRdTZGM7XaWDW1uTQ)
* [Python asyncio documentation](/rltoken/2Yw6_RN4gzEOTjK_flLgxw)
* [MDN WebSockets API](/rltoken/BqkC13KHwBQLUYXMNFwmBg)

---

## General Requirements

* The first line of all Python files must be:

```python
#!/usr/bin/env python3
```
This ensures the script uses the Python interpreter available in the system environment rather than relying on a fixed system path.

* All files must end with a new line.
* Code must follow **PEP8 style guidelines**.

* You must use:

    * the `websockets` library
    * asynchronous programming (`async` / `await`)

* Your implementation must:

    * behave exactly as specified
    * handle continuous communication correctly
    * support multiple concurrent connections when required

* Unless explicitly stated, do not:

    * introduce additional frameworks
    * modify the communication protocol
    * add features beyond the requirements

---

## Important Notes

* Communication is persistent: connections remain open and must be handled accordingly
* Multiple clients may interact at the same time
* Message formats must be respected exactly when specified

> When binding the server to the network interface, force an **IPv4 address like `127.0.0.1` instead of localhost or `0.0.0.0` for all intefaces**. 
> This prevents the Checker OS to use IPv6 that will raise an error.

---

## Final Remarks

This project focuses on building a working real-time communication system.

Accuracy in behavior is essential. Small deviations from the expected behavior may result in failure during evaluation.


## Task
### 0. Server <a name='subparagraph0'></a>

## Introduction

In this step, you will build your first WebSocket server.

Unlike traditional HTTP servers, a WebSocket server maintains a persistent connection with each client. This allows both the client and the server to send messages at any time, enabling real-time communication.

Your goal is to implement a minimal server that accepts connections and echoes back any message it receives.

This behavior establishes the basic communication loop that will be extended in later steps.

### Instructions

Implement a WebSocket server that:

* Listens on `localhost` at port `8765`
* Accepts multiple client connections
* Receives text messages from a client
* Sends back the exact same message to the sender (echo behavior)

### Expected Behavior

When a client sends:

```undefined
Hello
```

The server must respond:

```undefined
Hello
```

The connection must remain open after the response, allowing continuous communication.

### What you must build

An async `connection_handler(websocket)` that, for **each** text message received on that connection, **sends back** one outgoing text message whose value is **exactly** the same message string (no extra newline unless the client sent one).

### Constraints

* Use the `websockets` library
* Use asynchronous programming (`async` / `await`)
* The server must handle messages continuously (it must not stop after one message)
* Messages must be processed as they arrive (no batching or delays)
* Only text messages need to be supported
* The server must start when executing:

```undefined
python3 echo_server.py
```

### Suggested Approach

* Define an asynchronous handler function that receives a connection
* Use a loop to process incoming messages
* Send responses using the same connection
* Start the server using the appropriate `websockets` utility
* Do not modify messages in this step (output must match input exactly)
* Error handling is not required at this stage

### How to Test Manually

`websockets` provides an interactive client:

```sh
spam@camelot$ websockets ws://localhost:8765/
Connected to ws://localhost:8765/.
> Hello world!
< Hello world!
Connection closed: 1000 (OK).
```

Or you can test your server using:

* A Python client using `websockets.connect`
* A browser-based WebSocket client
* Tools such as `websocat`, Postman or Insomnia

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_advanced/websockets`
* File: `echo_server.py`

---

### 1. Client <a name='subparagraph1'></a>

## Introduction

In this step, you will implement a WebSocket client.

A WebSocket client connects to a WebSocket server and sends messages through an open connection. Unlike a traditional HTTP request, the connection does not need to be recreated for every message.

Your goal is to create a minimal client that connects to the echo server, sends one message, receives the response, and prints it.

This confirms that your server and client can communicate using the same WebSocket connection.

### Instructions

Implement a WebSocket client that:

* Connects to `ws://localhost:8765`
* Sends the message:

```text
Hello WebSocket
```

* Waits for the server response
* Prints the response exactly as received
* Closes the connection after receiving the response

### Expected Behavior

If the echo server is running and the client sends:

```text
Hello WebSocket
```

The client must print:

```text
Hello WebSocket
```

### What you must build

* `async def connect_and_send(uri: str, text: str) -> str` , open, `send` once, `recv` once, return a `str`, close cleanly.
* A small `main` that calls `connect_and_send` with the "demo" string; **stdout** for the platform’s subprocess run must be **exactly** `demo` with **no** final newline (use `print(response, end="")`.
* `connect_and_send` is also used when your module is imported: against a test server that replies with ` the same string you send .

### Constraints

* Use the `websockets` library
* Use asynchronous programming (`async` / `await`)
* The client must send only one message
* The client must print only the server response
* The client must not start the server
* The client must run when executing:

```text
python3 ws_client.py
```

### Suggested Approach

* Create an asynchronous function for the client logic
* Connect to the server using the WebSocket URL
* Send the required message
* Wait for one response
* Print the response
* Let the connection close cleanly after the exchange

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_advanced/websockets`
* File: `ws_client.py`

---

### 2. Validation <a name='subparagraph2'></a>

### Introduction

In this step, you will add basic message validation to your server.

Until now, messages were assumed to be valid. In real systems, this is not a safe assumption. Clients may send empty or invalid data, and the server must handle these cases correctly.

Your goal is to validate incoming messages before processing them.

### Instructions

Update your server so that it:

* Receives text messages from connected clients
* Validates each message before responding
* Rejects empty messages

A message is considered invalid when, after removing leading and trailing whitespace, it is empty.

### Expected Behavior

If a client sends:

```text
Hello
```

The server must respond:

```text
OK:Hello
```

If a client sends an empty message or only spaces the server must respond:

```text
ERR:EMPTY
```

### What you must build

* If the incoming `str` has `len(s.strip()) == 0`, send exactly `ERR:EMPTY`.
* Otherwise send `OK:` + the **original** string (e.g. `f"OK:{s}"` with the same `s` you read from the wire), so characters before/after a non-empty `strip()` are not lost in the `OK:` line.
* Include `ConnectionClosed` from `websockets.exceptions` in an `import` and/or `except` block in the file.

### Constraints

* Use the `websockets` library
* Use asynchronous programming (`async` / `await`)
* Validate each message before responding
* Do not close the connection after an invalid message
* The server must continue handling messages after validation

### Suggested Approach

* Receive messages continuously from each client
* Trim whitespace before validation
* Check if the message is empty after trimming
* Send the appropriate response
* Keep the connection open

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_advanced/websockets`
* File: `validation_server.py`

---

### 3. Unicast <a name='subparagraph3'></a>

### Introduction

In this step, you will manage multiple connected clients and control how messages are delivered.

Even when multiple clients are connected, messages must be sent only to the client that initiated the communication. This is known as **unicast** communication.

Your goal is to ensure that each message is handled independently for each client.

### Instructions

Implement a server that:

* Accepts multiple client connections
* Keeps track of connected clients
* Receives messages from any client
* Sends the response only to the sender
* Prefixes responses with:

```text
U:
```

### Expected Behavior

If a client sends:

```text
Hello
```

That client must receive:

```text
U:Hello
```

Other clients must not receive the message.

### What you must build

* A global `connected_clients` set.
* On each new connection, **add** the socket; on exit, **remove** it.
* For each incoming message `m`, send **only to that connection** the text `U:` + `m` (e.g. `a` → `U:a`).

### Constraints

* Maintain a collection of active connections
* Add clients on connect and remove on disconnect
* Do not broadcast messages in this step

### Suggested Approach

* Store active connections in a shared structure
* Process messages per connection
* Send responses only through the originating connection

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_advanced/websockets`
* File: `unicast_server.py`

---

### 4. Broadcast <a name='subparagraph4'></a>

### Introduction

In this step, you will implement broadcast communication.

Instead of responding only to the sender, the server must distribute messages to all connected clients. This pattern is commonly used in real-time applications such as chat systems.

### Instructions

Implement a server that:

* Accepts multiple client connections
* Keeps track of connected clients
* Receives messages from any client
* Sends each message to all connected clients
* Prefixes messages with:

```text
B:
```

### Expected Behavior

If a client sends:

```text
Hello
```

All connected clients must receive:

```text
B:Hello
```

### Constraints

* Maintain a collection of active connections
* Add clients on connect and remove on disconnect
* Do not send messages to disconnected clients

### Suggested Approach

* Store active connections
* Iterate over connections when broadcasting
* Send the message to each active client

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_advanced/websockets`
* File: `broadcast_server.py`

---

### 5. ASGI Integration <a name='subparagraph5'></a>

## Introduction

In this step, you will integrate WebSocket communication into a web-facing Python application.

Until now, your servers have been started using simple helper functions designed for development and experimentation. These approaches are useful for learning, but they are not suitable for real-world applications.

In production environments, applications must:

* Handle different types of traffic (HTTP and WebSocket)
* Support multiple simultaneous users
* Be scalable and maintainable
* Run behind a dedicated application server

To achieve this, Python web applications use standardized interfaces such as **WSGI** and **ASGI**.

* **WSGI (Web Server Gateway Interface)** is designed for traditional synchronous HTTP applications.
* **ASGI (Asynchronous Server Gateway Interface)** extends this model to support asynchronous communication and long-lived connections such as WebSockets.

ASGI is required in this project because:

* WebSockets rely on persistent connections
* Multiple clients must be handled concurrently
* The application must support both HTTP (for serving pages) and WebSocket communication

While it is possible to implement an ASGI application directly, it would require handling low-level details such as routing, connection management, and protocol handling.

Frameworks like **Starlette** provide a higher-level abstraction that simplifies this process. They allow you to:

* Define HTTP and WebSocket routes clearly
* Focus on application logic instead of protocol details
* Reduce boilerplate code
* Follow patterns commonly used in real-world applications

Using a framework in this step is intentional: it reflects how production systems are built, where developers rely on well-tested tools to manage infrastructure concerns while focusing on business logic.

In this step, you will build an ASGI application using **Starlette**, and run it using **Uvicorn**, a production-ready ASGI server.

This setup reflects how real-world applications are structured and deployed.

## Resources

* https://asgi.readthedocs.io/en/latest/introduction.html
* https://www.starlette.io/
* https://www.starlette.io/websockets/
* https://www.uvicorn.org/

## Instructions

Implement an application that:

* Serves an HTML page at:

```text
http://localhost:8000
```

* Exposes a WebSocket endpoint at:

```text
ws://localhost:8000/ws
```

* Accepts WebSocket connections on `/ws`
* Receives text messages from connected clients
* Sends back the exact same message to the sender (echo behavior)

## Expected Behavior

When accessing:

```text
http://localhost:8000
```

A web page must be returned with exactly the following content: `<h1>WebSocket Echo</h1>`

When connecting to:

```text
ws://localhost:8000/ws
```

and sending:

```text
Hello
```

The server must respond:

```text
Hello
```

## Constraints

* Use an ASGI-compatible application
* Use **Starlette** for routing
* The application must handle both HTTP and WebSocket connections
* The WebSocket endpoint must be `/ws`
* The WebSocket behavior must follow echo logic
* The application must listen on port `8000`

## Running the Application

You must run the application using **Uvicorn**:

```bash
uvicorn asgi_server:app --host 0.0.0.0 --port 8000 --reload
```

### Explanation of parameters

* `asgi_server:app`
Refers to the Python file and application instance:
* `asgi_server` → file name (`asgi_server.py`)
* `app` → ASGI application object inside the file
* `--host 0.0.0.0`
Makes the server accessible from outside the local machine (useful for testing and containers)
* `--port 8000`
Specifies the port where the server will run
* `--reload`
Automatically restarts the server when code changes (development only)

## Suggested Approach

* Create a Starlette application
* Define:

one HTTP route (`/`)
one WebSocket route (`/ws`)
* Accept the WebSocket connection before receiving messages
* Use a loop to receive and send messages continuously
* Keep the connection open for multiple exchanges

Example structure:

```python
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute

async def homepage(request):
    # HTML response here

async def websocket_endpoint(websocket):
    await websocket.accept()
    # message loop here

app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_advanced/websockets`
* File: `asgi_server.py`

---

### 6. Browser Client <a name='subparagraph6'></a>

## Introduction

In this step, you will build a browser-based client for your WebSocket application.

Until now, you have tested communication using scripts and tools. In real applications, users interact through a web interface that connects to a backend server using WebSockets.

This task is intentionally **open-ended**. Your goal is to create a simple but functional web client that demonstrates real-time communication using the system you have built.

This step completes the project by producing a working, user-facing application.

### Instructions

Create a web client that:

* Connects to your WebSocket endpoint:

```text
ws://localhost:8000/ws
```

* Allows a user to send messages
* Displays messages received from the server
* Works in real time without reloading the page

You are free to design the interface and structure the code as you prefer, as long as the required behavior is implemented.

### Requirements

Your implementation must include:

* An HTML file (`index.html`)
* A JavaScript file (`chat.js`)
* A CSS file (`style.css`)

The client must:

* Establish a WebSocket connection from the browser
* Send messages through that connection
* Receive messages from the server
* Display messages dynamically in the page

### Expected Behavior

When the application is running and the page is opened in a browser:

* The interface is displayed correctly
* The client connects to the WebSocket server
* The user can send messages
* Server responses are displayed in the page
* The page does not reload during interaction
* Multiple messages can be exchanged in a single session

### Suggested Approach

* Create a simple layout with:

a text input
a send button
a message display area
* Use the browser’s `WebSocket` API to:

open a connection
send messages
listen for responses
* Update the page dynamically using JavaScript

Example connection:

```javascript
const socket = new WebSocket("ws://localhost:8000/ws");

socket.onmessage = (event) => {
    console.log(event.data);
};
```

### How to Test

1. Start your ASGI server:

```bash
uvicorn asgi_server:app --reload
```

1. Open:

```text
http://localhost:8000
```

1. Interact with your interface and verify that communication works in real time.

### Optional Challenges

If you want to extend your implementation, you can try one or more of the following:

* Add a **username field** and display the sender name with each message
* Show a **timestamp** for each message
* Keep a **chat history** during the session (messages remain visible after sending new ones)
* Differentiate visually between:

sent messages
received messages
* Add basic **styling improvements** to make the interface more readable
* Display a message when:

the connection is established
the connection is lost

These improvements are optional. They are intended to help you explore how real-time applications are built and improve the user experience.

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_advanced/websockets`
* File: `index.html styles.css chat.js`

---

### 7. Quiz <a name='subparagraph7'></a>

## Introduction

In this step, you will complete a quiz to validate your understanding of the concepts covered in this project.

The quiz evaluates your understanding of:

* WebSocket communication principles
* Differences between HTTP and persistent connections
* Asynchronous message handling
* Client–server interaction patterns
* Message routing and validation

### Instructions

* Answer all questions
* Read each question carefully before selecting your answer
* Some questions may have more than one correct answer
* This quiz is **one-shot**
* Each question has a limited time to be answered
* You cannot retry the quiz once submitted

### Notes

* This is an individual evaluation
* No external help should be used during the quiz
* Time management is important

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
