from tkinter import *
from tkinter.simpledialog import askinteger
import math, time, sys

trace = lambda *args: None  # or print
RunningOnMac = sys.platform.startswith('darwin')  # [SA] Mac port
RunningOnWindows = sys.platform.startswith('win')  # [SA] Win backpot

# [SA] use PIL iff present
pillowwarning = """
Pillow 3rd-party package is not installed.
...This package is optional, but required for the clock images feature when
...using some image file types and Pythons (though not for GIFs with any Python,
...or PNGs with Pythons that use Tk 8.6 or later, including standard Windows 
...installs of Python 3.4+).  Pillow home: https://pypi.python.org/pypi/Pillow.
"""

try:
    from PIL.ImageTk import PhotoImage  # replace tkinter's version
except ImportError:
    from tkinter import PhotoImage  # else use the basic lib version

    print(pillowwarning)
    # but continue: falls back on Tk/tkinter's native PhotoImage, for PNGs, GIFs, etc.
    # Pillow install is required for source-code only: apps/exes have it "baked in"

# [SA]: set window icons on Windows and Linux
from windowicons import trySetWindowIcon


###############################################################################
# Option configuration classes and arg parser
###############################################################################

# [SA] DEFUNCT: now loaded from file or args


###############################################################################
# Digital display object
###############################################################################

class DigitalDisplay(Frame):
    """
    Digital display mode (too simple to doc)
    """

    def __init__(self, parent, cfg):  # [SA] tbd: help here too?
        Frame.__init__(self, parent)
        self.hour = Label(self)
        self.mins = Label(self)
        self.secs = Label(self)
        self.ampm = Label(self)
        for label in self.hour, self.mins, self.secs, self.ampm:
            label.config(bd=4, relief=SUNKEN, bg=cfg.BgColor, fg=cfg.FgColor)
            label.pack(side=LEFT)  # TBD: could expand, and scale font on resize

        # [SA] yes, make frame expandable; else tiny if window grows for digital
        for widget in (self, self.hour, self.mins, self.secs, self.ampm):
            widget.pack(expand=YES, fill=BOTH)

    def onUpdate(self, hour, mins, secs, ampm, cfg):
        mins = str(mins).zfill(2)  # or '%02d' % x
        self.hour.config(text=str(hour), width=4)
        self.mins.config(text=str(mins), width=4)
        self.secs.config(text=str(secs), width=4)
        self.ampm.config(text=str(ampm), width=4)

    def onResize(self, newWidth, newHeight, cfg):
        pass  # nothing to redraw here


###############################################################################
# Analog display object
###############################################################################

class AnalogDisplay(Canvas):
    def __init__(self, parent, cfg, size=None):
        """
        -----------------------------------------------------------------
        Draw analog clock at startup, to be shown/hidden per user.
        [SA] the hand line attrs are not used anymore (formerly for
        deleting on timer), now saves the image object to avoid a
        reload each second, and defers draw to first timer update;
        -----------------------------------------------------------------
        """
        self.size = size or int(cfg.InitialSize.split('x')[0])  # [SA] one: square
        Canvas.__init__(self, parent,
                        width=self.size, height=self.size, bg=cfg.BgColor)
        self.parent = parent
        self.image = None
        self.hourHand = self.minsHand = self.secsHand = self.cog = None
        # [SA] and wait for first unUpdate(), which calls drawClockface()

    def drawClockface(self, cfg):
        """
        -----------------------------------------------------------------
        On timer update and resize: draw ovals+picture on empty canvas.
        [SA] No longer called at startup: triggered by first onUpdate().
        -----------------------------------------------------------------
        """
        if cfg.PictureFile:
            self.loadImage(cfg)
            if self.image:
                imgx = (self.size - self.image.width()) // 2  # center it
                imgy = (self.size - self.image.height()) // 2  # 3.x // div
                self.create_image(imgx + 1, imgy + 1, anchor=NW, image=self.image)

        originX = originY = radius = self.size // 2  # 3.x // div

        for i in range(60):
            x, y = self.point(i, 60, radius - 6, originX, originY)
            self.create_rectangle(x - 1, y - 1, x + 1, y + 1, fill=cfg.FgColor)  # mins

        for i in range(12):
            x, y = self.point(i, 12, radius - 6, originX, originY)
            self.create_rectangle(x - 3, y - 3, x + 3, y + 3, fill=cfg.FgColor)  # hours

        self.ampm = self.create_text(3, 3, anchor=NW, fill=cfg.FgColor)

        # [SA] add help popup via '?' click
        help = self.create_text(self.size, 3, text='?', anchor=NE, fill=cfg.FgColor)
        self.tag_bind(help, '<Button-1>', lambda event: self.parent.onHelp())

        """
        [SA] this didn't work on Windows, and looked odd anyhow
        help = Button(self, text='?', command=self.parent.onHelp, fg=cfg.FgColor)
        self.create_window(self.size+1, 0, window=help, anchor=NE)
        """

    def point(self, tick, units, radius, originX, originY):
        """
        -----------------------------------------------------------------
        The geometry bit
        -----------------------------------------------------------------
        """
        angle = tick * (360.0 / units)
        radiansPerDegree = math.pi / 180
        pointX = int(round(radius * math.sin(angle * radiansPerDegree)))
        pointY = int(round(radius * math.cos(angle * radiansPerDegree)))
        return (pointX + originX + 1), (originY + 1 - pointY)

    def loadImage(self, cfg):
        """
        -----------------------------------------------------------------
        Load analog background image (if any) once.
        [SA] Factored off to make this more robust and explicit.
        The caching is moot now, as always redraws canvas in full.
        -----------------------------------------------------------------
        """
        if cfg.PictureFile and not self.image:
            try:
                self.image = PhotoImage(file=cfg.PictureFile)  # try first
            except:
                try:
                    self.image = BitmapImage(file=cfg.PictureFile)  # save ref
                except:
                    pass
        return self.image

    def onUpdate(self, hour, mins, secs, ampm, cfg):
        """
        -----------------------------------------------------------------
        On timer update callback: redraw three clock hands and cog.
        Run each second by the after() timer logic in Clock.onTimer().

        [SA] Recoded to work around a Tk (or Pillow) memory leak related
        to photo content buffering.  This now redraws the full clock face
        first, and the Clock class now destroys and remakes the entire
        analog display to force the prior Canvas to free its memory.

        This avoids the leak altogether by starting with a clean Canvas,
        and the full Canvas rebuild isn't noticeable in the GUI.  The
        downsides are that it's more CPU-intensive (but just 1.x% on Macs),
        and resizes now don't redraw the clockface during user drags.

        Neither a .delete('all') here nor the former scheme of just a
        .delete() of the clock hand lines were enough to avoid leaks.
        The leak was worse on Mac OS Sierra, largely applied to photos,
        and never happened when running source (e.g., PP4E original).
        -----------------------------------------------------------------
        """
        self.drawClockface(cfg)

        originX = originY = radius = self.size // 2  # 3.x div
        hour = hour + (mins / 60.0)

        hx, hy = self.point(hour, 12, (radius * .80), originX, originY)
        mx, my = self.point(mins, 60, (radius * .90), originX, originY)
        sx, sy = self.point(secs, 60, (radius * .95), originX, originY)

        self.hourHand = self.create_line(originX, originY, hx, hy,
                                         width=(self.size * .04),
                                         arrow='last', arrowshape=(25, 25, 15), fill=cfg.HhColor)

        self.minsHand = self.create_line(originX, originY, mx, my,
                                         width=(self.size * .03),
                                         arrow='last', arrowshape=(20, 20, 10), fill=cfg.MhColor)

        self.secsHand = self.create_line(originX, originY, sx, sy,
                                         width=1,
                                         arrow='last', arrowshape=(5, 10, 5), fill=cfg.ShColor)

        cogsz = self.size * .01
        self.cog = self.create_oval(originX - cogsz, originY + cogsz,
                                    originX + cogsz, originY - cogsz, fill=cfg.CogColor)

        self.dchars(self.ampm, 0, END)
        self.insert(self.ampm, END, ampm)

    def onResize(self, newWidth, newHeight, cfg):
        """
        -----------------------------------------------------------------
        On user resize of window, redraw clock face at new size.
        onUpdate will be run on next second to redraw clock hands.
        [SA] Now just resets size and waits for next onUpdate().
        -----------------------------------------------------------------
        """
        newSize = min(newWidth, newHeight)
        if newSize != self.size + 4:  # 4 for canvas border
            self.size = newSize - 4
            # to be followed by onUpdate(), which calls drawClockface()


###############################################################################
# Clock composite object
###############################################################################

ChecksPerSec = 10  # second change timer


class Clock(Frame):
    def __init__(self, configs=object(), parent=None):
        Frame.__init__(self, parent)
        self.root = parent  # [SA] for focus force
        self.cfg = configs
        self.makeWidgets(parent)  # children are packed but
        self.labelOn = 0  # clients pack or grid me
        self.display = self.digitalDisplay
        self.lastSec = self.lastMin = -1
        self.countdownSeconds = 0
        self.onSwitchMode(None)  # flip to draw analog now
        self.onToggleLabel(None)  # [SA] label starts on
        self.onTimer()

    def makeWidgets(self, parent):
        self.digitalDisplay = DigitalDisplay(self, self.cfg)
        self.analogDisplay = AnalogDisplay(self, self.cfg)
        self.dateLabel = Label(self, bd=3)
        # [SA] default colors (or bg='black', fg='white' (but not red/blue from PP4E))

        if not RunningOnMac:
            # original code: Windows, Linux
            parent.bind('<ButtonPress-1>', self.onSwitchMode)  # leftclick
            parent.bind('<ButtonPress-3>', self.onToggleLabel)  # rightclick

        else:
            # [SA] on Mac OS, can't bind B1 to root window, else fires
            # on window moves (i.e., border clicks); also use B2 instead
            # of B3 for right-click, and allow Control-B1 as a synonym;
            #
            parent.bind('<KeyPress-x>', self.onSwitchMode)
            parent.bind('<ButtonPress-2>', self.onToggleLabel)
            parent.bind('<Control-ButtonPress-1>', self.onToggleLabel)

        parent.bind('<Configure>', self.onResize)
        parent.bind('<KeyPress-s>', self.onCountdownSec)
        parent.bind('<KeyPress-m>', self.onCountdownMin)

    def onSwitchMode(self, event):
        trace('onSwitchMode', self.display.__class__.__name__)
        self.display.pack_forget()
        if self.display == self.analogDisplay:
            self.display = self.digitalDisplay
        else:
            self.display = self.analogDisplay
        self.display.pack(side=TOP, expand=YES, fill=BOTH)

    def onToggleLabel(self, event):
        self.labelOn += 1
        if self.labelOn % 2:
            self.dateLabel.pack(side=BOTTOM, fill=X)
        else:
            self.dateLabel.pack_forget()
        self.update()

    def onResize(self, event):
        if event.widget == self.display:
            trace('onResize', event.widget.__class__.__name__)
            self.display.onResize(event.width, event.height, self.cfg)

    def onTimer(self):
        secsSinceEpoch = time.time()
        timeTuple = time.localtime(secsSinceEpoch)
        hour, min, sec = timeTuple[3:6]
        if sec != self.lastSec:
            self.lastSec = sec
            ampm = ((hour >= 12) and 'PM') or 'AM'  # 0...23
            hour = (hour % 12) or 12  # 12..11

            # [SA] force canvas to free memory
            if self.display == self.analogDisplay:
                copysize = self.display.size - 2
                self.display.destroy()
                del self.display
                del self.analogDisplay
                newdisplay = AnalogDisplay(self, self.cfg, copysize)
                newdisplay.pack(side=TOP, expand=YES, fill=BOTH)
                self.display = self.analogDisplay = newdisplay

            # delegate to anolog or digital object
            self.display.onUpdate(hour, min, sec, ampm, self.cfg)

            # [SA] better time label format
            # self.dateLabel.config(text=time.ctime(secsSinceEpoch))
            timeFormat = '%a %b %d, %Y %X'
            self.dateLabel.config(text=time.strftime(timeFormat, timeTuple))

            self.countdownSeconds -= 1
            if self.countdownSeconds == 0:
                self.onCountdownExpire()  # countdown timer
        self.after(1000 // ChecksPerSec, self.onTimer)  # run N times per second

        # 3.x // trunc int div

    def onCountdownSec(self, event):
        secs = askinteger('Countdown', 'Seconds?')
        if secs: self.countdownSeconds = secs

    def onCountdownMin(self, event):
        secs = askinteger('Countdown', 'Minutes')
        if secs: self.countdownSeconds = secs * 60

    def onCountdownExpire(self):
        # caveat: only one active, no progress indicator
        win = Toplevel()
        if RunningOnMac:
            # [SA] emulate colored buttons on Mac
            msg = Label(win, text='Timer Expired!')
            msg.bind('<Button-1>', lambda e: win.destroy())
        else:
            msg = Button(win, text='Timer Expired!', command=win.destroy)
        msg.config(font=('courier', 80, 'normal'), fg='white', bg='navy')
        msg.config(padx=10, pady=10)
        msg.pack(expand=YES, fill=BOTH)
        win.lift()  # raise above siblings
        if sys.platform[:3] == 'win':  # full screen on Windows
            win.state('zoomed')
        elif RunningOnMac:  # [SA] Mac is different...
            win.wm_attributes('-fullscreen', 1)

    def onHelp(self):
        # [SA] clock display's '?' help callback
        from tkinter.messagebox import showinfo
        showinfo('PyClock Help',
                 'PyClock 3.0\n'
                 '\n'
                 'A Python/tkinter clock GUI.\n'
                 'For Mac OS, Windows, and Linux.\n'
                 'From the book Programming Python.\n'
                 'Author and © M. Lutz 2001-2017.\n'
                 '\n'
                 'Usage:\n'
                 '▶ Leftclick (key "X" on Macs) switches between analog and '
                 'digital displays \n'
                 '▶ Rightclick (2-finger press or control+click '
                 'on Macs) shows/hides date label\n'
                 '▶ Keys "S" and "M" start seconds and minutes timers, respectively\n'
                 '▶ Resizing the window resizes the current clock display.\n'
                 '\n'
                 'Clock photos: analog clocks in app and executable '
                 'PyClocks support all common image types.  For source-code, '
                 'GIF always works, PNG works for Tk 8.6+, and all types '
                 'work after Pillow install (see README.txt).\n'
                 '\n'
                 'Version history:\n'
                 '● 3.0: Sep 2017, standalone release\n'
                 '● 2.1: May 2010, Programming Python 4E\n'
                 '● 2.0: 2006 PP3E, 1.0: 2001 PP2E\n'
                 '\n'
                 'For downloads and more apps, visit:\n'
                 'http://learning-python.com/programs.html'
                 )
        if self.root: self.root.focus_force()  # [SA] for Mac


###############################################################################
# Standalone clocks
###############################################################################

appname = 'PyClock 3.0'

# use new custom Tk, Toplevel for icons, etc.
from PP4E.Gui.Tools.windows import PopupWindow, MainWindow


class ClockPopup(PopupWindow):
    def __init__(self, configs=object(), name=''):
        PopupWindow.__init__(self, appname, name)
        clock = Clock(configs, self)
        clock.pack(expand=YES, fill=BOTH)


class ClockMain(MainWindow):
    def __init__(self, configs=object(), name=''):
        MainWindow.__init__(self, appname, name)
        clock = Clock(configs, self)
        clock.pack(expand=YES, fill=BOTH)
        self.clock = clock


# b/w compat: manual window borders, passed-in parent

class ClockWindow(Clock):
    def __init__(self, config=object(), parent=None, name=''):
        Clock.__init__(self, configs, parent)
        self.pack(expand=YES, fill=BOTH)
        title = appname
        if name: title = appname + ' - ' + name
        self.master.title(title)  # master=parent or default
        self.master.protocol('WM_DELETE_WINDOW', self.quit)


###############################################################################
# Program run
###############################################################################

if __name__ == '__main__':
    from getConfigs import getConfigs  # [SA] new common gadgets utility

    defaults = dict(InitialSize='200x200',
                    BgColor='beige',  # canvas
                    FgColor='brown',  # ticks
                    HhColor='black',  # hour hand
                    MhColor='navy',  # minute hand
                    ShColor='blue',  # second hand
                    CogColor='white',  # center point
                    PictureFile=None)  # middle photo path
    configs = getConfigs('PyClock', defaults)  # load from file or args

    # alternatives
    # myclock = ClockWindow(Tk(), configs)
    # myclock = ClockPopup('popup', configs)

    # parent is Tk root if standalone
    myclock = ClockMain(configs)
    trySetWindowIcon(myclock, 'icons', 'pygadgets')  # [SA] for win+lin

    if RunningOnMac:
        # Mac requires menus, deiconifies, focus

        # [SA] on Mac, customize app-wide automatic top-of-display menu
        from guimaker_pp4e import fixAppleMenuBar

        fixAppleMenuBar(window=myclock,
                        appname='PyClock',
                        helpaction=myclock.clock.onHelp,
                        aboutaction=None,
                        quitaction=myclock.quit)  # app-wide quit: ask


        # [SA] reopen auto on dock/app click and fix tk focus loss on deiconify
        def onReopen():
            myclock.lift()
            myclock.update()
            temp = Toplevel()
            temp.lower()
            temp.destroy()


        myclock.createcommand('::tk::mac::ReopenApplication', onReopen)

    myclock.mainloop()
