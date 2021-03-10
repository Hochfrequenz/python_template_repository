"""
This a docstring for the module.
"""


class MyClass:  # pylint: disable=too-few-public-methods
    """
    This is a docstring for the class.
    """

    def __init__(self):
        """
        Initialize for the sake of initializing
        """
        pass

    def do_something(self) -> bool:  # pylint: disable=no-self-use
        """
        Actually does nothing
        :return:
        """
        return True
