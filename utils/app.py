from json import load, JSONDecodeError

import streamlit as st

class App:

    __slots__ = ('encoding', 'static', 'title', 'icon')

    def __init__(self, settings: dict) -> None:
        self.encoding = settings.get('encoding', 'utf-8')
        self.icon = settings.get('icon', ':warning:')
        self.title = settings.get('title', 'Nikita Teterin')
        
        if 'static' not in settings.keys():
            raise RuntimeError
        
        try:
            with open(settings['static'], 'r') as confile:
                self.static = load(confile)
            
        except (FileNotFoundError, JSONDecodeError):
            print(f'Failed to open {settings["static"]}')
            raise RuntimeError
    

    def run(self) -> None:
        st.set_page_config(
            page_title=self.title,
            page_icon=self.icon,
            layout='wide',
            menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"
                }
        )
    