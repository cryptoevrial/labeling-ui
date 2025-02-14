import streamlit as st



class Redactor:
    def __init__(self):
        self.edited_text = 'None'
        self.transcribe_text = 'None'
        self.path_to_file = 'data/2024-12-09 13-01-45-converted.mp3'

    def __create_audio_container(self):
        audio_container = st.container(border=True)
        audio_container.markdown('##### Аудио сегмент')
        audio_player = audio_container.audio(data=self.path_to_file)

    def __create_transcribe_container(self):
        transcribe_container = st.container(border=True)
        transcribe_container.markdown('##### Транскрибация:')
        transcribe_container.markdown(self.transcribe_text)

    def __create_edit_container(self):
        editor_container = st.container(border=True)
        editor_container.markdown('##### Отредактируйте текст:')
        self.edited_text = editor_container.text_area(label=' ', label_visibility='collapsed', value=self.transcribe_text)


        is_abbreviation = editor_container.checkbox('Есть аббревиатуры')
        is_missundertanding = editor_container.checkbox('Есть непонятный текст')
        # Размещаем кнопки напрямую
        buttons_columns = editor_container.columns([1, 7, 2])

        save_button = buttons_columns[0].button("Сохранить", type="primary")
        next_audio_button = buttons_columns[-1].button('Следующий файл', icon=':material/chevron_right:')

    def render_page(self):
        self.__create_audio_container()
        self.__create_transcribe_container()
        self.__create_edit_container()

if st.session_state['authentication_status']:
    app = Redactor()
    app.render_page()




