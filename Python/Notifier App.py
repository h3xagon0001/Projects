import time
from plyer import notification

def notifyFunction():
    while(True):
        halfs = 1
        notification.notify(
            title="Take a break",
            message=f"You should take a break you have been using for {halfs * 30} minutes.",
            app_name="Notifier App",
            # Remember to change file path when moving app location #
            app_icon="F:\Programs\Python\Media\Paomedia-Small-N-Flat-Bell.ico",
            timeout="30"
        )
        time.sleep(0.5*60*60)
        halfs = halfs + 1

notifyFunction()