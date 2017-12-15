import json, requests
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class initializer(Resource):
    def __init__(self):  
        global masterObj 
        self.server = masterObj
        super(initializer, self).__init__() 
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('repoState', type=int, location = 'json')  ##Whether slave has downloaded the repository
        self.reqparser.add_argument('CCN', type=float, location='json') ##Whether slave has calculated the complexity

    ##When slaves connects, this is the first function it will call in master, master will the slaves a repo
    def get(self):
        args = self.reqparser.parse_args()
        if args['repoState'] == 0:  ###slave does not have repo, then send
            print("Got a new slave, sending repo to pull...")
            return {'repoUrl': "https://github.com/smarthkatyal/FileSystem"}  # 'https://github.com/fchollet/deep-learning-models'
        if args['repoState'] == 1:  ##slave has the repo, then just incriment ready slaves counter
            self.server.gotSlaves += 1
        print("Slaves obtained: {}".format(self.server.gotSlaves))
    def post(self):
        pass
api.add_resource(initializer, "/repo", endpoint="repo")


    
class master():
    def __init__(self):
        #Below should be configurable
        repoShortPath="smarthkatyal/FileSystem/"
        self.totalSlaves = 1
        #Configurable part ends
        
        self.gotSlaves = 0  # Number of workers who have connected to the manager
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