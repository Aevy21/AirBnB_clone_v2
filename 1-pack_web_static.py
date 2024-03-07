#!/usr/bin/python3
""" This script generates a .tgz archive from the web_static folder """
from fabric.api import local
from datetime import datetime

def do_pack():
    """ Generates a .tgz archive """
    
    # Get current timestamp
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Define archive name with the specified format
    archive_name = "web_static_{}.tgz".format(current_time)
    
    # Define archive path
    archive_path = "versions/{}".format(archive_name)
    
    print("Packing web_static to {}".format(archive_path))
    
    # Create versions folder if it doesn't exist
    local("mkdir -p versions")
    
    # Create tgz archive
    result = local("tar -cvzf {} web_static".format(archive_path), capture=True)
    
    # Check if archive was created successfully
    if result.succeeded:
        print("Successfully packed web_static to {}".format(archive_path))
        return archive_path
    else:
        print("Failed to pack web_static")
        return None
