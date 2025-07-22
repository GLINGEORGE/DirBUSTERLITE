import requests

# Get target input from user
target_url = input('[*] Enter Target URL (e.g., https://example.com): ').strip()
file_name = input('[*] Enter path to the wordlist file: ').strip()

# Function to send HTTP GET request
def request(url):
    try:
        return requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        return None

# Read directory names from file and construct full URLs
try:
    with open(file_name, 'r') as file:
        for line in file:
            directory = line.strip()
            full_url = f"{target_url.rstrip('/')}/{directory}"
            response = request(full_url)
            if response and response.status_code != 404:
                print(f'[+] Discovered Directory: {full_url} (Status: {response.status_code})')
except FileNotFoundError:
    print(f'[!] The file {file_name} was not found.')
except KeyboardInterrupt:
    print("\n[!] Scan interrupted by user.")
