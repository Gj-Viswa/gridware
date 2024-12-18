import socket
import struct
import pickle
import json
from time import sleep
import urllib.request
import os
# Set up the UDP socket to receive data
UDP_IP = "127.0.0.1"  # Local IP address
UDP_PORT = 5005  # The port on which to listen for incoming data
UDP_PORT1 = 5006
UDP_PORT2 = 5007
# Create the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.bind((UDP_IP, UDP_PORT1))
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind((UDP_IP, UDP_PORT2))
print(f"Listening on {UDP_IP}:{UDP_PORT}")
h=0
hi=0
vi=0

data, addr = sock.recvfrom(8192)  # Buffer size of 1024 bytes
data2, addr2 = sock1.recvfrom(8192)
data3, addr3 = sock2.recvfrom(8192)
# Print the raw byte data
#print(f"Received raw byte data: {data} from {addr}")

# Check if the received data length matches the expected length for a double (8 bytes)
if len(data) == 8:  # For a single 64-bit float (8 bytes)
    try:
        # Unpack the byte data as a 64-bit float (double-precision)
        value = struct.unpack('d', data)[0]
        print(f"Decoded value as float: {value}")
    except Exception as e:
        print(f"Error unpacking data as float: {e}")
elif len(data) == 4:  # For a single 32-bit float (4 bytes)
    try:
        # Unpack the byte data as a 32-bit float
        value = struct.unpack('f', data)[0]
        print(f"Decoded value as float: {value}")
    except Exception as e:
        print(f"Error unpacking data as float: {e}")
elif len(data) == 4:  # For a single 32-bit integer (4 bytes)
    try:
        # Unpack the byte data as an integer
        value = struct.unpack('i', data)[0]
        print(f"Decoded value as integer: {value}")
    except Exception as e:
        print(f"Error unpacking data as integer: {e}")
else:
    print("Unexpected data format or size.")


# Check if the received data length matches the expected length for a double (8 bytes)
if len(data2) == 8:  # For a single 64-bit float (8 bytes)
    try:
        # Unpack the byte data as a 64-bit float (double-precision)
        value2 = struct.unpack('d', data2)[0]
        print(f"Decoded value as float: {value2}")
    except Exception as e:
        print(f"Error unpacking data as float: {e}")
elif len(data2) == 4:  # For a single 32-bit float (4 bytes)
    try:
        # Unpack the byte data as a 32-bit float
        value2 = struct.unpack('f', data2)[0]
        print(f"Decoded value as float: {value2}")
    except Exception as e:
        print(f"Error unpacking data as float: {e}")
elif len(data2) == 4:  # For a single 32-bit integer (4 bytes)
    try:
        # Unpack the byte data as an integer
        value2 = struct.unpack('i', data2)[0]
        print(f"Decoded value as integer: {value2}")
    except Exception as e:
        print(f"Error unpacking data as integer: {e}")
else:
    print("Unexpected data format or size.")



# Check if the received data length matches the expected length for a double (8 bytes)
if len(data3) == 8:  # For a single 64-bit float (8 bytes)
    try:
        # Unpack the byte data as a 64-bit float (double-precision)
        value3 = struct.unpack('d', data3)[0]
        print(f"Decoded value as float: {value3}")
    except Exception as e:
        print(f"Error unpacking data as float: {e}")
elif len(data3) == 4:  # For a single 32-bit float (4 bytes)
    try:
        # Unpack the byte data as a 32-bit float
        value3 = struct.unpack('f', data3)[0]
        print(f"Decoded value as float: {value3}")
    except Exception as e:
        print(f"Error unpacking data as float: {e}")
elif len(data3) == 4:  # For a single 32-bit integer (4 bytes)
    try:
        # Unpack the byte data as an integer
        value3 = struct.unpack('i', data3)[0]
        print(f"Decoded value as integer: {value3}")
    except Exception as e:
        print(f"Error unpacking data as integer: {e}")
else:
    print("Unexpected data format or size.")

filename = 'svm.sav'
loaded_model = pickle.load(open(filename, 'rb'))
print(value)
person_reports = [[value]]
predicted = loaded_model.predict(person_reports)
print(predicted)


if int(predicted)==1:
    print("NORMAL")
    hi=hi+1
    if True:
        hi=0
        x = "https://api.thingspeak.com/update?api_key=0P6P2OTY1S0528W5&field1="+str(value)+"&field2="+str(value2)+"&field3="+str(value3)
        conn = urllib.request.urlopen(x)
        response = conn.read()
        conn = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=16I4KHP9BXOUK1I7&field1=Normal"),
    
else:
    h=h+1
    if True:
        h=0
        print("FAULT")
        x = "https://api.thingspeak.com/update?api_key=0P6P2OTY1S0528W5&field1="+str(value)+"&field2="+str(value2)+"&field3="+str(value3)
        conn = urllib.request.urlopen(x)
        response = conn.read()
        conn = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=16I4KHP9BXOUK1I7&field1=Theft"),


        
    
