import json, os, subprocess, requests
from tkinter.tix import Shell
import os

def run():
    #Configuration
    masterip="127.0.0.1"
    masterport="8085"
    #Config part ends
    
    command = "rmdir /s /q downloadedCode"
    os.system(command)
    command ="mkdir downloadedCode && chdir downloadedCode"
    os.system(command)
    repo = requests.get("http://{}:{}/repo".format(masterip,masterport), json={'repoState': 0})##Get repo info and send current state as 0
    json_data = json.loads(repo.text)
    url = json_data['repoUrl']
    command="chdir downloadedCode && git init && git remote add origin {} && git pull".format(url)
    os.system(command)
    r = requests.get("http://{}:{}/repo".format(masterip,masterport), json={'repoState': 1})###Send the same request with current state as 1 so master can incriment counter
    moreWork = 1
    while moreWork:
        commits = requests.get("http://{}:{}/master".format(masterip,masterport)) # hardcode for now
        json_data = json.loads(commits.text)
        print(json_data)
        if json_data['status']==0:
            print("Wait till master gets all slaves")
        elif json_data['status']==1:
            print("Done, exit")
            break;
        elif json_data['status']==2:
            sha=json_data['sha']
            command2 = "cd downloadedCode && git reset --hard {}".format(sha)
            os.system(command2)
            out = subprocess.check_output(["lizard","downloadedCode"])
            out = out.decode("utf-8")
            lastline = out.splitlines()[-1:]
            CCN = lastline[0].split()[2]
            if CCN=="":
                print("Unable to get CCN")
                CCN=-1
            else:      
                print(CCN)
                r = requests.post("http://{}:{}/cyclomatic".format(masterip,masterport),json={'sha': json_data['sha'], 'CCN': CCN})
        else:
            print("Bad Response")
            print("Done for this commit {} with CCN= {}".format(json_data['sha'],CCN))

if __name__ == "__main__":
    run()