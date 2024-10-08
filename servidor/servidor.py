import socket
import threading
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.weather_api import obter_temperatura

def gerar_resposta(mensagem):
    mensagem = mensagem.lower()
    
    match mensagem:
        case "olá":
            return "Olá, cliente! Como posso ajudar?"
        case "como você está?":
            return "Sou apenas um servidor"
        case "qual é a melhor linguagem de programação?":
            return "A melhor linguagem de programação é o Python"
        case "qual é a temperatura no momento?":
            return obter_temperatura()
        case "encerrar" | "saiu":
            return "Encerrando conexão!"
        case _:
            return "Não entendi sua mensagem"

def tratar_cliente(conn, addr):
    print(f'Conectado por {addr}')
    while True:
        # Recebendo mensagem do cliente
        data = conn.recv(1024)
        if not data:
            break

        mensagem = data.decode()  # Decodificando bytes para string
        print(f"Mensagem recebida: {mensagem}")

        # Respondendo ao cliente
        resposta = gerar_resposta(mensagem)
        conn.sendall(resposta.encode())

        # Fechar a conexão se o cliente enviou "saiu" ou "encerrar"
        if "encerrar" in mensagem.lower() or "saiu" in mensagem.lower():
            break

    conn.close()
    print(f'Conexão com {addr} encerrada.')


# Criando um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Vinculando o socket ao endereço e porta
server_socket.bind(('localhost', 12345))

# Escutando por conexões
server_socket.listen(5)
print("Servidor escutando na porta...")

# Aceitando conexões de clientes
while True:
    conn, addr = server_socket.accept()
    
    cliente_thread = threading.Thread(target=tratar_cliente, args=(conn, addr))
    cliente_thread.start()
    