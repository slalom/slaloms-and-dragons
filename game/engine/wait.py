import time

wait_symbol = r"/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\| "


def wait_with_animation(animation, seconds=3):
    rate = 0.1
    loops = seconds / rate
    for i in range(int(loops)):
        print(' \r ' + animation[i % len(animation)], end='\r')
        time.sleep(rate)


def roll_wait():
    wait_with_animation(wait_symbol)


def step_wait():
    animation = '🐉🗡️🛡️⚔️🐲✨🏹🐉'
    wait_with_animation(animation)


def quick_spin():
    for i in wait_symbol:
        print("\r", i, end="")
        time.sleep(.04)

def just_wait(): 
    time.sleep(1.4)
