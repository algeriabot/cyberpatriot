# Ubuntu CP Script
# Gabe Tao
import os
commands = {
  "enable ufw firewall": ["sudo ufw enable",
                         "sudo ufw allow ssh/tcp",
                         "sudo ufw logging on",
                         "sudo ufw status"],
  "search for media files": ["sudo find /home -iregex '.*\.\(mp3\|mp4\|m4a\|mov\|aac\|ogg\|webm\|flac\|jpg\|gif\|png\|jpeg\|tiff\)$'"],
  "remove ftp": ["sudo apt-get remove -y ftp ftpd vsftpd pure-ftpd",
                "sudo apt-get remove -y --purge ftp ftpd vsftpd pure-ftpd"]
}

for count, c in enumerate(commands):
  print(f"========== Task #{count+1} ==========")
  print(f"This task will {c} and will run the command(s):")
  for i in commands[c]: print(i)
  response = input("Proceed? (y/n)")
  if response == "y":
    print()
    for i in commands[c]: os.system(i)
    print("========== SUCCESS ==========")
  else:

    print("========== SKIPPED ==========")

  print()
  print()
