from design.ui_template import Ui_MainWindow


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


