import ast
import random
from pygame import mixer
from contextlib import closing
import wave
from time import sleep

def load_minpairs():
    # open file with "menu" dictionary stored as string
    with open("pairs_list.txt", "r") as file:
        menu = file.read()
    # convert string into dict
    mdict = ast.literal_eval(menu)
    # print each key:value pair
    for key, value in mdict.items():
        print("{} : {} / {}".format(key, value[1], value[3]))
    return mdict


def user_selections(mdict):
    # user selects min_pair
    while True:
        try:
            select = int(input("Select minimum pair to play (or 0 for random play): "))
        except ValueError:
            print("Nope; enter NUMBER between 0 and 81.")
            continue
        if select < 0 or select > 81:
            print("Nope; enter number BETWEEN 0 and 81.")
            continue
        else:
            break
    
    # user selects number of trials
    while True:
        try:
            trials = int(input("Select number of trials (1-100): "))
        except ValueError:
            print("Nope; enter NUMBER between 1 and 100.")
            continue
        if trials < 0 or trials > 100:
            print("Nope; enter number BETWEEN 1 and 100.")
            continue
        else:
            break
    return select, trials

def random_play(trials, mdict):
    correct_answers = 0
    # initialize pygame mixer
    mixer.init()
    # for each trial...
    for trial in range(trials):
        # randomly select a aound pair...
        pair = random.randint(1, 81)
        # get sound pair from mdict
        pair_sounds = mdict[pair]
        # randomly select 1 of 2 sounds in pair...
        sound = random.randint(1, 2)
        # select sound file and word string from selected pair
        if sound == 1:
            sfile = pair_sounds[0]
            word1 = pair_sounds[1]
            word2 = pair_sounds[3]
        else:
            sfile = pair_sounds[2]
            word1 = pair_sounds[1]
            word2 = pair_sounds[3]
        # load sound file
        # determine length of wav files = (number of frames / framerate) + buffer
        with closing(wave.open(sfile,'r')) as s1:
            frames = s1.getnframes()
            rate = s1.getframerate()
            dur1 = (frames / float(rate)) + .02
        sound1 = mixer.Sound(sfile)
        # play sound
        sound1.play()
        sleep(dur1)
        # ask user for selection
        print()
        print("-------------------------")
        print("Trial {}".format(trial+1))
        print("What sound did you hear?")
        print("1) {} or 2) {}?".format(word1, word2))
        while True:
            try:
                answer = int(input("Enter 1 or 2: "))
            except ValueError:
                continue
            if answer < 1 or answer > 2:
                continue
            else:
                break
        # check answer
        if answer == sound:
            print("Correct!")
            correct_answers += 1
        else:
            print("Sorry, that's not correct.")
    # at end of trials, print results
    print()
    print()
    print("Trials played: {}".format(trials))
    print("Correct answers: {}".format(correct_answers))
    print("Wrong answers: {}".format(trials - correct_answers))
    print("--------------------")
    print("Score: {}".format(float(correct_answers)/trials))
    print()
    print()

def selected_play(select, trials, mdict):
    correct_answers = 0
    # initialize pygame mixer
    mixer.init()
    # get sound pair from mdict
    pair_sounds = mdict[select]
    # load sound files and words
    sfile1 = pair_sounds[0]
    word1 = pair_sounds[1]
    sfile2 = pair_sounds[2]
    word2 = pair_sounds[3]
    # determine length of wav files = (number of frames / framerate) + buffer
    with closing(wave.open(sfile1,'r')) as s1:
        frames = s1.getnframes()
        rate = s1.getframerate()
        dur1 = (frames / float(rate)) + .02
    with closing(wave.open(sfile2,'r')) as s2:
        frames = s2.getnframes()
        rate = s2.getframerate()
        dur2 = (frames / float(rate)) + .02
    # load wav files
    sound1 = mixer.Sound(sfile1)
    sound2 = mixer.Sound(sfile2)
    # for each trial...
    for trial in range(trials):
        # randomly select 1 of 2 sounds in pair...
        sound = random.randint(1, 2)
        # play sound
        if sound == 1:
            sound1.play()
            sleep(dur1)
        else:
            sound2.play()
            sleep(dur2)
        # ask user for selection
        print()
        print("-------------------------")
        print("Trial {}".format(trial+1))
        print("What sound did you hear?")
        print("1) {} or 2) {}?".format(word1, word2))
        while True:
            try:
                answer = int(input("Enter 1 or 2: "))
            except ValueError:
                continue
            if answer < 1 or answer > 2:
                continue
            else:
                break
        # check answer
        if answer == sound:
            print("Correct!")
            correct_answers += 1
        else:
            print("Sorry, that's not correct.")
    # at end of trials, print results
    print()
    print()
    print("Trials played: {}".format(trials))
    print("Correct answers: {}".format(correct_answers))
    print("Wrong answers: {}".format(trials - correct_answers))
    print("--------------------")
    print("Score: {}".format(float(correct_answers)/trials))
    print()
    print()
        
    

if __name__ == '__main__':
    menu = load_minpairs()
    select, trials = user_selections(menu)
    if select == 0:
        random_play(trials, menu)
    else:
        selected_play(select, trials, menu)