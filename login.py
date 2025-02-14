import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


class Login():
    def __init__(self):
        self.config = self.__load_config()
        self.authenticator = self.__create_auth()

    def __load_config(self):
        with open('login_config.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)
        return config

    def __create_auth(self):
        authenticator = stauth.Authenticate(
            self.config['credentials'],
            self.config['cookie']['name'],
            self.config['cookie']['key'],
            self.config['cookie']['expiry_days']
        )
        return authenticator

    def get_login(self):
        try:
            self.authenticator.login()
        except Exception as e:
            st.error(e)
        if st.session_state['authentication_status']:
            pass
        elif st.session_state['authentication_status'] is False:
            st.error('Логин/пароль не верный')
        elif st.session_state['authentication_status'] is None:
            st.warning('Введите логин и пароль')


