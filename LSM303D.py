# python用lsm303dライブラリのページ
# https://github.com/pimoroni/lsm303d-python
# 
# 下記ページに従ってモジュールを書き換える必要がある？？？
# https://tomosoft.jp/design/?p=41203

import numpy as np
import calc_attitude
from lsm303d import LSM303D

lsm = LSM303D(0x1d)  # Change to 0x1e if you have soldered the address jumper

def get_vec_acc():
    return np.mat(lsm.accelerometer()).T

def get_vec_mag():
    return np.mat(lsm.magnetometer()).T

def get_euler_angles():
    return calc_attitude.calc_attitude(get_vec_acc(), get_vec_mag())