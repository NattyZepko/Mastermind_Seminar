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

    def get_guess(self,guess):
        my_cypher = self.cypher.copy()
        self.findBh(my_cypher,guess)
        self.findnh(my_cypher,guess)

    def findBh(self,my_cypher,guess):
        self.bh=0
        idx=0   
        while idx < len(my_cypher):
            if(my_cypher[idx]==guess[idx]):
                self.bh+=1 
                my_cypher.pop(idx)
                guess.pop(idx)
            else:
                idx+=1 

    def findnh(self,my_cypher,guess):
        self.nh=0
        c_idx=0 
        found_match=False  
        while c_idx < len(my_cypher):
            for g_idx in range(len(guess)):
                if(guess[g_idx]==my_cypher[c_idx]):
                    self.nh +=1
                    my_cypher.pop(c_idx)
                    guess.pop(g_idx)
                    found_match=True
                    break
            if(not found_match):
                c_idx+=1
            else:
                found_match=False       



game = manual_bh(4,1)
game.cypher=[1,1,2,5]
guess= [5,1,2,2]
game.get_guess(guess)  
print("my bh ==> "+str(game.bh)) 
print("my nh ==> "+str(game.nh)) 

