#!/usr/bin/python3
"""
This Fabric file generates a .tgz archive from the contents  of the
web_static folder
"""


from fabric.operations import local
from datetime import datetime
from fabric.context_managers import lcd

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Archive path if the archive has been correctly generated, otherwise None.
    """
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Define archive name
    archive_name = "web_static_{}.tgz".format(timestamp)
    
    # Create versions folder if it doesn't exist
    local("mkdir -p versions")
    
    # Create tgz archive
    with lcd("web_static"):
        result = local("tar -czvf ../versions/{} .".format(archive_name))
        
    # Check if archive was created successfully
    if result.return_code == 0:
        return "versions/{}".format(archive_name)
    else:
        return None
