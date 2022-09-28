

class Model:
    def __init__(self):
        """
        The backend that contains all the data logic.
        The model's job is to simply manage the data. Whether the data is from a database,
        API, or a JSON object, the model is responsible for managing it.

        """
        super(Model, self).__init__()
        self.__parameter_path = "camera_parameter/camera_parameters.json"

    @property
    def parameter_path(self):
        """
        This function is to get image original from instruction controllers mvc model

        Returns:
            parameter_path = load image
        """
        return self.__parameter_path
