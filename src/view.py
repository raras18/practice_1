from design.ui_template import Ui_MainWindow
from moilutils import mutils


class View(Ui_MainWindow):
    def __init__(self, parent, model, controller):
        """

        Args:
            model:
            controller:
        """
        super().__init__()
        self.controller = controller
        self.model = model
        self.setupUi(parent)


