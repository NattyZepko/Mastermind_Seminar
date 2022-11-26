from random import randint


class ManualBH:

    def __init__(self, num_of_digits, zero_include):
        self.num_Of_Digits = None
        self.zero_Include = None
        self.bh = None
        self.nh = None
        self.cypher = None
        self.__newGame__(num_of_digits, zero_include)

    def __newGame__(self, num_of_digits, zero_include):
        self.num_Of_Digits = num_of_digits
        self.zero_Include = zero_include
        self.bh = 0
        self.nh = 0
        self.cypher = []
        self.gen_new_cypher()

    def gen_new_cypher(self):
        for element in range(self.num_Of_Digits):
            if element == 0:
                self.cypher.append(randint(1, 9))
            elif self.zero_Include:
                self.cypher.append(randint(0, 9))
            else:
                self.cypher.append(randint(1, 9))

    def get_guess(self, current_guess):
        my_cypher = self.cypher.copy()
        self.find_bh(my_cypher, current_guess)
        self.find_nh(my_cypher, current_guess)

    def find_bh(self, my_cypher, current_guess):
        self.bh = 0
        idx = 0
        while idx < len(my_cypher):
            if my_cypher[idx] == current_guess[idx]:
                self.bh += 1
                my_cypher.pop(idx)
                current_guess.pop(idx)
            else:  # Progress index only if we didn't pop.
                idx += 1

    def find_nh(self, my_cypher, current_guess):
        self.nh = 0
        c_idx = 0  # Current Index
        found_match = False  # Flag for each digit
        while c_idx < len(my_cypher):
            for g_idx in range(len(current_guess)):
                if current_guess[g_idx] == my_cypher[c_idx]:  # Found NH
                    self.nh += 1
                    my_cypher.pop(c_idx)  # Remove from cypher so we don't count it again
                    current_guess.pop(g_idx)  # Remove from guess so we don't count it again
                    found_match = True
                    break
            if not found_match:  # Only progress the index if we didn't pop
                c_idx += 1  # Because popping means everything goes one index back.
            else:
                found_match = False  # Flag for next iteration


game = ManualBH(4, 1)
game.cypher = [1, 1, 2, 5]
guess = [5, 1, 2, 2]
game.get_guess(guess)
print("my bh ==> "+str(game.bh))
print("my nh ==> "+str(game.nh)) 

