from src.views.design.ui_template import Ui_MainWindow
from src.moilutils import mutils


class View(Ui_MainWindow):
    def __init__(self, parent, model, controller):
        """
        The frontend or graphical user interface (GUI).
        The view's job is to decide what the user will see on their screen, and how.

        Args:
            model: The backend that contains all the data logic
            controller: The brains of the application that controls how data is displayed
        """
        super().__init__()
        self.controller = controller
        self.model = model
        self.setupUi(parent)

