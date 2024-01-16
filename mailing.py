
class Mailing:
    def __init__(self, to_addres, from_address, cost, track):
        self.to_address = to_addres
        self.from_address = from_address
        self.cost = int(cost) 
        self.track = str(track) 

    #def __str__(self):
       # return f"To: {self.to_addres}\nFrom: {self.from_address}\nCost: {self.cost}\nTrack: {self.track}"