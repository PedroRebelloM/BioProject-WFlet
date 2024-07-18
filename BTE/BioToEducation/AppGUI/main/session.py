class Session:
    def __init__(self):
        self.user = None
    
    def Login(self, user):
        self.user = user
        
    def Logout(self):
        self.user = None
        
    def isLogged(self):
        return self.user is not None
    
    def getUser(self):
        return self.user

session = Session()