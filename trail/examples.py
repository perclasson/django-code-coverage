from __future__ import print_function
import wrapt

def example(module):
    print('The trail package is absolutely amazing and you should use it.')


@wrapt.decorator
def urlresolver_resolve(wrapped, instance, args, kwargs):
    path = args[0]
    result = wrapped(path)
    print("type(result)", type(result))
    print("result.func", result.func)
    # wrap result function here?
    # also get name from result.func
    return result

@wrapt.decorator
def urlresolver_reverse(wrapped, instance, args, kwargs):
    viewname = args[0]
    print("url_reverse", viewname)
    return wrapped(*args, **kwargs)

def django_core_urlresolvers(module):
    module.RegexURLResolver.resolve = urlresolver_resolve(
        module.RegexURLResolver.resolve
    )
    module.reverse = urlresolver_reverse(module.reverse)