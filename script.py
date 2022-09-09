# Configuration settings
# Set controllers to True to enable them, False to disable them.
ENABLE_CONTROLLER_1 = True
ENABLE_CONTROLLER_2 = True
ENABLE_CONTROLLER_3 = True
ENABLE_CONTROLLER_4 = True

# Set to True to output to debug console.
DO_CONSOLE_OUTPUT = True

# MS between controller polls.
POLLING_PERIOD = 1

# Binds for guitar buttons to ppJoy buttons.
GUITAR_TO_JOY = {
    GuitarButtons.Green: 1,
    GuitarButtons.Red: 2,
    GuitarButtons.Yellow: 3,
    GuitarButtons.Blue: 4,
    GuitarButtons.Orange: 5,
    GuitarButtons.Plus: 6,
    GuitarButtons.Minus: 7,
    GuitarButtons.StrumDown: 8,
    GuitarButtons.StrumUp: 9,
}


def map_guitar_button(n, guitar_button):
    # Function called each poll to update virtual controller.
    if wiimote[n].guitar.buttons.button_down(guitar_button):
        ppJoy[n].setButton(GUITAR_TO_JOY[guitar_button], True)
    else:
        ppJoy[n].setButton(GUITAR_TO_JOY[guitar_button], False)


def bind_guitar_controller(n):
    # Function called by each controller on poll.
    for i in list(GUITAR_TO_JOY.keys()):
        map_guitar_button(n, i)

def g1_update():
    # Function for controller 1 to update with.
    bind_guitar_controller(0)

def g2_update():
    # Function for controller 2 to update with.
    bind_guitar_controller(1)

def g3_update():
    # Function for controller 3 to update with.
    bind_guitar_controller(2)

def g4_update():
    # Function for controller 4 to update with.
    bind_guitar_controller(3)

if starting:
    # Console debug stuff.
    diagnostics.debug("\n")
    diagnostics.debug("----------------")
    diagnostics.debug("Starting runtime")
    diagnostics.debug("----------------")
    
    # Set higher input polling.
    system.setThreadTiming(TimingTypes.HighresSystemTimer)
    system.threadExecutionInterval = POLLING_PERIOD
    
    # Append guitar update functions to guitars.
    if ENABLE_CONTROLLER_1:
        if DO_CONSOLE_OUTPUT:
            diagnostics.debug("Enabled Guitar 1")
        wiimote[0].guitar.update += g1_update
    if ENABLE_CONTROLLER_2:
        if DO_CONSOLE_OUTPUT:
            diagnostics.debug("Enabled Guitar 2")
        wiimote[1].guitar.update += g2_update
    if ENABLE_CONTROLLER_3:
        if DO_CONSOLE_OUTPUT:
            diagnostics.debug("Enabled Guitar 3")
        wiimote[2].guitar.update += g3_update
    if ENABLE_CONTROLLER_4:
        if DO_CONSOLE_OUTPUT:
            diagnostics.debug("Enabled Guitar 4")
        wiimote[3].guitar.update += g4_update

