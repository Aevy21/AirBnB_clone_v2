#!/usr/bin/python3
"""
This script generates a .tgz archive from the web_static folder
and distributes it to web servers using Fabric.
"""


from fabric.api import *
from fabric.api import runs_once
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
        str: Archive path if archive has been generated, otherwise None.
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
    result = local("tar -cvzf {} web_static".format(archive_path))

    # Check if archive was created successfully
    if result.succeeded:
        print("web_static packed: {} ".format(archive_path))
        return archive_path
    else:
        print("Failed to pack web_static")
        return None


def do_deploy(archive_path):
    """ Distributes an archive to webserver """

    if not exists(archive_path):
        return False

    print("Deploying new version")

    archive_name = archive_path.split("/")[-1]
    folder_name = archive_name[: -4]
    dir_path = "/data/web_static/releases/{}".format(folder_name)

    put(archive_path, "/tmp/")
    run("mkdir -p {}".format(dir_path))
    result = run("tar -xzf /tmp/{} -C {}".format(archive_name, dir_path))

    if result.failed:
        return False

    run("cp -r {}/web_static/* {}".format(dir_path, dir_path))
    run("rm -rf /tmp/{} {}/web_static".format(archive_name, dir_path))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(dir_path))

    print("New version deployed!")

    return True
def deploy():
    """
    Main deployment function.
    Creates and deploys a new version locally.
    """
    local_archive_path = do_pack()
    if not local_archive_path:
        print("Failed to create archive. Deployment aborted.")
        return False

    print("Local archive created successfully at: {}".format(local_archive_path))

    # Extract archive locally
    extraction_path = "extracted_version"
    local("mkdir -p {}".format(extraction_path))
    local("tar -xzf {} -C {}".format(local_archive_path, extraction_path))

    # Update current symlink to point to the new version
    local("rm -rf /data/web_static/current")
    local("ln -s {}/web_static /data/web_static/current".format(extraction_path))

    print("Deployment successful!")
    return True

# Call deploy function
deploy()
