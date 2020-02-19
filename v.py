import sys
import subprocess
import os
import json
import math
import time
import random
import string
# import the environment variable
env_dist = os.environ
if "EC2_BACKUP_FLAGS_SSH" in env_dist.keys():
    sshk =" -i "+env_dist['EC2_BACKUP_FLAGS_SSH']
else:
    sshk =""
if "EC2_BACKUP_FLAGS_AWS" in env_dist.keys():
    instance = env_dist['EC2_BACKUP_FLAGS_AWS']
else:
    instance =""
if "EC2_BACKUP_VERBOSE" in env_dist.keys():
    verbose = env_dist['EC2_BACKUP_FLAGS_AWS']
else:
    verbose = None
def excute(command):
    # with return valeu
    output = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True).communicate()
    output=output[0]
    try:
        output=output.decode(encoding="utf-8")
        return json.loads(output)
    except:
        return
sshk=""
group_name = ''.join(random.sample(string.ascii_letters + string.digits, 8))
command= "aws ec2 create-security-group --group-name %s --description \"My security group\""%group_name
gid = excute(command)['GroupId']
command = "aws ec2 authorize-security-group-ingress --group-id "+gid+" --protocol tcp --port 22 --cidr 0.0.0.0/0"
excute(command)
dir = sys.argv[2]
vid = sys.argv[1]
if vid =='null':
    vid =None
if dir == 'null':
    dir = os.getcwd()
if vid == None:
    command ="du -sm %s"%dir
    output = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True).communicate()
    num = output[0].split()
    num = str(math.ceil(int(num[0])/(1024*1024)*2))
    command ="aws ec2 create-volume --size %s --region us-east-1 --availability-zone us-east-1a --volume-type gp2"%num
    dic = excute(command)
    vid = dic['VolumeId']
command = "aws ec2 run-instances --key-name ec2-backup --image-id ami-569ed93c %s --count 1 --security-group-ids %s"%(instance,gid)
dic = excute(command)
iid= dic['Instances'][0]['InstanceId']
command ="aws ec2 describe-instances --instance-id "+iid
if verbose !=None:
    print("waiting for boot")
time.sleep(60)#sleep for boot
dic= excute(command)
iurl = dic['Reservations'][0]['Instances'][0]['PublicDnsName']
command = "aws ec2 attach-volume --volume-id %s --instance-id %s --device /dev/sdf"%(vid,iid)
if verbose !=None:
    print("waiting for attaching")
excute(command)
time.sleep(80)
command ="tar cf - %s |ssh -o stricthostkeychecking=no %s root@%s \"dd of=/dev/xbd2d\""%(dir,sshk,iurl)
if verbose !=None:
    print("writing")
excute(command)
command = "aws ec2 terminate-instances --instance-ids "+iid
subprocess.Popen(command,stdout=subprocess.PIPE,shell=True).communicate()
print(vid)
if verbose !=None:
    print("waiting for terminate-instances and delete-security-group")
time.sleep(50)
command="aws ec2 delete-security-group --group-id "+gid;
excute(command)