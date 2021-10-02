from plyer import notification
import time

title = 'Hello!'
message= 'My name is Anwesha Mishra.'

notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 60,
                    toast=False)
time.sleep(60)