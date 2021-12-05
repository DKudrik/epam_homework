import unittest

from hw.task03.task03 import Filter, make_filter


class TestFilter(unittest.TestCase):
    def test_filter_object_work(self):
        positive_even = Filter(
            lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
        )
        result = positive_even.apply(range(10))
        self.assertEqual(result, [2, 4, 6, 8])

    def test_make_filter_func(self):
        sample_data = [
            {
                "name": "Bill",
                "last_name": "Gilbert",
                "occupation": "was here",
                "type": "person",
            },
            {
                "is_dead": True,
                "kind": "parrot",
                "type": "bird",
                "name": "polly",
            },
        ]
        result = make_filter(name="polly", type="bird").apply(sample_data)
        self.assertEqual(
            result,
            [{"is_dead": True, "kind": "parrot", "type": "bird",
              "name": "polly"}],
        )


if __name__ == "__main__":
    unittest.main()
