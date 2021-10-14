from hstest import dynamic_test
from test.base import RegexToolTest


class RegexToolTestRunner(RegexToolTest):
    funcs = [
        # task 1
        RegexToolTest.check_create_record,
        # task 2
        RegexToolTest.check_home_page_greeting,
        RegexToolTest.check_the_csrf_token,
        RegexToolTest.check_home_page_layout,

    ]

    @dynamic_test(data=funcs)
    def test(self, func):
        return func(self)


if __name__ == '__main__':
    RegexToolTestRunner().run_tests()
