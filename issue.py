#!/usr/bin/env python

import codecs
import logging
import os
import tarfile
import tempfile
import time
from StringIO import StringIO

import docker
import git
import requests
from docker.errors import ImageNotFound


def save_tar_to_file(tb1):
    temporary_file = codecs.open("issue.tar", mode="w+b")
    temporary_file.write(tb1)


class DockerRenewer(object):
    def __init__(self):
        self.log = logging.getLogger()
        self.docker = docker.from_env()
        self.docker_image_tag = "letsencrypt_certbot_aws_%s" % int(time.time())

    def __del__(self):
        self.log.debug("Removing docker image %s" % self.docker_image_tag)
        try:
            self.docker.images.get(self.docker_image_tag)
            self.docker.images.remove(image=self.docker_image_tag, noprune=False)
        except ImageNotFound:
            self.log.warning("When trying to remove image {}, Docker said it didn't exist".format(self.docker_image_tag))

    def doit(self):
        self.log.info("Doing it") 
        self.create_image_if_needed()
        container = self._create_and_start_container()
        self.log.info("Sleeping for some time, so container can really be stopped")
        time.sleep(5);
        self._save_files(container)
        self._remove_container(container)

    def _remove_container(self, container):
        self.log.debug("Removing container %s" % container)
        container.remove()

    def _create_and_start_container(self):
        cmd = ("/to-be-run-in-container.sh")
        self.log.info("Doing work {} in container based on image: {}".format(cmd, self.docker_image_tag))
        container = self.docker.containers.run(self.docker_image_tag, cmd, detach=True, entrypoint="/bin/sh -c")
        return container

    def create_image_if_needed(self):
        try:
            self.docker.images.get(self.docker_image_tag)
            return
        except ImageNotFound:
            pass
        self.log.info("Building docker image %s" % self.docker_image_tag)
        self.docker.images.build(tag=self.docker_image_tag, path="src/docker")

    def _save_files(self, container):
        destination_directory = "untarred/"
        self.log.info("Waiting for container %s - usually takes a minute" % container)
        container.wait()
        self.log.info("Container %s done - here comes the logs:" % container)
        self.log.info(container.logs())

        self.log.debug("Extracting files")
        (tar_ball, data) = container.get_archive("/etc/letsencrypt/")
        tb1 = tar_ball.next()
        save_tar_to_file(tb1)
        ball = tarfile.open(fileobj=StringIO(tb1))
        [self.log.debug(m) for m in ball.getmembers()]
        [self.log.debug("Found tar file member {}".format(m)) for m in ball.getmembers()]
        [self._save_file(destination_directory, ball, m) for m in ball.getmembers() if m.name[-5:] == ".conf"]

    def _save_file(self, directory, tar_file, file_member):
        file_name = os.path.join(directory, file_member.name.split("/")[-1])
        self.log.debug("Saving file %s" % file_name)
        source = tar_file.extractfile(file_member)
        tarfile.copyfileobj(source, codecs.open(file_name, "w", "utf-8"))


if __name__ == '__main__':
    log_level = logging.INFO
    if os.getenv("USER") == "ceda":
        log_level = logging.DEBUG

    logging.basicConfig(level=log_level)
    DockerRenewer().doit()
