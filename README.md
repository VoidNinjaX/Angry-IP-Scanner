
---

# Angry Ip scanner 2.0

A simple multithreaded IP and port scanner built in Python. This tool checks whether hosts in a given IP range are online using TCP SYN scans and scans for open ports on reachable hosts.

## Features

- **IP Range Scanning**: Scans a specified range of IP addresses to check if hosts are online.
- **Port Scanning**: Scans commonly used ports (e.g., HTTP, HTTPS, SSH) on reachable hosts.
- **Multithreaded**: Performs scans concurrently, speeding up the process.
- **No Root Privileges Required**: The tool uses TCP SYN scans instead of ICMP ping, so it doesn't require administrator or root privileges.

## Requirements

- Python 3.x
- No external dependencies

## Usage

1. **Clone the repository** or download the Python script.

2. **Run the script** by providing the range of IP addresses you want to scan.

### Example

1. Open a terminal and navigate to the folder where the script is saved.

2. Run the following command:

   ```bash
   python3 your_script_name.py
   ```

3. The script will scan IP addresses from `192.168.1.1` to `192.168.1.10` by default. You can modify the range in the script or adjust it as needed.

### Modifying the IP Range

To change the IP range to scan, modify the following lines in the Python script:

```python
start_ip = "192.168.1.1"
end_ip = "192.168.1.10"
```

Change the `start_ip` and `end_ip` values to the desired range of IP addresses.

### Customizing the Port List

To scan a different set of ports, modify the `ports` list inside the `scan_ports` function:

```python
def scan_ports(ip, ports=[80, 443, 22, 8080]):
```

You can add or remove ports from this list to scan specific services.

## How It Works

1. **TCP SYN Scan**: The tool checks if hosts are online by attempting to establish a TCP connection to port 80 (HTTP). If the connection is successful, the host is considered reachable.
   
2. **Port Scanning**: After determining if a host is online, the tool attempts to connect to commonly used ports (e.g., 80, 443, 22, 8080) to check if they are open.

3. **Multithreading**: The tool scans multiple IP addresses concurrently, reducing the overall scanning time.

## License

This project is licensed under the MIT License.

---

