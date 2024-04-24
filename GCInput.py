import usb.core
import usb.util
import sys
import time
import datetime
import pyautogui
import pandas as pd

btn_map = {
    2: "A",
    4: "B",
    8: "Y",
    1: "X",
    16: "L",
    32: "R",
    128: "Z"
}


ctlr = usb.core.find(idVendor=121, idProduct=6214)
if ctlr is None:
    raise ValueError("Device not found")

# # Detach kernel driver if necessary
if ctlr.is_kernel_driver_active(0):
    ctlr.detach_kernel_driver(0)

# Set configuration
ctlr.set_configuration()

# Endpoint and interface number
endpoint = ctlr[0][(0,0)][0]
interface_number = ctlr[0][(0,0)].bInterfaceNumber

# Claim interface
# usb.util.claim_interface(ctlr, interface_number)

try:
    while True:
        try:
            data = ctlr.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, timeout=1000)
            if data[1] != 0:
                try:
                    print(f"PLAYER: {data[0]}, BTN_VAL: {btn_map[data[1]]}")
                except:
                    print(f"PLAYER: {data[0]}, BTN_VAL: Combination")
                    
        except usb.core.USBError as e:
            if e.args == ('Operation timed out',):
                continue
            raise
finally:
    # This ensures that the interface is released properly
    usb.util.release_interface(ctlr, interface_number)
    if ctlr.is_kernel_driver_active(0):
        ctlr.attach_kernel_driver(0)


# a_down = False
# b_down = False
# analog_up_down = False
# analog_down_down = False
# analog_left_down = False
# analog_right_down = False
# r_down = False
# l_down = False
# z_down = False


# AUTO GUI SHIT

# # while True:
# #     r=ctlr.read(eaddr, 16, 16)
# #     if r[5]== 47 and a_down==False:
# #         a_down=True
# #         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'A'})
# #         # pyautogui.press('a')
        
# #     if r[5]==15:
# #         a_down = False
# #         b_down = False

        
# #     if r[5]== 79 and b_down==False:
# #         b_down = True
# #         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'B'})
# #         # pyautogui.press('b')

# #     if r[4]==0:
# #         # analog_up_down = True
# #         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'An_U'})
# #         # pyautogui.press('up')
        
# #     if r[4]==255:
# #         # analog_down_down = True
# #         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'An_D'})
# #         # pyautogui.press('down')
    
# #     if r[4] != 255 and r[4] != 0:
# #         analog_down_down = False
# #         analog_up_down = False

# #     if r[3]== 0:
# #         # analog_left_down = True
# #         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'An_L'})
# #         # pyautogui.press('left')
        
# #     if r[3]==255:
# #         # analog_right_down = True
# #         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'An_R'})
# #         # pyautogui.press('right')
    
# #     # if r[3] != 255 and r[3] != 0:
# #     #     analog_left_down = False
# #     #     analog_right_down = False
        
# #     if r[6] == 0:
# #         l_down=False
# #         z_down=False
# #         r_down=False
        
# #     if r[6]==4 and l_down == False:
# #         l_down=True
# #         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'L'})
# #         # pyautogui.press('l')
# #     if r[6]==8  and r_down == False:
# #         r_down=True
# #         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'R'})
# #         # pyautogui.press('r')
# #     if r[6]==16:
# #         data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'Z'})
# #         # pyautogui.press('z')
        
# #     if r[6] == 32:
# #         # pyautogui.press('enter')
# #         break
    
#     # time.sleep(.003)



# //////SEND SHIT TO MAX//////////


# import socket

# # Set the IP address and port
# ip = "127.0.0.1"  # Localhost
# port = 5006       # Port number

# # Create a socket for UDP
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# # Bind the socket to the address and port
# sock.bind((ip, port))

# print(f"Listening for messages on {ip}:{port}")

# # Infinite loop to keep the server running
# while True:
#     data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
#     print(f"Received message: {data}")