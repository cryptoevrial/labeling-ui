import streamlit as st
import time

class AudioView:
    def __init__(self):
        self.current_audio_segment = None

    def initialize(self):
        if 'current_audio_segment' not in st.session_state:
            st.session_state.current_audio_segment = 'data/2024-12-09 13-01-45-converted.mp3' # Запрос к API
            self.current_audio_segment = st.session_state.current_audio_segment
        else:
            self.current_audio_segment = st.session_state.current_audio_segment

    def view(self):
        audio_container = st.container(border=True)
        audio_container.markdown('##### Аудио сегмент')
        audio_player = audio_container.audio(data=self.current_audio_segment)

    def render(self):
        self.initialize()
        self.view()


class TranscriptionView:
    def __init__(self):
        self.current_transcription = None

    def initialize(self):
        if 'current_transcription' not in st.session_state:
            st.session_state.current_transcription = 'Lorem ipsum dolor' # Запрос к API
            self.current_transcription = st.session_state.current_transcription
        else:
            self.current_transcription = st.session_state.current_transcription

    def view(self):
        transcribe_container = st.container(border=True)
        transcribe_container.markdown('##### Транскрибация:')
        transcribe_container.markdown(self.current_transcription)

    def render(self):
        self.initialize()
        self.view()


class EditorView:
    def __init__(self):
        self.edited_text = None
        self.is_abbreviation = None
        self.is_missundertanding = None
        self.save_button = None
        self.next_audio_button = None

    def view(self):
        editor_container = st.container(border=True)
        editor_container.markdown('##### Отредактируйте текст:')
        self.edited_text = editor_container.text_area(label=' ', label_visibility='collapsed', value=st.session_state.current_transcription)


        self.is_abbreviation = editor_container.checkbox('Есть аббревиатуры')
        self.is_missundertanding = editor_container.checkbox('Есть непонятный текст')
        # Размещаем кнопки напрямую
        buttons_columns = editor_container.columns([1, 7, 2])
        self.save_button = buttons_columns[0].button("Сохранить", type="primary")
        self.next_audio_button = buttons_columns[-1].button('Следующий файл',
                                                            icon=':material/chevron_right:',
                                                            on_click=self.change_transcription
                                                            )

        if self.save_button:
            with st.spinner(text='Сохранение...'):
                time.sleep(5)
            st.success('Сохранено')
            f_row = f'Текст: {self.edited_text}\n\nАббревиатуры: {self.is_abbreviation}\n\nНепонятный текс: {self.is_missundertanding}'
            st.markdown(f_row)

    def change_transcription(self):
        st.session_state.current_transcription = self.edited_text

    def render(self):
        self.view()


audio = AudioView()
transcription = TranscriptionView()
editor = EditorView()

audio.render()
transcription.render()
editor.render()

