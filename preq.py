import os
import pwd
import subprocess
import sys

# Function to run shell commands
def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout)
    return result

# Install necessary packages if not already installed
def install_packages():
    packages = ["git", "ffmpeg", "python3-venv"]
    for package in packages:
        run_command(f"sudo apt-get install -y {package}")

# Create a virtual environment and install requirements
def setup_virtualenv():
    run_command("python3 -m venv .venv")
    run_command(".venv/bin/pip install --upgrade pip")
    run_command(".venv/bin/pip install -r requirements.txt")

# Get current user and home directory
username = pwd.getpwuid(os.getuid()).pw_name
home_dir = os.path.expanduser("~")
current_dir = os.getcwd()

# Define the service content
service_content = f"""[Unit]
Description=Terabox Downloader Bot
After=network.target

[Service]
ExecStart={current_dir}/.venv/bin/python {current_dir}/main.py
Restart=always
User={username}
Group={username}
WorkingDirectory={current_dir}
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
"""

# Write the service file to the current directory
service_file_path = os.path.join(current_dir, 'tera_proxy.service')
# with open(service_file_path, 'w') as f:
#     f.write(service_content)

# Copy the service file to /etc/systemd/system/
def setup_service():
    run_command(f"sudo cp {service_file_path} /etc/systemd/system/tera_proxy.service")
    run_command("sudo systemctl daemon-reload")
    run_command("sudo systemctl enable terabox_downloader.service")
    run_command("sudo systemctl start terabox_downloader.service")

def main():
    # install_packages()
    # setup_virtualenv()
    setup_service()
    print("Service file created and service started successfully.")

if __name__ == '__main__':
    main()
