# explanation: ラズパイサーバーからオイラー角を受け取るプログラム
# creator：R Suzuki
# date：2020.12.26
# coding: UTF-8
# 
# ソケット通信の基礎
# https://qiita.com/megadreams14/items/32a3eed4661e55419e1c
# 
# ソケット通信　python公式ドキュメント
# https://docs.python.org/ja/3.6/howto/sockets.html

import socket
import numpy as np

CRLF = "\r\n"

class socket_comm:
    def __init__(self, ip_adr, port):
        self.ip_adr = ip_adr
        self.port = port
    
    def connect(self):
        try:
            # AF_INET: IPv4, SOCK_STREAM: TCP/IP
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.ip_adr, self.port)) # サーバを指定
        except:
            raise
            

    def request_attitude(self, message = "attitude"):
        try:
            self.message = message.encode()
            self.s.sendall(self.message) # サーバにメッセージを送る
            data = self.s.recv(1024) # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
            euler_angles = data.decode().split(CRLF)
            euler_angles = [float(tmp) for tmp in euler_angles]
            return np.array(euler_angles)
        except:
            raise


if __name__ == "__main__":
    RPi_3Dcmps = socket_comm("192.168.0.6", 50007)
    RPi_3Dcmps.connect()
    euler_angles = RPi_3Dcmps.request_attitude()
    print(euler_angles)

