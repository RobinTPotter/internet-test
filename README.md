# internet-test
pings google, creates a big log and sends an email

0 */3 * * * cd /home/pi/internet-test && ./pingres.sh
* * * * * cd /home/pi/internet-test && flock -w 5 /tmp/pinglock /home/pi/pingrun.sh

