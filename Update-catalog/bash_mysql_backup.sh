#!bin/sh
#####################################
### Backup script - run_backup.sh  ##
#####################################
### Desc: Runs backup on MYSQL     ##
### database and then emails to    ##
### confirm                        ##
#####################################
# Empty folder by deleting everithing in that folder

find /data/SQL -type f -mtime +1 -delete;

# Settings
MY_USER="user"
MY_PWORD="12345"
MY_DATABASE="database"

# Email To ?
EMAIL="example@example.com"

# Get hostname
HOST="$(hostname)"

# Get date
NOW="$(date +"%Y-%m-%d")"
###################################

# Do backup
cd /data/SQL

mysqldump -u$MY_USER -p$MY_PWORD $MY_DATABASE > $NOW.sql

tar -zcvf "backup"_$NOW.tgz *.sql

rm *.sql
###################################

# Build and send email
# email subject
SUBJECT="Database backup - "$NOW

# Email text/message
EMAILMESSAGE="/tmp/emailmessage.txt"
echo "CRON JOB has backed up database: "$MY_DATABASE" by User: Tina Backup on Server: "$HOST >$EMAILMESSAGE
echo " ">> $EMAILMESSAGE
echo "This was completed on date: "$NOW>> $EMAILMESSAGE
echo " ">> $EMAILMESSAGE
echo "Webmaster.">> $EMAILMESSAGE
# send an email using /bin/mail
/bin/mail -s "$SUBJECT" "$EMAIL" < $EMAILMESSAGE

#remove the temp file
rm $EMAILMESSAGE
