import bluetooth
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(("00:16:53:02:B8:D5", 1))
print("connected")
#LSBsize,MSBsize,type,CMD,data (if wordsize = lsb, msb)
#data=bytearray((2,0,0x01,0x9B)) #name
#data=bytearray((2,0,0x01,0x88))#version
data=bytearray((6,0,0x00,0x03,128,1,0,4))

sock.send(bytes(data))
print("sent")
buf=sock.recv(16)
print("received"+str(buf))
print("end")
