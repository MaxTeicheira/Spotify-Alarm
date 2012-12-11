#! /bin/sh

osascript -e 'tell application "Spotify" to play';
sudo pmset repeat cancel;
/usr/local/sbin/sleepwatcher -w ./nothing.sh;

