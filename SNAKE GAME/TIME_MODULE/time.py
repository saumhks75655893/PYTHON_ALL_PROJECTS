import time as tm
from time import gmtime, strftime

#  Today 
# gmtime : return tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst 

# 1970
# gmtime = tm.gmtime(0)
gtime = tm.gmtime()
print(gtime)

# strptime 
print()
y = tm.strptime("20 apr 20",'%d %b %y')
print(y)

# strftime

# Program To show How can we use different derivatives
# Multiple at a time and single at a time


# importing the srtftime() and gmtime()
# if not used the gm time, time changes
# to the local time

# using simple format of showing time
s = strftime("%a, %d %b %Y %H:%M:%S + 1010", gmtime())
print("Example 1:", s)

print()

# only change in this is the full names
# and the representation
s = strftime("%A, %D %B %Y %H:%M:%S + 0000", gmtime())
print("Example 2:", s)

print()

# this will show you the preferred date time format
s = strftime("%c")
print("Example 3:", s)

print()

# this will tell about the centuries
s = strftime("%C")
print("Example 4:", s)

print()

# MOTY: month of the year
# DOTY: Day of the year
# Simple representation
# % n - new line
# s = strftime("%A, %D %B %Y, %r, %nMOTY:%m %nDOTY:% j")
# print("Example 5:", s)

print()

# % R - time in 24 hour notation
s = strftime(" %R ")
print("Example 6:", s)

print()

# % H - hour, using a 24-hour clock (00 to 23) in Example 1, 2, 3
# % I - hour, using a 12-hour clock (01 to 12)
s = strftime("%a, %d %b %Y %I:%M:%S + 0000", gmtime())
print("Example 7:", s)

print()

# % T - current time, equal to % H:% M:% S
s = strftime("%r, %T ", gmtime())
print("Example 8:", s)

print()

# % u an % U use (see difference)
s = strftime("%r, %u, %U")
print("Example 9:", s)

print()

# use of % V, % W, % w
s = strftime("%r, %V, %W, %w")
print("Example 10:", s)

print()

# use of % x, % X, % y, % Y
s = strftime("%x, %X, %y, %Y")
print("Example 11:", s)

print()

# use of % Z, % z
s = strftime("%r, %z, %Z")
print("Example 12:", s)
