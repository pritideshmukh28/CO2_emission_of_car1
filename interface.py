from flask import Flask, request, jsonify, render_template
from utils import CO2emission


app = Flask(__name__)

@app.route('/')
def home():
    
    return jsonify({"Result":"Successful"})

@app.route('/CO2_emission_pred')
def home1():

    return render_template('CO2_emission.html')


@app.route('/emission_pred',methods = ['GET'])
def emission_pred():
    data = request.args.get
    print("Data :",data)
    Car= data('Car')
    Model =data('Model')
    Volume = eval(data('Volume'))
    Weight = eval(data('Weight'))
   
    Obj = CO2emission(Car,Model,Volume,Weight)
    pred_emission = Obj.get_predicted_emission()


    
    return render_template('CO2_emission.html',prediction=pred_emission)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=False)