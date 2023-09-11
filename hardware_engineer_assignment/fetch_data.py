import os
import time
from shutil import copyfile
# from smb.SMBConnection import SMBConnection

def fetch_data_from_ubuntu(remote_path, local_path):
    pass
    # use sftp to transfer files from Ubuntu

# For the Windows 10 remote


def fetch_data_from_windows(remote_path, local_path):
    # use SMB to transfer files from Windows
    pass


def data_crawler():
    while True:
        try:
            # Define paths (you would need to replace with actual paths)
            ubuntu_remote_path = "path/to/ubuntu/data"
            windows_remote_path = "path/to/windows/data"
            local_path_ubuntu = "path/to/local/directory/ubuntu"
            local_path_windows = "path/to/local/directory/windows"

            fetch_data_from_ubuntu(ubuntu_remote_path, local_path_ubuntu)
            fetch_data_from_windows(windows_remote_path, local_path_windows)
        except Exception as e:
            print(f"An error occurred: {e}")

        # Let the crawler sleep for a certain period before checking again
        time.sleep(60 * 60)  # Adjust the time as necessary


if __name__ == "__main__":
    data_crawler()
