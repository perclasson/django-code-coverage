"""Provides the bootstrap functions to be invoked on Python interpreter
startup to register any post import hook callback functions. These would
be invoked from from a custom 'sitecustomize' module setup by the 'trail'
wrapper script."""

import site

_registered = False


def register_bootstrap_functions():
    """Register all post import hooks."""
    # This can be called twice. We therefore protect ourselves
    # just in case it is called a second time as we
    # only want to force registration once.

    global _registered

    if _registered:
        return

    _registered = True

    # It should be safe to import wrapt at this point as this code will
    # be executed after all Python module search directories have been
    # added to the module search path.

    from wrapt import register_post_import_hook

    # here is where I should add a lot of wrappers for django modules

    register_post_import_hook(
        'trail.examples:example',
        'this'
    )
    register_post_import_hook(
        'trail.examples:django_core_urlresolvers',
        'django.core.urlresolvers'
    )
    # register_post_import_hook(
    #     'trail.examples:django_template',
    #     'django.template'
    # )
    # register_post_import_hook(
    #     'trail.examples:django_template_loader_tags',
    #     'django.template.loader_tags'
    # )
    # register_post_import_hook(
    #     'trail.examples:django_core_servers_basehttp',
    #     'django.core.servers.basehttp'
    # )
    # register_post_import_hook(
    #     'trail.examples:django_contrib_staticfiles_views',
    #     'django.contrib.staticfiles.views'
    # )
    # register_post_import_hook(
    #     'trail.examples:django_contrib_staticfiles_handlers',
    #     'django.contrib.staticfiles.handlers'
    # )
    # register_post_import_hook(
    #     'trail.examples:django_views_debug',
    #     'django.views.debug'
    # )
    # register_post_import_hook(
    #     'trail.examples:http_multipartparser',
    #     'django.http.multipartparser'
    # )
    # register_post_import_hook(
    #     'trail.examples:core_mail',
    #     'django.core.mail'
    # )
    # register_post_import_hook(
    #     'trail.examples:core_mail_message',
    #     'django.core.mail.message'
    # )
    # register_post_import_hook(
    #     'trail.examples:views_generic_base',
    #     'django.views.generic.base'
    # )
    # register_post_import_hook(
    #     'trail.examples:core_management_base',
    #     'django.core.management.base'
    # )
    # register_post_import_hook(
    #     'trail.examples:template_base',
    #     'django.template.base'
    # )


def _execsitecustomize_wrapper(wrapped):
    def _execsitecustomize(*args, **kwargs):
        try:
            return wrapped(*args, **kwargs)
        finally:
            # Check whether 'usercustomize' module support is disabled.
            # In the case of 'usercustomize' module support being
            # disabled we must instead do our work here after the
            # 'sitecustomize' module has been loaded.

            if not site.ENABLE_USER_SITE:
                register_bootstrap_functions()

    return _execsitecustomize


def _execusercustomize_wrapper(wrapped):
    def _execusercustomize(*args, **kwargs):
        try:
            return wrapped(*args, **kwargs)
        finally:
            register_bootstrap_functions()

    return _execusercustomize

_patched = False


def bootstrap():
    """Patches the 'site' module such that the bootstrap functions for
    registering the post import hook callback functions are called as
    the last thing done when initialising the Python interpreter."""

    global _patched

    if _patched:
        return

    _patched = True

    # We want to do our real work as the very last thing in the 'site'
    # module when it is being imported so that the module search path is
    # initialised properly. What is the last thing executed depends on
    # whether the 'usercustomize' module support is enabled. Support for
    # the 'usercustomize' module will not be enabled in Python virtual
    # enviromments. We therefore wrap the functions for the loading of
    # both the 'sitecustomize' and 'usercustomize' modules but detect
    # when 'usercustomize' support is disabled and in that case do what
    # we need to after the 'sitecustomize' module is loaded.
    #
    # In wrapping these functions though, we can't actually use wrapt to
    # do so. This is because depending on how wrapt was installed it may
    # technically be dependent on '.pth' evaluation for Python to know
    # where to import it from. The addition of the directory which
    # contains wrapt may not yet have been done. We thus use a simple
    # function wrapper instead.

    site.execsitecustomize = _execsitecustomize_wrapper(site.execsitecustomize)
    site.execusercustomize = _execusercustomize_wrapper(site.execusercustomize)
