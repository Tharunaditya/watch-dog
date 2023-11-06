# watch-dog
Watchdog v1.0 is a Python-based program designed for capturing and analyzing network packets. It provides users with the ability to monitor and gain insights into network traffic, making it a valuable resource for network administrators, cybersecurity enthusiasts, and anyone interested in understanding the flow of data across a network.


# WatchDog Packet Analyzer

![Banner](watchdog_banner.png)

## Overview

WatchDog Packet Analyzer is a Python script for capturing and analyzing network packets using Scapy. It provides detailed packet information, including source and destination MAC and IP addresses, port numbers, and packet data. This tool is designed for network troubleshooting, monitoring, and security analysis.

## Developer

- **Developer:** Tharunaditya Anuganti

## Features

- Capture and analyze network packets.
- Colorful console output using the Colorama library.
- Filter packets by protocol (IP, TCP, UDP, ICMP, DNS, ARP, or all packets).
- Save captured packet information to a text file.
- User-friendly menu for filter selection and packet capture options.

## Requirements

- Python 3
- Scapy
- Colorama

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/watchdog-packet-analyzer.git
   cd watchdog-packet-analyzer
   ```

2. Install the required libraries:

   ```bash
   pip install scapy colorama
   ```

3. Run the WatchDog Packet Analyzer:

   ```bash
   python watchdog.py
   ```

4. Follow the on-screen instructions to select a packet filter and specify the number of packets to capture.

5. Optionally, save the captured packet information to a file.

## Packet Filters

- 1: IP (Internet Protocol)
- 2: TCP (Transmission Control Protocol)
- 3: UDP (User Datagram Protocol)
- 4: ICMP (Internet Control Message Protocol)
- 5: DNS (Domain Name System)
- 6: ARP (Address Resolution Protocol)
- 7: All (No Filter)

## Contribution

If you want to contribute to this project, please refer to the [contribution guidelines](CONTRIBUTING.md) for rules and guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
