# Ubuntu CP Script
# Gabe Tao
import os
print(f"Currently running in {os.getcwd()}")

# Section 1: Define commands
commands = {
  "install cool new sounds": ["cp /opt/CyberPatriot/gain.wav /opt/CyberPatriot/gain.bak",
                              "cp /opt/CyberPatriot/alarm.wav /opt/CyberPatriot/alarm.bak",
                              "mv ./new_sounds/new-gain.wav /opt/CyberPatriot/gain.wav",
                              "mv ./new_sounds/emotional-damage.wav /opt/CyberPatriot/alarm.wav"],

  "APT sources list (UBUNTU ONLY)": ["cp /etc/apt/sources.list /etc/apt/sources.list.bak", 
                                 "wget -O /etc/apt/sources.list https://raw.githubusercontent.com/algeriabot/cyberpatriot/refs/heads/main/sources.list"],
  "APT sources list (MINT ONLY)": ["cp /etc/apt/sources.list.d/official-package-repositories.list /etc/apt/sources.list.d/official-package-repositories.list.bak",
                                   "wget -O /etc/apt/sources.list.d/official-package-repositories.list https://raw.githubusercontent.com/algeriabot/cyberpatriot/refs/heads/main/official-package-repositories.list"],
                              
  "run prelim updates": ["apt-get update -y"],
  
  "install packages": ["apt-get install -y wget curl libpam-pwquality gufw bat auditd clamtk htop apparmor"],

  "install helpme command into /usr/bin/helpme.py": ["wget -O /usr/bin/helpme.py https://raw.githubusercontent.com/algeriabot/helpme/main/helpme.py",
                             "alias helpme='sudo python3 /usr/bin/helpme.py'"],
  
  "run Conduro security script": ["wget -O ./conduro.sh https://raw.githubusercontent.com/algeriabot/ubuntu/main/install.sh",
                                  "chmod +x ./conduro.sh",
                                  "./conduro.sh"],
    
  "install micro text editor": ["curl https://getmic.ro | bash", "mv ./micro /bin/micro"],
    
  "enable audits": ["auditctl -e 1"],
  
  "enable ufw firewall": ["ufw enable",
                         "ufw allow ssh/tcp",
                         "ufw logging on",
                         "ufw logging high",
                         "ufw status verbose"],
  
  "search for media files in /home": ["find /home -iregex '.*\.\(mp3\|mp4\|mp6\|pdf\|m4a\|mov\|aac\|ogg\|webm\|flac\|jpg\|gif\|png\|jpeg\|tiff\)$'"],

  "look for even more bad files in /home": ["bash -c 'for s in mp3 txt wav wma aac ogg mp4 mov avi gif flac webm pdf tiff jpg jpeg png bmp img exe msi bat sh; do sudo find /home -iname \"*.$s\"; done'"],
  
  "remove ftp": ["apt-get remove --purge ftp* ftpd vsftpd pure-ftpd"],
  
  "remove samba": ["apt-get remove --purge samba* samba-common* smbclient*"],
  
  "remove avahi": ["apt-get remove --purge avahi-daemon*"],
  
  "remove apache(2)": ["apt-get remove --purge apache* apache2"],
  
  "remove telnet": ["apt-get remove --purge telnet*"],
  
  "remove snmp email server": ["service snmp stop", "apt-get remove --purge snmp*"],
  
  "remove pop3": ["service pop3 stop", "apt-get remove --purge pop3*"],

  "remove nginx": ["systemctl stop nginx", "apt-get remove --purge nginx*"],
    
  "list contents of rc.local": ["cat /etc/rc.local"],
  
  "lock root user locally": ["passwd -l root"], 

  #"set root user password for bootloader": ["passwd root"],
  
  "make sure there are no uid 0 besides root": ["grep :0: /etc/passwd"],
  
  "make sure there are no users with unset or empty password": ["awk -F: '($2==\"\"){print $1}' /etc/shadow"],
  
  "display groups": ["cat /etc/group | less"],
  
  "check for shellshock vulnerability": ["env 'VAR=() { :;}; echo Bash is vulnerable!' 'FUNCTION()=() { :;}; echo Bash is vulnerable!' bash -c 'echo Bash is safe if this is the only line displayed.'"],
  
  "search top for bad processes": ["htop",
                                   "ps aux | less",
                                   "ps aux | grep python | less"],
  
  "check for rootkits": ["apt-get install -y chkrootkit", "chkrootkit -q"],
  
  "secure shared memory": ["echo 'none  /run/shm  tmpfs rw,noexec,nosuid,nodev	0	0' >> /etc/fstab"],
  
  #"check /etc/sudoers for bad stuff": ["visudo", "ls -la /etc/sudoers.d/"],

  "remove all files in sudoers.d": ["rm -rf /etc/sudoers.d/*"],
  
  #"enable snap": ["systemctl unmask snapd", "systemctl start snapd"],
  
  #"list snap packages": ["snap list"],
  
  "configure 644 permissions on /etc/[passwd/group/shells/sudoers]": ["chown root:root /etc/passwd",
                                           "chmod 644 /etc/passwd",
                                           "chown root:root /etc/group",
                                           "chmod 644 /etc/group",
                                           "chown root:root /etc/shells",
                                           "chmod 644 /etc/shells",
                                           "chown root:root /etc/sudoers",
                                           "chmod 0644 /etc/sudoers"],
  
  "overwrite and configure 644 on /etc/[motd/issue/issue.net]":
    ["cp /dev/null /etc/motd && chown root:root /etc/motd && chmod 0644 /etc/motd",
     "cp /dev/null /etc/issue && chown root:root /etc/issue && chmod 0644 /etc/issue",
     "cp /dev/null /etc/issue.net && chown root:root /etc/issue.net && chmod 0644 /etc/issue.net"],

  "configure 640 permissions on /etc/[shadow/gshadow/opasswd]": ["chown root:root /etc/shadow",
                                           "chmod 640 /etc/shadow",
                                           "chown root:root /etc/gshadow",
                                           "chmod 640 /etc/gshadow",
                                           "chown root:root /etc/opasswd",
                                           "chmod 640 /etc/opasswd"],
  
  "configure 600 permissions on /boot/grub/grub.cfg": [
    "chmod u-wx,go-rwx /boot/grub/grub.cfg",
    "chown root:root /boot/grub/grub.cfg"],
  
  "check for files with 777 permissions": ["ls -laR / 2> /dev/null | grep rwxrwxrwx | grep -v 'lrwx'"],
  
  "list user home directories (make sure everyone owns their own)": ["ls -lah /home/"],
  
  "print PATH": ['echo "$PATH" | tr ":" "\n" | nl'],

  "list manually installed software packages": ["bash -c \"comm -23 <(apt-mark showmanual | sort -u) <(gzip -dc /var/log/installer/initial-status.gz | sed -n 's/^Package: //p' | sort -u)\""],
}


# Section 2: some bad programs to always get rid of
bad_programs = ["zenmap*", "nmap*", "telnet*", "hydra*", "john*", "freeciv*", "ophcrack*", "minetest*", "openvpn*", "wireshark*", "postfix*", "hexchat*", "bind9*", "aisleriot*", "deluge*", "netcat*", "rpcbind*"]

commands["get rid of always bad programs"] = ["apt-get remove --purge " + " ".join(bad_programs)]
commands["apt-get cleanup stuff"] = ["apt-get autoremove", "apt-get autoclean"]

# Section 3: Execute the commands
for count, c in enumerate(commands):
  
  print(f"\033[92m ========== TASK #{count+1} ========== \033[00m")
  print()
  print(f"\033[96m        Description: {c} Commands: \033[00m")
  for i in commands[c]:
    print("        " + i)
  print()
  response = input("        Proceed? [y/n/s]: ")
  print()
  
  if response == "y":
    
    for i in commands[c]:
      if c == "set up aliases" or c == "list manually installed software packages":
        os.system(i)
      else:
        os.system("sudo " + i)
    print("\033[92m ========== SUCCESS ========== \033[00m")
    
  elif "s" in response:
    
    print("Stopping script.")
    break

    
  else:
    print("\033[91m ========== SKIPPED ========== \033[00m")

  print()
  print()
  
  
# # Section 4: Bulk password changes
# print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
# print("Time to do user password changes")
# print("Type the names of the users, NOT INCLUDING YOURSELF, and type stop to stop:")
# username_password_list = []
# while True:
#   username = input("username:")
#   if username != "stop":
#     username_password_list.append(f"{username}:Cyb3rP4triot!@#$%\n")
#     print(f"    added {username}:Cyb3rP4triot!@#$% successfully")
#   else:
#     break

# bulkpasswords = open("bulkpasswords", "w")
# bulkpasswords.writelines(username_password_list)
# bulkpasswords.close()
# print("Done")

# input("Check over file 'bulkpasswords'....")

# print("Running command 'chpasswd < bulkpasswords'...")
# os.system("sudo chpasswd < bulkpasswords")
# print("done")

            
    
