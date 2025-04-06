# ------------------------------ Imports ------------------------------ #

import os
import socket
import concurrent.futures
from rich.console import Console

# ---------------------------- Terminal ------------------------------- #

terminal = Console()

# ----------------------- Port Scanning Engine ------------------------ #

def check_single_port(host, port_num, active_ports):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        if sock.connect_ex((host, port_num)) == 0:
            try:
                detected_service = socket.getservbyport(port_num)
            except:
                detected_service = "Unknown"
            terminal.print(f"[green][+] Port {port_num} OPEN — {detected_service.upper()}")
            active_ports.append(port_num)

# ---------------------- Input + Scan Trigger ------------------------- #

def launch_scanner():
    host_ip = terminal.input(r"[bold cyan][?] Enter Target IP: ")
    terminal.print(r"[bold cyan][?] Use commas for multiple ports (e.g., 21,22,80), or leave blank to scan all.")
    custom_ports = terminal.input(r"[bold cyan][?] Enter Port(s): ")

    port_range = list(map(int, custom_ports.split(','))) if custom_ports else range(1, 65536)
    found_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as pool:
        pool.map(lambda prt: check_single_port(host_ip, prt, found_ports), port_range)

    if not found_ports:
        terminal.print(f"[red][-] No open ports detected on {host_ip}")
    else:
        terminal.print(f"[green][✓] Scan completed — {len(found_ports)} open port(s) found.")

# ----------------------------- Banner ------------------------------- #

def print_banner():
    terminal.print(r"""[bold green]


                                                                                                                                                                                                                 

:'######::'##::::'##::::'###::::'########:::'#######::'##:::::'##:'########:::'#######::'########::'########:
'##... ##: ##:::: ##:::'## ##::: ##.... ##:'##.... ##: ##:'##: ##: ##.... ##:'##.... ##: ##.... ##:... ##..::
 ##:::..:: ##:::: ##::'##:. ##:: ##:::: ##: ##:::: ##: ##: ##: ##: ##:::: ##: ##:::: ##: ##:::: ##:::: ##::::
. ######:: #########:'##:::. ##: ##:::: ##: ##:::: ##: ##: ##: ##: ########:: ##:::: ##: ########::::: ##::::
:..... ##: ##.... ##: #########: ##:::: ##: ##:::: ##: ##: ##: ##: ##.....::: ##:::: ##: ##.. ##:::::: ##::::
'##::: ##: ##:::: ##: ##.... ##: ##:::: ##: ##:::: ##: ##: ##: ##: ##:::::::: ##:::: ##: ##::. ##::::: ##::::
. ######:: ##:::: ##: ##:::: ##: ########::. #######::. ###. ###:: ##::::::::. #######:: ##:::. ##:::: ##::::

    Speed • Silent • Simplicity         

    """)
    terminal.print("[bold green]╔══════════════════════════════════════════════════════════════════════════╗")
    terminal.print("[bold green]║ [white]Tool:[bold cyan] ShadowPort [green]| [white]Author:[bold cyan] Anand [green]                                      ║")
    terminal.print("[bold green]║ [white]GitHub:[bold cyan] github.com/w4r70ck                                  [green]             ║")
    terminal.print("[bold green]║ [white]Mode:[bold cyan] Fast • Silent • Terminal-native Scanner               [green]             ║ ") 
    terminal.print("[bold green]╚══════════════════════════════════════════════════════════════════════════╝")


# ---------------------------- Entry Point ---------------------------- #

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print_banner()
    launch_scanner()
    terminal.print("[bold green]+------------------------------------------------------------------+")
