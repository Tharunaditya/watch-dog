from scapy.all import sniff, conf
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

# Function to print a banner with the program name
def print_banner():
    banner_text = r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠤⠤⣤⠀⠀⠀⠀⡼⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⡄⠀⢀⡤⠔⠊⠁⠀⠀⠀⣰⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⠀⠀⠀⠚⠂⠀⠉⠒⠢⠤⠤⠄⠀⡰⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠿⠟⠛⠛⠋⠉⠉⠉⠉⠉⠉⠛⠛⠛⠷⢷⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠙⠛⠓⠓⠒⠒⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣴⣶⣶⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⠟⠉⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠀⠀⠀⠉⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⣽⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷⠀⠀⠀⠀⠀
⠀⠀⢰⣿⡏⣤⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡀⠀⠀⢤⢠⣼⡇⠀⠀⠀⠀⠀
⠀⠀⠀⢿⣿⠁⠀⠀⠀⠀⣴⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠈⣇⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⠀⡀⣀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⢠⣠⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣷⣇⣽⠀⢈⡏⠀⠀⠀⠀⣀⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣦⣤⠀⠀⠀⠀⠀⣿⣿⣧⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠿⣿⣧⣾⣿⡄⠀⠀⠀⠙⠿⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠋⠀⠀⠀⠀⠀⢸⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣿⡇⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢶⣼⣿⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀
⠀⠀⣠⣶⣾⠿⠛⠛⠻⢷⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡿⠋⠉⠉⠉⠛⢿⣦⡀⠀⠀
⢀⣾⡿⠋⠀⠀⠀⠀⠀⠀⠙⣿⡆⢀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣿⡟⠀⠀⠀⠀⠀⠀⠀⠹⣿⡇⠀
⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⣿⣷⣧⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⢠⡾⣠⣇⣠⣿⣿⣿⡇⠀⢀⠀⠀⠀⢀⠀⠀⢹⣷⠀
⣿⣷⡀⠀⣷⠀⠀⠀⣼⣦⣴⣿⠏⠙⠻⠿⣷⡿⠷⣶⣶⡾⠿⠿⠷⢶⣶⣦⣤⣾⣿⣷⣿⣿⠿⠿⠛⠛⠙⠻⣿⣤⣾⣇⠀⢀⣸⡇⠀⠀⠀⠀
⠘⢿⣿⣾⣿⣷⣴⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠋⠀⠀       ⠀⠀⠀⠀⠀⠀⠀
__          __   _       _     _____              
\ \        / /  | |     | |   |  __ \             
 \ \  /\  / /_ _| |_ ___| |__ | |  | | ___   __ _ 
  \ \/  \/ / _` | __/ __| '_ \| |  | |/ _ \ / _` |
   \  /\  / (_| | || (__| | | | |__| | (_) | (_| |
    \/  \/ \__,_|\__\___|_| |_|_____/ \___/ \__, |
                                             __/ | version 1.0   
                                            |___/ 

Developer : Tharunaditya Anuganti 
Copyrights reserved please refer the contribution.md for the rules and guidelines
                                            
'''
    print(Fore.YELLOW + banner_text)

# Set the network interface you want to capture packets on (replace 'Wi-Fi' with your interface name)
conf.iface = 'Wi-Fi'

# Define a packet processing function
def packet_handler(packet):
    # Initialize packet analysis as an empty string
    packet_analysis = ""

    # Display source and destination MAC addresses
    src_mac = packet.src
    dst_mac = packet.dst
    packet_analysis += f"Source MAC: {src_mac}, Destination MAC: {dst_mac}\n"

    # Check if it's an IP packet
    if packet.haslayer('IP'):
        # Extract IP information
        ip_layer = packet['IP']
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        packet_analysis += f"Source IP: {src_ip}, Destination IP: {dst_ip}\n"

        # Check if it's a TCP packet
        if packet.haslayer('TCP'):
            tcp_layer = packet['TCP']
            src_port = tcp_layer.sport
            dst_port = tcp_layer.dport
            packet_analysis += f"Source Port: {src_port}, Destination Port: {dst_port}"

            # Map common ports to service names
            service_names = {
                80: "HTTP",
                443: "HTTPS",
                21: "FTP",
                22: "SSH",
                25: "SMTP",
                53: "DNS",
                67: "DHCP",
                68: "DHCP",
                110: "POP3",
                # Add more port-to-service mappings as needed
            }

            src_service = service_names.get(src_port, "Unknown")
            dst_service = service_names.get(dst_port, "Unknown")

            packet_analysis += f" (Service: {src_service} to {dst_service})\n"

    # Display packet data
    packet_data = str(packet)
    packet_analysis += f"Packet Data: {packet_data}\n"

    # Print the packet analysis to the terminal
    print(Fore.GREEN + "Packet Analysis:")
    print(packet_analysis)

    # Append the packet analysis to the list for saving to the file
    captured_packets.append(packet_analysis)

# Display the filter menu
print_banner()  # Print the program banner
print(Fore.CYAN + "Select a packet filter option:")
print(Fore.CYAN + "1. IP (Internet Protocol)")
print(Fore.CYAN + "2. TCP (Transmission Control Protocol)")
print(Fore.CYAN + "3. UDP (User Datagram Protocol)")
print(Fore.CYAN + "4. ICMP (Internet Control Message Protocol)")
print(Fore.CYAN + "5. DNS (Domain Name System)")
print(Fore.CYAN + "6. ARP (Address Resolution Protocol)")
print(Fore.CYAN + "7. All (No Filter)")

# Get user input for the filter option
filter_option = input(Fore.YELLOW + "Please choose the filter option from the above: ")

# Define the filter based on the user's input
if filter_option == '1':
    packet_filter = 'ip'
elif filter_option == '2':
    packet_filter = 'tcp'
elif filter_option == '3':
    packet_filter = 'udp'
elif filter_option == '4':
    packet_filter = 'icmp'
elif filter_option == '5':
    packet_filter = 'dns'
elif filter_option == '6':
    packet_filter = 'arp'
elif filter_option == '7':
    packet_filter = None  # No filter
else:
    print(Fore.RED + "Invalid option. Using default filter: All (no filter)")
    packet_filter = None  # No filter

# Get the number of packets or continuous capture option
num_packets = input(Fore.CYAN + "Enter the number of packets to capture or 'c' for continuous capture: ")

if num_packets.strip().lower() == 'c':
    # Continuously capture packets until the user decides to stop
    print(Fore.CYAN + "Capturing packets continuously. Press Ctrl+C to stop.")
    try:
        captured_packets = []
        sniff(
            filter=packet_filter,
            prn=packet_handler,  # Process each packet using the defined function
        )
    except KeyboardInterrupt:
        pass
else:
    num_packets = int(num_packets)
    # Sniff packets with the selected filter and a specified number of packets
    captured_packets = []
    sniff(
        filter=packet_filter,
        prn=packet_handler,  # Process each packet using the defined function
        count=num_packets,  # Capture a maximum of the specified number of packets
    )

# Ask the user whether to save the output
save_output = input(Fore.CYAN + "Do you want to save the captured packets to a file? (y/n): ").strip().lower()

if save_output == 'y':
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the output file name
    if packet_filter:
        output_file = f"{timestamp}_{packet_filter}_Packet_Analysis.txt"
    else:
        output_file = f"{timestamp}_All_Packet_Analysis.txt"

    # Save the captured packets to the output file
    with open(output_file, 'w') as file:
        for packet_analysis in captured_packets:
            file.write(packet_analysis + '\n\n')

    print(Fore.GREEN + f"Captured packets have been saved to '{output_file}'.")

elif save_output == 'n':
    print(Fore.RED + "Captured packets have not been saved.")

else:
    print(Fore.RED + "Invalid input. Captured packets have not been saved.")
