import json, os, subprocess, requests
from tkinter.tix import Shell
import os

def run():
    masterip="127.0.0.1"
    masterport="8085"
    command = "rmdir /s /q downloadedCode"
    os.system(command)
    command ="mkdir downloadedCode && chdir downloadedCode"
    os.system(command)
    repo = requests.get("http://{}:{}/repo".format(masterip,masterport), json={'repoState': 0})
    json_data = json.loads(repo.text)
    url = json_data['repoUrl']
    command="chdir downloadedCode && git init && git remote add origin {} && git pull".format(url)
    os.system(command)
    sha = "480fa7bda123368fe7cdf87d46ddb62e452e0a1c"
    command2 = "cd downloadedCode && git reset --hard {}".format(sha)
    os.system(command2)
    out = subprocess.check_output(["lizard","downloadedCode"])
    out = out.decode("utf-8")
    lastline = out.splitlines()[-1:]
    CCN = lastline[0].split()[2]
    print(CCN)

if __name__ == "__main__":
    run()