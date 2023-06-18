from sklearn import datasets
import numpy as np


def search(keyword, filename):
    """
    :param keyword: the keyword to search
    :param filename: the file the search from
    :return: the lines that match the keyword
    """
    with open(filename, 'r') as f:
        # Your code here
        pass


sql_query = '''

            '''


def train_model():
    iris = datasets.load_iris()
    data = iris.data
    np.random.seed(42)
    # Your code here


def extract_dates(input_string):
    """
    :param input_string: date string follows this pattern - '05/22/2023 - 08/23/2023'
    :return: the start date and end date of the input_string
    """
    # Your code here
    pass


def play_round():
    # Roll a 100 sided die.
    # Use the roll_dice function defined above.
    # Return True if win and False if lose.
    # Your code here
    pass


def double_bettor_v2(initial_funds, initial_wager, intended_rounds):
    # Your code here
    pass


def scaler_bettor(initial_funds, initial_wager, intended_rounds, scaler=1):
    # Your code here
    pass


def general_bettor(initial_funds, initial_wager, intended_rounds, scaler=1, increment=0):
    # Your code here
    pass
