#
# JavaScript-like function
# Mikhail Kormanowsky
# 2018
#

# Usage:
# def <function_name>(<params>):
#   <code>
# fn = Function(<function_name>)

# Methods:
# fn(<params>) - calls function with params (as usual function)
# fn.set(<new_function_name>) - sets new function
# fn.call(<list>) - calls function with list of params
# fn.call(<dict>) - calls function with dict of params
# fn.print_output(True|False) - enables/disables print() instead of return
# fn.apply_to(<list>) - calls function for each element of the <list>


class Function:

    #
    # INIT METHODS
    #

    # get class instance
    @classmethod
    def instance(cls):
        return cls()

    # constructor
    def __init__(self, fn=None):
        if not fn:
            fn = lambda x : x
        self.fn = fn
        self.ret = True

    # function setter
    def set(self, fn=None):
        self.__init__(fn)
        return self

    #
    # ARGS PROCESSING METHOD
    #

    @classmethod
    def _prepare_kwargs(cls, kwargs):
        if type(kwargs) is type(dict()):
            return kwargs
        elif type(kwargs) is type(list()):
            _kwargs = dict()
            for i, e in enumerate(kwargs):
                _kwargs[i] = e
            return _kwargs
        raise TypeError("\n".join([
            "kwargs must be either a dictionary or a list.",
            "If your want to call a Function with multiple parameters instead of a list,",
            "use Function(<parameters>) instead of Function.call(<parameters>)"
        ]))

    #
    # RESULT PROCESSING METHODS
    #

    # should we print function output?
    def print_output(self, flag=True):
        self.ret = not flag
        return self

    # inner method for processing function output (print or return depending on the flag)
    def _callback(self, val):
        if self.ret:
            return val
        print(val)

    #
    # CALL METHODS
    #

    # call with list or dictionary of args
    def call(self, kwargs):
        try:
            kwargs = Function._prepare_kwargs(kwargs)
        except TypeError:
            raise
        if not kwargs:
            kwargs = dict()
        args = list()
        _kwargs = dict()
        for i, e in kwargs.items():
            if type(i) == type(0):
                args.append(e)
            else:
                _kwargs[i] = e
        try:
            return self._callback(self.fn(*args, **_kwargs))
        except TypeError as error:
            if error.message.find("argument") != -1:
                _args = list()
                for i in range(int(error.message.split()[3])):
                    try:
                        _args.append(args[i])
                    except ReferenceError:
                        raise
                return self._callback(self.fn(*_args, **dict()))
            raise

    # usual call (function())
    def __call__(self, *args, **kwargs):
        for i, val in enumerate(args):
            kwargs[i] = val
        return self.call(kwargs)

    #
    # OTHER METHODS
    #

    # apply function to each element
    def apply_to(self, elements):
        for i, e in enumerate(elements):
            elements[i] = self.__call__(e)
