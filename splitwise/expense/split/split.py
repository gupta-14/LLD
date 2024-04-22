from user.user import User

class Split:
    def __init__(self, user, amount_owe) -> None:
        self.user: User = user
        self.amount_owe = amount_owe
        
    def get_amount_owe(self):
        return self.amount_owe
    
    def get_user(self):
        return self.user
    
    def set_user(self, user):
        self.user = user
    
    def set_amount_owe(self, amount_owe):
        self.amount_owe = amount_owe
