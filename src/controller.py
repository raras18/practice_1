# import necessary library you used here
from moilutils import utils


class Controller:
    def __init__(self, model):
        super().__init__()
        self.model = model
        utils.form_camera_parameter()