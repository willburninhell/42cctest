from django.conf import settings


def projectsettings(reqest):
    return {'SETTINGS': settings}
