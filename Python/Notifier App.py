####################
#### UNFINISHED ####
####################

import time
from plyer import notification

def notifyFunction():
    halfs = 1
    while(True):
        time.sleep(0.5*60*60)
        notification.notify(
            title="Take a break",
            message=f"You should take a break you have been using for {halfs * 30} minutes.",
            app_name="Notifier App",
            # Remember to change file path when moving app location #
            app_icon="F:\Programs\Python\Media\Paomedia-Small-N-Flat-Bell.ico",
            timeout="30"
        )
        halfs = halfs + 1
notifyFunction()
