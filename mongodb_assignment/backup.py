import time
import os

def backup_data():
    # Step 1: Run mongodump to backup MongoDB data
    backup_command = "mongodump --uri='mongodb://localhost:27017/' --out=/path/to/backup/folder"
    exit_code = os.system(backup_command)
    if exit_code == 0:
        print("Backup successfully created.")
    else:
        print(f"Error during backup: {exit_code}")
        return

    # Step 2: Copy backup data to another server using scp
    scp_command = "scp -r /path/to/backup/folder username@remote_server:/path/to/remote/backup/folder"
    exit_code = os.system(scp_command)
    if exit_code == 0:
        print("Backup successfully transferred to the remote server.")
    else:
        print(f"Error during transfer: {exit_code}")

def job():
    print("Starting backup job...")
    backup_data()
    print("Backup job completed.")

# Run the job indefinitely every 7 days (604800 seconds)
while True:
    job()
    time.sleep(604800)
