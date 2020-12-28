# explanation: ソケット通信用のパッケージ
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
        print("receive: ", data.decode().split(CRLF))
    except:
        raise
    finally:
        s.close()
    
    return data

def attitude_server():
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
                        x = 12.13523452345
                        y = -235342.2342345
                        z = 29384.2452345
                        message = (str(x)+CRLF+str(y)+CRLF+str(z)).encode()
                        conn.sendall(message)
    except:
        raise
    finally:
        print("server close")
        s.close()

if __name__ == "__main__":
    request_attitude()
    # attitude_server()