questions = [
    'how many legs does a spider have ?',
    'how many legs does human have ?',
    'how is it possible to human can fly ?',
    'why javascript is popular then python ?',
    'why java is not javascript ?',
]
answers = [
    'A: 8, B: 4, C: 11, D: 2',
    'A: 4, B: 1, C: 2, D: 3',
    'A: because of wings, B: because we can, C: because of gravity, D: because of jetpack',
    'A: javascript is easy, B: javascript is hard, C: javascript is not popular, D: javascript is better',
    'A: because Java is another Language, B: because Java is not javascript, C: because Java is not popular, D: those are same',
]
correct_answers = [
    'A',
    'C',
    'D',
    'D',
    'A'
]
guesses = [
# appended uesr answers here
]
scores = 0

i = 0
while i < len(questions):
    print('--------------------------------------------------------')
    print(questions[i])
    options = answers[i].split(', ')
    j = 0
    while j < len(options):
        print(options[j])
        j += 1
    guess = input('Enter your answer: ')
    guesses.append(guess.upper())
    if guesses[i] == correct_answers[i]:
        print('Correct!')
        scores += 1
    else:
        print('Incorect!')
    i += 1
print('______________Results_______________')
print(f'Test answers: {correct_answers}')
print(f'your answers: {guesses}')
print(f'scores: Correct: {scores}, Incorrect: {len(questions) - scores}')
percent = (scores / len(questions)) * 100
print(f'you taken {percent:.2f}% of the test')
if(percent >= 60):
    print('you passed 🎉')
else:
    print('you failed 💀')