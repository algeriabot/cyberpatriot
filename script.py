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
                                   "ps -aux",
                                   "ps -aux | grep python"]  
  
}

for count, c in enumerate(commands):
  print(f"========== Task #{count+1} ==========")
  print(f"This task will {c} and will run the command(s):")
  for i in commands[c]: print("sudo " + i)
  response = input("Proceed? (y/n)")
  if response == "y":
    print()
    for i in commands[c]: os.system("sudo " + i)
    print("========== SUCCESS ==========")
  else:

    print("========== SKIPPED ==========")

  print()
  print()
