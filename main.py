import sys
import logging
from network_toolkit.cli import running_cli

def loggin_basic_config():
    logging.basicConfig(
        filename="network_scanner.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

if __name__ == "__main__":
    loggin_basic_config()

    try:
      running_cli()
    except KeyboardInterrupt:
        logging.info("Appp stoped! with interrupt by user's keyboard (Ctrl+c)")
        print("\nAppp stoped!")
        sys.exit(0)
    except Exception as e:
        logging.critical(f"Somthing wrong. Error: {e}")
        print(f"\n[!] Somthing wrong. Error: {e}")
        sys.exit(1)