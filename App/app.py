from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__, template_folder='./Templates', static_folder='./Static')

Pkl_Filename = "Predic.pickle" 

with open(Pkl_Filename, 'rb') as file:  
    model = pickle.load(file)

    
@app.route('/')

def hello_world():
    return render_template('home.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    input_data = [int(x) for x in request.form.values()]

    #print(features)
    input_arr = np.array(input_data).reshape((1, 12))
    input_df = pd.DataFrame(data = input_arr, columns = ['Airline', 'Source', 'Destination', 'Total_Stops', 'Additional_Info', 'Jorney_day', 'Jorney_month', 'Dep_hour', 'Dep_min', 'Arr_hour', 'Arr_min', 'Duration(min)'])
    print(input_df)
    pred = model.predict(input_df)[0]
    print(pred)

    
    if pred < 0:
        return render_template('op.html', pred='Error calculating Amount!')
    else:
        return render_template('op.html', pred='Expected amount is {0:.3f}'.format(pred))

if __name__ == '__main__':
    app.run(debug=True)