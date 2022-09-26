from design.ui_template import Ui_MainWindow
from moilutils import utils


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
        # utils.form_camera_parameter()
        a = utils.select_camera_name()
        print(a)
        file = utils.select_file()
        utils.connect_to_moildev(camera_parameter=file)


