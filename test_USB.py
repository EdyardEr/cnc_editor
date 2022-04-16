import usb.core
import usb.util
import array

dev = usb.core.find(find_all=False)
if dev is None:
    raise ValueError('Device not found')

print(dev)