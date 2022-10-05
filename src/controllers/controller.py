# import necessary library you used here
from src.views.ui_template import Ui_MainWindow


class Controller(Ui_MainWindow):
    def __init__(self, parent, model):
        """
        The controllers class is The brains of the application that controls how data is displayed.
        The controller's responsibility is to pull, modify, and provide data to the user.
        Essentially, the controllers is the link between the view and model.

        Args:
            model: The backend that contains all the data logic
        """
        super().__init__()
        self.setupUi(parent)
        self.model = model
