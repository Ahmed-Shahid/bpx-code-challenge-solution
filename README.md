NumberSpeller
===================
This repository contains a solution to Exercise 1 - Numbers to Words (see [Original_Problem_Statement.md](Original_Problem_Statement.md))

### System Requirements
For full requirements, see [requirements.txt](requirements.txt).  The main requirements are:
- Python 3.8
- Flask framework
- Docker (if you are interested in running the docker build)
- Windows/Linux/MacOS

**NOTE:** This GitHub Repository has Linux line endings (\n)

### Functionality
This code converts numeric input into its spelled out form (i.e. 2354 --> two thousand three hundred fifty-four)

This code handles the following:
- Integers (maximum 12 digits)
- Mixed numbers (1-12 digits to left of decimal, 1-11 digits to right of decimal)
- Negative numbers
- Type errors, value errors

This code has the following features:
- Command line usage
- REST API service
- User interface through web browser
- Docker build (Incomplete)

### Usage: Command Line Only
1. From command line, navigate to source code
2. Run all unit tests by typing in the following command:
    ```commandline
    $ python -m unittest discover package/unit_tests
    ```
3. Run individual unit tests by executing the following commands:
    ```commandline
    $ python -m package.unit_tests.Test_IntegerSpeller
    $ python -m package.unit_tests.Test_NumberSpeller
    ```
4. Use the Number Spell code directly from the python console with the following commands:
    ```commandline
    $ python
    >>> from package.NumberSpeller import NumberSpeller
    >>> instance = NumberSpeller()
    >>> instance.spellNumber(<NUMBER_FORMATTED_AS_STRING>)
    ```
   For Example:
   ```commandline
    >>> instance.spellNumber("-534.02")
    negative five hundred thirty-four and two hundredths
    ```
   
### Usage: REST API and Web Page
1. From command line, navigate to source code
2. Run the following command to start the REST API Service:
    ```commandline
    $ python numberSpellService.py
    ```
3. Open an internet browser (i.e. Google Chrome)
4. Navigate to localhost at the following URL:
    http://127.0.0.1:5000/
    or
    http://localhost:5000/
5. Type any text into the text box and click "Submit"
6. The next page will show SUCCESS if the text entered is properly handled, otherwise the page will show FAILURE
7. Click "Back" to go back to the form page (or the previous page in your history)


### Usage: Docker Build (Incomplete)
1. From command line, navigate to source code
2. Run the following command to initiate the docker build:
    ```commandline
    $ docker build -t numspell:latest .
    $ docker run -p 5000:5000 numspell:latest
    ```
3. The intent here is to be able to follow steps 4-7 from **Usage: REST API and Web Page** once the container is running.

### Other Files/Packages In This Directory
- **package** - directory containing the main source code and unit tests
- **DEVELOPMENT_LOG.txt** - a log tracking ideas, work, and design decisions throughout the week
- **Dockerfile** - file that enables docker build, even though I don't know how to test the service!!!
- **numberSpellService.py** - code that exposes *package* as a REST API service
- **Original_Problem_Statement.md** - original document received from BPx
- **requirements.txt** - list of Python libraries and versions used; may be passed as an argument into pip install (as shown in Dockerfile)
 
### Future Enhancements
- Better logging in debug mode versus regular mode
- Just have one web page that dynamically updates text as user types
- Set up automated build pipeline

### More Info
See [DEVELOPMENT_LOG.txt](DEVELOPMENT_LOG.txt) for more information on design decisions, etc.
    
### Authors
- Ahmed Shahid 