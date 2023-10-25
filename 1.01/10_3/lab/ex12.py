# Exercise 1.2. Write Python code to evaluate these expressions.
# The answers can be stored in a name, or evaluated in a print statement

# 1. How many seconds are there in 42 minutes 42 seconds?

print(42*60+42)

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61
# kilometers in a mile.

#this answer uses variables 
kilometers = 10
miles = kilometers/1.61
print(miles)

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your
# average pace (time per mile in minutes and seconds)? What is your average
# speed in miles per hour?

#long way of doing this
miles = 6.21
secpermiles = 2562/miles

pacespm = secpermiles
print(pacespm)

pacempm = secpermiles/60 
print(pacempm)

pacehpm = pacempm/60
print(pacehpm)

#print("Our average pace is"+str(pace_in_minutes))

x=(((10+5)%2)*25)
print(str(x))