import socket  # import library socket for Server


def start_my_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create Server with socket and use connect AF_INET
        server.bind(('127.0.0.1', 2000))  # Use LOCAL ADDRESS and PORT
        server.listen(4)  # Say SERVER Listen 4 request
        while True:
            print('Working')
            client_socket, Address = server.accept()  # Create user-socket for return Address and data client
            data = client_socket.recv(1024).decode('utf-8')  # Install long package
            # print(data)
            content = load_data_from_get_request(data)  # return message in utf-8
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('Fuck You')  # with best wishes


def load_data_from_get_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'  # Return 200 kod request
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'  # Return 404 kod request
    path = request_data.split(' ')[1]
    response = ''
    try:
        with open('views' + path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + 'Sorry Bro! No Page').encode('utf-8')


if __name__ == '__main__':
    start_my_server()
