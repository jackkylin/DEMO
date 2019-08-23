import requests
import time
terminal = ''
j = 0
while True:
    requests.get(terminal)
    time.sleep(300)
    j += 1
    print(j)
