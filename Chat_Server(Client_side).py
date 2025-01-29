import socket
import threading

# Server Configuration
HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    """
    Receive and print messages from the server.
    """
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            print("Disconnected from the server.")
            client_socket.close()
            break

def start_client():
    """
    Connect to the chat server and start sending/receiving messages.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Connected to the chat server.")

    # Receive welcome and existing users
    print(client_socket.recv(1024).decode('utf-8'))  # Welcome message
    print(client_socket.recv(1024).decode('utf-8'))  # Prompt for username

    # Get username and inform the server
    username = input()
    client_socket.send(username.encode('utf-8'))

    # Start a thread to receive messages
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input()
        if message.lower() == '/quit':
            client_socket.send('/quit'.encode('utf-8'))
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
