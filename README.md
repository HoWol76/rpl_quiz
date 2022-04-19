# Too complicated, let's start easier

## Classes

### `Quiz` -- The main driver of the quiz.

#### Inputs:
- Filename of question database
- `Quiz_UI_Callback` instance to interact with the user

#### Methods
- `start_quiz() -> None` Resets the quiz.
- 

### `Quiz_Scorer` Dataclass
- `num_questions`
- `num_answered`
- `num_correct`

### `Quiz_UI_Callback` -- Abstract Class

#### Abstract methods:
- `pose_question(question:str) -> Null` poses the question
- `add_answer(answer:str) -> Null` adds a possible multiple-choice answer
