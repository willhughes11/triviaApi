import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_cors import CORS
import random
from models import setup_db, Question, Category

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  #----------------------------------------------------------------------------#
  # After request decorators to set Access-Control-Allow
  #----------------------------------------------------------------------------#
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

  # Pagination
  #----------------------------------------------------------------------------#
  QUESTIONS_PER_PAGE = 10
  def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


  # GET endpoint handles requests for all categories
  #----------------------------------------------------------------------------#
  @app.route('/categories')
  def get_categories():
    categories = Category.query.all()
    
    if len(categories) == 0:
      abort(404)

    return jsonify({
      'success':True,
      'categories': {
        category.id: category.type for category in categories
      },
      'total_categories':len(categories)
    })


  # GET endpoint for questions
  #----------------------------------------------------------------------------#
  @app.route('/questions')
  def get_questions():
    selection = Question.query.order_by(func.random()).all()
    categories = Category.query.all()
    current_questions = paginate_questions(request, selection)

    if len(current_questions) == 0:
      abort(404)

    return jsonify({
      'success':True,
      'questions': current_questions,
      'total_questions': len(Question.query.all()),
      'categories': {
        category.id: category.type for category in categories
      }
    })

  # DELETE endpoint for questions
  #----------------------------------------------------------------------------#
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      if question is None:
        abort(404)
      
      question.delete()
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'deleted': question_id,
        'questions': current_questions,
        'total_questions': len(Question.query.all())
      })

    except:
      abort(422)

  # Create endpoint to post a new question
  #----------------------------------------------------------------------------#
  @app.route('/questions/submit', methods=['POST'])
  def create_question():
    body = request.get_json()

    new_question=body.get('question', None)
    new_answer=body.get('answer', None)
    new_category=body.get('category', None)
    new_difficulty=body.get('difficulty', None)

    try:
      question = Question(question=new_question,answer=new_answer,category=new_category,difficulty=new_difficulty)
      question.insert()

      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'created': question.id,
        'total_questions': len(Question.query.all())
      })

    except:
      abort(422)

  # GET endpoint searches for questions 
  #----------------------------------------------------------------------------#
  @app.route('/questions/search', methods=['POST'])
  def search_question():
    data = request.get_json()
    search_term = data.get('searchTerm')
    selection = Question.query.filter(Question.question.ilike('%{}%'.format(search_term))).all()
    current_questions = paginate_questions(request, selection)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(current_questions)
    })

  # GET endpoint based on category
  #----------------------------------------------------------------------------#
  @app.route('/categories/<int:category_id>/questions')
  def get_questions_by_category(category_id):
    selection = Question.query.order_by(func.random()).filter(Question.category == category_id).all()
    current_questions = paginate_questions(request, selection)

    if len(current_questions) == 0:
      abort(404)

    return jsonify({
      'success':True,
      'questions': current_questions,
      'total_questions': len(current_questions)
    })

  # Quiz endpoint
  #----------------------------------------------------------------------------#
  @app.route('/quizzes', methods=['POST'])
  def play_trivia():
    try:
      data = request.get_json()
      category = data.get('quiz_category')
      previous_questions = data.get('previous_questions')
      questions = []
      unused_questons = []

      if category['id'] == 0:
        questions = Question.query.order_by(func.random()).all()
      else:
        questions = Question.query.filter(Question.category == category['id']).order_by(func.random())
      
      for question in questions:
        if question.id not in previous_questions:
          unused_questons.append(question)

        total_unused_questions = len(unused_questons)
        if total_unused_questions == 0:
          result = None
        elif total_unused_questions > 1:
          result = unused_questons[random.randrange(
            0, len(unused_questons), 1)].format()
        elif total_unused_questions == 1:
          result = unused_questons[0].format()

        return jsonify({
          'success': True,
          'question': result,
        })
    except:
      abort(422)

  #----------------------------------------------------------------------------#
  # Error handlers
  #----------------------------------------------------------------------------#
  
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message':'bad request'
    }), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message':'resource not found'
    }), 404

  @app.errorhandler(405)
  def not_allowed(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message':'method not allowed'
    }), 405

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message':'unprocessable'
    }), 422

  @app.errorhandler(500)
  def server_error(error):
    return jsonify({
      'success': False,
      'error': 500,
      'message':'internal server error'
    }), 500

  return app    