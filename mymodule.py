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
        self.foo = "foo"

    def do_something(self) -> str:
        """
        Actually does nothing.
        :return: the value of foo
        """
        return self.foo
