import sys
import socket

def probe_port(ip, port, timeout=0.6):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            return result == 0
    except Exception:
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python port_scanner.py <target-ip>")
        sys.exit(1)

    ip = sys.argv[1]
    open_ports = []

    print(f"[+] Scanning ports on {ip}...\n")

    for port in range(1, 65536):
        if probe_port(ip, port):
            open_ports.append(port)

    if open_ports:
        print("[+] Open Ports Found:")
        for port in open_ports:
            print(f"    - Port {port}")
    else:
        print("[-] No open ports found.")

if __name__ == "__main__":
    main()