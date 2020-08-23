# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API Documentation

### Trivia Endpoints
- GET /categories
- GET /questions
- DELETE /questions/question_id
- POST /questions/submit
- POST /questions/search
- GET /categories/category_id/questions
- POST /quizzes

### GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
```
Example: curl http://localhost:5000/categories
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true,
  "total_categories": 6
}
```

### GET '/questions'
- A dictionary of of categories and a random list of questions in which the answer, difficulty, id, question, and category are all fetched
- Request Arguments: None
- Returns: A categories object a single key: categories and an object of multiple keys: answer, category, difficulty, id, and question. 
```
Example: curl http://localhost:5000/questions
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Death",
      "category": 1,
      "difficulty": 4,
      "id": 26,
      "question": "What is the 8th gate, the gate of?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 21
}
```
### DELETE '/questions/int:question_id'
- Deletes a question based on question id
- Request Arguments: None
- Returns: An object with a multiple values: deleted question id, question list, success, and total questions. 
```
Example: curl -X DELETE http://127.0.0.1:5000/questions/21
{
  "deleted": 21,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```

### POST '/questions/submit'
- Creates a trivia question, with an answer, difficulty rating and category
- Request Arguments: {question, answer, category, difficulty}
- Returns: Question id, success, and the total amount of questions
```
Example: curl -X POST http://127.0.0.1:5000/questions/submit -H "Content-Type: application/json" -d '{"question":"Who was Goku fighting when he unlocked Super Saiyan?","answer":"Frieza", "category":4, "difficulty":1}'
{
  "created": 27,
  "success": true,
  "total_questions": 20
}
```

### POST '/questions/search'
- Fetches the questions that match the term that is searched
- Request Arguments: {searchTerm}
- Returns: Questions that matched the search term, success, and the total amount of questions that matched the search term. 
```
Example: curl -X POST http://127.0.0.1:5000/questions/search -H "Content-Type: application/json" -d '{"searchTerm":"Goku"}'
{
  "questions": [
    {
      "answer": "Frieza",
      "category": 4,
      "difficulty": 1,
      "id": 27,
      "question": "Who was Goku fighting when he unlocked Super Saiyan?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```

### GET '/categories/category_id/questions'
- Fetches questions based on category id
- Request Arguments: None
- Returns: Questions that are under the category, success, and the total amount of questions that are under the category. 
```
Example: curl http://127.0.0.1:5000/categories/4/questions
{
  "questions": [
    {
      "answer": "Frieza",
      "category": 4,
      "difficulty": 1,
      "id": 27,
      "question": "Who was Goku fighting when he unlocked Super Saiyan?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    }
  ],
  "success": true,
  "total_questions": 5
}
```

### POST '/quizzes'
- Fetches a question, that has not already been fetched with in the same trivia session
- Request Arguments: {preivous_questions, quiz_category}
- Returns: A question object with the answer, category, difficulty, id, and question key value pairs, and success. 
```
Example: curl -X POST http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d '{"previous_questions":[],"quiz_category":{"type":"history","id":"4"}}'
{
  "question": {
    "answer": "Frieza",
    "category": 4,
    "difficulty": 1,
    "id": 27,
    "question": "Who was Goku fighting when he unlocked Super Saiyan?"
  },
  "success": true
}
```

### Error Handling'
```
{
  "error": 400, 
  "message": "bad request", 
  "success": false
}
```
```
{
  "error": 404, 
  "message": "resource not found", 
  "success": false
}
```
```
{
  "error": 405, 
  "message": "method not allowed", 
  "success": false
}
```
```
{
  "error": 422, 
  "message": "unprocessable", 
  "success": false
}
```
```
{
  "error": 500, 
  "message": "internal server error", 
  "success": false
}
```

## Testing
To run the tests, 
cd to the backend directory, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python3 test_flaskr.py 
```