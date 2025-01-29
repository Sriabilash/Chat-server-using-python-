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
Run the Server on a Public or Local Network
If running on your local network (LAN), find your local IP address using:
# ipconfig  # Windows
# ifconfig  # Linux/Mac
Then, modify the server to bind to this IP instead of "0.0.0.0":

# server.bind(("YOUR_LOCAL_IP", 12345))
If running over the internet, forward port 12345 in your router settings and use your public IP.
2. Connect Clients from Different Devices
Modify the client script (chat_client_auth.py) to connect using the server's IP address instead of 127.0.0.1:

#client.connect(("SERVER_IP", 12345))  # Replace SERVER_IP with the server's local or public IP

Then, run the client on different devices.
