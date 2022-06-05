
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.app import App
from kivy.graphics import Color, Line
from numpy import spacing


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 10
    V_LINES_NB = .1     #pourcentage in screen width
    vertical_lines = []

    H_NB_LINES = 15
    H_LINES_NB = .2     #pourcentage in screen width
    horizontal_lines = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        #print("INIT W:" + str(self.width) + " H:"+ str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()
    def on_parent(self, widget, perent):
        
        print("on parent W:" + str(self.width) + " H:"+ str(self.height))

    def on_size(self, *args):
        self.update_vertical_lines()
        self.update_horizontal_lines()
        #print("on size W:" + str(self.width) + " H:"+ str(self.height))
        #self.perspective_point_x = self.width/2
        #self.perspective_point_y = self.height*3/4
        
    def on_perspective_point_x(self, widget, value):
        #print('PX: '+ str(value))
        pass
    def on_perspective_point_y(self, widget, value):
        #print('PY: '+ str(value))
        pass
    
    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(self.V_NB_LINES):
                self.vertical_lines.append(Line())
        
    def update_vertical_lines(self):
        central_line_x = self.width/2
        spacing = self.V_LINES_NB * self.width
        #line_offset = central_line_x + spacing/2
        offset = -int(self.V_NB_LINES/2)+0.5
        for i in range(self.V_NB_LINES):
            line_x = int(central_line_x + offset * spacing)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, int(self.height))
            self.vertical_lines[i].points = [x1, y1 ,x2, y2]
            offset += 1

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(self.H_NB_LINES):
                self.horizontal_lines.append(Line())
        
    def update_horizontal_lines(self):
        central_line_x = self.width/2
        spacing = self.V_LINES_NB * self.width
        #line_offset = central_line_x + spacing/2
        offset = -int(self.V_NB_LINES/2)+0.5
        x_min = central_line_x + offset * spacing
        x_max = central_line_x - offset * spacing
        spacing_y = self.H_LINES_NB * self.height
        for i in range(self.H_NB_LINES):
            line_y = i * spacing_y
            x1, y1 = self.transform(x_min, line_y)
            x2, y2 = self.transform(x_max, line_y)
            self.horizontal_lines[i].points = [x1, y1 ,x2, y2]

    def transform(self, x, y):
        #return self.transform_2D(x, y)
        return self.transform_persperctive(x, y)

    def transform_2D(self, x, y):
        return int(x), int(y)

    def transform_persperctive(self, x ,y):
        lin_y = y * self.perspective_point_y / self.height
        if lin_y > self.perspective_point_y:
            lin_y = self.perspective_point_y
        diff_y = self.perspective_point_y - lin_y
        facteur_y = diff_y / self.perspective_point_y
        facteur_y = pow(facteur_y, 2)  
        diff_x = x - self.perspective_point_x
        tr_y = self.perspective_point_y - facteur_y * self.perspective_point_x
        
        
        
        
        offset_x = diff_x * facteur_y
        tr_x = self.perspective_point_x + offset_x
        
        return int(tr_x), int(tr_y)





class GalaxyApp(App):
    pass


GalaxyApp().run()