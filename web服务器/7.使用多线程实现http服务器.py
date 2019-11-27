import socket
import re
import threading


def server_client(new_socket):
    # 解码用decode
    request = new_socket.recv(1024).decode("utf-8")
    print(request)
    request_lines = request.splitlines()
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    filename = " "
    if ret:
        filename = ret.group(1)
        if filename == "/":
            filename = "/index.html"

    try:
        f = open("./html" + filename, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "file not found"
        # 编码用incode
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content)
        new_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)
    while True:
        new_socket, client_addr = tcp_server_socket.accept()
        p = threading.Thread(target=server_client, args=(new_socket,))
        p.start()
        # new_socket.close()

    tcp_server_socket.close()


if __name__ == "__main__":
    main()
