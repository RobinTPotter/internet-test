# internet-test

pings google, creates a big log and sends an email

# email setup for googlemail

sing ssmtp as the email client (check pingres.sh) and need to set up gmail as the mail exchange.
visit google and create a new app to access gmail and create a accesskey.
edit ```/etc/ssmtp/ssmtp.conf``` and add to bottom:

```
root=postmaster
mailhub=smtp.gmail.com:465
FromLineOverride=YES
AuthUser={gmail mail address}
AuthPass={not the password but the access key you created}
UseTLS=YES
```

# Crontab's
```
0 */3 * * * cd /home/pi/internet-test && ./pingres.sh
* * * * * cd /home/pi/internet-test && flock -w 5 /tmp/pinglock /home/pi/pingrun.sh
```

# result

[result]: im.jpg "result"
