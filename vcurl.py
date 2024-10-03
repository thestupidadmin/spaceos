import requests
url = input("Send GET request to :")
if url.startswith(('http://', 'https://')):
    print("Please retry the command without entering the protocol (http://, https://)")
else:
  requests.get(url)
