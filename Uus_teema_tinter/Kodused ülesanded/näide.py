import sys # for Python version
pv3 = sys.version_info[0] > 2 # True for Python version 3, else 2
if pv3: import tkinter as tk
else: import Tkinter as tk
root = tk.Tk()
import os, time # os makes the os._exit function available
from threading import Timer

root.title("Digital Clock")

holdsecs = 1.0 # interval between time displays, seconds

cw, ch = 250, 250 # canvas width and height in pixels

# Create the Canvas on which the clock will be drawn
canvas = tk.Canvas(root, width=cw, height=ch, borderwidth=0,
  highlightthickness=0, bg='black')

# Create the label on which the digital date and time will be drawn
label = tk.Label(root, width = 20, height = 1, bg = 'light blue') # width in characters

# Draw the clock face and frame ovals
def drawface(canvas, framewh=[]):
  # Define the corners of the frame rectangle and draw the contained oval
  border, framewidth = 20, 20 # pixels
  frame = (border, border, framewh[0] - border, framewh[1] - border)
  canvas.create_oval (frame, fill = 'brown')
  bpf = border + framewidth
  face = (bpf, bpf, frame[2] - framewidth, frame[3] - framewidth)
  canvas.create_oval (face, fill = 'white')

# Display the specified time on the label
def drawlabel(now=''):
  # Reset the label to the current time
  label.config (text = now)

# The event handler for the Event caused by clicking the dismiss button
def ondismiss():
  # Shutdown immediately
  os._exit(0)

# Get the local time from the list returned by the timeinfo function
def process(canvas):
  # Get the current local hour, minute, and second in 12-hour format and
  # redraw the label with the new value
  now = timeinfo()[3]
  drawlabel(now)

# The callback function called when the Timer expires
def run():
  # Loop processing, waiting holdseconds, then starting a new timer
  process(canvas)
  global timer
  timer.cancel()
  timer = Timer (holdsecs, run)
  timer.start()

# Get the local time from the built-in time function and format it for display
def timeinfo():
  # Returns a Tuple with 4 elements: the current local hour (in 12-hour format),
  # minute, and second, and the date and time as formatted text.  See, for example,
  # http://pythoncentral.io/how-to-get-and-format-the-current-time-in-python/
  lt = time.localtime()
  year, month, day = lt[0], lt[1], lt[2]
  hour, minute, second = lt[3], lt[4], lt[5]
  hour12 = hour % 12
  if hour12 == 0: hour12 = 12
  ampm = (' AM', ' PM')[int(hour/12)]
  nowasc = '{0:d}:{1:02d}:{2:02d}'.format(hour12, minute, second) + ampm
  mons = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
    'Nov', 'Dec')
  date = '{0:s} {1:d}, {2:d}'.format(mons[month-1], day, year)
  nowasc = date + ' ' + nowasc
  return (hour12, minute, second, nowasc)

# Create the timer
timer = Timer (holdsecs, run)

# Create the layout
canvas.pack()
label.place (x = cw/2 - 70, y = ch/2 - 8) # note pixels, not characters

# Draw the clock face
drawface (canvas, framewh=(cw, ch))

# Specify that the root window will call the ondismiss handler when the window is dismissed.
# Without this, the application will crash instead of exiting gracefully.
root.protocol('WM_DELETE_WINDOW', ondismiss)

# Start the run loop
run()

root.mainloop()