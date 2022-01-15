from .app import App

def main() -> None:
    settings = {
        'encoding': 'utf-8',
        'content': 'static/page.json',
        'icon': ':globe_with_meridians:',
        'title': 'sudotouchwoman'
    }

    App(settings).run()