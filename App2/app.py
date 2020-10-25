from flask import Flask, render_template, url_for, request, redirect
import pickle
import random
from joblib import dump, load
app = Flask(__name__)

def m_learning(zip, demo1, demo2, demo3, demo4, enroll, satpercent):
    #loaded_model = pickle.load(open('rick.pkl', 'rb'))
    loaded_model = load('a.joblib')
    inputs = [zip,demo1,demo2,demo4,demo3,satpercent]
    outputs = loaded_model.predict([inputs])*100 + random.randrange(0,9)*10
    return outputs[0]


def r_learning(zip, demo1, demo2, demo3, demo4, enroll, satpercent):
    #loaded_model = pickle.load(open('rick.pkl', 'rb'))
    loaded_model = load('read.joblib')
    inputs = [zip,demo1,demo2,demo4,demo3,satpercent]
    outputs = loaded_model.predict([inputs])*100 + random.randrange(0,9)*10
    return outputs[0]

def w_learning(zip, demo1, demo2, demo3, demo4, enroll, satpercent):
    #loaded_model = pickle.load(open('rick.pkl', 'rb'))
    loaded_model = load('writing.joblib')
    inputs = [zip,demo1,demo2,demo4,demo3,satpercent]
    outputs = loaded_model.predict([inputs])*100 + random.randrange(0,9)*10
    return outputs[0]

@app.route('/', methods = ['GET', 'POST'])
def index():
    print("We made it here!")
    if request.method == 'POST':
        buroughs = request.form["buroughs"] # String
        print("Buroughs: " , buroughs)
        zip_code = request.form["zipcode"] # String
        print("Zip_Code: " , zip_code)
        demographic_1 = request.form["demo1"] # String
        print("Demo1: " , demographic_1)
        demographic_2 = request.form["demo2"] # String
        print("Demo2: " , demographic_2)
        demographic_3 = request.form["demo3"] # String
        print("Demo3: " , demographic_3)
        demographic_4 = request.form["demo4"] # String
        print("Demo4: " , demographic_4)
        enrollment_number = request.form["enroll"] # Values can be: 750,1500,2250,3000,3750,4500,5250,6000
        print("Enroll: " , enrollment_number)
        satpercent = request.form["satpercent"] # String
        print("Satpercent: " , satpercent)
        #run machine_learning
        print("WE DID IT!") 
        math = m_learning(float(zip_code),float(demographic_1)/100,float(demographic_2)/100,float(demographic_3)/100,float(demographic_4)/100,float(enrollment_number),float(satpercent)/100)
        read = r_learning(float(zip_code),float(demographic_1)/100,float(demographic_2)/100,float(demographic_3)/100,float(demographic_4)/100,float(enrollment_number),float(satpercent)/100)
        write = w_learning(float(zip_code),float(demographic_1)/100,float(demographic_2)/100,float(demographic_3)/100,float(demographic_4)/100,float(enrollment_number),float(satpercent)/100)
            
        return render_template('index2.html', math=math, read=read, write=write)
    else:
        return render_template('index.html')

@app.route('/results/',methods = ['GET', 'POST'] )
def index1():
    print("We made it here!")
    if request.method == 'POST':
        buroughs = request.form["buroughs"] # String
        print("Buroughs: " , buroughs)
        zip_code = request.form["zipcode"] # String
        print("Zip_Code: " , zip_code)
        demographic_1 = request.form["demo1"] # String
        print("Demo1: " , demographic_1)
        demographic_2 = request.form["demo2"] # String
        print("Demo2: " , demographic_2)
        demographic_3 = request.form["demo3"] # String
        print("Demo3: " , demographic_3)
        demographic_4 = request.form["demo4"] # String
        print("Demo4: " , demographic_4)
        enrollment_number = request.form["enroll"] # Values can be: 750,1500,2250,3000,3750,4500,5250,6000
        print("Enroll: " , enrollment_number)
        satpercent = request.form["satpercent"] # String
        print("Satpercent: " , satpercent)
        #run machine_learning
        print("WE DID IT!") 
        value = m_learning(float(zip_code),float(demographic_1)/100,float(demographic_2)/100,float(demographic_3)/100,float(demographic_4)/100,float(enrollment_number),float(satpercent)/100)
        print(value)    
    return render_template('index2.html', value=value)


if __name__ == '__main__':
    app.run(debug = True)


    