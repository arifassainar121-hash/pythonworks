# x=20
# print("outer",x)
# def f():
#     print('inside',x)
#
# f()
#
# def f():
#     x=30  #local scope
#     print("inside",x)
#
# f()


def outer():
    x=30
    print('outre',x)
    def inner():
        print('inner',x)
        return

    inner()
outer()
