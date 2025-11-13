#!/bin/bash
if [ $# -lt 2 ]; then
	echo "Usage: sudo ./auditUsers.sh [users] [admins]"
	echo "where [users] and [admins] are text files"
	echo "containing the lists of allowed users"
	exit 1
fi
if [ "$(whoami)" != "root" ]; then
	echo "Must run as root"
	exit 1
fi 

echo -e "*** AUDITING USERS ***"

declare -a users

while read -r user; do
	echo "auditing user: $user"
	groups=$(id -nG $user)
	#echo "$groups"
	if [[ "$groups" =~ "sudo" ]]; then
		echo "   *** user $user is administrator! fixing"
		deluser $user sudo
		deluser $user admin
		deluser $user wheel 
	fi
	echo "    changing password for user: $user"
	echo "$user:Cyb3rP4triot!@#\$%" | chpasswd
	chage -d 0 $user
	users+=("$user")
done < "$1"


echo -e "\n\n*** AUDITING ADMINS ***"
echo -n "Enter YOUR username: "
read my_name

while read -r adm; do
	if [[ "$adm" == "$my_name" ]]; then
		echo "skipping admin: $adm"
	else
		echo "changing password for admin: $adm"
		echo "$adm:Cyb3rP4triot!@#\$%" | chpasswd
		chage -d 0 $adm
	fi
	users+=("$adm")
done < "$2"


echo -e "\n\n*** CHECKING FOR BAD USERS ***"
compgen -u | while read -r user; do
	if [[ " ${users[@]} " =~ " $user " ]]; then
		echo "    OK $user"
	else
		echo "    *** user $user is not listed, try: sudo userdel -r $user"
	fi
done
