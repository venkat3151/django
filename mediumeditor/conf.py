from django.conf import settings  # noqa
from appconf import AppConf


class MediumEditorConf(AppConf):
    THEME = 'bootstrap'
    OPTIONS = {
        'toolbar': {
            'static': True,
            'buttons': [
                'bold',
                'italic',
                'underline',
                'strikethrough',
                'anchor',
                'quote',
                'pre',
                'indent',
                'outdent',
                'justifyLeft',
                'justifyCenter',
                'justifyRight',
                'justifyFull',
                'h1',
                'h2',
                'h3',
                'image',
            ]
        }
    }

    class Meta:
        prefix = 'medium_editor'
