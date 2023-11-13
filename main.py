import usb.core
import usb.util
import time

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
    if r[5]== 47 and aDown==False:
        aCount+=1
        aDown=True
    if r[5]==15:
        aDown = False
        bDown = False
        
    if aCount != prevAcount:  
        print("a ", aCount)
        prevAcount = aCount
        
    if r[5]== 79 and bDown==False:
        bCount+=1
        bDown = True
        
    if bCount != prevBcount:  
        print("b ", bCount)
        prevBcount = bCount
    
    time.sleep(.01)
    
    
    
# [1]- up and down C
# [2]- left and right C
# 3 - LR analog
# 4 - UD analog
# 5 - dpad(0-7) + a(47) + b(79)  
# 6 - z + L + r + start

