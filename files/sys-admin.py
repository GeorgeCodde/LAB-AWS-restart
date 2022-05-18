#import os
#os.system("ls")

import subprocess
subprocess.run(["ls"])
print("--------------------------------------------------------------")
subprocess.run(["ls","-lha"])
print("--------------------------------------------------------------")
subprocess.run(["ls","-lha","README.md"])
print("--------------------------------------------------------------")
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
print("--------------------------------------------------------------")
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

