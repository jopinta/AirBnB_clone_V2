#!/usr/bin/env bash
#script that sets up your web servers for the deployment
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" \etc/nginx/sites-available/default
sudo service nginx start
