def add_methods_from(*modules):
    def decorator(__class__):
        for module in modules:
            for method in getattr(module, "__methods__"):
                setattr(__class__, method.__name__, method)
        return __class__
    return decorator


def register_method(methods):
    def register_method_to_variable(method):
        methods.append(method)
        return method
    return register_method_to_variable
