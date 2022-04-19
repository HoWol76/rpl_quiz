from typing import List
from questionaire import Questionaire

def break_line(text: str, width:int = 40):
    result = []
    for line in text.splitlines():
        while True:
            if len(line) <= width:
                result.append(line)
                break
            idx = line[:width].rfind(' ')
            result.append(line[:idx])
            line = line[idx+1:]
    return result

def score_string(points, maxpoints):
    fraction = (points * 100) // maxpoints
    return f"{points}/{maxpoints} ({fraction}%)"

def main():
    questionaire = Questionaire('pre-circuit_solo.yaml')
    while questionaire.remaining > 0:
        question = questionaire.question
        for line in break_line(question, 60):
            print(line)
        for key, value in questionaire.answers.items():
            lines = break_line(value, 55)
            print(f"{key:>3}: {lines[0]}")
            for line in lines[1:]:
                print(f"     {line}")    
        answer = ""
        while answer not in questionaire.answers:
            answer = input(f"Make your choice: ")
        points, correct = questionaire.answer(answer)
        if points > 0:
            print("Correct!")
        else:
            print(f"Incorrect. Correct was {correct}")
        print(f"Points: {score_string(questionaire.points, questionaire.maxpoints)}")
        if questionaire.remaining > 0:
            questionaire.next()
        print("===========================================")
        print("")
    print(f"Final Score: {score_string(questionaire.points, questionaire.maxpoints)}")


if __name__ == '__main__':
    main()