批量添加用户，先判断用户名是否存在，不存在再进行添加；添加完成后，显示一共添加了几个用户；最后显示当前系统上共有多少个用户。
 
#!/bin/python3
import os
import subprocess
 
count = 0
for i in range(5,10):
  count = count + 1
  list = 'user'+str(i)
 # print(list)
  (status,result) = subprocess.getstatusoutput(
"cat /etc/passwd | awk -F ':' '{print $1}' | grep " +list
)  
 # print(status)
  (status,result) = subprocess.getstatusoutput(
"cat /etc/passwd | awk -F ':' '{print $1}' | grep " +list
)
 # print(status)
  if status !=0:
    print(list+" is not exist")
    os.system('useradd  '+list+'&& echo 123456 | passwd -- stdin '+list)
  else:
    pass
print("共添加了"+str(count)+"个用户")
 
(status,result) = subprocess.getstatusoutput(
"cat /etc/passwd | awk -F ':' '{print $1}' | wc -l")
print("当前系统上共有"+str(result)+"个用户")
