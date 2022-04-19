from turtle import pos
from typing import Dict

from questionaire import Question

def make_question(
        question:str = "What is the colour of the sky?",
        answers:Dict = {'a': 'Blue', 'b': 'Green', 'c': 'Red'},
        solution:str = 'a',
        points:int = None
    ):
    d_question = {
        'question': question,
        'answers': answers,
    }
    if points:
        d_question['points'] = points
    
    return Question(d_question, solution)


def test_question():
    q = make_question()
    assert q.question == "What is the colour of the sky?"
    possible_answers = q.answers
    assert 'a' in possible_answers
    assert possible_answers['a'] == 'Blue'
    assert 'b' in possible_answers
    assert possible_answers['b'] == 'Green'
    assert 'c' in possible_answers
    assert possible_answers['c'] == 'Red'
    assert 'd' not in possible_answers

def test_question_false_answer():
    q = make_question(solution='a')
    result = q.answer('b')
    assert result == 0

def test_question_correct_answer():
    q = make_question(solution='b')
    result = q.answer('b')
    assert result == 1

def test_question_more_points():
    q = make_question(points=4, solution='a')
    result = q.answer('b')
    assert result == 0
    result = q.answer('a')
    assert result == 4
