import numpy as np
import math

def Rx(roll):
    cos = math.cos(roll)
    sin = math.sin(roll)
    mat_tmp = np.mat([
        [1, 0, 0],
        [0, cos, -sin],
        [0, sin, cos]
    ])
    return mat_tmp

def Ry(pitch):
    cos = math.cos(pitch)
    sin = math.sin(pitch)
    mat_tmp = np.mat([
        [cos, 0, sin],
        [0, 1, 0],
        [-sin, 0, cos]
    ])
    return mat_tmp

def Rz(yaw):
    cos = math.cos(yaw)
    sin = math.sin(yaw)
    mat_tmp = np.mat([
        [cos, -sin, 0],
        [sin, cos, 0],
        [0, 0, 1]
    ])
    return mat_tmp

def accel2roll(vec_a_car):
    ay = vec_a_car[1]
    az = vec_a_car[2]
    try:
        roll = math.atan(ay / az)
    except:
        if ay > 0:
            roll = math.pi/2
        else:
            roll = - math.pi/2

    return roll

def accel2pitch(vec_a_car):
    ax = vec_a_car[0]
    az = vec_a_car[2]
    try:
        pitch = - math.atan(ax/az)
    except:
        if ax > 0:
            pitch = math.pi/2
        else:
            pitch = - math.pi/2
    return pitch

def magnet2yaw(vec_m_car, roll, pitch):
    vec_m_gnd = Ry(pitch) * Rx(roll) * vec_m_car
    yaw = - math.atan(vec_m_gnd[1] / vec_m_gnd[0])
    return yaw

def get_attitude(vec_a_car, vec_m_car):
    roll = accel2roll(vec_a_car)
    pitch = accel2pitch(vec_a_car)
    yaw = magnet2yaw(vec_m_car, roll, pitch)

    vec_attitude = np.array([roll, pitch, yaw])
    return vec_attitude