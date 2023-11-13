import usb

ctlr = usb.core.find(idVendor=0x0e8f, idProduct=0x3013)
ep=ctlr[0].interfaces()[0].endpoints()[0]
i=ctlr[0].interfaces()[0].bInterfaceNumber

ctlr.reset()

if ctlr.is_kernel_driver_active(i):
    ctlr.detach_kernel_driver(i)
    
ctlr.set_configuration()
eaddr=ep.bEndpointAddress

while True:
    r=ctlr.read(eaddr, 1024, 1024)
    print(r)