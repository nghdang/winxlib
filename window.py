from Xlib import X

class WindowFactory:
    @staticmethod
    def create(display, base_window):
        return Window(display, base_window)

class Window(object):
    def __init__(self, display, base_window):
        self.__display = display
        self.__base_window = base_window
        self.__parent = base_window.query_tree().parent

    def get_id(self):
        return self.__base_window.id

    def get_name(self):
        return self.__base_window.get_wm_name()

    def get_class(self):
        return self.__base_window.get_wm_class()

    def get_location(self):
        parent_geometry = self.__parent.get_geometry()
        self_geometry = self.__base_window.get_geometry()
        return parent_geometry.x + self_geometry.x, parent_geometry.y + self_geometry.y

    def get_size(self):
        self_geometry = self.__base_window.get_geometry()
        return self_geometry.width, self_geometry.height

    def move(self, x, y):
        curX, curY = self.get_location()
        if curX != x or curY != Y:
            self.__base_window.configure(x=x, y=y)
            self.__display.sync()

    def resize(self, width, height):
        curWidth, curHeight = self.get_size()
        if curWidth != width or curHeight != height:
            self.__base_window.configure(width=width, height=height)
            self.__display.sync()

    def activate(self):
        self.__base_window.set_input_focus(X.RevertToParent, X.CurrentTime)
        self.__base_window.configure(state=X.Above)
        self.__display.sync()
