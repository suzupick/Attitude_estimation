import sys
from socket_comm import sckcomm


def main_fn():
    sckcomm.request_attitude()

if __name__ == "__main__":
    try:
        main_fn()
    except KeyboardInterrupt:
        print("Program ended by user.\n")
        sys.exit()