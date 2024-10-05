# SpaceOS

Welcome to **SpaceOS**, an ultra-lightweight, flexible, and highly customizable operating system built entirely in Python. SpaceOS brings the simplicity of Python programming to the world of operating systems, allowing you to run anything from small scripts to complex applications. It's designed with flexibility in mind, offering low system requirements while remaining as powerful and adaptable as modern Linux distributions like Arch Linux.

## Key Features

- **Python-based**: The entire OS is built using Python 3, making it accessible to developers and enthusiasts familiar with Python. You can write your own scripts, applications, and manage system-level tasks all within a Python environment.
  
- **Extremely Lightweight**: SpaceOS can run on minimal hardware requirements (1KB RAM, 1MB storage, and a single CPU core), making it ideal for low-resource environments or educational use. Despite being lightweight, it remains highly functional.

- **Custom File System**: SpaceOS introduces its own file system architecture that organizes user, system, and application files in a simple and intuitive manner. There's a `/root` directory for the root user, and all applications are managed within `/bin`. However the filesystem is limited and contains some bugs.

- **Open-source Package Repositories**: SpaceOS integrates with open-source repositories, making it easy to install Python-based packages from community-maintained sources. Applications are simply Python scripts that can be installed, removed, and managed directly from the system.

- **Run Linux with SpaceOS**: If you know how to run Linux using `proot` in Python, SpaceOS allows you to extend its functionality to run a Linux environment on top of it. Add Linux packages seamlessly and execute Linux commands from within SpaceOS, giving you the power of Linux and the simplicity of Python.

- **Flexibility**: SpaceOS is as flexible as you want it to be. From installing lightweight Python-based applications to running full Linux packages, SpaceOS adapts to your needs without excessive overhead.

- **Ideal for VPS Hosting**: With its Python-centric design, SpaceOS is an excellent choice for those looking to host virtual private servers (VPS). If you're familiar with building a Discord bot or other server-based applications, you can easily scale SpaceOS to serve as a minimal yet capable VPS environment.

- **Isolated File System**: SpaceOS features an isolated file system that prevents interference with the host file system. This means it cannot access or modify files on the host system unless explicitly allowed. However, running Python 3 with `sudo` can expose vulnerabilities to commands like `rm -rf` and package-related attacks, ensuring that users remain cautious when granting elevated permissions.

## System Requirements

- **RAM**: 1KB minimum (256MB RAM recommanded to avoid crashes due to python)
- **Storage**: 1MB minimum (256MB recommanded for lots of packages (they might need 3rd party pip packages))
- **CPU**: 1 core (recommanded 1core)

SpaceOS can run on virtually any hardware setup, making it ideal for embedded systems, low-power devices, and educational projects where resources are limited.

## Package Management

SpaceOS's package management system is simple and open-source. All packages are Python-based and can be installed directly from repositories specified in configuration files.

All applications are installed into the `bin` directory, and they can be executed directly from there. If you can upload files, you can directly program the apps or upload them without using `appinstall`.

## File System Overview

SpaceOS uses a minimalist and straightforward file structure:

- `/bin`: Directory for installed applications.
- `/etc`: Configuration files, including the list of repositories for app installations.
- `/home`: Home directories for user data.
- `/root`: Root user’s directory for administrative tasks.
- `/os.py`: Init System Starter (Starts the cmd, etc).

## Running Linux on SpaceOS

If you’re familiar with using `proot` to run Linux in a Python environment, you can add the ability to run Linux distributions inside SpaceOS. This gives you the flexibility to combine the lightweight design of SpaceOS with the power of a Linux environment, making SpaceOS a versatile base for a wide range of tasks.

## Getting Started

### Installation
To install SpaceOS, simply clone the repository and execute the main script:
```bash
git clone https://github.com/thestupidadmin/spaceos.git
cd spaceos
python3 os.py
```

SpaceOS will initialize, and you’ll be ready to start installing packages or writing your own Python-based applications.

### For pterodactyl
You can use our egg. Just look in the repo files and download it and upload it to the panel. For use in pterodactyl ONLY! Also if you are looking to make cloud images for SpaceOS. Use cloud.py. its meant for cloud and its made for that. Be aware that the cloud image uses password root. 

## Contributing

Contributions are welcome! If you have an idea for improving SpaceOS or wish to contribute Python-based packages, feel free to submit issues or pull requests to the repository.

## License

SpaceOS is open-source and available under the MIT License.

Experience the power of simplicity with **SpaceOS** — a Python-based operating system that makes development and deployment fast, efficient, and accessible to all.

Fun fact: You can run spaceos in spaceos in spaceos in spaceos using the isovm package.
