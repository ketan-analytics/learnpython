from functools import wraps


def I_am_decorator(input_func):
    @wraps(input_func)
    def wrap_function():
        print("I am you begining decorator")

        input_func()

        print("I am you after decorator")

    return wrap_function


@I_am_decorator
def function_required_decoration():
    print('I need decoration')


function_required_decoration()

print(function_required_decoration.__name__)

print("===================Decorator 2========================")


def logit(logfile='out.log'):

    def logging_decorator(input_func):
        @wraps(input_func)

        def decorator(*args, **kwargs):
            logstring = "Function: " + input_func.__name__ + " was called"
            print(logstring)
            with open(logfile, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(logstring + '\n')
        return decorator

    return logging_decorator


@logit()
def myfunc():
    pass

myfunc()

