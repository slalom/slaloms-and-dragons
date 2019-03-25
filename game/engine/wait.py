import time


def wait_with_animation(seconds=3):
    rate = 0.1
    loops = seconds / rate
    animation = '|/-\\'
    idx = 0
    for i in range(int(loops)):
        print(animation[i % len(animation)], end='\r')
        time.sleep(rate)
