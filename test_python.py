

import unittest


class TestSumaFunction(unittest.TestCase):
    def test_suma_15_10(self):
        self.assertEqual(suma(15, 10), 25)

    def test_suma__10_10(self):
        self.assertEqual(suma(-10, 10), 0)

    def test_suma__2__15(self):
        self.assertEqual(suma(-2, -15), -17)

    def test_suma_6__15(self):
        self.assertEqual(suma(6, -15), -57)

    def test_suma__2__10(self):
        self.assertEqual(suma(-2, -10), -17)

    def test_suma__3__10(self):
        self.assertEqual(suma(-3, -10), -17)


def evaluate_code():
    try:
        import js
        import unittest
        import io

        stream = io.StringIO()
        suite = unittest.loader.TestLoader().loadTestsFromTestCase(TestSumaFunction)
        result = unittest.TextTestRunner(stream=stream).run(suite)

        js.results = {
            'tests_number': result.testsRun,
            'failed': len(result.failures),
            'success': result.testsRun - len(result.failures)
        }

        stream.seek(0)
        print(stream.read())

    except Exception as err:
        print(err)
        
