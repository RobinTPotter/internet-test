#! /bin/sh
{ echo  "Subject: Outages\nFrom: pi3\nContent-Type: text/html; charset=\"utf-8\"\n" && python3 pingtes2t.py ; } | /usr/sbin/ssmtp robin.t.potter@googlemail.com

