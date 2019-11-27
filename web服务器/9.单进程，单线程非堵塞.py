import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(("", 7890))
tcp_server_socket.listen(128)
tcp_server_socket.setblocking(False)

client_list = list()
while True:
    try:
        new_socket, client_addr = tcp_server_socket.accept()
    except Exception as ret:
        print("没有客户端请求")
    else:
        new_socket.setblocking(False)
        client_list.append(new_socket)

    for client_socket in client_list:
        try:
            recv_data = new_socket.recv(1024)
        except Exception as ret:
            print("没有数据到来")
        else:
            print(recv_data)
        if recv_data:
            print("对方发来了数据")
        else:
            client_socket.close()
            client_list.remove(client_socket)
            print("客户端已经关闭")
