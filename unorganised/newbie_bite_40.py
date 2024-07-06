object = "This is the global object."


def use_local_object():
    """Implement local scope here"""
    object = "This is the local object."

    def modify_global_object():
        global object
        object = "This is the modified global object."

    modify_global_object()

    return object


def use_global_object():
    """Implement global scope here"""
    global object
    return object


print(f"Before modification: {object}")

print(use_local_object())

print(f"After modification: {object}")
