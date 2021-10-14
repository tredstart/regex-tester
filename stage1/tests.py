from hstest import dynamic_test
from test.base import RegexToolTest


class RegexToolTestRunner(RegexToolTest):
    funcs = [
        # task 1
        RegexToolTest.check_create_record,

    ]

    @dynamic_test(data=funcs)
    def test(self, func):
        return func(self)


if __name__ == '__main__':
    RegexToolTestRunner().run_tests()
