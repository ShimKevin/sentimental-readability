from cs50 import get_string
import re


def main():
    text = get_string('Text: ')

    words = get_words_count(text)
    letters = get_letters_count(text) / words
    sentences = get_sentences_count(text) / words

    calculate_grade(letters, words, sentences)


def get_letters_count(text):
    letters = re.findall('[A-Za-z]', text)
    letters_count = len(letters)
    return letters_count


def get_words_count(text):
    words = text.split(' ')
    words_count = len(words)
    return words_count


def get_sentences_count(text):
    matches = re.findall('[!.?]', text)
    sentences_count = len(matches)
    return sentences_count


def calculate_grade(l, w, s):
    grade = round(0.0588 * (l * 100) - 0.296 * (s * 100) - 15.8)

    if grade < 1:
        print('Before Grade 1')
    elif grade >= 16:
          print('Grade 16+')
    else:
        print(f'Grade {grade}')


main()
