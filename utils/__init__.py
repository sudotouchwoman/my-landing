from .app import App

def main() -> None:
    settings = {
        'encoding': 'utf-8',
        'static': 'static.json',
        'icon': ':globe_with_meredans:',
        'title': 'Hello!'
    }

    App(settings).run()