# -*- coding: utf-8 -*-
__author__ = 'S1ndbad'

# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3

def convert_seconds(number):
    result = ''
    sec_per_hour = 3600.0
    hours_left = int(number/sec_per_hour)
    minutes_left = int((number - hours_left*sec_per_hour)/60)
    seconds_left = number - hours_left*int(sec_per_hour) - minutes_left*60
    if hours_left > 1 or hours_left==0:
        result = str(hours_left) + ' hours, '
    else:
        result = str(hours_left) + ' hour, '
    if minutes_left > 1 or minutes_left==0:
        result = result + str(minutes_left) + ' minutes, '
    else:
        result = result + str(minutes_left) + ' minute, '
    if seconds_left > 1 or seconds_left==0:
        result = result + str(seconds_left) + ' seconds '
    else:
        result = result + str(seconds_left) + ' second '
    return result



print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

print convert_seconds(3600)
