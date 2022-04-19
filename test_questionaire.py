import pytest
from questionaire import Questionaire, AlreadyAnswered

def make_questionaire():
    return Questionaire('test_questions.yaml')


def test_length():
    q = make_questionaire()
    assert len(q) == 2

def test_remaining_at_beginning():
    q = make_questionaire()
    assert q.remaining == 2

def test_maxpoints():
    q = make_questionaire()
    assert q.maxpoints == 3

def test_initial_points():
    q = make_questionaire()
    assert q.points == 0

def test_questions_remaining_true():
    q = make_questionaire()
    assert q.questions_remaining

def test_give_right_answer():
    q = make_questionaire()
    points, _ = q.answer('a')
    assert points == 1
    assert q.points == 1

def test_give_wrong_answer():
    q = make_questionaire()
    points, solution = q.answer('b')
    assert points == 0
    assert q.points == 0
    assert solution == 'a'

def test_answer_twice():
    q = make_questionaire()
    points, _ = q.answer('b')
    with pytest.raises(AlreadyAnswered):
        points, _ = q.answer('a')

def test_solution_before():
    q = make_questionaire()
    result = q.solution
    assert result == "_"

def test_solution_after():
    q = make_questionaire()
    q.answer('b')
    result = q.solution
    assert result == 'a'

def test_first_question():
    q = make_questionaire()
    assert q.question == "What colour is the sky?"

def test_second_question():
    q = make_questionaire()
    q.next()
    assert q.question == "Which force keeps an aircraft in the air?"

def test_next_past_last_question():
    q = make_questionaire()
    q.next()
    q.next()
    assert q.question == "What colour is the sky?"

def test_next_raise_ValueError():
    q = make_questionaire()
    q.answer('b')
    q.next()
    q.answer('b')
    with pytest.raises(ValueError):
        q.next()