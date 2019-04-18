from pygame import mixer

def play_music():
    mixer.init()
    print(mixer.get_init()) 
    mixer.music.load("game/media/intro_music.mp3")
    mixer.music.play()

play_music()