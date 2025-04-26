from flask import Flask
import json
import os


app = Flask("__name__")

def loadmock():
    file_path = os.path.join(os.path.dirname(__file__), 'mock.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file) 

data = loadmock()

@app.route('/getoverall_stats')
def getoverall_stats():
    overall_stats = data['overall_stats']
    return overall_stats


def detect_language():
    with open('data.json','w') as file:
        return json.load(file)
    
    
@app.route('/createdetect_language',methods=['POST'])
def detect():
    languages=[]
    lang=detect()
    
    lang.append()
    
    
if (__name__=='__main__'):
    app.run(debug='true')
    
    

    