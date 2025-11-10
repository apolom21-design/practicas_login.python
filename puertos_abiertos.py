import socket

ip = input ("ingrese la dirección ip que quiera escanear: ")

for puerto in range(1, 65535):
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, puerto))
    
    if result == 0:
        print(f"El puerto {puerto} está abierto")
        sock.close()
        
    else:
        print(f"el puerto {puerto} está cerrado")
        