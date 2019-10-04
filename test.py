from flask import Flask, render_template
import numpy as np
import pandas as pd
import random

app = Flask(__name__)


@app.route("/")
def colour_format():
    probability = pd.read_csv('export_dataframe.csv')
    cols = list(probability)
    v = probability.values
    categories_blue_to_red = np.array(['191970', '4169E1', '6495ED', 'DCDCDC', 'CD5C5C', 'B22222', '8B0000'])
    code_blue_to_red = np.searchsorted([0.15, 0.3, 0.47, 0.54, 0.7, 0.85,  1], v.ravel(), side='left').reshape(v.shape)
    colours = pd.DataFrame(categories_blue_to_red[code_blue_to_red], probability.index, probability.columns)
    # categories_just_red = np.array(['DCDCDC', 'CD5C5C', 'B22222', '8B0000'])
    # code_just_red = np.searchsorted([0.49, 0.7, 0.85, 1], v.ravel(), side='left').reshape(v.shape)
    # colours = pd.DataFrame(categories_just_red[code_just_red], probability.index, probability.columns)
    return render_template('test.html', probability=probability, hex_codes=colours, cols=cols)


def get_random_values():
    # Generating 'Random' Data
    col_list = ['Income Tax', 'Super Tax', 'Go', 'Free Parking', 'Chance', 'Community Chest']
    matrix = []
    row = []
    for i in range(100):
        row = random.sample(range(0, 101), len(col_list))
        row = [x / 100 for x in row]
        matrix.append(row)
    dataframe = pd.DataFrame(matrix, columns=col_list)
    dataframe.to_csv(r'.\export_dataframe.csv', index=None, header=True)
    # return dataframe


if __name__ == '__main__':
    # get_random_values()
    app.run(debug=True)


