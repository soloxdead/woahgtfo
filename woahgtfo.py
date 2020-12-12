import urllib3
import os

# Find SUID programs running on the system
suids = os.popen('find / -perm -u=s -type f 2>/dev/null | awk -F \'/\' {\'print $NF\'}').readlines()

for suid in suids:
    r = urllib3.PoolManager().request('GET', 'https://gtfobins.github.io/gtfobins/{}/'.format(suid.rstrip()))
    if r.status == 404:
        continue
    else:
        print('https://gtfobins.github.io/gtfobins/{}/'.format(suid.rstrip()))