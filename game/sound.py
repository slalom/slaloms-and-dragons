from pygame import mixer

def play_music():
    mixer.init()
    mixer.music.load("game/media/intro_music.mp3")
    mixer.music.play()
