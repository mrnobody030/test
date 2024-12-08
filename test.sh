#!/bin/bash

# Update package list
sudo apt update -y

# Install required dependencies
sudo apt install -y wget gpg apt-transport-https software-properties-common

# Add Microsoft's GPG key
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo gpg --dearmor -o /usr/share/keyrings/microsoft.gpg

# Add the Microsoft Edge repository
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/edge stable main" | sudo tee /etc/apt/sources.list.d/microsoft-edge.list

# Update package list again to include Edge repository
sudo apt update -y

# Install Microsoft Edge
sudo apt install -y microsoft-edge-stable

# Confirm installation
microsoft-edge --version

python test.py
