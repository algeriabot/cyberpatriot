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

  "go and change the update sources! enter to continue": ["nano /etc/apt/sources.list"],

  "fix apt sources list": ["cp /etc/apt/sources.list /etc/apt/sources.list.bak", 
                                 "wget -O /etc/apt/sources.list https://raw.githubusercontent.com/algeriabot/cyberpatriot/refs/heads/main/sources.list"],
                              
  "run prelim updates": ["apt-get update -y"],
  
  "install packages": ["apt-get install -y wget curl libpam-pwquality bat gufw bum auditd clamtk htop"],

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

  "look for even more bad files in /home": ['for s in mp3 txt wav wma aac mp4 mov avi gif jpg png bmp img exe msi bat sh; do sudo find /home -name "*.$s"; done'],
  
  "remove ftp": ["apt-get remove --purge ftp ftpd vsftpd pure-ftpd"],
  
  "remove samba": ["apt-get remove --purge samba samba-common smbclient"],
  
  "remove avahi": ["apt-get remove --purge avahi-daemon"],
  
  "remove apache(2)": ["apt-get remove --purge apache apache2"],
  
  "remove telnet": ["apt-get remove --purge telnet"],
  
  "remove snmp email server": ["service snmp stop", "apt-get remove --purge snmp"],
  
  "remove pop3": ["service pop3 stop", "apt-get remove --purge pop3"],
    
  "list contents of rc.local": ["cat /etc/rc.local"],
  
  "lock root user locally": ["passwd -l root"], 
  
  "make sure there are no uid 0 besides root": ["grep :0: /etc/passwd"],
  
  "make sure there are no users with unset or empty password": ["cat /etc/shadow | awk -F: '($2==""){print $1}'"],
  
  "display groups": ["cat /etc/group | less"],
  
  "check for shellshock vulnerability": ["env 'VAR=() { :;}; echo Bash is vulnerable!' 'FUNCTION()=() { :;}; echo Bash is vulnerable!' bash -c 'echo Bash is safe if this is the only line displayed.'"],
  
  "search top for bad processes": ["htop",
                                   "ps aux | less",
                                   "ps aux | grep python | less"],
  
  "check for rootkits": ["apt-get install -y chkrootkit",
                         "chkrootkit -q"],
  
  "secure shared memory": ["echo 'none  /run/shm  tmpfs rw,noexec,nosuid,nodev	0	0' >> /etc/fstab"],
  
  "check /etc/sudoers for bad stuff": ["visudo", "ls -la /etc/sudoers.d/"],
  
  #"enable snap": ["systemctl unmask snapd", "systemctl start snapd"],
  
  #"list snap packages": ["snap list"],
  
  "configure sensitive file permissions (first, open a terminal and check who owns these: \n/etc/shadow\n/etc/gshadow\n": ["chown root:root /etc/passwd",
                                           "chmod u-x,go-wx /etc/passwd",
                                           "chown root:root /etc/group",
                                           "chmod u-x,go-wx /etc/group",
                                           "chown root:shadow /etc/shadow",
                                           "chmod u-x,g-wx,o-rwx /etc/shadow",
                                           "chown root:shadow /etc/gshadow",
                                           "chmod u-x,g-wx,o-rwx /etc/gshadow"],
  
  "check for files with 777 permissions": ["cd / && ls -laR 2> /dev/null | grep rwxrwxrwx | grep -v 'lrwx'"],
  
  "list user home directories (make sure everyone owns their own)": ["ls -lah /home/"],
  
  "print PATH": ['echo "$PATH" | tr ":" "\n" | nl'],

  "list manually installed software packages": ["comm -23 <(apt-mark showmanual | sort -u) <(gzip -dc /var/log/installer/initial-status.gz | sed -n 's/^Package: //p' | sort -u)"],
                                                
  "set up aliases": ["echo >> .bashrc",
                     "echo \"alias canhas='sudo apt-get install -y'\" >> .bashrc",
                     "echo \"alias kthxbye='sudo apt-get remove --purge'\" >> .bashrc",
                     "echo \"alias c='clear'\" >> .bashrc",
                     "echo \"alias edit='micro'\" >> .bashrc",
                     "echo \"alias nano='micro'\" >> .bashrc",
                     "echo \"alias sudo='sudo '\" >> .bashrc",
                     "echo \"alias cat='batcat'\" >> .bashrc",
                     "echo \"alias top='htop'\" >> .bashrc",
                     "echo \"alias helpme='python3 /usr/bin/helpme.py'\" >> .bashrc",
                     "source ~/.bashrc"]
}


# Section 2: some bad programs to always get rid of
bad_programs = ["zenmap", "nmap", "telnet", "hydra", "john", "nitko", "freeciv", "ophcrack", "kismet", "minetest", "openvpn", "wireshark", "ntalk", "postfix"]

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
      if c == "set up aliases":
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
  
  
# Section 4: Bulk password changes
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Time to do user password changes")
print("Type the names of the users, NOT INCLUDING YOURSELF, and type stop to stop:")
username_password_list = []
while True:
  username = input("username:")
  if username != "stop":
    username_password_list.append(f"{username}:Cyb3rP4triot!@#$%\n")
    print(f"    added {username}:Cyb3rP4triot!@#$% successfully")
  else:
    break

bulkpasswords = open("bulkpasswords", "w")
bulkpasswords.writelines(username_password_list)
bulkpasswords.close()
print("Done")

input("Check over file 'bulkpasswords'....")

print("Running command 'chpasswd < bulkpasswords'...")
os.system("sudo chpasswd < bulkpasswords")
print("done")

            
    
