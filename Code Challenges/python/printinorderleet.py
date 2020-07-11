# not done
# https://leetcode.com/problems/print-in-order/
# The same instance of Foo will be passed to three different threads.
# Thread A will call first(),
# thread B will call second(),
# and thread C will call third().
# Design a mechanism
# and modify the program
# to ensure that second() is executed after first(),
# and third() is executed after second().


class Foo:
    def __init__(self):
        pass

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """

        # printThird() outputs "third". Do not change or remove this line.
        printThird()


aa = Foo
