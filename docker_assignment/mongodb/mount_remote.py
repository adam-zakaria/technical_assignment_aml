import os

def main():
    # Set up SSHFS mount
    os.system('sshfs -o StrictHostKeyChecking=no -o allow_other -o reconnect user@remote-server:/path/to/remote/folder /remote_folder')
    
    # Start the MongoDB server
    os.system('docker-entrypoint.sh mongod')

if __name__ == "__main__":
    main()
