# Project Title 项目名称

> It can auto back up files into an AWS VOLUME

## Getting Started
> ec2-backup-v2 file_name

### Prerequisites

```
AWS_CLI
aws credentials
```

### Installation


```sh
git clone https://github.com/zlaomin/Auto_backup_for_aws.git
make install
```

### NOTE

>This script must run on a instance that has aws credentials.  

>The Result of aws command can be JSON, use JSON rather than stander formate to process it.


>Beware that the output of command can be nothing. Direct transform it to JSON will be wrong. As for double check it. I maybe using try: except: is a better choice.
When editing security groups, take care of the fact that there is not only OutBound but also Inbound.


>Add -o StrictHostKeyChecking=no in "ssh ...." In script. DO NOT FORGET IT AGAIN

>Use eval `ssh-agent -s` before ssh-add !!!

>Use "group_name = ''.join(random.sample(string.ascii_letters + string.digits, 8))" to get random name so it will not be conflict.
The command for Makefile is make install
The sector before d is read only. And dmesg command is very useful in FreeBDS.
## Authors

* **Yuchen Zeng** - *Initial work*

