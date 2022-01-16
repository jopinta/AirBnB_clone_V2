#!/usr/bin/env bash
#script that sets up your web servers for the deployment
sudo su
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current/
chown -R ubuntu:ubuntu /data/
sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" \etc/nginx/sites-available/default
service nginx start
