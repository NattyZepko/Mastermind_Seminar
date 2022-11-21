from random import randint



class manual_bh:
    
    def __init__(self, num_Of_Digits, zero_Include):
        self.num_Of_Digits = None
        self.zero_Include =None
        self.bh= None
        self.nh=None
        self.cypher=None
        self.__newGame__(num_Of_Digits, zero_Include)


    def __newGame__(self,num_Of_Digits, zero_Include):
        self.num_Of_Digits = num_Of_Digits
        self.zero_Include =zero_Include
        self.bh= 0
        self.nh = 0
        self.cypher=[]
        self.gen_new_cypher()



    def gen_new_cypher(self):
        for element in range(self.num_Of_Digits):
            if element == 0:
                self.cypher.append(randint(1,9))
            elif self.zero_Include:
                self.cypher.append(randint(0,9))
            else:
                self.cypher.append(randint(1,9))
