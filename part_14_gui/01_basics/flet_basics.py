import flet as ft


def main(page: ft.Page):
    text_element = ft.Text(value="Hi all", color="red", size=20)
    page.add(text_element)


ft.app(target=main)
