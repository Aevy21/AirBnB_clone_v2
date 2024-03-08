#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static.

# Install Nginx if it's not already installed
if ! [ -x "$(command -v nginx)" ]; then
  sudo apt-get update
  sudo apt-get install nginx -y
fi

# Define array for folders to be created
folders_to_create=(
  "/data/"
  "/data/web_static/"
  "/data/web_static/releases/"
  "/data/web_static/shared/"
  "/data/web_static/releases/test/"
)

# Create necessary directories if they don't exist
for folder in "${folders_to_create[@]}"; do
  sudo mkdir -p "$folder"
done

# Give ownership of the /data/ folder to the ubuntu user AND group recursively
sudo chown -R ubuntu:ubuntu /data/*

# create an html file with fake content to test configuration
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t<h1>Hello Ms Aevy </h1>\n\t</body>\n</html>" > /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Ensure ownership of the symbolic link
sudo chown -h ubuntu:ubuntu /data/web_static/current

# Update Nginx configuration
cat << EOF | sudo tee /etc/nginx/sites-available/default >/dev/null
server {
    listen 80;
    listen [::]:80;
    server_name aevycreations.tech;

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}
EOF

# Restart Nginx
sudo service nginx restart
