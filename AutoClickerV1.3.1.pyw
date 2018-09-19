import asyncio, os, time, json
from tkinter import *
#gets hotkeys from config file
configfile = 'autoclicker_config.json'
exists = os.path.isfile(configfile)
if not exists:
    with open(configfile, 'w+') as f:
        hotkeys = {'activate': 'F8', 'deactivate': 'F9'}
        json.dump(hotkeys, f)
with open(configfile, 'r') as f:
    hotkeys = json.load(f)
def errorMessage(title, message):
    import tkinter
    from tkinter import messagebox
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showerror(title, message)
#a special importer that handles any exceptions
try:
    import mouse
except:
    try:
        import pip
        pip.main(['install','mouse'])
        import mouse
    except:
        errorMessage('Error.','For this application to work, you must have pip installed on your computer.')
        sys.exit()
try:
    import keyboard
except:
    try:
        import pip
        pip.main(['install','keyboard'])
        import keyboard
    except:
        errorMessage('Error.','For this application to work, you must have pip installed on your computer.')
        sys.exit()
delay = 1000 #default delay in ms
active = False #states whether the clicker is clicking or not
mode = 'left' #states which mouse button is utilised

#kills the tkinter GUI and async event loop, then closes the program
def close_app():
    window.destroy()
    loop.stop()
    exit()

#resets configuration to default
def resetConfig():
    global hotkeys
    global mode
    global delay
    global active
    delay = 1000
    active = False
    mode = 'left'
    with open(configfile, 'w+') as f:
        hotkeys = {'activate': 'F8', 'deactivate': 'F9'}
        json.dump(hotkeys, f)
    labelText.set("Delay: {}ms".format(delay))
    activeText.set("Inactive.")
    modeText.set("Mouse Button: Left")
    inactiveHotkeyDisp.set("Deactivate ({})".format(hotkeys['deactivate']))
    activeHotkeyDisp.set("Activate ({})".format(hotkeys['activate']))

#increases and decreases delays by certain amounts
def incDelay1():
    global delay
    delay+=1
    labelText.set("Delay: {}ms".format(delay))
def incDelay2():
    global delay
    delay+=10
    labelText.set("Delay: {}ms".format(delay))
def incDelay3():
    global delay
    delay+=100
    labelText.set("Delay: {}ms".format(delay))
def incDelay4():
    global delay
    delay+=1000
    labelText.set("Delay: {}ms".format(delay))
def incDelay5():
    global delay
    delay+=10000
    labelText.set("Delay: {}ms".format(delay))
def decDelay1():
    global delay
    delay-=1
    if delay < 0:delay=0
    labelText.set("Delay: {}ms".format(delay))
def decDelay2():
    global delay
    delay-=10
    if delay < 0:delay=0
    labelText.set("Delay: {}ms".format(delay))
def decDelay3():
    global delay
    delay-=100
    if delay < 0:delay=0
    labelText.set("Delay: {}ms".format(delay))
def decDelay4():
    global delay
    delay-=1000
    if delay < 0:delay=0
    labelText.set("Delay: {}ms".format(delay))
def decDelay5():
    global delay
    delay-=10000
    if delay < 0:delay=0
    labelText.set("Delay: {}ms".format(delay))

#activates and deactivates the clicker
def activate():
    global active
    active = True
    activeText.set("Running.")
def deactivate():
    global active
    active = False
    activeText.set("Inactive.")

#switches between mouse buttons
def changeMode():
    global mode
    omode = mode
    if omode == 'left':
        mode = 'right'
        modeText.set("Mouse Button: Right")
    if omode == 'middle':
        mode = 'left'
        modeText.set("Mouse Button: Left")
    if omode == 'right':
        mode = 'middle'
        modeText.set("Mouse Button: Middle")

def setActivationHotkey():
    global hotkeys
    x = keyboard.read_hotkey()
    hotkeys['activate']=x.upper()
    activeHotkeyDisp.set("Activate ({})".format(hotkeys['activate']))
    with open(configfile, 'w+') as f:
        json.dump(hotkeys, f)

def setDeactivationHotkey():
    global hotkeys
    x = keyboard.read_hotkey()
    hotkeys['deactivate']=x.upper()
    inactiveHotkeyDisp.set("Deactivate ({})".format(hotkeys['deactivate']))
    with open(configfile, 'w+') as f:
        json.dump(hotkeys, f)

window = Tk()
window.title("Turret172\'s Auto Clicker")
window.configure(background='white')
window.protocol("WM_DELETE_WINDOW", close_app)

labelText = StringVar()
activeText = StringVar()
modeText = StringVar()

activeHotkeyDisp = StringVar()
inactiveHotkeyDisp = StringVar()

labelText.set("Delay: {}ms".format(delay))
activeText.set("Inactive.")
modeText.set("Mouse Button: Left")

inactiveHotkeyDisp.set("Deactivate ({})".format(hotkeys['deactivate']))
activeHotkeyDisp.set("Activate ({})".format(hotkeys['activate']))

Button(window, text="Exit", width=32, command=close_app).grid(row=8, column=0, sticky='W')
Button(window, text="Reset Configuration", width=16, command=resetConfig).grid(row=8, column=1, sticky='W')
Button(window, text="Change Mouse Button", width=32, command=changeMode).grid(row=7, column=0, sticky='W')
Button(window, textvariable=activeHotkeyDisp, width=32, command=activate).grid(row=5, column=0, sticky='W')
Button(window, textvariable=inactiveHotkeyDisp, width=32, command=deactivate).grid(row=6, column=0, sticky='W')
Button(window, text="Set Activation Hotkey", width=32, command=setActivationHotkey).grid(row=3, column=0, sticky='W')
Button(window, text="Set Deactivation Hotkey", width=32, command=setDeactivationHotkey).grid(row=4, column=0, sticky='W')
Button(window, text="Delay -10000ms", width=16, command=decDelay5).grid(row=3, column=1, sticky='W')
Button(window, text="Delay -1000ms", width=16, command=decDelay4).grid(row=4, column=1, sticky='W')
Button(window, text="Delay -100ms", width=16, command=decDelay3).grid(row=5, column=1, sticky='W')
Button(window, text="Delay -10ms", width=16, command=decDelay2).grid(row=6, column=1, sticky='W')
Button(window, text="Delay -1ms", width=16, command=decDelay1).grid(row=7, column=1, sticky='W')
Button(window, text="Delay +10000ms", width=16, command=incDelay5).grid(row=3, column=2, sticky='W')
Button(window, text="Delay +1000ms", width=16, command=incDelay4).grid(row=4, column=2, sticky='W')
Button(window, text="Delay +100ms", width=16, command=incDelay3).grid(row=5, column=2, sticky='W')
Button(window, text="Delay +10ms", width=16, command=incDelay2).grid(row=6, column=2, sticky='W')
Button(window, text="Delay +1ms", width=16, command=incDelay1).grid(row=7, column=2, sticky='W')
Label(window, textvariable=labelText, bg="white", fg="black", font="none 12 bold").grid(row=0, column=0, sticky='W')
Label(window, textvariable=activeText, bg="white", fg="black", font="none 12 bold").grid(row=1, column=0, sticky='W')
Label(window, textvariable=modeText, bg="white", fg="black", font="none 12 bold").grid(row=2, column=0, sticky='W')

async def mainApp():
    while True:
        #makes sure the status text is accurate
        if active:
            activeText.set("Running.")
        else:
            activeText.set("Inactive.")
        #updates the window, mainloop() does not allow it to work with async
        window.update()
        await asyncio.sleep(0.01)

async def click():
    global delay
    global active
    global mode
    while True:
        if active:
            mouse.click(button=mode)
            await asyncio.sleep(delay/1000)
        await asyncio.sleep(0.0001)

#listens for any hotkey presses
async def keyPressed():
    global active
    global delay
    global hotkeys
    while True:
        if keyboard.is_pressed(hotkeys['activate']):
            activate()
        if keyboard.is_pressed(hotkeys['deactivate']):
            deactivate()
        await asyncio.sleep(0.01)

async def main():
    await asyncio.wait( [
    click(),
    keyPressed(),
    mainApp()
    ] )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
