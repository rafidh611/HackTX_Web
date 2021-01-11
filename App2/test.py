from flask import Flask, render_template, url_for, request, redirect
import pickle
import random
from joblib import dump, load

loaded_model = load('a.joblib')

zip_code = 1
demographic_1 = 2
demographic_2 = 3
demographic_3 = 4
demographic_4 = 5
satpercent = 6
enrollment_number = 7




def m_learning(zip, demo1, demo2, demo3, demo4, enroll, satpercent):
    loaded_model = load('a.joblib')
    inputs = [zip,demo1,demo2,demo4,demo3,satpercent]
    print(inputs)
    print(loaded_model.predict([inputs]))
    outputs = loaded_model.predict([inputs])*100 + random.randrange(0,9)*10
    return output[0]
    return 0

value = m_learning(float(zip_code),float(demographic_1)/100,float(demographic_2)/100,float(demographic_3)/100,float(demographic_4)/100,float(enrollment_number),float(satpercent)/100)
