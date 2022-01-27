from pywebio.input import *
from pywebio.output import *
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH, start_server
from flask import Flask,send_from_directory
import pickle
import argparse
app=Flask(__name__)
model=pickle.load(open('model4.pkl','rb'))
def predict():
    put_markdown("# Predict cancer for you")
    radius=input("Enter the radius",type=FLOAT)
    texture=input("Enter the texture",type=FLOAT)
    perimeter=input("Enter the perimeter",type=FLOAT)
    area=input("Enter the area",type=FLOAT)
    smoothness=input("Enter the smoothness",type=FLOAT)
    output=model.predict([[radius,texture,perimeter,area,smoothness]])
    if output==1:
        put_text("Malignant")
    else:
        put_text("Benign")
app.add_url_rule('/tool', 'webio_view',webio_view(predict),methods=['GET','POST','OPTIONS'])
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=8080)
    args=parser.parse_args()
    start_server(predict, port=args.port)
    #app.run(debug=True)
    #predict()
    