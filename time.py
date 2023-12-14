#time()
#	returns the current time in seconds since the epoch
#	jan 1 1970 at 00:00:00


#ctime()
#	-Converts a timestamp (seconds since the epoch) into a human-readable string representing the local time.
#syntax : time.ctime([seconds])


#gmtime()
#	-These functions convert a timestamp into a struct_time object representing UTC time and local time,respectively.
	#syntax: same as ctime()
#		timestamp ----> struct_object
#		gmtime() :- UTC
#		localtime:- current timezone of system
		


localtime()
sleep()
#	-Suspends the execution of the current thread for specified number of seconds.
#syntax : time.sleep(seconds)
	#default is timestamp

strftime() and strptime()
monotonic()
