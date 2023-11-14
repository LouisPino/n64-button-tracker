import usb.core
import usb.util
import time
import datetime
# import pyautogui
import pandas as pd
import matplotlib.pyplot as plt

# Initialize an empty DataFrame
data_list = []
# pyautogui.PAUSE = 0.003

# Assign a numeric value to each button
button_mapping = {'A': 1, 'B': 2, 'Start': 3, "An_L": 4, "An_R": 5, "An_U": 6, "An_D": 7, "R": 8, "L": 9, "Z": 10}


start_time = time.time()
# ctlr = usb.core.find(idVendor=0x0e8f, idProduct=0x3013)
# if ctlr is None:
#     print("No devices found.")
    
# ep=ctlr[0].interfaces()[0].endpoints()[0]
# i=ctlr[0].interfaces()[0].bInterfaceNumber

# ctlr.reset()

# if ctlr.is_kernel_driver_active(i):
#     ctlr.detach_kernel_driver(i)
    
# ctlr.set_configuration()
# eaddr=ep.bEndpointAddress



a_down = False
b_down = False
analog_up_down = False
analog_down_down = False
analog_left_down = False
analog_right_down = False
r_down = False
l_down = False
z_down = False

data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'A'})


# while True:
#     r=ctlr.read(eaddr, 16, 16)
#     if r[5]== 47 and a_down==False:
#         a_down=True
#         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'A'})
#         # pyautogui.press('a')
        
#     if r[5]==15:
#         a_down = False
#         b_down = False

        
#     if r[5]== 79 and b_down==False:
#         b_down = True
#         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'B'})
#         # pyautogui.press('b')

#     if r[4]==0:
#         # analog_up_down = True
#         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'An_U'})
#         # pyautogui.press('up')
        
#     if r[4]==255:
#         # analog_down_down = True
#         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'An_D'})
#         # pyautogui.press('down')
    
#     if r[4] != 255 and r[4] != 0:
#         analog_down_down = False
#         analog_up_down = False

#     if r[3]== 0:
#         # analog_left_down = True
#         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'An_L'})
#         # pyautogui.press('left')
        
#     if r[3]==255:
#         # analog_right_down = True
#         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'An_R'})
#         # pyautogui.press('right')
    
#     # if r[3] != 255 and r[3] != 0:
#     #     analog_left_down = False
#     #     analog_right_down = False
        
#     if r[6] == 0:
#         l_down=False
#         z_down=False
#         r_down=False
        
#     if r[6]==4 and l_down == False:
#         l_down=True
#         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'L'})
#         # pyautogui.press('l')
#     if r[6]==8  and r_down == False:
#         r_down=True
#         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'R'})
#         # pyautogui.press('r')
#     if r[6]==16:
#         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'Z'})
#         # pyautogui.press('z')
        
#     if r[6] == 32:
#         # pyautogui.press('enter')
#         break
    
    # time.sleep(.003)

import socket

# Set the IP address and port
ip = "127.0.0.1"  # Localhost
port = 5006       # Port number

# Create a socket for UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
sock.bind((ip, port))

print(f"Listening for messages on {ip}:{port}")

# Infinite loop to keep the server running
while True:
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received message: {data}")



data= pd.DataFrame(data_list)
data['ButtonValue'] = data['button'].map(button_mapping)

character = "Samus"
opponent = "Pikachu"

colors = {
    1: 'blue',  # A button is blue
    2: 'green', # B button is green
    3: 'red' ,   # Start button is red
    4: 'gray' ,   # Start button is red
    5: 'gray' ,   # Start button is red
    6: 'gray',    # Start button is red
    7: 'gray',    # Start button is red
    8: 'gray',    # Start button is red
    9: 'gray',    # Start button is red
    10: 'gray'    # Start button is red
}
shapes = {
    1: '.',  # A button is blue
    2: '.', # B button is green
    3: '.' ,   # Start button is red
    4: '<' ,   # Start button is red
    5: '>' ,   # Start button is red
    6: '^',    # Start button is red
    7: 'v',    # Start button is red
    8: 's',    # Start button is red
    9: 's',    # Start button is red
    10: 'd'    # Start button is red
}

# Create a scatter plot
for button_value, marker in shapes.items():
    subset_data = data[data['ButtonValue'] == button_value]
    plt.scatter(subset_data['timestamp'], subset_data['ButtonValue'], c=colors[button_value], s=10, marker=marker, label=f'Button {button_value}')


plt.xlabel('Time')
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],["A","B","Start", "An_L", "An_R", "An_U", "An_D", "L", "R", "Z"])
plt.title(f"{character} vs. {opponent} Buttons Pressed")
plt.legend()

csv_file_path= f"./storedgames/{character}/{datetime.datetime.now()}"
data.to_csv(csv_file_path, index=False)
plt.show()
    
# 1 - up(32) and down(224) C
# 2 - left(224) and right(32) C
# 3 - LR analog (0-255)
# 4 - UD analog (0-255)
# 5 - dpad(0-7){+32 when a held, +64 when b held, = 96 when both held} + a(47) + b(79)  {111 a and b together}
# 6 - z(16) + L(4) + r(8) + start(32) {numbers add when held together}


# refactor to get info from max instead of pyusb