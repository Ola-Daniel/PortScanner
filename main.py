# a simple port scanner
import socket
import subprocess
import sys
from time import time
import platform


subprocess.call('clear' if platform.platform() in ("Linux", "Darwin") else "cls", shell=True)

# Ask for input
remoteServer = input("Please Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)
# check what time the scan started
t1 = time()
# Using the range function to specify ports ( here it will scan all port between 1 and 1024
# We also put in some error handling for catching errors
try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:      Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit(2)

except socket.gaierror:
    print('Hostname could not be resolved. Existing')
    sys.exit(1)

except socket.error:
    print("Couldn't connect to server")
    sys.exit(3)

# Checking the time again
t2 = time()

# Calculates the difference of time to see how long the scan took
total = t2 - t1
# Printing the information to screen
print(f"Scanning completed in about {total} seconds")


