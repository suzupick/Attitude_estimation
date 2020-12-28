import sys
import sckcomm


def main_fn():
    raspi_sck = sckcomm.sckcomm("127.0.0.1", 50007)
    raspi_sck.send_rcv("123")

if __name__ == "__main__":
    try:
        main_fn()
    except KeyboardInterrupt:
        print("Program ended by user.\n")
        sys.exit()