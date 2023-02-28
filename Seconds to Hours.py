seconds = input("give me seconds, I'll tell you how many hours, minutes, and seconds it is: ")
seconds = int(seconds)
hours = seconds//(60*60)
remainder = seconds%(60*60)
minutes = remainder//60
units = seconds%60

print(seconds, "seconds is", hours, "hours", minutes, "minutes", units, "seconds")
