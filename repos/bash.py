import os
import sys
import subprocess

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    except Exception as e:
        print(f"Error executing command: {e}", file=sys.stderr)

def main():
    if len(sys.argv) != 2:
        print("Usage: bash [file]")
        sys.exit(1)

    commands_file = sys.argv[1]

    if not os.path.isfile(commands_file):
        print(f"File '{commands_file}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(commands_file, 'r') as file:
        commands = file.readlines()

    for command in commands:
        command = command.strip()
        if command:
            print(f"$ {command}")
            execute_command(command)

if __name__ == "__main__":
    main()
