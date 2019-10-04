from flask import Flask, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route("/")
def hello():
    probability = pd.read_csv('test_data.csv')
    cols = list(probability)
    v = probability.values
    categories = np.array(['191970', '4169E1', 'B0C4DE', 'CD5C5C', 'B22222', '8B0000'])
    code = np.searchsorted([0.15, 0.3, 0.5, 0.7, 0.85,  1], v.ravel(), side='left').reshape(v.shape)
    colours = pd.DataFrame(categories[code], probability.index, probability.columns)
    # probability.join(cdf.add_suffix('_cat'))
    print(probability)
    print(colours)
    return render_template('test.html', probability=probability, hex_codes=colours, cols=cols)

if __name__ == '__main__':
    app.run(debug=True)


