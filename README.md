
 
**The Code Challenge** - Your coding assignment should you choose to accept it is to pick one of the following coding exercises. Please choose the exercise that you believe best reflects your skill set and experience. You may implement the exercise in any language of your choice. Unless otherwise noted, the minimum requirement is that we can run your application in a CLI. Optionally you can implement the user interface in a web page. 

At the end of this page be sure to read the Documentation and Deliverables sections regardless of which exercise you choose.

Exercise 1 – Numbers to Words
===================
Write some code that will accept an integer and convert it to the appropriate word representation.

Example:

Convert 2523 to "Two thousand five hundred twenty-three "

**Optional**
- Allow the user the option to enter decimals and provide the proper translation. Example: 23.5 to “twenty three point five” or “twenty three and five tenths”
- Allow the user the option to enter a dollar amount and provide the proper translation. Example $85052.50 to “eighty five thousand fifty two dollars and fifty cents”
- Allow the user the option to enter a calculation. Example 530 + 250 to “seven hundred eighty”
- An endpoint that accepts the numeric value and returns the word representation
- Appropriate Unit Tests
- A Dockerfile that allows us to run your application in a container
- A UI that can be run locally or link to a website that allows us to enter numeric values outside of the console


Exercise 2 - Best Poker Hand
===================

Write some code that will evaluate a 5 card poker hand between 2 players and determine the winner

Example:

Hand: Kh Kc 3s 3h 2d (2 Pair)

Hand: Kh Qh 6h 2h 9h (Flush) *winner*

**Optional**
- Allow the user to choose how many players to deal to
- Give the user an option to choose how many cards are dealt to each player (and determines the best poker hand out of 5 cards)
- An endpoint that handles dealing cards to each player
- An endpoint that accepts an array of cards for each player and determines the winner 
- Appropriate Unit Tests
- A Dockerfile that allows us to run your application in a container
- A UI that can be run locally or link to a website that allows us to play the game outside of the console


Exercise 3 - Anagrams API
===================

Build an API that allows fast searches for anagrams using the supplied dictionary.txt file. The API you design should respond on the following endpoints as specified:
Takes a JSON array of English-language words and adds them to the dictionary (data store).
Returns a JSON array of English-language words that are anagrams of the word passed in the URL. 
Deletes a single word (but not it’s associated anagrams) from the data store.

Example:

API response to possible anagrams for “integral”

{ "results": ["alerting", "altering", "relating", "triangle"] }

**Optional**
- An optional query parameter that indicates the maximum number of results to return in the array of anagrams
- Endpoint that returns a count of words in the dictionary and min/max/median/average word length
- Respect a query param for whether or not to include proper nouns in the list of anagrams
- Endpoint that identifies words with the most anagrams
- Endpoint that takes a set of words and returns whether or not they are all anagrams of each other
- Endpoint to return all anagram groups of size >= x
- Endpoint to delete a word and all of its anagrams
- Appropriate Unit Tests
- A Dockerfile that allows us to run your application in a container



Exercise 4 - Front End Challenge - Tic-tac-toe
===================

Create a website that has a tic tac toe board that two people could use to play against each other. Being a front end project, emphasis will be on usability, design, and aesthetics. You don't have to use the base of 3x3 board with x's and o's but the game needs to be tic-tac-toe of some form.

**Optional**
- Score/games won tracker
- Hosted online (https://www.heroku.com/free has some free options)
- Computer AI that plays against you
- User controls. For instance options to refresh, alter who goes first, or any other feature you can think of
- Full stack aspects such as a database to save score


Documentation for all projects
===================
Provide documentation that is useful to consumers and/or maintainers of your application.

Suggestions for documentation topics include:
- Implementation details (which data store you used, why you chose a particular technology or language, etc.)
- How to test calls to your API (curl, postman, etc)
- Features you think would be useful to add to your application
- Limitations to your application or any edge cases you found while working on the project
- Design overview and trade-offs you considered


Deliverables
===================
Please provide the code for the assignment either in a code repository (GitHub or Bitbucket) or as a zip file. If you have a deliverable that is deployed on the web please provide a link, otherwise give us instructions for running it locally.
