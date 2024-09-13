import socket
import threading

def is_host_online(ip, port=80):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0 
    except socket.error:
        return False

def scan_ip(ip):
    if is_host_online(ip, port=80):
        print(f"{ip} is online.")
        scan_ports(ip)
    else:
        print(f"{ip} is offline.")

def scan_ports(ip, ports=[80, 443, 22, 8080]):
    print(f"Scanning ports for {ip}...")
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    if open_ports:
        print(f"Open ports for {ip}: {open_ports}")
    else:
        print(f"No open ports found for {ip}")

def scan_ip_range(start_ip, end_ip):
    start_octets = start_ip.split('.')
    end_octets = end_ip.split('.')

    for i in range(int(start_octets[3]), int(end_octets[3]) + 1):
        ip = f"{start_octets[0]}.{start_octets[1]}.{start_octets[2]}.{i}"
        t = threading.Thread(target=scan_ip, args=(ip,))
        t.start()

start_ip = "192.168.1.1"
end_ip = "192.168.1.10"

scan_ip_range(start_ip, end_ip)
