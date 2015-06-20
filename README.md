# blink1-python-hid
A HID wrapper for the blink(1) device. 

Heavily inspired by blink1 pyusb wrapper: https://github.com/todbot/blink1/blob/master/python/alternative_libraries/blink1_pyusb.py

libusb does not allow access to HID devices on OS X (as far as I could google), so I wrote a wrapper that uses HIDAPI to send commands to the blink device. 

This wrapper is dependent on python hidapi: https://pypi.python.org/pypi/hidapi/0.7.99-5
