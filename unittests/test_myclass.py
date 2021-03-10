from mymodule import MyClass


class TestMyClass:
    """
    A class with pytest unittests.
    """

    def test_something(self):
        my_class = MyClass()
        assert my_class.do_something() == "foo"
