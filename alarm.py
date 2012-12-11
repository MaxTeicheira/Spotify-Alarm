#!/usr/bin/python

from os import popen
from re import search, match

PREVIOUS_ALARMS = './PrevAlarm.hist'


def alarm_set():
  popen("/usr/local/sbin/sleepwatcher -w ./wakePlay.sh")

def reset_alarms():
  popen("sudo pmset repeat cancel")

def wake_time_set(time):
  reset_alarms()
  popen("sudo pmset repeat wakeorpoweron MTWRFSU " + time['comp'])
  recent_history_write(time['pretty'])
  alarm_set()
  return True

def input_handler():
  Input = raw_input("Please input a time(ex. 9:00, 4:00pm, 7:30am): ")
  if match("^[0-9]{1-2}$", Input) != None:
    Input = recent_history_read(Input)
  time = format(Input)
  if time == None:
    return False
  print "Is this correct: " + time["pretty"], time['comp']
  if raw_input("Y(es) or N(o)")[0].lower() == 'y':
    return wake_time_set(time)
  return False 

def inputTkinter(time_string):
  time_formatted = format(time_string)
  if time_formatted == None:
    return False
  else:
    print "Setting wakeup time"
    return wake_time_set(time_formatted)


def format(time):#Currently Best
  time24hr = "[0-2]{0,1}[0-9]:[0-6][0-9]$"
  time12hr = "[0-1]{0,1}[0-9]:[0-6][0-9](a|A|p|P)(m|M)"
  hr24, hr12 = {}, {}
  if search(time24hr, time) != None: #user input is in form of 24hr
    print '24 hour'
    hr24 = {'hour':time.split(':')[0], 'minute':time.split(':')[1]}
    hr12['AmPm'] = 'am' if int(hr24['hour']) < 12 else 'pm'
    hr12['minute'] = hr24['minute']
    if hr24['hour'] == '0': hr12['hour'] = '12'
    hr12['hour'] = str(int(hr24['hour']) - 12) if int(hr24['hour']) > 12 else hr24['hour']
  elif search(time12hr, time) != None: #user input is in form of 12hr
    print '12 hour'
    hr12 = {'hour':time.split(':')[0], 'minute':time.split(':')[1]}
    hr12['AmPm'] = hr12['minute'][-2:].lower()
    hr12['minute'] = hr12['minute'][:-2]
    hr24['minute'] = hr12['minute']
    hr24['hour'] = hr12['hour'] if hr12['AmPm'] == 'am' and hr12['hour'] != '12' else '0'
    hr24['hour'] = str(int(hr12['hour']) - 12) if hr12['AmPm'] == 'am' and hr12['hour'] != '12' else '12'
    hr24['hour'] = hr24['hour'] if match('[0-2][0-9]', hr24['hour']) != None else '0' + hr24['hour']
  else:
    print 'Incorrect format'
    return None
  hr24string = hr24['hour'] + ':' + hr24['minute'] + ':00'
  hr12string = hr12['hour'] + ':' + hr12['minute'] + hr12['AmPm']
  return {'comp':hr24string, 'pretty':hr12string}


def menu():
  print"""
#########################################################################
#                    Welcome to the Spotify Alarm Clock                 #
#   Usage:                                                              #
#       1. Leave Spotify at the beginning of the desired wakeup song.   #
#       2. Input desired wakeup time.                                   #
#                                                                       #
#  Note: The Spotify Alarm Clock requires the laptop's lid to be open.  #
#                                                                       #
#########################################################################
 
"""
  count = 0
  for line in recent_history_read('all'):
    print '('+str(count)+') ' + line


def recent_history_write(time):
  f = open(PREVIOUS_ALARMS, 'w')
  f.write(time)
  f.close()

def recent_history_read(index):
  f = open(PREVIOUS_ALARMS, 'r')
  hist = f.read().split('\n')
  f.close()
  if index == 'all': return hist
  if index < len(hist):
    return hist[index]
  return False


if __name__ == "__main__":
  while True:
    menu()
    if input_handler():
      break
  alarm_set()
