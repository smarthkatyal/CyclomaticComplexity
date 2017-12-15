import os, subprocess
from subprocess  import Popen, PIPE
command = "rmdir /s /q downloadedCode"
os.system(command)
command ="mkdir downloadedCode && chdir downloadedCode"
os.system(command)
command="chdir downloadedCode && git init && git remote add origin {} && git pull".format("https://github.com/smarthkatyal/FileSystem")
os.system(command)
sha = "480fa7bda123368fe7cdf87d46ddb62e452e0a1c"
command2 = "cd downloadedCode && git reset --hard {}".format(sha)
os.system(command2)
out = subprocess.check_output(["lizard","downloadedCode"])
out = out.decode("utf-8")
lastline = out.splitlines()[-1:]
CCN = lastline[0].split()[2]
print(CCN)