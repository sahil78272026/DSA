def outer_func(param):

    def inner_func():
        print(param)
        return 1

    return inner_func


hi_func = outer_func('Hi')
bye_func = outer_func('Bye')

print(hi_func())
bye_func()
