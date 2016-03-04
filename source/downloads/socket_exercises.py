import socket


def get_constants(prefix):
    return {getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)}


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')


def get_address_info(host, port):
    for response in socket.getaddrinfo(host, port):
        fam, typ, pro, nam, add = response
        print('family: {}'.format(families[fam]))
        print('type: {}'.format(types[typ]))
        print('protocol: {}'.format(protocols[pro]))
        print('canonical name: {}'.format(nam))
        print('socket address: {}'.format(add))
        print()


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
