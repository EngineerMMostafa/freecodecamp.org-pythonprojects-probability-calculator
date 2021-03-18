import copy
import random
# Consider using the modules imported above.

class Hat:
    '''The class should take a variable number of arguments
    that specify the number of balls of each color that are in the hat'''

    def __init__ (self, **kwargs):
        '''The arguments passed into the hat object upon creation should be converted to a contents instance variable'''

        self.contents = list()
        
        if len(kwargs) > 0:
            # kwargs is a dictionary.
            for k,v in kwargs.items():
                if v > 0:
                    for i in range(v):
                        # append each argument string to contents variable list of strings
                        self.contents.append(k)

    def draw(self, draws):
        '''The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat.
        This method should remove balls at random from contents and return those balls as a list of strings.
        The balls should not go back into the hat during the draw'''
        
        # check if number of required draws is greater than or equal the number of balls in the hat >>> return all balls in the hat directly
        if draws >= len(self.contents):
            rslt = self.contents
        else:
            # Initialize result empty list
            rslt = list()
            # repeat draw n (draws) times
            for i in range(draws):
                # Each time generate a random number from 0 to (number of balls in the hat) exclusive (to index inside contents list)
                j = random.randrange(len(self.contents))
                # remove the drawn ball from the hat (contents list) and append to result list
                rslt.append(self.contents.pop(j))

        return rslt


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # hat: A hat object containing balls that should be copied inside the function.
    # expected_balls: A dictionary of the exact group of balls to attempt to draw (ex. {"blue":2, "red":1})

    # Initialze M variable to increment each success trial (when get expected balls)
    M = 0

    # repeat the experiment n (num_experiments) times
    for i in range(num_experiments):
        # every experiment make a deep copy of the hat instance
        expr_hat = copy.deepcopy(hat)
        # call draw method on the copied instance with num_balls_drawn argument
        expr_rslt = expr_hat.draw(num_balls_drawn)

        # Convert experiment result from list of strings in to dictionary {'color':count}
        rslt_dict = dict()
        for color in expr_rslt:
            rslt_dict[color] = rslt_dict.get(color,0) + 1

        # check if all expected_balls is in rslt dictionary
        found = True
        for k,v in expected_balls.items():
            if k not in rslt_dict or v > rslt_dict[k]:
                found = False
        if found:
            # If got expected_balls (found = True) increment M variable
            M += 1
    # Calculate probability = number of success trials / total number of experiments
    # change M from int to float to insure result is float
    prob = float(M) / num_experiments

    return prob
