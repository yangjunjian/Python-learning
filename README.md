# Python-learning
#This is my first little python project
#This is used to backup important data to data server

import os
import time

source = r'C:\adb*'

cdate = time.strftime('%Y%m%d')
ctime = time.strftime('%H%M%S')

target_dir = r'\\192.168.4.11\Share\CentrifyQA_Cloud\Jason.Yang\\'+cdate

if not os.path.exists(target_dir):
  print 'Folder',cdate,'does not exist. Will create one.'
  os.mkdir(target_dir)
  print 'Folder',cdate,'is created!'

name = raw_input('Please input compressed file name: ')

if len(name) == 0:
  print 'Use default name as no name is specified.'
  target = target_dir+os.sep+ctime+'.zip'
else:
  target = target_dir+os.sep+ctime+'_'+name.replace(' ','_')+'.zip'

ziptuple = r'C:\7z\7za.exe','a -tzip',target,source

zipcommand = ' '.join(ziptuple)

if os.system(zipcommand) == 0:
  print 'Successfully back up to',target
else:
  print 'Backup failed'
