0x13. Firewall

# Custom UFW Firewall Configuration

This is a custom UFW (Uncomplicated Firewall) configuration that blocks all incoming traffic by default, except for specific TCP ports: 22 (SSH), 80 (HTTP), and 443 (HTTPS).

## Prerequisites

- A Linux-based system (Ubuntu/Debian preferred) with UFW installed.
- Superuser (root) or sudo privileges.

## Installation

1. Install UFW if not already installed:

   ```bash
   sudo apt install ufw

Configure the firewall by allowing the necessary ports:

bash
Copy code
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp
sudo ufw enable
Configuration Details
sudo ufw default deny incoming: Sets the default policy for incoming traffic to deny.
sudo ufw default allow outgoing: Sets the default policy for outgoing traffic to allow.
sudo ufw allow 22/tcp: Allows incoming SSH traffic on port 22.
sudo ufw allow 443/tcp: Allows incoming HTTPS traffic on port 443.
sudo ufw allow 80/tcp: Allows incoming HTTP traffic on port 80.
sudo ufw enable: Enables the firewall.
sudo ufw status verbose: Shows the firewall status with details.
Custom Rules
You can add additional custom rules in /etc/ufw/before.rules to fine-tune your firewall configuration.
