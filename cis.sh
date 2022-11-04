#!/bin/bash

"Making directory:"
cd ~
mkdir cis
cd cis

echo "Installing Ansible:"
apt install software-properties-common
apt-add-repository --yes --update ppa:ansible/ansible
apt install ansible

echo "Fetching Playbook into playbook.yml:"
wget https://raw.githubusercontent.com/t-ebag/cyberpatriot/main/playbook.yml

echo "Fetching Tasks into ubuntu2204_cis:"
git clone https://github.com/t-ebag/ubuntu2204_cis

echo "All done! Make sure to check over defaults/main.yml before running." 
echo "Run with:"
echo "ansible-playbook playbook.yml"
echo "\n"
