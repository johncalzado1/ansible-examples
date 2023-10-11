FROM python:3.10-buster

RUN python3 -m pip install ansible
RUN python3 -m pip install ansible-lint
RUN ansible-galaxy collection install community.docker
RUN ansible-galaxy install one_mind.harbor_ansible_role

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    sshpass

WORKDIR /ansible