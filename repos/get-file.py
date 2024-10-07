import sys
import subprocess

def download(url):
    try:
        subprocess.check_call(["wget", url])
    except subprocess.CalledProcessError as e:
        print(f"Failed to download file from {url}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: get-file <url>")
        return

    url = sys.argv[1]
    download(url)

if __name__ == "__main__":
    main()
