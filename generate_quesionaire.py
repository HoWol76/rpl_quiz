import yaml
from string import ascii_lowercase as letters

def main():
    filename = input("Enter filename: ")
    questionaire = []
    number = 0
    while True:
        q = {}
        number += 1
        q['number'] = number
        q['question'] = input(f"Question {number}: ")
        if len(q['question']) == 0: break
        answers = {}
        for idx in letters:
            a = input(f"{idx}: ")
            if len(a) == 0: break
            answers[idx] = a
        q['answers'] = answers
        questionaire.append(q)

    with open(filename, 'w') as f:
        yaml.dump(questionaire, f)

if __name__ == '__main__':
    main()