# Update the OS configuration to adjust user settings for smoother login and file access.
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
