while getopts "v:h" opt; do
  case $opt in
    v)
      if [  "$3" = ""  ]
      then
         python3.7 v.py $2 null
         exit 0
      fi
      python3.7 v.py $2 $3
      exit 0
      ;;
    h)
      echo "This is the script for backup. It is based on AWS."
      echo "It might take a while due to AWS instance need time to boot"
      echo "-h for help"
      echo "-v to encforce the volume you want to store your data"
      echo "You can also set environment variable such as EC2_BACKUP_VERBOSE for adjust output"
      echo "EC2_BACKUP_FLAGS_SSH can set adjust ssh and EC2_BACKUP_FLAGS_AWS to change for AWS"
      exit 0
      ;;
    ?)
      echo "Invalid option: -$OPTARG"
      exit 2
      ;;
  esac
done
if [  "$2" = ""  ]
then
  if [ "$1" = "" ]
    then
      python3.7 v.py null null
      exit 0
  else
   python3.7 v.py null $1
   exit 0
  fi
fi
python3.7 v.py $1 $2
exit 0