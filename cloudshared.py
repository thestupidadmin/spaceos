import os
import sys
import subprocess
import signal
import time

def signal_handler(sig, frame):
    pass

signal.signal(signal.SIGINT, signal_handler)

print("Starting SpaceOS Init (Cloud-Python-discord.gg/hetzner)")
total_steps = 100
for i in range(total_steps + 1):
    time.sleep(0.0005)
    print(f"\r[{'#' * (i // 2)}{' ' * (50 - i // 2)}] {i}%", end="")
    sys.stdout.flush()
print("\nSpaceOS Init Complete!")

base_directory = os.path.dirname(os.path.abspath(__file__))
hostname = os.uname()[1]
USERS_FILE = os.path.join(base_directory, 'etc', 'users')
REPO_FILE = os.path.join(base_directory, 'etc', 'appinstallrepos')
HOME_DIR = os.path.join(base_directory, 'home')
ROOT_HOME_DIR = os.path.join(HOME_DIR, 'root')
DEFAULT_REPO = "https://raw.githubusercontent.com/thestupidadmin/spaceos/refs/heads/main/repos"

def initialize_file_system():
    os.makedirs(os.path.join(base_directory, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(base_directory, 'etc'), exist_ok=True)
    os.makedirs(os.path.join(base_directory, 'root'), exist_ok=True)
    os.makedirs(HOME_DIR, exist_ok=True)

    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            f.write("root:root:/root\n")
            print("Default user 'root' created with password root.")

    if not os.path.exists(REPO_FILE):
        with open(REPO_FILE, 'w') as f:
            f.write(f"{DEFAULT_REPO}\n")
            print(f"Default repository added: {DEFAULT_REPO}")

def login():
    global current_user, current_home
    username = input("Username: ")
    password = input("Password: ")

    if not os.path.exists(USERS_FILE):
        print("Error: Users file does not exist.")
        return False

    with open(USERS_FILE, 'r') as f:
        users = f.readlines()

    for user in users:
        user_info = user.strip().split(':')

        if user_info[0] == username:
            if len(user_info) > 1 and user_info[1] != password:
                print("Incorrect password.")
                return False
            current_user = username
            current_home = user_info[2]
            print(f"Logged in as {username}. Home directory: {current_home}")
            return True
    print("User not found.")
    return False

def appinstall(app_name):
    with open(REPO_FILE, 'r') as f:
        repos = f.readlines()

    for repo in repos:
        repo = repo.strip()
        file_url = f"{repo}/{app_name}.py"
        try:
            response = subprocess.run(['curl', '-Is', file_url], stdout=subprocess.PIPE)
            if response.returncode == 0:
                print(f"Installing {app_name}...")
                total_steps = 100
                for i in range(total_steps + 1):
                    time.sleep(0.0018)
                    progress = f"\r[{ '#' * (i // 2) }{ ' ' * (50 - i // 2) }] {i}%"
                    print(progress, end="")
                    sys.stdout.flush()

                destination_file = os.path.join(base_directory, 'bin', f"{app_name}.py")
                os.system(f"curl -s {file_url} -o {destination_file}")
                os.chmod(destination_file, 0o755)
                print(f"\n{app_name} installed successfully at {destination_file}.")
                return
        except Exception as e:
            print(f"Error during installation: {e}")
    print(f"Application '{app_name}' not found in any repository.")

def appremove(app_name):
    app_path = os.path.join(base_directory, 'bin', f"{app_name}.py")
    
    if os.path.exists(app_path):
        os.remove(app_path)
        print(f"{app_name} removed successfully.")
    else:
        print(f"Error: {app_name} not found in the bin directory.")

def appreinstall(app_name):
    print(f"Reinstalling {app_name}...")
    appremove(app_name)
    appinstall(app_name)

def vpasswd(username):
    if username != "root":
        print("Password change is allowed only for the root user.")
        return

    new_password = input("Enter new password: ")
    
    with open(USERS_FILE, 'r') as f:
        users = f.readlines()

    for i in range(len(users)):
        user_info = users[i].strip().split(':')
        if user_info[0] == username:
            users[i] = f"{username}:{new_password}:{user_info[2]}\n"
            break

    with open(USERS_FILE, 'w') as f:
        f.writelines(users)
    
    print(f"Password for user '{username}' changed successfully.")

def rm(target):
    target_path = os.path.join(current_home, target)
    if os.path.exists(target_path):
        if os.path.isdir(target_path):
            os.rmdir(target_path)
            print(f"Directory '{target}' removed.")
        else:
            os.remove(target_path)
            print(f"File '{target}' removed.")
    else:
        print(f"Error: '{target}' does not exist.")

def execute_command(command):
    parts = command.split()
    if not parts:
        return

    cmd = parts[0]

    if cmd == "exit":
        print("Exiting SSH.")
        sys.exit(0)
    elif cmd == "clear":
        os.system('clear')
    elif cmd == "echo":
        if len(parts) < 2:
            print("Usage: echo <text>")
            return
        text = ' '.join(parts[1:])
        with open(os.path.join(base_directory, 'bin', 'echo_output.txt'), 'w') as f:
            f.write(text)
        print(f"Written to echo_output.txt: {text}")
    elif cmd == "cat":
        if len(parts) < 2:
            print("Usage: cat <filename>")
            return
        filename = parts[1]
        try:
            with open(os.path.join(base_directory, 'bin', filename), 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print(f"{filename} not found.")
    elif cmd == "appinstall":
        if len(parts) < 2:
            print("Usage: appinstall <app_name>")
            return
        app_name = parts[1]
        appinstall(app_name)
    elif cmd == "appremove":
        if len(parts) < 2:
            print("Usage: appremove <app_name>")
            return
        app_name = parts[1]
        appremove(app_name)
    elif cmd == "appreinstall":
        if len(parts) < 2:
            print("Usage: appreinstall <app_name>")
            return
        app_name = parts[1]
        appreinstall(app_name)
    elif cmd == "ls":
        print("\n".join(os.listdir(os.path.join(base_directory, 'bin'))))
    elif cmd.startswith("vpasswd"):
        if len(parts) < 2:
            print("Usage: vpasswd <username>")
            return
        username = parts[1]
        vpasswd(username)
    elif cmd == "rm":
        if len(parts) < 2:
            print("Usage: rm <file/directory>")
            return
        target = parts[1]
        rm(target)
    elif cmd == "help":
        help_command()
    elif cmd == "mkdir":
        if len(parts) < 2:
            print("Usage: mkdir <directory>")
            return
        dirname = parts[1]
        mkdir(dirname)
    elif cmd == "touch":
        if len(parts) < 2:
            print("Usage: touch <filename>")
            return
        filename = parts[1]
        touch(filename)
    elif cmd == "pwd":
        pwd()
    else:
        bin_cmd_path = os.path.join(base_directory, 'bin', f"{cmd}.py")
        if os.path.exists(bin_cmd_path):
            os.system(f"python3 {bin_cmd_path} {' '.join(parts[1:])}")
        else:
            print("Command not found.")

def touch(filename):
    print("Due to how SpaceOS is created. we as the developrs are unable to make write perms due to how the vfs is made. Please make a pr and add code. we would love it <3")

def pwd():
    print(current_home)

def mkdir(dirname):
    print("Due to how SpaceOS is created. we as the developrs are unable to make write perms due to how the vfs is made. Please make a pr and add code. we would love it <3")

def help_command():
    commands = {
        "echo": "Print text to the output.",
        "cat": "Display the contents of a file.",
        "appinstall": "Install an application.",
        "appremove": "Remove an installed application.",
        "appreinstall": "Reinstall an application.",
        "vpasswd": "Change the password for the root user.",
        "help": "Display this help message.",
        "exit": "Exit the OS.",
        "pwd": "Print the current working directory.",
        "rm": "Remove a file or directory."
    }
    for cmd, desc in commands.items():
        print(f"{cmd}: {desc}")

initialize_file_system()

if login():
    while True:
        command = input(f"{current_user}@spaceOS ~ $ ")
        execute_command(command)
else:
    print("Failed to login.")
