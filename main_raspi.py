# explanation: 3Dコンパスの出力から推定した姿勢をsendするラズパイサーバー
# creator：R Suzuki
# date：2020.12.28
# coding: UTF-8
# 
# ソケット通信の基礎
# https://qiita.com/megadreams14/items/32a3eed4661e55419e1c
# 
# ソケット通信　python公式ドキュメント
# https://docs.python.org/ja/3.6/howto/sockets.html

import socket
import LSM303D
import numpy as np

CRLF = "\r\n"

def attitude_server():
    ip_adr = "192.168.0.9"
    port = 50007
    message = ""

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip_adr, port)) # IPアドレスとポートを指定
    s.listen(1) # 並列処理数

    N_ave = 10
    roll = np.empty(N_ave)
    pitch = np.empty(N_ave)
    yaw = np.empty(N_ave)

    try:
        while True:
            conn, addr = s.accept() # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
            with conn:
                while True:
                    data = conn.recv(1024) # データを受け取る
                    if not data:
                        break
                    print('data : {}, addr: {}'.format(data, addr))
                    
                    if data == b'attitude': # attitudeリクエストの場合の処理
                        euler_angles = LSM303D.get_euler_angles()
                        
                        if len(roll) > N_ave:
                            roll.pop(0)
                            pitch.pop(0)
                            yaw.pop(0)

                        roll = np.append(roll, euler_angles[0,0])
                        pitch = np.append(pitch, euler_angles[1,0])
                        yaw = np.append(yaw, euler_angles[2,0])
                        message = (str(roll.mean()) + CRLF + str(pitch.mean()) + CRLF + str(yaw.mean())).encode() # エンコード
                        message = message[::-1] # Unity用にエンディアン変換

                    conn.sendall(message) # send    
    except:
        raise
    finally:
        print("server close")
        s.close()

if __name__ == "__main__":
    attitude_server()