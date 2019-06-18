import os
import time
import signal
from random import randint
from multiprocessing import Lock, Process, Value

# class Dummy:
#     def __init__(self, pid):
#         self.pid = pid

def wait_for_signal(other_process):
    while True:
        time.sleep(.5)
        ha = randint(0,20)
        print(ha)
        if ha == 9:
            print('Your time has come process :(', other_process.value)
            os.kill(other_process.value,signal.SIGKILL)
            break

def lumbdydum(other_process):
    time.sleep(2)
    print('system timed out')
    print('killing @', other_process.value)
    os.kill(other_process.value, signal.SIGKILL)

if __name__ == '__main__':


    idle_id = Value('i',10000)
    interrupt_id = Value('i', 11000)
    idle = Process(target=lumbdydum, args=(interrupt_id,))
    idle.start()
    print('idle started')
    

    
    interrupt = Process(target=wait_for_signal, args=(idle_id,))
    interrupt.start()
    print('interrupt started')
    interrupt_id.value = interrupt.pid
    idle_id.value = idle.pid
    

    
    idle.join()
    interrupt.join()