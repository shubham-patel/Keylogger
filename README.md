# Keylogger

A Python keylogger that captures all keystrokes and emails them to a specified address on a configurable interval. Built for learning how keyloggers work at the OS level using the `pynput` library.

> **Disclaimer:** For educational purposes only. Only use on your own devices or systems you have explicit written permission to monitor. Deploying a keylogger on someone else's device without consent is illegal in most jurisdictions. The author is not responsible for any misuse.

---

## How it works

1. Listens for all keypresses using `pynput`
2. Buffers keystrokes in memory
3. Every N seconds, emails the buffer to a configured Gmail address
4. Clears the buffer and repeats

## Requirements

```bash
pip install -r requirements.txt
```

## Setup

Edit the credentials at the bottom of `keylogger.py`:

```python
keylogger = Keylogger(interval=60, email="your@gmail.com", password="your_app_password")
```

> **Note:** Use a [Gmail App Password](https://support.google.com/accounts/answer/185833) — not your main account password. Enable 2FA first, then generate an app-specific password.

## Usage

```bash
python3 keylogger.py
```

---

## Part of [H-Tools](https://github.com/shubham-patel/H-Tools)

Built during B.Tech studies. H-Tools bundles this and other networking/security utilities in a single CLI menu.
