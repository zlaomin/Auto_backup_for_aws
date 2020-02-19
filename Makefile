all:
	@true
install:
	mkdir -p /usr/local/bin/
	cp ec2-backup-v2.sh /usr/local/bin/ec2-backup
	cp v.py /usr/local/bin 