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
aDown = False
prevAcount = -1
while True:
    r=ctlr.read(eaddr, 32, 32)
    if r[5]== 47 and aDown==False:
        aCount+=1
        aDown=True
    if r[5]==15 and aDown == True:
        aDown = False
    if aCount != prevAcount:  
        print(aCount)
        prevAcount = aCount
    time.sleep(.01)
    
    
# [1]- up and down C
# [2]- left and right C
# 3 - LR analog
# 4 - UD analog
# 5 - dpad + a + b
# 6 - z + L + r + start

