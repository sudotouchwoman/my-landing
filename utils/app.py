from json import load, JSONDecodeError

import streamlit as st
from PIL import Image, UnidentifiedImageError

class App:

    __slots__ = ('encoding', 'content', 'title', 'icon')

    def __init__(self, settings: dict) -> None:
        self.encoding = settings.get('encoding', 'utf-8')
        self.icon = settings.get('icon', ':warning:')
        self.title = settings.get('title', 'Nikita Teterin')
        
        if 'content' not in settings.keys():
            raise RuntimeError
        
        try:
            with open(settings['content'], 'r') as confile:
                self.content = load(confile)
            
        except (FileNotFoundError, JSONDecodeError):
            raise RuntimeError(f'Failed to open {settings["content"]}')


    def run(self) -> None:
        st.set_page_config(
            page_title=self.title,
            page_icon=self.icon,
            layout='wide'
        )

        st.markdown(
            """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """,
            unsafe_allow_html=True)
    
        st.title(self.content['h1'])
        st.subheader(self.content['h2'])
        
        me, bio = st.columns(2)

        with me:
            try:
                image = Image.open(self.content['image'])
                st.image(image, use_column_width=True)
            except (FileNotFoundError, UnidentifiedImageError):
                st.warning('## The image is missing (_　_)。゜zｚＺ')

            with st.expander('Contacts'):
                for contact, link in self.content['contacts'].items():
                    st.markdown(f'+ **[{contact}]({link})**')

                st.markdown(f'+ **Write me an email: {self.content.get("email", "")}**')

        with bio:
            bio_text = '## About me:' + '\n+ ' + '\n+ '.join(self.content['bio'])
            st.info(bio_text)

        _, body, _ = st.columns([1, 2, 1])
        
        with body:
            st.markdown(self.content['body'])
        