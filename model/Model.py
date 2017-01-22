from subprocess import call

class Model():
    def __init__(self,cmd): #cmd = array of string
        self.command = "deBGA" 
        if self.launched:
            return "ERROR"
        else:
           for i in cmd:
                self.command=self.command+ " " +i
                call(self.command)
        
        self.command=[] #clear attribute "command" for launching other run
    
    def launched(self): #test if command already launched, return true if running
        launch=call("ps aux |grep "+self.command)#launch contains return code
        if launch !="0":
            return False
        return True
