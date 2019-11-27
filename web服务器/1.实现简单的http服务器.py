import socket


def server_client(new_socket):
    request = new_socket.recv(1024)
    print(request)
    response = "HTTP/1.1 200 OK \r\n"
    response += "\r\n"
    response += "hahaha"

    new_socket.send(response.encode("utf-8"))
    new_socket.close()


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定套接字
    tcp_server_socket.bind(("", 7890))
    # 3.变为监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 等待客户端的连接
        new_socket, client_addr = tcp_server_socket.accept()
        # 为这个客户端服务
        server_client(new_socket)
        # 4.关闭监听套接字
    new_socket.close()


if __name__ == "__main__":
    main()
