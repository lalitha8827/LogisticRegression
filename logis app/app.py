from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
app = Flask(__name__)
@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method=='POST':
        try:
            occ1=1.0
            occ2=float(request.form['occ2'])
            occ3 = float(request.form['occ3'])
            occ4 = float(request.form['occ4'])
            occ5 = float(request.form['occ5'])
            occ6 = float(request.form['occ6'])
            oc2 = float(request.form['oc2'])
            oc3 = float(request.form['oc3'])
            oc4 = float(request.form['oc4'])
            oc5 = float(request.form['oc5'])
            oc6 = float(request.form['oc6'])
            mrg_rating=float(request.form['mrg_rating'])
            age=float(request.form['age'])
            yrs_married = float(request.form['yrs_married'])
            children = float(request.form['children'])
            religious = float(request.form['religious'])
            educational_standard = float(request.form['educ'])
            filename='finalized_model_logis.pickle'
            model=pickle.load(open(filename,'rb'))
            proba=model.predict_proba([[occ1,occ2,occ3,occ4,occ5,occ6,oc2,oc3,oc4,oc5,oc6,mrg_rating,age,yrs_married,children,religious,educational_standard]])
            prediction=model.predict([[occ1,occ2,occ3,occ4,occ5,occ6,oc2,oc3,oc4,oc5,oc6,mrg_rating,age,yrs_married,children,religious,educational_standard]])
            if(prediction[0]==0.0):
                predict="woman does not have any affair as probability of woman having affair is less i.e.,"+str(int(proba[0][1]*100))+"%"
            else:
                predict="woman is having an affair as the probability of having affair is more i.e., "+str(int(proba[0][1]*100))+"%"
            return render_template('results.html',prediction=predict)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    else:
        return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)