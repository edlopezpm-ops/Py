<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Observe a decorated call and its returned value

The original final print displays a function object. Call the decorated function to observe the wrapper message and arithmetic return separately.

Source: [decoradores.py](../../Py%20Scripts/decoradores.py#L3). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/decorator-invocation.py

See the complete [runnable example](../examples/decorator-invocation.py). It uses synthetic values and the Python standard library.

Expected result: "wrapper: Name: Nombre Decorador; return: 5; metadata name: envolvedor".

Limit: The source omits functools.wraps, so wrapper metadata replaces the original name. Its function named sum shadows the builtin locally.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
