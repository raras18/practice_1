# import necessary library you used here
from moilutils import mutils


class Controller:
    def __init__(self, model):
        """
        The controllers class is The brains of the application that controls how data is displayed.
        The controllers's responsibility is to pull, modify, and provide data to the user.
        Essentially, the controllers is the link between the view and model.

        Args:
            model: The backend that contains all the data logic
        """
        super().__init__()
        self.model = model
