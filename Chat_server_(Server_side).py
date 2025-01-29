import socket
import threading

# Server Configuration
HOST = '127.0.0.1'
PORT = 12345
clients = []
usernames = {}

def broadcast(message, client_socket):
    """
    Broadcast message to all clients except the sender.
    """
    for client in clients:
        if client != client_socket:
            client.send(message)

def handle_client(client_socket):
    """
    Handle messages from the client.
    """
    client_socket.send("Welcome to the chat server!".encode('utf-8'))
    
    # Ask for the user's name once
    client_socket.send("Enter your username:".encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8')
    usernames[client_socket] = username
    clients.append(client_socket)

    # Send the list of existing users to the new user
    user_list = "Existing users: " + ", ".join(usernames.values())
    client_socket.send(user_list.encode('utf-8'))

    # Inform all clients about the new user
    broadcast(f"{username} has joined the chat!".encode('utf-8'), client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == '/quit':
                broadcast(f"{username} has left the chat.".encode('utf-8'), client_socket)
                clients.remove(client_socket)
                del usernames[client_socket]
                client_socket.close()
                break
            else:
                broadcast(f"{username}: {message}".encode('utf-8'), client_socket)
        except:
            clients.remove(client_socket)
            del usernames[client_socket]
            client_socket.close()
            break

def start_server():
    """
    Start the server and accept incoming connections.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("Server started, waiting for clients to connect...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        
        # Start a thread to handle the new client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
