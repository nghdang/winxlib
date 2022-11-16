from Xlib import X
from Xlib.display import Display as BaseDisplay
from window import WindowFactory
import time

class DisplayFactory:
    @staticmethod
    def create():
        base_display = BaseDisplay()
        return Display(base_display)

class Display(object):
    TIME_TO_SYNC = 20 / 1000 # 20ms

    def __init__(self, base_display):
        self.__base_display = base_display
        self.__root = base_display.screen().root

    def get_base(self):
        return self.__base_display

    def get_root(self):
        return self.__root

    def sync(self):
        self.__base_display.sync()
        time.sleep(self.TIME_TO_SYNC)

    def flush(self):
        self.__base_display.flush()

    def get_available_windows(self):
        NET_CLIENT_LIST = self.__base_display.intern_atom('_NET_CLIENT_LIST')
        windows = []
        for window_id in self.__root.get_full_property(NET_CLIENT_LIST, X.AnyPropertyType):
            base_window = self.__base_display.create_resource_object('window', window_id)
            window = WindowFactory.create(self, base_window)
            windows.append(window)
        return windows

    def get_windows_by_name(self, name):
        windows = []
        for _window in self.getAvailableWindows():
            if _window.get_name() == name:
                windows.append(_window)
        return windows

    def get_windows_by_class(self, classname):
        windows = []
        for _window in self.getAvailableWindows():
            if _window.get_class() == classname:
                windows.append(_window)
        return windows

    def get_active_window(self):
        NET_ACTIVE_WINDOW = self.__base_display.intern_atom('_NET_ACTIVE_WINDOW')
        window_id = self.__root.get_full_property(NET_ACTIVE_WINDOW, X.AnyPropertyType).value
        base_window = self.__base_display.create_resource_object('window', window_id)
        window = WindowFactory.create(self, base_window)
        return window

