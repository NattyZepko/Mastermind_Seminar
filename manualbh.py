from random import randint


class ManualBH:

    def __init__(self, num_of_digits, zero_include):
        """ Init function
        :param num_of_digits: Number of digits to guess. This value commonly determines the size of a row
        :type num_of_digits: int
        :param zero_include: 0 if exclude the digit zero from the game, any other value otherwise
        :type zero_include: int
        """
        self.num_Of_Digits = None
        self.zero_Include = None
        self.bh = None
        self.nh = None
        self.cypher = None
        self.__newGame__(num_of_digits, zero_include)

    def __newGame__(self, num_of_digits, zero_include):
        """ Reset all attributes to default values
        :param num_of_digits: Number of digits to guess
        :type num_of_digits: int
        :param zero_include: 0 if exclude the digit zero from the game, any other value otherwise
        :type zero_include: int
        """

        self.num_Of_Digits = num_of_digits
        self.zero_Include = zero_include
        self.bh = 0
        self.nh = 0
        self.cypher = []
        self.gen_new_cypher()

    def gen_new_cypher(self):
        """
        Use RNG to generate a random cypher (secret number to guess)
        """

        for element in range(self.num_Of_Digits):
            if element == 0:
                self.cypher.append(randint(1, 9))
            elif self.zero_Include:
                self.cypher.append(randint(0, 9))
            else:
                self.cypher.append(randint(1, 9))

    def get_guess(self, current_guess):
        """ Check the status of the current guess, and update the values of find_bh and find_nh
        :param current_guess: the number representing the current guess
        :type current_guess: str or int
        """
        my_cypher = self.cypher.copy()
        self.find_bh(my_cypher, current_guess)
        self.find_nh(my_cypher, current_guess)

    def get_cypher(self):
        """
        :return: The secret number - one is supposed to guess
        :rtype: str
        """
        return self.cypher

    def find_bh(self, my_cypher, current_guess):
        """ Count how many 'Bull' the guess has
        :param my_cypher: The secret number to guess
        :type my_cypher: list of (str or int)
        :param current_guess: The player's guess to compare
        :type current_guess: list of (str or int)
        """

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
        """ Count how many 'Hit' the guess has
        :param my_cypher: The secret number to guess
        :type my_cypher: list of (str or int)
        :param current_guess: The player's guess to compare
        :type current_guess: list of (str or int)
        """

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
