"""
This a docstring for the module.
"""
from typing import Optional


class MyClass:  # pylint: disable=too-few-public-methods
    """
    This is a docstring for the class.
    """

    def __init__(self):
        """
        Initialize for the sake of initializing
        """
        self.my_instance_var: str = "abc"

    def do_something(self) -> Optional[list]:  # another wrong type hint for mypy to find
        """
        Actually does nothing.
        :return: the value of an instance variable
        """
        # this is a super long line with: 100 < line length <= 120 to demonstrate the purpose of pyproject.toml
        self.do_somthing_else(self.my_instance_var)  # something goes wrong here. let mypy find it
        return self.my_instance_var

    def do_somthing_else(self, argument: int) -> None:
        """
        This method prints the argument
        """
        print(f"I'm doing something with '{argument}'...")
