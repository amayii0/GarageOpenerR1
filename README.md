GarageOpenerR1
==============

Raspberry Pi Garage door opener using jQuery Mobile and Flask.
This was created because most samples I found were note able to both monitor door state and send commands to it.
It also uses two switches to monitor open/close states.

This work is based on :
  Raspberry Pi control from mobile device or desktop web browser 
  http://electronicsbyexamples.blogspot.be/2014/02/raspberry-pi-control-from-mobile-device.html
  
It was quite heavily hacked to offer :
- Ability to read states of 2 garage door switches (look after "zinc alloy garage reed switch")
- Ability to send commands to garage motor using a 3V Relay (look after "3v relay optocoupler")

I have a Creative Labs webcam around, I might try to add live streaming to monitor door remotely.
For safety, I don't allow access to the RPi outside of home LAN (use VPN for remote control).
