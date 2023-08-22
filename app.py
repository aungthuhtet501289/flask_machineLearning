import pickle
from flask import Flask ,render_template,request,redirect, url_for
model=pickle.load(open('lr_classifier.pkl','rb'))

app=Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if(request.method=='POST'):
        sepalLength=float(request.form['Sepallength'])
        sepalWidth=float(request.form['Sepalwidth'])
        petallength=float(request.form['Petallength'])
        petalwidth=float(request.form['Petalwidth'])
        pred=model.predict([[sepalLength,sepalWidth,petallength,petalwidth]])
        return render_template('index.html',result=pred[0])
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
