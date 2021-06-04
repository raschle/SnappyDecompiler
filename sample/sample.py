ledState = False
BUTTON_PIN = 1
LED_PIN = 2

@setHook(HOOK_STARTUP)
def startupEvent():
    monitorPin(BUTTON_PIN, True)

@setHook(HOOK_GPIN)
def buttonEvent(pin, isSet):
    global ledState
    if not isSet:
        ledState = not ledState
        writePin(LED_PIN, ledState)


