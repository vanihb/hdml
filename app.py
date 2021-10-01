from flask import Flask, render_template
from flask import request,session

from sklearn.metrics import accuracy_score
import joblib
app = Flask(__name__)




@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')




@app.route('/prediction')
def prediction():
    return render_template('pre.html',msg="undone")


@app.route('/prediction1', methods=['POST', 'GET'])
def pred():
    a = []
    global x_train,y_train,model
    if request.method == "POST":
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        cg = request.form['cg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']
        model = joblib.load('gbmodel.pkl')
        #model.fit(x_train, y_train)
        y_pred = model.predict([[age, sex, cp, trestbps, chol, fbs, cg, thalach, exang, oldpeak, slope, ca, thal]])
        return render_template('pre.html', msg="done", op=y_pred)
    return render_template('pre.html',msg="notdone")


if __name__ =='__main__':
    app.secret_key = "vee"
    app.run(debug=True)