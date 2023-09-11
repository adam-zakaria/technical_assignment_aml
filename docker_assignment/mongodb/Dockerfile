# Use the official MongoDB image as a base image
FROM mongo:latest

# Install SSHFS and necessary packages
RUN apt-get update && \
    apt-get install -y iputils-ping openssh-client sshfs python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add a script to mount the remote folder using SSHFS
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
COPY mount_remote.py /usr/local/bin/mount_remote.py

RUN chmod +x /usr/local/bin/mount_remote.py
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set the new script as the entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]