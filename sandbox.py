CRLF = "\r\n"

# x = "{:+010.5f}".format(123.456)
# y = "{:03.5f}".format(123.456)
# z = "{:03.5f}".format(123.456)
# print(x)

x = 12.13523452345
y = -235342.2342345
z = 29384.2452345
message = (str(x)+CRLF+str(y)+CRLF+str(z)).encode()
message = message.decode().split(CRLF)
print(message[0])