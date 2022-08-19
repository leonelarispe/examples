def hola():
    print("Hola desde github")



if __name__ == '__main__':
    import unittest
    import io


    class TestSumaFunction(unittest.TestCase):

        def test_suma_15_10(self):
            self.assertEqual(suma(15,10), 25)

        def test_suma__10_10(self):
            self.assertEqual(suma(-10,10), 0)

        def test_suma__2__15(self):
            self.assertEqual(suma(-2,-15), -17)

    def suites():
        return[
            TestSumaFunction
        ]

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    stream = io.StringIO()
    for test_case in suites():
        suite.addTests(loader.loadTestsFromTestCase(test_case))
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)

    stream.seek(0)
    print(stream.read())
