from flask import Flask,render_template,request

import inputScript
import pickle
from sklearn.tree import DecisionTreeClassifier
app = Flask(__name__,static_url_path='/static/', static_folder='/static/')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/getURL',methods=['POST'])
def getURL():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        data = inputScript.main(url)
        #print(data)
        dtmodel = pickle.load(open('decissionTree.pkl','rb'))
        predicted_value = dtmodel.predict(data)
        #print(predicted_value)
        if predicted_value == -1:    
            value = "Legitimate Site"
            return render_template("index.html",predicted_value=value)
        else:
            value = "Phishing Site"
            return render_template("index.html",predicted_value=value)
if __name__ == "__main__":
    app.run(debug=True)