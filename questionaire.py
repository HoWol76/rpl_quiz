from typing import Dict, List


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

    # @property
    # def solution(self):
    #     return self.__solution

    @property
    def points(self):
        return self.__points

class Questionaire:
    pass