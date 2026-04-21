import socket
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def _scan_single_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)

            result = s.connect_ex((ip, port))

            if result == 0:
                logging.info(f"Success connect to {ip}:{port}")
                return port, True
            else: 
                return port, False
    except socket.error as e:
        logging.debug(f"Socket error on port {port}: {e}")
        return port, False
    except Exception as e:
        logging.error(f"Unexpected error on port {port}: {e}")
        return port, False

def start_scan(target_ip, port_list, verbose=False):
    start_time = datetime.now()
    open_ports = []

    print(f"\n[>] Starting a scan on the target: {target_ip}")
    print(f"[>] Start time: {start_time.strftime('%y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    with ThreadPoolExecutor(max_workers=100) as executor:
        task_queue = {
            executor.submit(_scan_single_port, target_ip, port): port
            for port in port_list
        }

        for task in as_completed(task_queue):
            checking_port = task_queue[task]

            try:
                port, is_open = task.result()

                if is_open:
                    open_ports.append(port)
                    print(f"[+] PORT {port} \t: OPEN")
                elif verbose:
                    print(f"[-] Port {checking_port} \t: CLOSED")
            
            except Exception as e:
                logging.error(f"Failed to proccess the result for port {checking_port}: {e}")
        
    end_time = datetime.now()
    duration = end_time - start_time

    print("-" * 50)
    print(f"[*] The scan is completed in {duration.total_seconds():.2f} seconds.")
    print(f"[*] Total opened ports: {len(open_ports)}")

    return open_ports