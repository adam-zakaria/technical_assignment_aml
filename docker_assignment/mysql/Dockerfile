# Use the official MariaDB base image
FROM mariadb:latest

# Customizations can go here. For instance, if you need to install additional tools:
RUN apt-get update && \
    apt-get install -y vim iputils-ping openssh-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Define the environment variables (optional)
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=userpassword

# Copy any custom configuration files if necessary (uncomment the following line if applicable)
# COPY ./my-custom.cnf /etc/mysql/mariadb.conf.d/

# Expose port 3306 for the MariaDB service (optional, since it is exposed in the base image by default)
EXPOSE 3306

# No need to specify a CMD directive because the base image already defines it to run MariaDB server