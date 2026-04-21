import argparse
import sys

def running_cli():
    parser = argparse.ArgumentParser(
        description="Network Scanner CLI - Network port scanning tool.",
        epilog="example: python main.py 192.168.1.1 -p 80,443 -v"
    )

    parser.add_argument(
        "target",
        type=str,
        help="Target IP address or domain (example: 192.168.1.1 or google.com)"
    )

    parser.add_argument(
        "-p", "--ports",
        type=str,
        default="1-1024",
        help="Target port. Format: '80', '80,433', or '1-1024' (Default: 1-1024)"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show the scanning process in detail in the terminal"
    )

    args = parser.parse_args()

    print("\n" + "="*40)
    print("SETTING UP NETWORK SCAN")
    print("="*40 + "\n")
    print(f"[>] Target        : {args.target}")
    print(f"[>] Port          : {args.ports}")
    print(f"[>] Mode Verbose  : {'ACTIVE' if args.verbose else 'NOT ACTIVE'}")

    print("[*] (Simulation) Sending data to Validator...")

    from .validator import target_validation, port_validation
    from .scanner import start_scan

    ip_target = target_validation(args.target)
    ports = port_validation(args.ports)

    if ip_target and ports:
      start_scan(ip_target, ports, args.verbose)
    else:
        sys.exit(1)

    print("[*] (Simulation) Running Scanner...\n")