import socket

def enviar_mensagem(cliente_socket, mensagem):
    cliente_socket.sendall(mensagem.encode())
    data = cliente_socket.recv(1024)
    print(f"Resposta do servidor: {data:decode()}")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client_socket.connect(('localhost', 12345))


while True: 

    # Enviando um mensagem para o servidor
    message = input("Digite sua mensagem (ou 'saiu' ou 'encerrar' para encerrar): ")
    enviar_mensagem(client_socket, message)

    # Encerrar a conexão se o cliente enviar "saiu" ou "encerrar"
    if "encerrar" in message.lower() or "saiu" in message.lower():
        break

client_socket.close()
