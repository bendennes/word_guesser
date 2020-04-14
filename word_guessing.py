# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:09:42 2020

@author: bdenn
"""

import string
import json

with open('english_words_by_length.json', 'r') as fp:
    all_words = json.load(fp)

def words_by_incorrect_letter(words, incorrect_letter):
    return [word for word in words if incorrect_letter not in word]

def words_by_correct_letter(words, correct_letter, places):
    new_words = []
    
    for word in words:
        reject = False
        for place in places:
            if word[place-1] != correct_letter:
                reject = True
        if word.count(correct_letter) > len(places):
            reject = True
        if reject == False:
            new_words.append(word) 
    return new_words

def letter_frequency(words):
    alphabet = dict.fromkeys(string.ascii_lowercase,0)
    for word in words:
        for letter in set(word):
            alphabet[letter] += 1
    return alphabet

def get_guess(words, letters_guessed):
    frequencies = letter_frequency(words)
    frequencies = sorted(frequencies, key=frequencies.get)
    frequencies.reverse()
    frequencies = [item for item in frequencies if item not in letters_guessed]
    return frequencies[0]

def game():
    print("Think of a word (in English)")
    length = int(input("How many letters does the word have? "))
    
    words = all_words[str(length)]
    
    letters_guessed = []
    iterations = 0
    guessed = False
    
    while not guessed:
        guess = get_guess(words, letters_guessed)
        
        print("Does your word contain the letter", guess, "?")
        response = input("Give places in word (numbers separated by commas), or 0 if it doesn't: ")
        
        if response == "0":
            words = words_by_incorrect_letter(words, guess)
            
        else:
            places = response.split(",")
            places = [int(x) for x in places]
    
            #mask = get_places_mask(places, length)
            words = words_by_correct_letter(words, guess, places)
            
        iterations += 1   
        
        letters_guessed.append(guess)
        
        if len(words) == 1:
            print("Your word is ",words[0])
            guessed = True








