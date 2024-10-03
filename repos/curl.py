import argparse
import requests

def send_request(method, url, headers=None, data=None, params=None):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers, params=params)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=data)
        else:
            print(f"Method {method} not supported.")
            return

        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple curl-like tool.")
    parser.add_argument('url', help="The URL to send the request to (without protocol)")
    parser.add_argument('-X', '--request', help="HTTP method to use (GET or POST)", default='GET')
    parser.add_argument('-H', '--header', action='append', help="Custom headers (key:value)")
    parser.add_argument('-d', '--data', help="Data for POST request (key=value)")
    parser.add_argument('-p', '--params', help="Query parameters for GET request (key=value)")

    args = parser.parse_args()

    # Process headers
    headers = {}
    if args.header:
        for header in args.header:
            key, value = header.split(':', 1)
            headers[key.strip()] = value.strip()

    # Process data (for POST requests)
    data = args.data if args.data else None

    # Process params (for GET requests)
    params = {}
    if args.params:
        for param in args.params.split('&'):
            key, value = param.split('=', 1)
            params[key] = value

    send_request(args.request.upper(), args.url, headers=headers, data=data, params=params)
