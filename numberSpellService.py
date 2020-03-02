from package.NumberSpeller import NumberSpeller
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_landing_page():
    if request.method == 'GET':
        html = ('<form action="/getNumSpell" method="GET">' +
                '<center>' +
                '<label for="number">Enter Number Here:</label><br>' +
                '<input type="text" id="number" name="number"><br><br>' +
                '<input type="submit" value="Submit">' +
                '</center>' +
                '</form>')

        return html


@app.route('/getNumSpell', methods=['GET'])
def get_num_spell():
    if request.method == 'GET':
        numSpellInstance = NumberSpeller()

        requestID = uuid.uuid1()
        args_in = request.args
        num = args_in["number"]

        try:
            numText = numSpellInstance.spell_number(num)

            # response = jsonify({'requestID': requestID,
            #                     'response': numText,
            #                     'message': 'Success',
            #                     'request': args_in})

            status = 'SUCCESS'
            statusColor = 'green'

        except Exception as e:
            status = 'FAILURE'
            statusColor = 'red'
            numText = str(e)

        response = ('<html><center>' +
                    '<h1>Status: <br><font color="' + statusColor + '">' + status + '</font></h1>' +
                    '<h2>You entered: <br><font color="blue">' + num + '</font></h2>' +
                    '<h2>Returned text: <br><font color="blue">' + numText + '</font></h2>' +
                    '<h3>RequestID: <br><font color="blue">' + str(requestID) + '</font></h3><br><br>' +
                    '<button onclick="goBack()">Go Back</button>' +
                    '<script>'
                    'function goBack() {'
                    '   window.history.back();'
                    '}'
                    '</script>'
                    '</center></html>')

        return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
