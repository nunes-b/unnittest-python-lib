import unittest


def str_to_bool(value):
    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f"{value} must be a string")

    true_values = ["y", "yes"]
    false_values = ["no", "n"]

    if value in true_values:
        return True
    if value in false_values:
        return False


def sum(a, b):
    return a + b


class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        self.assertTrue(str_to_bool("y"))
        self.assertTrue(str_to_bool("yes"))

    def test_n_is_false(self):
        self.assertFalse(str_to_bool("n"))
        self.assertFalse(str_to_bool("no"))

    def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            str_to_bool(1)

    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(1, 3), 4)


if __name__ == "__main__":
    unittest.main()
