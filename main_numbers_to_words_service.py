"""
Author:         Ahmed Shahid

Usage:          python main_numbers_to_words_service.py

Description:    This is a backend REST API service that receives a json object with a numeric string
                (negatives and decimals ok) and returns a json object with the words that represent
                the input string

Example:        "-2345.45" --> "negative two thousand three hundred forty-five and forty-five hundredths"
"""

from package.NumbersToWordsConverter import NumbersToWordsConverter
from flask import Flask, jsonify, request
import uuid

# Script-level parameters
ENGINE_NAME = 'numbers_to_words_converter'
HOST_NAME = 'localhost'
PORT = 8080
SUCCESS_MESSAGE = 'The ' + ENGINE_NAME + ' service returned successfully'
DEBUG_MODE = True  # TODO: Set up logging

# Instantiate app
app_service = Flask(__name__)


@app_service.route('/' + ENGINE_NAME, methods=['POST'])
def numbers_to_words():
    """
    Main functionality of service
    """

    # Instantiate converter class
    n2w_instance = NumbersToWordsConverter()

    request_id = uuid.uuid1()

    # Input request should be of format {'number': ...}
    # TODO: Validate input request
    args_in = request.get_json()
    num = args_in["number"]

    try:
        word_out = n2w_instance.convert_number_to_word(num)  # Actual conversion
        status = 'SUCCESS'
        message = SUCCESS_MESSAGE

    except Exception as e:
        word_out = None
        status = 'FAILURE'
        message = str(e)  # These will be one of the custom errors defined in converter class

    # TODO: Move json format into global or script-level parameter
    response = jsonify({'request_id': request_id,
                        'response': word_out,
                        'status': status,
                        'message': message,
                        'request': args_in})

    return response


if __name__ == '__main__':
    app_service.run(host=HOST_NAME, port=PORT, debug=DEBUG_MODE)
