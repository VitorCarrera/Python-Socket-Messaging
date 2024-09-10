import socket

def enviar_mensagem(cliente_socket, mensagem):
    cliente_socket.sendall(mensagem.encode())
    data = cliente_socket.recv(1024)
    print(f"Resposta do servidor: {data:decode()}")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client_socket.connect(('localhost', 12345))



# Enviando um mensagem para o servidor
message = "Olá, servidor!!"
client_socket.sendall(message.encode())

# Recebendo resposta do servidor
data = client_socket.recv(1024)
print(f"Resposta do servidor {data.decode()}")

client_socket.close()
