from __future__ import absolute_import, division, print_function, unicode_literals

from six import iteritems

import django.conf


class OTPEmailSettings(object):
    """
    This is a simple class to take the place of the global settings object. An
    instance will contain all of our settings as attributes, with default values
    if they are not specified by the configuration.
    """
    defaults = {
        'OTP_EMAIL_SENDER': '',
        'OTP_EMAIL_SUBJECT': 'OTP token',
        'OTP_STEP_TIME': 900,
    }

    def __init__(self):
        """
        Loads our settings from django.conf.settings, applying defaults for any
        that are omitted.
        """
        for name, default in iteritems(self.defaults):
            value = getattr(django.conf.settings, name, default)
            setattr(self, name, value)


settings = OTPEmailSettings()
