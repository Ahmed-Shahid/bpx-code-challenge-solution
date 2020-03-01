from package.numberSpeller import numberSpeller
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)
    
@app.route('/numSpell', methods = ['POST'])
def getNumText():
    numSpellInstance = numberSpeller()
    
    requestID = uuid.uuid1()
    json_in = request.get_json()
    num = json_in["number"]
    numText = numSpellInstance.spellNumber(num)
    
    response =  jsonify({'requestID': requestID,
                    'response': numText, 
                    'message': 'Success', 
                    'request': json_in})
                    
    return response
    
    
if __name__ == '__main__':
    app.run(debug=True)