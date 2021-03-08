"""
This a docstring.
"""


class MyClass:  # pylint: disable=too-few-public-methods
    """ "
    This class is just an example class.
    """

    def __init__(self):
        """
        Initialize for the sake of initializing
        """

    def do_something(self) -> bool:  # pylint: disable=no-self-use
        """
        Actually does nothing
        :return:
        """
        return True
