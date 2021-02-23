from numpy import array
from math import cos, sin, atan2, asin
from arm_controller import ArmController

# get position and roll, pitch, and yaw
# create T table with info
if __name__ == "__main__":
    # get info
    print("All input in radians")
    info = input("[x position, y position, z position, x rotation, y rotation, z rotation]: ")
    x_pos = info[0]
    y_pos = info[1]
    z_pos = info[2]
    roll = info[3]
    pitch = info[4]
    yaw = info[5]

    origin_x_offset = 0.01225
    origin_z_offset = 0.077

    L1 = 0.19567
    L2 = 0.126

    gen_trans_matrix = array([[cos(yaw) * cos(pitch), -sin(yaw) * cos(roll) + cos(yaw) * sin(pitch) * sin(roll), sin(yaw) * sin(roll) + cos(yaw) * sin(pitch) * cos(roll), x_pos],
                              [sin(yaw) * cos(pitch), cos(yaw) * cos(roll) + sin(yaw) * sin(pitch) * sin(roll), -cos(yaw) * sin(roll) + sin(yaw) * sin(pitch) * cos(roll), y_pos],
                              [-sin(pitch), cos(pitch) * sin(roll), cos(pitch) * cos(roll), z_pos],
                              [0, 0, 0, 1]])

    c1 = gen_trans_matrix[1][1]
    s1 = gen_trans_matrix[0][1]

    theta1 = atan2(s1, c1)

    c2 = (gen_trans_matrix[1][3] - (gen_trans_matrix[0][1] * L2 * gen_trans_matrix[2][2])) / L1
    s2 = (origin_z_offset - gen_trans_matrix[2][3] - (L2 * gen_trans_matrix[2][0])) / L1

    theta2 = atan2(s2, c2)

    # c3 = 0
    # s3 = 0

    theta3 = asin(gen_trans_matrix[2][0]) - theta2
    # theta3 = acos(gen_trans_matrix[2][2]) - theta2

    # do forward kinematics to check if the angles are reasonable

    print("Solution joint angles 1:{}, 2:{}, 3:{}".format(theta1, theta2, theta3))
    
    ac = set_joints([theta1, theta2, 0, theta3])
