import unittest

from hw.task01.task01 import cache


class TestCache(unittest.TestCase):
    def test_cache_set_1(self):
        @cache(times=2)
        def foo() -> int:
            return 1

        foo()
        foo()
        foo()
        foo()
        self.assertEqual(foo.invocations, 2)

    def test_cache_set_2(self):
        @cache(times=3)
        def foo() -> int:
            return 1

        foo()
        foo()
        foo()
        foo()
        self.assertEqual(foo.invocations, 1)

    def test_cache_set_3(self):
        @cache(times=2)
        def foo() -> int:
            return 1

        foo()
        foo()
        foo()
        foo()
        foo()
        foo()
        foo()
        self.assertEqual(foo.invocations, 3)


if __name__ == "__main__":
    unittest.main()
