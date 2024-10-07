import sys
import subprocess
import os
import shutil

def download(url):
    try:
        subprocess.check_call(["wget", url])
    except subprocess.CalledProcessError as e:
        print(f"Failed to download file from {url}: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    filename = url.split("/")[-1]
    return filename

def move_file_to_bin(filename):
    if not filename:
        return
    
    current_dir = os.getcwd()
    bin_dir = os.path.join(current_dir, 'bin')

    if not os.path.exists(bin_dir):
        print(f"Something went wrong.")
        return
    
    src = os.path.join(current_dir, filename)
    dest = os.path.join(bin_dir, filename)
    
    try:
        shutil.move(src, dest)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: get-file <url>")
        return

    url = sys.argv[1]
    filename = download(url)

    if filename:
        move_file_to_bin(filename)

if __name__ == "__main__":
    main()
