# Ubuntu CP Script
# Gabe Tao
import os

commands = {
  "run Conduro security script": ["wget -O ./conduro.sh https://raw.githubusercontent.com/t-ebag/ubuntu/main/install.sh",
                                  "chmod +x ./conduro.sh",
                                  "./conduro.sh"],
  "install password checking module": ["apt-get install libpam-pwquality"],
  "install text editor": ["curl https://getmic.ro | bash", "mv ./micro /bin/micro"],
  "install gufw": ["apt-get install gufw"],
  "install bum": ["apt-get install bum"],
  "install auditing program": ["apt-get install auditd"],
  "install antivirus": ["apt-get install clamtk"],
  "enable audits": ["auditctl -e 1"],
  "enable ufw firewall": ["ufw enable",
                         "ufw allow ssh/tcp",
                         "ufw logging on",
                         "ufw status verbose"],
  "search for media files": ["find /home -iregex '.*\.\(mp3\|mp4\|m4a\|mov\|aac\|ogg\|webm\|flac\|jpg\|gif\|png\|jpeg\|tiff\)$'"],
  "remove ftp": ["apt-get autoremove -y --purge ftp ftpd vsftpd pure-ftpd"],
  "remove samba": ["apt-get autoremove -y --purge samba samba-common smbclient"],
  "remove avahi": ["apt-get autoremove -y --purge avahi-daemon"],
  "list contents of rc.local": ["cat /etc/rc.local | less"],
  "lock root user locally": ["passwd -l root"],
  "display groups": ["cat /etc/group | less"],
  "check for shellshock vulnerability": ["env 'VAR=() { :;}; echo Bash is vulnerable!' 'FUNCTION()=() { :;}; echo Bash is vulnerable!' bash -c 'echo Bash is safe if this is the only line displayed.'"],
  "search top for bad processes": ["top",
                                   "ps -aux | less",
                                   "ps -aux | grep python | less"],
  "check for rootkits": ["apt-get install -y chrootkit",
                         "chrootkit -q"],
  "list snap packages": ["snap list"],
  "configure sensitive file permissions (first, open a terminal and check who owns these: \n/etc/shadow\n/etc/gshadow\n": ["chown root:root /etc/passwd",
                                           "chmod u-x,go-wx /etc/passwd",
                                           "chown root:root /etc/group",
                                           "chmod u-x,go-wx /etc/group",
                                           "chown root:root /etc/shadow",
                                           "chmod u-x,g-wx,o-rwx /etc/shadow",
                                           "chown root:root /etc/gshadow",
                                           "chmod u-x,g-wx,o-rwx /etc/gshadow"],
  "list user home directories (make sure everyone owns their own)": ["ls -lah /home/"]
  
}

for count, c in enumerate(commands):
  print(f"========== Task #{count+1} ==========")
  print(f"This task will {c} and will run the command(s):")
  for i in commands[c]: print("sudo " + i)
  response = input("Proceed? [y/n]: ")
  if response == "y":
    print()
    for i in commands[c]: os.system("sudo " + i)
    print("========== SUCCESS ==========")
  elif response == "stop":
    print("Stopping script.")
    break
  else:

    print("========== SKIPPED ==========")

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

            
    
