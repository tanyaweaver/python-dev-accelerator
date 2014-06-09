import socket


def get_constants(prefix):
    """mapping of socket module constants to their names."""
    return dict(
        (getattr(socket, n), n)
        for n in dir(socket)
        if n.startswith(prefix)
    )



streams = [info for info in socket.getaddrinfo('crisewing.com', 'http') if info[1] == socket.SOCK_STREAM]
info = streams[0]
cewing_socket = socket.socket(*info[:3])
cewing_socket.connect(info[-1])
msg = "GET / HTTP/1.1\r\n"
msg += "Host: crisewing.com\r\n\r\n"
cewing_socket.sendall(msg)
cewing_socket.shutdown(socket.SHUT_WR)
buffsize = 4096
response = ''
done = False
while not done:
    msg_part = cewing_socket.recv(buffsize)
    if len(msg_part) < buffsize:
        done = True
        cewing_socket.close()
    response += msg_part
len(response)
cewing_socket.shutdown(socket.SHUT_RD)
cewing_socket.close()
