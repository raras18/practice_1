# import necessary library you used here
from src.views.image_processing import Ui_MainWindow
from src.models.moilutils import mutils
from src.models.model import Model
import pyqtgraph as pq
from pyqtgraph.Qt import QtCore, QtGui, uic
import cv2
# import matplotlib.pylab as plt
from matplotlib import pyplot as plt

class Controller(Ui_MainWindow):
    def __init__(self, parent):
        """
        The controllers class is The brains of the application that controls how data is displayed.
        The controller's responsibility is to pull, modify, and provide data to the user.
        Essentially, the controllers is the link between the view and model.

        Args:
            model: The backend that contains all the data logic
        """
        super().__init__()
        self.setupUi(parent)
        self.model = Model()
        # self.horizontalSlider.setMinimum(0)
        # self.horizontalSlider.setMaximum(255)
        # self.horizontalSlider.setValue(1)

        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.filtering)
        self.horizontalSlider.valueChanged.connect(self.slide)

    def open_file(self):
        file = mutils.select_file(title="select image", file_filter="*.jpg, *.png")
        self.img = mutils.read_image(file)
        mutils.show_image_to_label(self.label, self.img, 400)
        # image_filter = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # mutils.show_image_to_label(self.label_2, image_filter, 400)
        # mutils.show_image_to_label(self.label_5, hist2, 400)
        hist = cv2.calcHist([self.img], [0], None, [256], [0, 256])
        plt.plot(hist)
        plt.show()
    def filtering(self):
        try:
            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            mutils.show_image_to_label(self.label_2, gray, 400)
            # hist = cv2.calcHist([self.label_2], [0], None, [256], [0, 256])
            # plt.plot(hist)
            # mutils.show_image_to_label(self.label_5, plt.show(), 400)
            self.plotwi
        except:
            print("Input the image first")

    def slide(self, value):
        self.label_3.setText(str(value))
        value_text = self.label_3.text()
        self.value = int(value_text)
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.image = cv2.blur(gray, (self.value, self.value))
        # cv2.imshow("test", new_image)
        mutils.show_image_to_label(self.label_2, self.image, 400)
