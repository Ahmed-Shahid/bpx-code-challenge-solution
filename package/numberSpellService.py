from package.NumberSpeller import NumberSpeller
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)


@app.route('/numSpellForm', methods=['GET'])
def get_landing_page():
    if request.method == 'GET':
        html = ('<form action="/getNumSpell" method="GET">' +
                '<label for="number">Enter Number Here:</label><br>' +
                '<input type="text" id="number" name="number"><br><br>' +
                '<input type="submit" value="Submit">' +
                '</form>')

        return html


@app.route('/getNumSpell', methods=['GET'])
def get_num_spell():
    if request.method == 'GET':
        numSpellInstance = NumberSpeller()

        requestID = uuid.uuid1()
        args_in = request.args
        num = args_in["number"]
        numText = numSpellInstance.spell_number(num)

        # response = jsonify({'requestID': requestID,
        #                     'response': numText,
        #                     'message': 'Success',
        #                     'request': args_in})

        status = 'SUCCESS' if numText else 'FAILURE'

        response = ('<html>' +
                    '<h1>Status: ' + status + '</h1>' +
                    '<h2>You entered: ' + num + '</h2>' +
                    '<h2>Returned text: ' + numText + '</h2>' +
                    '<h3>RequestID: ' + str(requestID) + '</h3><br><br>' +
                    '<button onclick="goBack()">Go Back</button>' +
                    '<script>'
                    'function goBack() {'
                    '   window.history.back();'
                    '}'
                    '</script>'
                    '</html>')

        return response


if __name__ == '__main__':
    app.run(debug=True)
