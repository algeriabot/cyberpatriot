# Ubuntu CP Script
# Gabe Tao
import os
commands = {
  "run Conduro security script": ["wget -O ./conduro.sh https://raw.githubusercontent.com/t-ebag/ubuntu/main/install.sh",
                                  "chmod +x ./conduro.sh",
                                  "./conduro.sh"],
  "install password checking module": ["apt-get install libpam-pwquality"],
  "install gufw": ["apt-get install gufw"],
  "install bum": ["apt-get install bum"],
  "install auditing program": ["apt-get install auditd"],
  "enable audits": ["auditctl -e 1"],
  "enable ufw firewall": ["ufw enable",
                         "ufw allow ssh/tcp",
                         "ufw logging on",
                         "ufw status"],
  "search for media files": ["find /home -iregex '.*\.\(mp3\|mp4\|m4a\|mov\|aac\|ogg\|webm\|flac\|jpg\|gif\|png\|jpeg\|tiff\)$'"],
  "remove ftp": ["apt-get autoremove -y --purge ftp ftpd vsftpd pure-ftpd"],
  "remove samba": ["apt-get -y autoremove --purge samba samba-common smbclient"],
  "list contents of rc.local": ["cat /etc/rc.local"],
  "lock root user locally": ["passwd -l root"]
  
}

for count, c in enumerate(commands):
  print(f"========== Task #{count+1} ==========")
  print(f"This task will {c} and will run the command(s):")
  for i in commands[c]: print(i)
  response = input("Proceed? (y/n)")
  if response == "y":
    print()
    for i in commands[c]: os.system("sudo " + i)
    print("========== SUCCESS ==========")
  else:

    print("========== SKIPPED ==========")

  print()
  print()
