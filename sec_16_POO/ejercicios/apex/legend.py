class legend:

    def __init__(self, name, passive, ulti):

        self.name = name
        self.passive = passive
        self.ulti = ulti

    
    def getInfo(self):

        result = "-- The Legend --"
        result += "\nName: " + self.name
        result += "\nPassive: " + self.passive
        result += "\nUlti: " + self.ulti

        return result


