#########################
### SPARTA UNIVERSITY ###
#########################

class University():
    def __init__(self,trainername,trainees):
        self.trainername=trainername
        self.trainee=trainees

class people():
    def __init__(self,fname,lname,age,id):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.id=int(id)

class trainees(people):
    def __init__(self,stream):
        super().__init__()
        self.stream=stream
t1=trainees()
