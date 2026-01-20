import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = 'Empire of the sun'
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text(value='hello world')

    greeting_history = []
    history_text = ft.Text('History of greetings:')

    # color=ft.Colors.RED_900
    # text_hello.value = 'Hello'
    # text_hello.color = ft.Colors.GREEN_900
    def text_name(_):
        # print(name_input.label)
        name = name_input.value.strip()

        if name:
            now = datetime.now()
            current_time = now.strftime("%Y:%m:%d - %H:%M:%S")

            text_hello.color = None
            text_hello.value = f'{current_time} - hello, {name}!'
            name_input.value = None

            greeting_history.append(name)
            print(greeting_history)
            history_text.value = 'History of greetings:\n ' + ', \n'.join(greeting_history)
        else:
            text_hello.value = 'Введите имя!'
            text_hello.color = ft.Colors.RED

    def switch_icon(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK


    # text_button = ft.TextButton('SEND')
    elevated_button = ft.ElevatedButton('send', on_click=text_name, icon=ft.Icons.SEND)
    # icon_button = ft.IconButton(icon=ft.Icons.SEND)

    name_input = ft.TextField(label='Введиет текст', on_submit=text_name, expand=True)

    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=switch_icon)

    def clear_history(_):
        print(greeting_history)
        greeting_history.clear()
        print(greeting_history)
        history_text.value = 'History of greetings:'

    def sort_history(_):
        greeting_history.sort(key=str.lower)
        history_text.value = 'History of greetings:\n ' + ', \n'.join(greeting_history)

    def cleare_history(_):
        print(greeting_history)
        greeting_history.clear()
        print(greeting_history)
        history_text.value = 'History of greetings:'

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    sort_button = ft.IconButton(icon=ft.Icons.SORT_BY_ALPHA, tooltip='Sort history', on_click=sort_history)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=cleare_history)
    main_object = ft.Row([name_input, elevated_button, thememode_button, sort_button, clear_button])

    page.add(text_hello, main_object, history_text)

ft.app(target=main)