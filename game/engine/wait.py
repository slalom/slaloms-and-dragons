import time


def wait_with_animation(seconds=3):
    rate = 0.1
    loops = seconds / rate
    animation = '🐉🗡️🛡️⚔️🐲✨🏹🐉'
    for i in range(int(loops)):
        print(' \r ' + animation[i % len(animation)], end='\r')
        time.sleep(rate)


def quick_spin():
    simulate_pause = r"/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\| "
    for i in simulate_pause:
        print("\r", i, end="")
        time.sleep(.04)
