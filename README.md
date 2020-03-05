NumbersToWordsConverter
===================
This repository contains a solution to Exercise 1 - Numbers to Words (see [Original_Problem_Statement.md](Original_Problem_Statement.md))

## System Requirements
For full requirements, see [requirements.txt](requirements.txt).  The main requirements are:
- Python 3.8
- Flask framework
- Docker (if you are interested in running the docker build)
- Windows/Linux/MacOS

**NOTE:** This GitHub Repository has Linux line endings (\n)

## Functionality
This code converts numeric input into its spelled out form (i.e. 2354 --> two thousand three hundred fifty-four)

This code handles the following:
- Integers (maximum 12 digits)
- Mixed numbers (1-12 digits to left of decimal, 1-11 digits to right of decimal)
- Negative numbers
- Type errors, value errors

This code has the following features:
- Command line usage
- Back-end REST API service
- Docker build (Incomplete)

## Usage
#### Usage: Command Line (without REST service)
1. From command line, navigate to source code
2. Run all unit tests by typing in the following command:
    ```commandline
    $ python -m unittest discover package/unit_tests
    ```
3. Run individual unit tests by executing the following commands:
    ```commandline
    $ python -m package.unit_tests.TestIntegersToWordsConverter
    $ python -m package.unit_tests.TestNumbersToWordsConverter
    ```
4. Use the Number Converter code directly from the python console with the following commands:
    ```commandline
    $ python
    >>> from package.NumbersToWordsConverter import NumbersToWordsConverter
    >>> instance = NumbersToWordsConverter()
    >>> instance.convert_number_to_word(<NUMBER_FORMATTED_AS_STRING>)
    ```
   For Example:
   ```commandline
    >>> instance.convert_number_to_word("-534.02")
    negative five hundred thirty-four and two hundredths
    ```
   
#### Usage: REST service with Postman
1. From command line, navigate to source code
2. Run the following command to start the REST API Service:
    ```commandline
    $ python main_numbers_to_words_service.py
    ```
3. Open Postman (or another REST tool)
4. Navigate to localhost at the following URL:
    
    http://127.0.0.1:8080/numbers_to_words_converter
    
    or
    
    http://localhost:8080/numbers_to_words_converter
5. Configure the request type to "POST"
6. Enter a JSON into the request body in the following format:
    ```buildoutcfg
    {
       "number": "<INPUT_NUMBER>"
   }
    ```
   For example:
   ```buildoutcfg
    {
       "number": "-4561.1564"
   }
    ```
6. The response should show the word as a response, along with a message, status, request ID, and original request.
    
    For example:
    ```buildoutcfg
    {
       "message": "The numbers_to_words_converter service returned successfully",
       "request": {
           "number": "-4561.1564"
       },
       "request_id": "ce33c6f2-5ea9-11ea-b74e-0cdd24aac147",
       "response": "negative four thousand five hundred sixty-one and one thousand five hundred sixty-four ten-thousandths",
       "status": "SUCCESS"
    }
    ```

#### Usage: Docker Build (Incomplete)
1. From command line, navigate to source code
2. Run the following command to initiate the docker build:
    ```commandline
    $ docker build -t num-to-word:latest .
    $ docker run -p 8080:8080 num-to-word:latest
    ```
3. The intent here is to be able to follow steps 4-6 from **Usage: REST service with Postman** once the container is running.

## Design

#### Design Overview
This package was developed starting with the smallest unit of conversion (a single-digit, positive integer).
From there, double- and triple-digit values were handled, and then longer integers were handled recursively
(since any integer longer than three digits repeats the same format as the first three digits, except in the
thousands place, millions place, etc.). All of this development took place in *IntegersToWordsConverter.py*.

*NumbersToWordsConverter.py* was subsequently developed to handle more complete numbers (negatives, decimals, etc.).
Decimals just required "place" mapping (tenths, hundredths, etc.), but aside from that, any number after the 
decimal point was handled as an integer. Negative values were also trivial because the word "negative" just
had to be prepended to the result that was already being computed.

Unit tests were created in parallel to development. See [DEVELOPMENT_LOG.txt](DEVELOPMENT_LOG.txt) for more
 information on design decisions, etc.

#### Files and Packages In This Directory
- **package** - directory containing the main source code and unit tests
- **main_numbers_to_words.py** - [ENTRY POINT]; code that exposes *package* as a REST API service
- **DEVELOPMENT_LOG.txt** - a log tracking ideas, work, and design decisions throughout the week
- **Dockerfile** - file that enables docker build, even though I don't know how to test the service!!!
- **Original_Problem_Statement.md** - original document received from BPx
- **requirements.txt** - list of Python libraries and versions used; may be passed as an argument into pip install
 (as shown in Dockerfile)

#### Edge Cases
- Leading and trailing zeroes
- Sets of zeroes in the middle of a number
- More edge cases are documented in package/unit_tests/
- Edge cases are handled in package/IntegersToWordsConverter.py and package/NumbersToWordsConverter.py

#### Future Enhancements
- Better logging in debug mode versus regular mode
- User interface on a webpage
- Set up automated build pipeline
    
## Authors
- Ahmed Shahid 