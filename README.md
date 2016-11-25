# Python-learning

#This is my first little python project which used to backup important data to data server
import os
import time
source = r'C:\adb*'
target_dir = r'\\192.168.4.11\Share\CentrifyQA_Cloud\Jason.Yang'
tstamp = time.strftime('%Y%m%d%H%M%S')
target = target_dir+'\\'+tstamp+'.zip'
zp_dir = r'C:\7z\7za.exe'
zptuple = zp_dir,'a -tzip',target,source
zpcommand = ' '.join(zptuple)

if os.system(zpcommand) == 0:
  print 'Backup to',target
else:
  print 'Backup failed'
