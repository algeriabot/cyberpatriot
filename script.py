# Ubuntu CP Script
# Gabe Tao
import os

commands = {
  "run prelim updates": ["apt-get update -y"],
  
  "install dependencies": ["apt-get install -y wget curl"],
  
  "run Conduro security script": ["wget -O ./conduro.sh https://raw.githubusercontent.com/t-ebag/ubuntu/main/install.sh",
                                  "chmod +x ./conduro.sh",
                                  "./conduro.sh"],
  
  "check for bad apt sources": ["micro /etc/apt/sources.list"],
  
  "install password checking module": ["apt-get install libpam-pwquality"],
  
  "install micro text editor": ["curl https://getmic.ro | bash", "mv ./micro /bin/micro"],
  
  "install bat": ["apt-get install bat"],
  
  "install gufw": ["apt-get install gufw"],
  
  "install bum": ["apt-get install bum"],
  
  "install auditing program": ["apt-get install auditd"],
  
  "install antivirus": ["apt-get install clamtk"],
  
  "install htop": ["apt-get install htop"],
  
  "enable audits": ["auditctl -e 1"],
  
  "enable ufw firewall": ["ufw enable",
                         "ufw allow ssh/tcp",
                         "ufw logging on",
                         "ufw logging high",
                         "ufw status verbose"],
  
  "search for media files": ["find /home -iregex '.*\.\(mp3\|mp4\|m4a\|mov\|aac\|ogg\|webm\|flac\|jpg\|gif\|png\|jpeg\|tiff\)$'"],
  
  "remove ftp": ["apt-get remove --purge ftp ftpd vsftpd pure-ftpd"],
  
  "remove samba": ["apt-get remove --purge samba samba-common smbclient"],
  
  "remove avahi": ["apt-get remove --purge avahi-daemon"],
  
  "remove apache(2)": ["apt-get remove --purge apache apache2"],
  
  "list contents of rc.local": ["cat /etc/rc.local"],
  
  "lock root user locally": ["passwd -l root"], 
  
  "make sure there are no uid 0 besides root": ["cat /etc/passwd | grep :0:"],
  
  "display groups": ["cat /etc/group | less"],
  
  "check for shellshock vulnerability": ["env 'VAR=() { :;}; echo Bash is vulnerable!' 'FUNCTION()=() { :;}; echo Bash is vulnerable!' bash -c 'echo Bash is safe if this is the only line displayed.'"],
  
  "search top for bad processes": ["top",
                                   "ps -aux | less",
                                   "ps -aux | grep python | less"],
  
  "check for rootkits": ["apt-get install -y chrootkit",
                         "chrootkit -q"],
  
  "enable snap": ["systemctl unmask snapd", "systemctl start snapd"],
  
  "list snap packages": ["snap list"],
  
  "configure sensitive file permissions (first, open a terminal and check who owns these: \n/etc/shadow\n/etc/gshadow\n": ["chown root:root /etc/passwd",
                                           "chmod u-x,go-wx /etc/passwd",
                                           "chown root:root /etc/group",
                                           "chmod u-x,go-wx /etc/group",
                                           "chown root:shadow /etc/shadow",
                                           "chmod u-x,g-wx,o-rwx /etc/shadow",
                                           "chown root:shadow /etc/gshadow",
                                           "chmod u-x,g-wx,o-rwx /etc/gshadow"],
  
  "list user home directories (make sure everyone owns their own)": ["ls -lah /home/"],
  
  "print PATH": ['echo "$PATH" | tr ":" "\n" | nl'],
                                                
  "set up aliases": ["echo >> .bashrc",
                     "echo \"alias canhas='sudo apt-get install -y'\" >> .bashrc",
                     "echo \"alias kthxbye='sudo apt-get remove --purge'\" >> .bashrc",
                     "echo \"alias c='clear'\" >> .bashrc",
                     "echo \"alias edit='micro'\" >> .bashrc",
                     "echo \"alias nano='micro'\" >> .bashrc",
                     "echo \"alias sudo='sudo '\" >> .bashrc",
                     "echo \"alias cat='batcat'\" >> .bashrc",
                     "echo \"alias top='htop'\" >> .bashrc",
                     "source ~/.bashrc"],
  "apt-get cleanup stuff": ["apt-get autoremove", "apt-get autoclean"]
  
}

for count, c in enumerate(commands):
  
  print(f"\033[92m ========== TASK #{count+1} ========== \033[00m")
  print()
  print(f"\033[96m        This task will {c} and will run the command(s): \033[00m")
  for i in commands[c]:
    print("        sudo " + i)
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
  
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Time to do user password changes")
print("Type the names of the users, NOT INCLUDING YOURSELF, and type stop to stop:")
username_password_list = []
while True:
  username = input("username:")
  if username != "stop":
    username_password_list.append(f"{username}:CyberPatriot!123\n")
    print(f"    added {username}:CyberPatriot!123 successfully")
  else:
    break

bulkpasswords = open("bulkpasswords", "w")
bulkpasswords.writelines(username_password_list)
bulkpasswords.close()
print("Done")

input("Check over file 'bulkpasswords'....")

print("Running command 'chpassword < bulkpasswords'...")
os.system("sudo chpassword < bulkpasswords")
print("done")

            
    
