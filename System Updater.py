import subprocess
import getpass

def update_sources(password):
    try:
        command = f"echo {password} | sudo -S apt-get update"
        subprocess.run(command, shell=True, check=True)
        print("Package sources updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating package sources: {e}")
        # Add error handling as per your requirements

def upgrade_system(password):
    try:
        command = f"echo {password} | sudo -S apt-get full-upgrade -y"
        subprocess.run(command, shell=True, check=True)
        print("System upgrade completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error upgrading system: {e}")
        # Add error handling as per your requirements

if __name__ == '__main__':
    password = getpass.getpass("Enter your sudo password: ")
    update_sources(password)
    upgrade_system(password)
