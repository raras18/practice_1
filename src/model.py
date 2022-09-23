

class Model:
    def __init__(self):
        super(Model, self).__init__()
        self.__parameter_path = "models/camera_parameters.json"

    @property
    def parameter_path(self):
        """
        This function is to get image original from instruction controllers mvc model

        Returns:
            parameter_path = load image
        """
        # print("getter parameter_path")
        return self.__parameter_path
