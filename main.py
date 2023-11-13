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
aCount = 0
bCount = 0
aDown = False
bDown = False
prevAcount = -1
prevBcount = -1
while True:
    r=ctlr.read(eaddr, 32, 32)
    print(r)
    if r[5]== 47 and aDown==False:
        aCount+=1
        aDown=True
        print(f"A #{aCount} pressed at {time.time()- start_time}")
    if r[5]==15:
        aDown = False
        bDown = False
        
    if aCount != prevAcount:  
        prevAcount = aCount
        
    if r[5]== 79 and bDown==False:
        bCount+=1
        bDown = True
        
    if bCount != prevBcount:  
        prevBcount = bCount
        
    if r[6] == 32:
        break
    
    time.sleep(.01)

print(f"A: {aCount}\nB: {bCount}")
    
# [1]- up(32) and down(224) C
# [2]- left(224) and right(32) C
# 3 - LR analog (0-255)
# 4 - UD analog (0-255)
# 5 - dpad(0-7){+32 when a held, +64 when b held, =96 when both held} + a(47) + b(79)  {111 a and b together}
# 6 - z(16) + L(4) + r(8) + start(32) {numbers add when held together}



# decide a clean way to scale controller before more inputs