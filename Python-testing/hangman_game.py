import random

def main():
    words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "him", "know", "take",
    "people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
    "than", "then", "now", "look", "only", "come", "its", "over", "think", "also",
    "back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
    "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"]
    hang_man = {
        0: ("   ", "   ", "   "),
        1: (" o ", "   ", "   "),
        2: (" 0 ", " | ", "   "),
        3: (" o ", "/| ", "   "),
        4: (" o ", "/|\\", "   "),
        5: (" o ", "/|\\", "/  "),
        6: (" o ", "/|\\", "/ \\")
    }
    random_words = random.choice(words)
    word_length_list = ['_'] * len(random_words)
    guesses = 0
    is_running = True

    while is_running:

        if guesses == 6:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            b = 0
            while b < len(hang_man[guesses]):
                print(hang_man[guesses][b])
                b += 1
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('YOU LOSE')
            print(f'word was {' '.join(random_words)}')
            is_running = False

        j = 0
        print('************************')
        while j < len(hang_man[guesses]):
            print(hang_man[guesses][j])
            j += 1
        print('************************')
        print(' '.join(word_length_list))
        guess_word = input('guess word: ').lower()

        if not guess_word.isalpha() or guess_word.isdigit() or len(guess_word) > 1:
            print('wrong enter')
        elif guess_word not in random_words:
            print('Incorrect')
            guesses += 1
            continue

        x = 0
        while x < len(random_words):
            if random_words[x] == guess_word:
                word_length_list[x] = guess_word
            x += 1
        print(' '.join(word_length_list))
        if '_' not in word_length_list:
            print(f'word: {random_words}')
            print('YOU WIN!')
            is_running = False

# start
print(main())