# Modifies the ulimit setting for Nginx and restarts the service
exec { '/usr/bin/env sed -i s/15/1024/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
