import numpy as np

# CRLF = "\r\n"

# # x = "{:+010.5f}".format(123.456)
# # y = "{:03.5f}".format(123.456)
# # z = "{:03.5f}".format(123.456)
# # print(x)

# x = 12.13523452345
# y = -235342.2342345
# z = 29384.2452345
# message = (str(x)+CRLF+str(y)+CRLF+str(z)).encode()
# message = message.decode().split(CRLF)
# print(message[0])

xyz = (1.23, 4.56, 7.89)
print(xyz)
print(type(xyz))
print(xyz[0])

xyz_mat = np.mat(xyz).T
print(xyz_mat)