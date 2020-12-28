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

import sys
import socket
import numpy as np

CRLF = "\r\n"

def main_fn():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 50007)) # IPアドレスとポートを指定
    s.listen(1) # 並列処理数
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
                        euler_angles = np.mat([1.0,2.0,3.0]).T
                        roll = euler_angles[0,0]
                        pitch = euler_angles[1,0]
                        yaw = euler_angles[2,0]

                        message = (str(roll) + CRLF + str(pitch) + CRLF + str(yaw)).encode() # エンコード
                        conn.sendall(message) # send
    except:
        raise
    finally:
        print("server close")
        s.close()


if __name__ == "__main__":
    try:
        main_fn()
    except KeyboardInterrupt:
        print("Program ended by user.\n")
        sys.exit()
    except:
        raise