from typing import Dict, List
import yaml


class AlreadyAnswered(Exception):
    pass


class Question:
    def __init__(self, d_question:Dict, solution:str):
        assert 'question' in d_question
        assert 'answers' in d_question
        assert type(d_question['answers']) == dict
        self.__question = d_question['question']
        self.__answers = d_question['answers']
        self.__solution = solution
        assert solution in self.__answers
        if 'points' in d_question:
            self.__points = d_question['points']
        else:
            self.__points = 1
    
    @property
    def question(self) -> str:
        return self.__question

    @property
    def answers(self) -> List[Dict]:
        return self.__answers

    def answer(self, answer:str) -> int:
        """(str) -> int

        Returns the number of points for this answer.
        """
        if answer == self.__solution:
            return self.__points
        # elif answer == self.__answers[self.__solution]:
        #     return self.__points
        else:
            return 0

    @property
    def solution(self):
        return self.__solution

    @property
    def points(self):
        return self.__points


class Questionaire:
    def __init__(self, questionaire_file:str):
        self.__read_questionaire(questionaire_file)
        self.__active = 0
        self.__active_question = self.__questionaire[0]
        self.__points = [0]*len(self)
        self.__answered = [False]*len(self)

        self.__maxpoints = sum([q.points for q in self.__questionaire])

    def __read_questionaire(self, questionaire_file:str):
        with open(questionaire_file, 'r') as qfile:
            questionaire = yaml.safe_load(qfile)
            assert 'questions' in questionaire
            assert 'solutions' in questionaire
            self.__questionaire = []
            for question in questionaire['questions']:
                solution = questionaire['solutions'][question['number']]
                self.__questionaire.append(
                    Question(question, solution)
                )

    def __len__(self):
        return len(self.__questionaire)

    @property
    def remaining(self):
        return self.__answered.count(False)

    @property
    def maxpoints(self):
        return self.__maxpoints

    @property
    def points(self):
        return sum(self.__points)

    @property
    def questions_remaining(self):
        return not all(self.__answered)

    def answer(self, answer:str):
        if self.__answered[self.__active]:
            raise AlreadyAnswered("This question was already answered.")
        result = self.__active_question.answer(answer)
        self.__points[self.__active] = result
        self.__answered[self.__active] = True
        return result, self.__active_question.solution

    @property
    def solution(self):
        if self.__answered[self.__active]:
            return self.__active_question.solution
        return '_'

    @property
    def question(self):
        return self.__active_question.question

    def next(self):
        if self.remaining == 0:
            raise ValueError("No questions remaining")
        self.__active += 1
        self.__active %= len(self)
        while self.__answered[self.__active]:
            self.__active += 1
            self.__active %= len(self)
        self.__active_question = self.__questionaire[self.__active]

    @property
    def answers(self):
        return self.__active_question.answers