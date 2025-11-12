import pygame.mixer
import random
from glob import glob
import os


def play_music():
    # songs need to be a list instead of tuple if random.shuffle() is used
    os.chdir("C:/Users/admin/Desktop/Study_music")
    songs = []
    for song in glob('*.mp3'):
        songs.append(song)
    random.shuffle(songs)    # randomize the song list
    pygame.mixer.music.set_volume(0.2)  # setting the song volume
    for song in songs:    # play the songs in the list one by one
        print(f"playing '{song}' ...")
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():        # wait until the song completes
            pass


pygame.init()
play_music()