# Chat-server-using-python-
# 🗨️ Chat Server  

A lightweight and scalable chat server for real-time messaging using  [Python].  
A real-time chat server built using Python and WebSockets, designed for seamless and scalable communication. This server enables multi-user messaging, supports authentication, and can be integrated with any frontend or mobile app.

## 🚀 Features  
- 🔄 Real-time messaging  
- 👥 Multi-user chat support  
- 🔐 Secure authentication  
- 📦 Scalable architecture  
- 📝 Message history storage  
# Chat Server with Authentication

## Description
This is a simple chat server that allows multiple users to connect, authenticate using an ID and password, and communicate in real-time. New users joining the chat can see the list of active users.

## Setup

### Running the Server on a Local or Public Network

#### 1. Find Your Local IP Address
If running on your **local network (LAN)**, find your **local IP address**:

- **Windows:** Run the following command in Command Prompt:
  ```sh
  ipconfig
  ```
- **Linux/Mac:** Run the following command in Terminal:
  ```sh
  ifconfig
  ```

#### 2. Modify the Server Script
Edit the `server.bind` line in `chat_server_auth.py` to bind to your local IP instead of `0.0.0.0`:
```python
server.bind(("YOUR_LOCAL_IP", 12345))
```

If you want to allow connections over the internet, set up **port forwarding** on your router and use your **public IP address**.

---

## Running the Client on Multiple Devices

Modify the client script (`chat_client_auth.py`) to connect using the **server's IP address** instead of `127.0.0.1`:
```python
client.connect(("SERVER_IP", 12345))  # Replace SERVER_IP with the server's local or public IP
```
Then, run the client script on different devices.

---

## Running the Server
To start the server, run:
```sh
python chat_server_auth.py
```

## Running the Client
To connect a client to the server, run:
```sh
python chat_client_auth.py
```

---

## Notes
- Ensure that **port 12345 is open** on your firewall or router.
- If using the internet, configure **port forwarding** for external access.
- The server allows **multiple clients** to connect and chat simultaneously.
- Users **must authenticate** before joining the chat.

---

Enjoy chatting securely! 🚀

