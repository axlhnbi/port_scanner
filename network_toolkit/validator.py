import ipaddress
import socket
import logging

def target_validation(target):
    try:
        ip = ipaddress.ip_address(target)
        return str(ip)
    except ValueError:
        try:
            ip_from_domain = socket.gethostbyname(target)
            logging.info(f"Domain '{target}' success convert to IP Address: {ip_from_domain}")
            return ip_from_domain    
        except socket.gaierror:
            logging.error(f"Target'{target}' is not valid or unreachable.")
            print(f"\n[X] Error: Target {target} is not valid IP Address or Domain")
            return None

def port_validation(port_string):
    ports = set()

    try:
        if '-' in port_string:
            start, end = map(int, port_string.split('-'))

            if start > end or not (1 <= start <= 65535) or not (1 <= end <= 65535):
                raise ValueError("The port range is unreasonable or out of bounds (1 - 65535)")
            
            ports.update(range(start, end + 1))
        
        elif ',' in port_string:
            for p in port_string.split(','):
                port_int = int(p.strip())
                if not (1 <= port_int <= 65535):
                    raise ValueError("The port range is unreasonable or out of bounds (1 - 65535)")
                ports.add(port_int)
        
        else:
            port_int = int(port_string.strip())
            if not (1 <= port_int <= 65535):
                raise ValueError("The port range is unreasonable or out of bounds (1 - 65535)")
            ports.add(port_int)

        return sorted(list(ports))
    except ValueError as e:
        logging.error(f"Kesalahan input port: {e}")
        print("\n[X] Error: Format port tidak valid.")
        print("    Gunakan format '80', '80,443', atau '1-1024'.")
        print("    Pastikan port berupa angka antara 1 sampai 65535.")
        return None