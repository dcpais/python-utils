import utils.builtins

def bind_func(instance, func, as_name=None):
    """
    Bind the function *func* to *instance*, with either provided name *as_name*
    or the existing name of *func*. The provided *func* should accept the 
    instance as the first argument, i.e. "self".
    """
    if as_name is None:
        as_name = func.__name__

    bound_method = func.__get__(instance, instance.__class__)
    setattr(instance, as_name, bound_method)
    return bound_method

def immutable_args(func):
    def wrapper(*args, **kwargs):
        args = utils.builtins.deep_iter_to_tuple(args)
        result = func(*args, **kwargs)
        return result
    return wrapper