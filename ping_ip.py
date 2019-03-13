#批量ping IP
#!/bin/python3
import os
import subprocess
#import commands
 
for i in range(1,255):
   ip = "192.168.1."+str(i)
   (status,result) = subprocess.getstatusoutput('ping '+ip+' -c 1')
   print(status)
   if status !=0 :
     print(ip+" down")
   else:
     pass
