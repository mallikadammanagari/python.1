import os
import datetime
os.chdir('.\\mocktest_1')
print(os.getcwd())
info=os.stat('ex.py')
atime=info.st_atime
mtime=info.st_mtime
print(datetime.datetime.fromtimestamp(atime).ctime())
print(datetime.datetime.fromtimestamp(mtime).ctime())

