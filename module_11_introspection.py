def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [i for i in attributes if callable(getattr(obj, i))]
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},

    return info


number_info = introspection_info(42)
print(number_info)
