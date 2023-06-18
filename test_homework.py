from homework import *
from pathlib import Path
from typing import Generator
import urllib.request
import sqlite3
import pandas as pd
import sklearn
import re


def test_python():
    urllib.request.urlretrieve('https://raw.githubusercontent.com/AC4RM/AC4RM-dataset/main/homework/example.txt',
                               'example.txt')

    text_generator = search('lorem', 'example.txt')

    assert isinstance(text_generator, Generator)
    assert len(list(text_generator)) == 2

    Path('example.txt').unlink(missing_ok=True)


def test_sql():
    urllib.request.urlretrieve('https://github.com/AC4RM/AC4RM-dataset/blob/main/sql/data.db?raw=true', 'data.db')

    con = sqlite3.connect('data.db')

    customer_df = pd.read_sql_query(sql_query, con)

    assert customer_df.loc[customer_df['type'] == 'Bronze'].shape[0] == 6
    assert customer_df.loc[customer_df['type'] == 'Silver'].shape[0] == 2

    Path('data.db').unlink(missing_ok=True)


def test_model():
    model = train_model()
    iris = datasets.load_iris()
    data = iris.data

    assert isinstance(model, sklearn.cluster._agglomerative.AgglomerativeClustering)
    assert set(model.fit_predict(data)) == set([0, 1, 2])


def test_regex():
    start_date_1, end_date_1 = extract_dates('05/22/2023 - 08/23/2023')
    start_date_2, end_date_2 = extract_dates('[P] 01/01/2023 - 12/31/2023 [P]')

    assert start_date_1 == '05/22/2023' and end_date_1 == '08/23/2023'
    assert start_date_2 == '01/01/2023' and end_date_2 == '12/31/2023'


def test_monte_carlo():
    bettor_v2_results = []
    scaler_bettor_results = []
    general_bettor_results = []
    np.random.seed(42)
    for i in range(50):
        result = double_bettor_v2(10000, 100, 20)
        bettor_v2_results.append(result)

    for i in range(50):
        result = scaler_bettor(10000, 100, 20, 3)
        scaler_bettor_results.append(result)

    for i in range(50):
        result = general_bettor(10000, 100, 20, 2, 600)
        general_bettor_results.append(result)

    assert len(list(filter(lambda y: y < 10000, map(lambda x: x[-1], bettor_v2_results)))) == 9
    assert len(list(filter(lambda y: y < 10000, map(lambda x: x[-1], scaler_bettor_results)))) == 15
    assert len(list(filter(lambda y: y < 10000, map(lambda x: x[-1], general_bettor_results)))) == 7

