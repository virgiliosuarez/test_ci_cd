from django.apps import AppConfig


class SampleAppConfig(AppConfig):
    name = 'sample_app'

    def ready(self):
        pass
