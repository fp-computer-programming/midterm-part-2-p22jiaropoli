# Author JRI 12/14/21

initial_velocity = int(input("Please enter the initial velocity in meters per second "))
final_velocity = int(input("Please enter the final velocity in meters per second "))
time = int(input("Please enter the time over which the velocity changed in seconds "))

average_acceleration = (final_velocity - initial_velocity) / time

x = "The average acceleration is {0}.".format(average_acceleration)
print(x)