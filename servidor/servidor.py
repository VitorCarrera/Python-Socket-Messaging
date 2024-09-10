import socket

def gerar_resposta(mensagem):
    if "olá" in mensagem.lower():
        return "Olá, cliente! Como posso ajudar?"
    elif "como você está?" in mensagem.lower():
        return "Sou apenas um servidor"
    elif "qual é a melhor linguagem de programação?" in mensagem.lower():
        return "A melhor linguagem de programação é o C#"
    elif "encerrar" in mensagem.lower() or "saiu" in mensagem.lower():
        return "Encerrando conexão!"
    else:
        return "Não entendi sua mensagem"

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
    print(f"Conectado por {addr}")

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
