from socket import socket, AF_INET, SOCK_STREAM, timeout
# TODO: create an .html file. For example "www.google.com"

PORT: int = 80
BYTE_BUFFER_SIZE: int = 4096

def get_url(url: str, name: str) -> None:
    client_socket: socket = socket(AF_INET, SOCK_STREAM) # AF_NET -> IPv4 & Ipv6, SOCK_STREAM -> TCP
    client_socket.settimeout(5) # DoS -> Decline of Service
    client_socket.connect((url, PORT)) # HTTP: 80, HTTPS: 443
    request: bytes = b"GET / HTTP/1.1\r\nHOST: " + url.encode() + b"\r\n\r\n"
    client_socket.sendall(request)
    response: bytes = b""
    while True:
        try:
            data = client_socket.recv(BYTE_BUFFER_SIZE) # 10_000: 4_000 (6_000), 4_000 (2_000), 2_000 (0)
            if not data:
                break
            response += data
        except timeout:
            break
    client_socket.close()
    
    with open(f"/home/simon/GitHub/Projects/cli/apps/webbrowser/webbrowser_cli.py{name}.html", 'w') as file:
        file.write(response.decode('latin-1'))  # latin-1

if __name__ == "__main__":
    url: str = input("Please enter a url for example www.google.com\t")
    name: str = input("Please enter a filename:\t")
    get_url(url=url, name=name)