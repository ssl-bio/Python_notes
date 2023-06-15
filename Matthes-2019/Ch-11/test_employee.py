import unittest
import employee


class EmployeeTestCase(unittest.TestCase):
    """Test functions defined in the employee class
    """

    def setUp(self):
        self.worker = employee.Employee('tim', 'jones', 50_000)

    def test_raise_default(self):
        self.worker.give_raise()
        salary = self.worker.annu_salary
        self.assertEqual(salary, 55_000)

    def test_raise_custom(self):
        self.worker.give_raise(20_000)
        salary = self.worker.annu_salary
        self.assertEqual(salary, 70_000)


if __name__ == '__main__':
    unittest.main()
