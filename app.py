import mailbox
from flask import Flask, render_template, request, redirect
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = 'no data'

    if (request.method == 'POST'):

        pickled_model = pickle.load(open('model.pkl', 'rb'))
        f_model = pickle.load(open('feature.pkl', 'rb'))



        input_mail = [request.form['mail']]

# convert text to feature vectors
        input_data_features = f_model.transform(input_mail)
        resultOut = pickled_model.predict(input_data_features)

        if resultOut[0] == 0: 
            result = 'Spam Mail'
        else:
            result = 'Ham Mail'
            
        return render_template('index.html',result=result)
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
