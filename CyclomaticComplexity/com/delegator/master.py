import json, requests
from flask import Flask

app = Flask(__name__)

class master():
    def __init__(self):
        repoShortPath="smarthkatyal/FileSystem/"
        self.numWorkers = 1
        self.currNumWorkers = 0  # Number of workers who have connected to the manager
        self.startTime = 0.0  # Start time for the timer
        # request repository info using the github API
        self.shaList = []  # List containing all commit sha values
        r = requests.get("https://api.github.com/repos/{}commits?page=1&per_page=200".format(repoShortPath)) 
        commits = json.loads(r.text)
        for i in commits:
            self.shaList.append(i['sha'])
            print("Commit Sha: {}".format(i['sha']))
        print("\nNumber of commits:{}".format(len(self.shaList)))
        self.listOfCCs = []
        


if __name__ == "__main__":
    masterObj = master()  # ini an instance of managerServer()
app.run(port=8085) # int(sys.argv[1])  , debug=True