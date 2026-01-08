import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = 'Empire of the sun'
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text(value='hello world') 
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

    name_input = ft.TextField(label='Введиет текст', on_submit=text_name)

    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=switch_icon)

    page.add(text_hello, name_input, elevated_button, thememode_button)



ft.app(target=main)