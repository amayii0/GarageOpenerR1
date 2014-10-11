# Original source code taken from
#   Raspberry Pi control from mobile device or desktop web browser 
#   http://electronicsbyexamples.blogspot.be/2014/02/raspberry-pi-control-from-mobile-device.html

from flask import Flask, render_template, request, jsonify
import Pins

app = Flask(__name__)

# Return index page when IP/port address of RPi is typed in the browser
@app.route("/")
def Index():
    return render_template("index.html", uptime=GetUptime())

# Ajax GET call this function to send switch comands
@app.route("/_ToggleSwitch")
def _ToggleSwitch():
    action = request.args.get('action')
    initialDoorState = Pins.ReadDoorState()
    print "Got request to set door to {0} state".format(action)

    # Open action    
    if action=="open":
      if initialDoorState==0:
        print "Door is closed, open it"
        Pins.ShortSwitch()

      if initialDoorState==1:
        print "Door is open, do nothing"

      if initialDoorState==-2:
        print "FIX ME : Door is intermediate, wait ? send command ? what to do ?"
        print "Using fallback to simply send a switch command"
        Pins.ShortSwitch()

    # Close action    
    if (action=="close"):
      if initialDoorState==0:
        print "Door is closed, do nothing"

      if initialDoorState==1:
        print "Door is open, close it"
        Pins.ShortSwitch()

      if initialDoorState==-2:
        print "FIX ME : Door is intermediate, wait ? send command ? what to do ?"
        print "Using fallback to simply send a switch command"
        Pins.ShortSwitch()

    # Close action    
    if (action=="intermediate"):
      print "FIX ME : Intermediate command, what to do ? We don't know if door is moving/stopped and what to send."

    return ""

# ajax GET call this function periodically to read button state
# the state is sent back as json data
@app.route("/_ReadState")
def _ReadState():
    return jsonify(openState=Pins.ReadOpenSwitch(), closedState=Pins.ReadClosedSwitch(), doorState=Pins.ReadDoorState())

# Get the uptime
def GetUptime():
    # get uptime from the linux terminal command
    from subprocess import check_output
    output = check_output(["uptime"])
    # return only uptime info
    uptime = output[output.find("up"):output.find("user")-5]
    return uptime
    
# run the webserver on defined port, requires sudo
# Default port is 80, use whatever else you prefer if 80 is already busy
if __name__ == "__main__":
    Pins.Init()
    app.run(host='0.0.0.0', port=81, debug=True)
