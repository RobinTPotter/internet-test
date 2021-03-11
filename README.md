# internet-test
pings google, creates a big log and sends an email

# results every 3 hours
```0 */3 * * * cd /home/pi/internet-test && ./pingres.sh```

# run the ping test unless locked (already running)
```* * * * * cd /home/pi/internet-test && flock -w 5 /tmp/pinglock /home/pi/internet-test/pingrun.sh```

# logrotate
```0 0 * * 0 cd /home/pi/internet-test && sudo logrotate pinglogrot.conf```

# Also server:

install gunicorn for python3 (```sudo apt-get install gunicorn3```)

```gunicorn3 --bind=0.0.0.0 pingflask:app```
