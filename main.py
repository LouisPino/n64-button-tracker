import usb.core
import usb.util
import time


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
    r=ctlr.read(eaddr, 32, 32)
    if r[5]== 47 and a_down==False:
        a_count+=1
        a_down=True
        a_times.append(round(time.time()-start_time,2))
    if r[5]==15:
        a_down = False
        b_down = False
        
    if a_count != prev_a_count:  
        prev_a_count = a_count
        
    if r[5]== 79 and b_down==False:
        b_count+=1
        b_down = True
        b_times.append(round(time.time()-start_time, 2))
        
    if b_count != prev_b_count:  
        prev_b_count = b_count
        
    if r[6] == 32:
        break
    
    time.sleep(.01)

print(f"A pressed {a_count} times at {a_times} seconds")
print(f"B pressed {b_count} times at {b_times} seconds")
    
# 1 - up(32) and down(224) C
# 2 - left(224) and right(32) C
# 3 - LR analog (0-255)
# 4 - UD analog (0-255)
# 5 - dpad(0-7){+32 when a held, +64 when b held, = 96 when both held} + a(47) + b(79)  {111 a and b together}
# 6 - z(16) + L(4) + r(8) + start(32) {numbers add when held together}



# decide a clean way to scale controller before more inputs