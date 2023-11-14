import usb.core
import usb.util
import time
import datetime
import pyautogui
import pandas as pd
import matplotlib.pyplot as plt

# Initialize an empty DataFrame
data_list = []

# Assign a numeric value to each button
button_mapping = {'A': 1, 'B': 2, 'Start': 3}  # continue for all buttons





start_time = time.time()
ctlr = usb.core.find(idVendor=0x0e8f, idProduct=0x3013)
if ctlr is None:
    print("No devices found.")
    
ep=ctlr[0].interfaces()[0].endpoints()[0]
i=ctlr[0].interfaces()[0].bInterfaceNumber

ctlr.reset()

if ctlr.is_kernel_driver_active(i):
    ctlr.detach_kernel_driver(i)
    
ctlr.set_configuration()
eaddr=ep.bEndpointAddress



a_count = 0
b_count = 0
a_down = False
b_down = False
a_times = []
b_times = []
prev_a_count = -1
prev_b_count = -1


while True:
    r=ctlr.read(eaddr, 16, 16)
    print(r[5])
    if r[5]== 47 and a_down==False:
        a_count+=1
        a_down=True
        data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'A'})
        pyautogui.press('a')
        
    if r[5]==15:
        a_down = False
        b_down = False

        
    if r[5]== 79 and b_down==False:
        b_count+=1
        b_down = True
        data_list.append({'timestamp': round(time.time()-start_time,2), 'button': 'B'})
        pyautogui.press('b')
        
    if b_count != prev_b_count:  
        prev_b_count = b_count

    
        
    if r[6] == 32:
        pyautogui.press('enter')
        break
    
    time.sleep(.01)

data= pd.DataFrame(data_list)
data['ButtonValue'] = data['button'].map(button_mapping)

# Create a scatter plot
plt.scatter(data['timestamp'], data['ButtonValue'])

# Add labels and a legend
plt.xlabel('Time')
plt.ylabel('Button Pressed')
plt.title('N64 Button Presses Over Time')
plt.legend()
# Show the plot


character = "Samus"
csv_file_path= f"./storedgames/{character}/{datetime.datetime.now()}"
data.to_csv(csv_file_path, index=False)
plt.show()
# print(f"A pressed {a_count} times at {a_times} seconds")
# print(f"B pressed {b_count} times at {b_times} seconds")
    
# 1 - up(32) and down(224) C
# 2 - left(224) and right(32) C
# 3 - LR analog (0-255)
# 4 - UD analog (0-255)
# 5 - dpad(0-7){+32 when a held, +64 when b held, = 96 when both held} + a(47) + b(79)  {111 a and b together}
# 6 - z(16) + L(4) + r(8) + start(32) {numbers add when held together}



# decide a clean way to scale controller before more inputs