import sys
import subprocess

def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package {package}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: pip3-install <package_name>")
        return

    package = sys.argv[1]
    install(package)

if __name__ == "__main__":
    main()
