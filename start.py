# -*- coding: utf-8 -*-

from src._client import Client
from src._settings import FB_EMAIL, FB_PASSWORD, FB_SESSION, ALWAYS_ACTIVE

running = True

if __name__ == "__main__":
    while (running):
        try:
            client = Client(FB_EMAIL, FB_PASSWORD, session_cookies=FB_SESSION)
            client.listen()
        except Exception as e:
            raise e
