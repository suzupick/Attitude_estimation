from matplotlib.pyplot import axes
import numpy as np
import math

def map_to_anguler_domain(rad):
    # まず(0,2π)にマップ (剰余計算が負の数に対して使いづらいため)
    if rad < 0 or 2*math.pi < rad:
        rad = rad % (2*math.pi)

    # (-π,π)にマップ
    if math.pi < rad:
        rad = rad - 2*math.pi

    return rad

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

def euler_rotate(roll_input, pitch_input, yaw_input):
    tmp1 = Rx( roll_input )
    tmp2 = Ry( pitch_input )
    tmp3 = Rz( yaw_input )
    return tmp3 * tmp2 * tmp1

def accel2roll(vec_acc):
    ay = vec_acc[1]
    az = vec_acc[2]
    roll = -math.atan(ay / az)

    if ay>0 and az>0 :
        roll += math.pi
    elif ay<0 and az>0:
        roll -= math.pi
    
    # (-π,π)にマップ
    roll = map_to_anguler_domain(roll)
    
    return roll

def accel2pitch(vec_acc):
    ax = vec_acc[0]
    az = vec_acc[2]

    # ピッチを計算
    pitch = + math.atan(ax/az)
    if ax>0 and az>0 :
        pitch -= math.pi
    elif ax<0 and az>0:
        pitch += math.pi
    
    # (-π,π)にマップ
    pitch = map_to_anguler_domain(pitch)
    
    return pitch

def magnet2yaw(vec_acc, vec_mag):
    # ロールとピッチを補正
    roll = accel2roll(vec_acc)
    pitch = accel2pitch(vec_acc)
    vec_mag = Ry(pitch) * Rx(roll) * vec_mag

    mx = vec_mag[0]
    my = vec_mag[1]

    # ヨーを計算
    yaw = math.atan(my/mx)
    if mx<0 and my>0:
        yaw += math.pi
    elif mx<0 and my<0:
        yaw -= math.pi
    
    # (-π,π)にマップ
    yaw = map_to_anguler_domain(yaw)
    return yaw

def get_attitude(vec_acc, vec_mag):
    roll = accel2roll(vec_acc)
    pitch = accel2pitch(vec_acc)
    yaw = magnet2yaw(vec_acc, vec_mag)

    attitude = np.array([roll, pitch, yaw])
    return attitude