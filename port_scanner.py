import socket
import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def scan_ports(target_ip):
    print(f"Starting port scan for {target_ip}")
    for port in range(1, 1025):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            try:
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    print(f"Port {port} is open.")
            except Exception as e:
                print(f"Error scanning port {port}: {e}")

target_ip = input("Enter the target IP: ")

if is_valid_ip(target_ip):
    scan_ports(target_ip)
else:
    print("The entered IP address is not valid.")
