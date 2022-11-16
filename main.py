from display import DisplayFactory
from listeners import EventListener

def main():
    display = DisplayFactory.create()
    listener = EventListener(display)
    listener.start()
    while True:
        if input('Continue [y/n]? ') == 'n':
            break
    listener.join()

if __name__ == '__main__':
    main()
