from PySide2.QtGui import QColor
from PySide2.QtWidgets import *

_NORMAL_LEAK = 20
_NORMAL_TEMPERATURE = 30
_NORMAL_DEPTH = 3
_NORMAL_ACCELERATION = 5
_CRITICAL_LEAK = 50
_CRITICAL_TEMPERATURE = 50
_CRITICAL_DEPTH = 5
_CRITICAL_ACCELERATION = 10


class Indicator(QGraphicsScene):
    def __init__(self, normal, critical, name, unit, number):
        super(Indicator, self).__init__()
        self.normal = normal
        self.critical = critical
        self.name = name
        self.unit = unit
        self.number = number
        self.indicator = ("Normal", "Attention", "Critical")
        self.color = (QColor(157, 206, 209), QColor(255, 150, 0), QColor(255, 0, 0))
        self.color_indicator = self.color[0]

        self._config()

    def _config(self) :
        self._set_indicator()

    def _set_indicator(self):
        self.text_name = QGraphicsTextItem()
        self.text_number = QGraphicsTextItem()
        self.text_indicator = QGraphicsTextItem()
        self.addItem(self.text_name)
        self.addItem(self.text_number)
        self.addItem(self.text_indicator)
        self.text_name.setHtml(self.name)
        self.text_number.setHtml(str(self.number) + self.unit)
        self.text_indicator.setHtml(self._indicator())
        self.text_name.setPos(45, 25)
        self.text_number.setPos(45, 50)
        self.text_indicator.setPos(45, 75)

    def _color(self, color):
        self.text_indicator.setDefaultTextColor(color)
        self.text_number.setDefaultTextColor(color)
        self.text_name.setDefaultTextColor(color)

    def _indicator(self):
        if self.number < self.normal:
            self._color(self.color[0])
            return self.indicator[0]
        elif (self.number >= self.normal) & (self.number < self.critical):
            self._color(self.color[1])
            return self.indicator[1]
        elif self.number >= self.critical:
            self._color(self.color[2])
            return self.indicator[2]

    def _get_scene(self):
        return self.scene_indicator


class Leak_Sensor(Indicator):

    def __init__(self):
        super(Leak_Sensor, self).__init__(_NORMAL_LEAK, _CRITICAL_LEAK, "Leak Sensor", "%", 50)


class Temperature(Indicator):

    def __init__(self):
        super().__init__(_NORMAL_TEMPERATURE, _CRITICAL_TEMPERATURE, "Temperature", "℃", 32)


class Depth(Indicator):

    def __init__(self):
        super().__init__(_NORMAL_DEPTH, _CRITICAL_DEPTH, "Depth", "m", 3.5)


class Acceleration(Indicator):

    def __init__(self):
        super().__init__(_NORMAL_ACCELERATION, _CRITICAL_ACCELERATION, "Acceleration", "m", 4.5)


class Rotation(QGraphicsScene):

    def __init__(self):
        super(Rotation, self).__init__()
        self.number_rotation_x = 30
        self.number_rotation_y = 65
        self.number_rotation_z = 27
        self._set_rotation()

    def _set_rotation(self):
        self.text_name = QGraphicsTextItem()
        self.text_x = QGraphicsTextItem()
        self.text_y = QGraphicsTextItem()
        self.text_z = QGraphicsTextItem()
        self.text_name.setDefaultTextColor(QColor(157, 206, 209))
        self.text_x.setDefaultTextColor(QColor(157, 206, 209))
        self.text_y.setDefaultTextColor(QColor(157, 206, 209))
        self.text_z.setDefaultTextColor(QColor(157, 206, 209))
        self.addItem(self.text_name)
        self.addItem(self.text_x)
        self.addItem(self.text_y)
        self.addItem(self.text_z)
        self.text_name.setHtml("Rotation")
        self.text_x.setHtml("x: " + str(self.number_rotation_x) + "°")
        self.text_y.setHtml("y: " + str(self.number_rotation_y) + "°")
        self.text_z.setHtml("z: " + str(self.number_rotation_z) + "°")
        self.text_name.setPos(45, 25)
        self.text_x.setPos(27, 50)
        self.text_y.setPos(63, 50)
        self.text_z.setPos(45, 75)
