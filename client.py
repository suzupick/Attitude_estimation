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

from RaspberryPi.LSM303D import get_euler_angles
import socket

CRLF = "\r\n"

def request_attitude():
    ip_adr = "127.0.0.1"
    port = 50007
    message = "attitude"

    try:
        # AF_INET: IPv4, SOCK_STREAM: TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_adr, port)) # サーバを指定
        message = message.encode()
        s.sendall(message) # サーバにメッセージを送る
        print("send: ", repr(message))
        data = s.recv(1024) # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        euler_angles = data.decode().split(CRLF)
        print("receive: ", euler_angles)
    except:
        raise
    finally:
        s.close()
    
    return euler_angles


if __name__ == "__main__":
    request_attitude()