from time import sleep
from colorama import Fore, Style, init
import subprocess
import socket

# Initialize colorama for text color
init()

# Function to print colored text
def print_colored(text, color):
    print(color + text + Style.RESET_ALL)

# Function for the intro screen
def intro_screen():
    global user_name # Declare user_name as we need it!
    print("\033c")  # Clear screen
    print_colored(app_name, Fore.YELLOW)
    sleep(1)
    print_colored(f"Hello, I am {ai_name}!", Fore.BLUE)
    sleep(1)
    print_colored("I am your Bug Bounty Hunting AI Companion to help guide you throughout your target and help earn you those amazing P3 ~ P1 Vulnerabilities!", Fore.BLUE)
    sleep(2)
    print_colored("Now that you know a little bit about me, let me get your name! You can use an alias if you would like!", Fore.BLUE)
    sleep(1)
    user_name = input(Fore.BLUE + "Please enter your name: " + Fore.GREEN)
    sleep(1)
    print_colored(f"I am SUPER excited to meet you {user_name}! Let's Get Started!!!!", Fore.BLUE)
    sleep(1)
    print("\033c")  # Clear screen

# Function for the main menu
def main_menu():
    print("\033c")  # Clear screen
    print_colored(app_name, Fore.YELLOW)
    sleep(1)
    print_colored(f"Hello, I am {ai_name} and I am ready to assist you {user_name}!", Fore.BLUE)
    sleep(1)
    print_colored(f"Developing Company: {dev_comp}", Fore.CYAN)
    sleep(1)
    print_colored(f"Developed By: {dev_name}", Fore.GREEN)
    sleep(1)
    print_colored("Main Menu", Fore.RED)
    sleep(1)
    print(Fore.YELLOW + "")
    print("1) Recon Work")
    print("2) Framework Auditing")
    print("3) Website Auditing")
    print("4) Server Auditing")
    print("5) Android Auditing")
    print("6) iOS Auditing")
    print("0) Exit Application")

    choice = input("Enter your choice: ")

    if choice == '1':
       recon_work()
    elif choice == '0':
       exit_program()

# Function to exit the program
def exit_program():
    print("\033c")  # Clear screen
    print_colored(app_name, Fore.YELLOW)
    sleep(1)
    print_colored(f"It was a pleasure working with you {user_name}!", Fore.BLUE)
    sleep(1)
    print_colored("Shutting down systems...", Fore.BLUE)
    sleep(1)
    print_colored("Disconnected from Servers...", Fore.RED)
    sleep(1)
    exit()


# Function for Custom Port Scanning
def custom_port_scan(target):
    clear_screen()
    print_colored(app_name, Fore.YELLOW)
    sleep(1)
    print_colored(dev_comp, Fore.GREEN)
    sleep(1)
    print_colored(f"Alright! So we are going to find Port & Services running on {target}", Fore.BLUE)
    sleep(1)
    print_colored("Please wait while I prepare for the port scan...", Fore.BLUE)
    sleep(2)

    open_ports = perform_custom_port_scan(target)

    if open_ports:
        print(Fore.GREEN + "Open Ports:")
        for port, service in open_ports.items():
            print(f"Port #: {port} | Service: {service}")

        save_results = input(Fore.BLUE + "Do you want to save the results of the scan as an xml file? (Yes/No): " + Fore.GREEN)
        if save_results.lower() in ("yes", "y"):
            with open(f"port_discovery_{target}.xml", "w") as file:
                for port, service in open_ports.items():
                    file.write(f"Port #: {port} | Service: {service}\n")
            input(Fore.GREEN + f"Results saved as port_discovery_{target}.xml. Press Enter to continue.")
        else:
            input(Fore.GREEN + "Press Enter to continue.")
    else:
        print(Fore.RED + "No open ports found.")
        input(Fore.GREEN + "Press Enter to continue.")

    recon_menu()

# Function to perform custom port scan with verbose output
def perform_custom_port_scan(target):
    open_ports = {}
    try:
        print(Fore.RED + "Starting port scan...")

        for port in range(1, 65536):  # Scan ports 1-65535
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Adjust the timeout as needed

            result = sock.connect_ex((target, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                    open_ports[port] = service
                    print(Fore.RED + f"Port {port} is open - Service: {service}")
                except:
                    service = "Unknown"
                    open_ports[port] = service
                    print(Fore.RED + f"Port {port} is open - Service: {service}")

            sock.close()

        print(Fore.RED + "Port scan completed.")
    except Exception as e:
        print(Fore.RED + f"An error occurred during the port scan: {str(e)}")

    return open_ports

# Global variable to store the target
target = ""

# Function for Recon Work
def recon_work():
    global target  # Declare target as a global variable

    print("\033c")  # Clear screen
    print_colored(app_name, Fore.YELLOW)
    sleep(1)
    print_colored("Alright! Recon Work! My specialty!", Fore.BLUE)
    sleep(2)
    
    # Check if the target is already set
    if target:
        use_stored_target = input(Fore.BLUE + f"I see that we have a target already listed as {target}. Do you want to use this target? (Yes/No): " + Fore.GREEN)
        if use_stored_target.lower() in ("yes", "y"):
            print_colored(f"Locking on... {target}", Fore.BLUE)
            sleep(1)
            recon_menu()
        else:
            target = input(Fore.BLUE + f"Tell me hacker {user_name}... Who are we going after now?\n"
                            f"You can use one of the following examples:\n"
                            f"(https://target.com | http://target.com | 192.168.0.1 | http://192.168.0.1 | https://192.168.0.1)\n"
                            f"I just need something that is online & active to lock onto! " + Fore.GREEN)
            print_colored(f"I have locked onto the target! We are now going after... {target}", Fore.BLUE)
            sleep(2)
            recon_menu()
    else:
        target = input(Fore.BLUE + f"Tell me hacker {user_name}... Who are we going after now?\n"
                        f"You can use one of the following examples:\n"
                        f"(https://target.com | http://target.com | 192.168.0.1 | http://192.168.0.1 | https://192.168.0.1)\n"
                        f"I just need something that is online & active to lock onto! " + Fore.GREEN)
        print_colored(f"I have locked onto the target! We are now going after... {target}", Fore.BLUE)
        sleep(2)
        recon_menu()


# Function for Recon Menu
def recon_menu():
    while True:
        clear_screen()
        print_colored(app_name, Fore.YELLOW)
        sleep(1)
        print_colored("Recon Work", Fore.RED)
        sleep(1)
        print_colored(f"Alright {user_name}, together, we will find information to help with our Bug Bounty Hunting!", Fore.BLUE)
        sleep(1)
        print_colored(target, Fore.GREEN)
        sleep(1)
        print(Fore.YELLOW + "Menu:")
        print("1) Port & Service Discovery")
        print("2) OSINT Discovery")
        print("3) Data Harvesting")
        print("4) Main Menu")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            custom_port_scan(target)
        elif choice == '2':
            osint_discovery()
        elif choice == '3':
            data_harvesting()
        elif choice == '4':
            main_menu()
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")

# Function to clear the screen
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Constants
app_name = """
 _    _      _     _    _                 _            
| |  | |    | |   | |  | |               (_)           
| |  | | ___| |__ | |  | | __ _ _ __ _ __ _  ___  _ __ 
| |/\| |/ _ \ '_ \| |/\| |/ _` | '__| '__| |/ _ \| '__|
\  /\  /  __/ |_) \  /\  / (_| | |  | |  | | (_) | |   
 \/  \/ \___|_.__/ \/  \/ \__,_|_|  |_|  |_|\___/|_|   
"""

ai_name = "WarriorBot"
dev_comp = "Global Bug Hunters"
dev_name = "Aubrey Love (AKA V1k1ng)"
dev_name_short = "V1k1ng"

# Start the program
user_name = ""
intro_screen()
main_menu()

