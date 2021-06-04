#!/bin/python3
import yaml
import subprocess

images = [
    {"image": "fedora", "tag": "34", "Dockerfile": "Dockerfile_fedora"},
    {"image": "fedora", "tag": "33", "Dockerfile": "Dockerfile_fedora"},
    {"image": "fedora", "tag": "32", "Dockerfile": "Dockerfile_fedora"},
    {"image": "fedora", "tag": "31", "Dockerfile": "Dockerfile_fedora"},
    {"image": "fedora", "tag": "30", "Dockerfile": "Dockerfile_fedora"},
    {"image": "fedora", "tag": "29", "Dockerfile": "Dockerfile_fedora"},
    {"image": "debian", "tag": "bullseye-slim", "Dockerfile": "Dockerfile_debian"},
    {"image": "debian", "tag": "buster-slim", "Dockerfile": "Dockerfile_debian"},
    {"image": "debian", "tag": "stretch-slim", "Dockerfile": "Dockerfile_debian"},
    {"image": "debian", "tag": "jessie-slim", "Dockerfile": "Dockerfile_debian"},
    {"image": "ubuntu", "tag": "14.04", "Dockerfile": "Dockerfile_debian"},
    {"image": "ubuntu", "tag": "16.04", "Dockerfile": "Dockerfile_debian"},
    {"image": "ubuntu", "tag": "18.04", "Dockerfile": "Dockerfile_debian"},
    {"image": "ubuntu", "tag": "20.04", "Dockerfile": "Dockerfile_debian"},
    {"image": "alpine", "tag": "3.13", "Dockerfile": "Dockerfile_alpine"},
    {"image": "alpine", "tag": "3.12", "Dockerfile": "Dockerfile_alpine"},
    {"image": "alpine", "tag": "3.11", "Dockerfile": "Dockerfile_alpine"},
    {"image": "alpine", "tag": "3.10", "Dockerfile": "Dockerfile_alpine"},
]
images.reverse()

for image in images:
    commands = "docker build . -t bensuperpc/distcc:" + image['image'] + "_" + image['tag'] + " -f " \
        + image['Dockerfile'] + " --build-arg DOCKER_IMAGE=" + image['image'] + ":" + image['tag']
    subprocess.call(commands, shell=True)
    
exit(0)
with open('data.yaml', 'w') as outfile:
    yaml.dump(images, outfile, default_flow_style=False)

out =  []
with open("data.yaml") as f:
    out = yaml.load(f)