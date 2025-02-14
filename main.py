import streamlit as st
from login import Login

st.set_page_config(
    layout="wide",  # это сделает контейнер на всю ширину
    initial_sidebar_state="expanded",
)

login = Login()
login.get_login()

main_page = st.Page('app.py', title='Главная', icon=':material/work:')
dashboard_page = st.Page('dashboard.py', title='Аналитика', icon=':material/dashboard:')

if st.session_state['authentication_status']:
    pg = st.navigation(pages=[main_page, dashboard_page], position='sidebar')
    login.authenticator.logout(button_name='Выход', location='sidebar')
    pg.run()



