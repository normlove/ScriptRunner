import subprocess
import getpass

def delete_file(file_path):
    try:
        subprocess.run(['sudo', 'rm', file_path], check=True)
        print(f"File '{file_path}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting file: {e}")
        # Add error handling as per your requirements

def select_file():
    file_path = subprocess.run(['zenity', '--file-selection'], capture_output=True, text=True).stdout.strip()
    return file_path

if __name__ == '__main__':
    file_path = select_file()
    if file_path:
        try:
            delete_file(file_path)
        except PermissionError:
            password = getpass.getpass("Superuser password required: ")
            command = f"echo {password} | sudo -S rm {file_path}"
            try:
                subprocess.run(command, shell=True, check=True)
                print(f"File '{file_path}' deleted successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error deleting file: {e}")
    else:
        print("No file selected.")
