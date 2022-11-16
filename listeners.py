import threading

class EventListener(threading.Thread):
    SLEEP_PERIOD = 100 / 1000 # 100ms

    def __init__(self, display, name=''):
        self._stop_event = threading.Event()
        threading.Thread.__init__(self, name=name)

        self._display = display

    def join(self, timeout=None):
        self._stop_event.set()
        threading.Thread.join(self, timeout)

    def run(self):
        base_display = self._display.get_base()
        while self._stop_event.is_set():
            self._stop_event.wait(self.SLEEP_PERIOD)

            # Wait for display to send something, or a timeout of one second
            readable, w, e = select.select([base_display], [], [], 1)

            # if no files are ready to be read, it's an timeout
            if not readable:
                self.handle_timeout()

            # if display is readable, handle as many events as have been received
            elif base_display in readable:
                i = base_display.pending_events()
                while i > 0:
                    event = base_display.next_event()
                    self.handle_event(event)
                    i = i - 1

            # loop around to wait for more things to happen

    def handle_timeout(self):
        pass

    def handle_event(self, event):
        pass
