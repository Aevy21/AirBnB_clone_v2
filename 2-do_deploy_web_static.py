#!/usr/bin/python3
"""
This script generates a .tgz archive from the web_static folder
and distributes it to web servers using Fabric.
"""

from fabric.api import *
from fabric.api import env
from fabric.api import local
from os.path import exists
from datetime import datetime

env.hosts = ["54.165.47.248", "100.25.193.107"]
env.user = "ubuntu"

def do_pack():
    """
    Generates a .tgz archive from the web_static folder.

    Returns:
        str: Archive path if the archive has been correctly generated, otherwise None.
    """
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
        print("web_static packed: {} ".format(archive_path))
        return archive_path
    else:
        print("Failed to pack web_static")
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    if not exists(archive_path):
        print("Archive doesn't exist.")
        return False

    archive_filename = archive_path.split("/")[-1]
    archive_folder = archive_filename.replace(".tgz", "")

    for host in env.hosts:
        with Connection(host) as c:
            c.put(archive_path, "/tmp")

            c.run("mkdir -p /data/web_static/releases/{}".format(archive_folder))
            c.run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_filename, archive_folder))
            c.run("rm /tmp/{}".format(archive_filename))
            c.run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive_folder, archive_folder))
            c.run("rm -rf /data/web_static/releases/{}/web_static".format(archive_folder))
            c.run("rm -rf /data/web_static/current")
            c.run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_folder))

    return True
