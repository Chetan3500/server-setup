#!/usr/bin/env bash

set -e

LOGFILE="/var/log/setup_server.log"
exec > >(tee -a "$LOGFILE") 2>&1
echo "Starting setup at $(date)"

# Check root privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root (use sudo)"
    exit 1
fi

# Check internet connectivity
echo "Checking internet connectivity..."
if ! ping -c 1 google.com &> /dev/null; then
    echo "Error: No internet connection."
    exit 1
fi

# update and upgrade system
apt update && apt upgrade -y

# Install Nginx
apt install nginx -y

# Create a basic webpage
echo "Setting up webpage..."
echo "<h1>Welcome to My Server</h1>" > /var/www/html/index.html

# Start and enable Nginx
echo "Starting Nginx..."
systemctl start nginx
systemctl enable nginx

# Check Nginx status
echo "Check Nginx status..."
if systemctl is-active --quiet nginx; then
    echo "Nginx is running successfully!"
else
    echo "Error: Nginx failed to start."
    exit 1
fi

# Print server URL
IP=$(hostname -I | awk '{print $1}')
echo "Server is up! Access it at http://$IP"
echo "Setup completed at $(date)"

