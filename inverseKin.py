import numpy as np

print("what would you like your X coordinate to be? ")
xCoord = input()
print("what would you like your Y coordinate to be? ")
yCoord = input()
print("what would you like your Z coordinate to be? ")
zCoord = input()
print("what would you like your roll to be? ")
roll = input()
print("what would you like your pitch to be? ")
pitch = input()
print("what would you like your yaw to be? ")
yaw = input()

l1 = 0.19567
l2 = 0.126

T = [[(np.cos(yaw)*np.cos(roll)), ((-np.sin(yaw)*np.cos(pitch))+(np.cos(yaw)*np.sin(roll)*np.sin(pitch))), ((np.sin(yaw)*np.sin(pitch))+(np.cos(yaw)*np.sin(roll)*np.cos(pitch))), xCoord],
    [(np.sin(yaw)*np.cos(roll)), ((np.cos(yaw)*np.cos(pitch))+(np.sin(yaw)*np.sin(roll)*np.sin(pitch))), ((-np.cos(yaw)*np.sin(pitch))+(np.sin(yaw)*np.sin(roll)*np.cos(pitch))), yCoord],
    [(-np.sin(roll)), (np.cos(roll)*np.sin(pitch)), (np.cos(roll)*np.cos(pitch)), zCoord],
    [0, 0, 0, 1]]

c1 = (xCoord - l2*T[0,0])/l1
s1 = (yCoord - l2*T[1,0])/l1

angle1 = np.arctan2(s1, c1)
angle2 = np.arctan2(T[1,0], T[0,0]) - angle1

print("The angle of joint 1 is " + str(yaw) + ", the angle of joint 2 is " + str(angle1) + ", and the angle of joint 4 is " + str(angle2) + ".")
