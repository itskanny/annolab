import os


def export_vars(request):
    data = {'DOMAIN': os.environ['DOMAIN']}
    return data
