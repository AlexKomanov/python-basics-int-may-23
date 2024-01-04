import flet as ft


def main(page: ft.Page):
    def button_clicked(event: ft.ControlEvent):
        # print(event.__repr__())
        # print(event.control.text)
        page.add(ft.Text(value=f"My name is {text_field.value}"))

    text_element = ft.Text(value="Hi all", color="red", size=20)
    button = ft.ElevatedButton(text="Click Me", on_click=button_clicked)
    text_field = ft.TextField(label="My Name")
    row = ft.Row(controls=[
        text_field,
        button
    ])

    page.add(text_element, row)


ft.app(target=main)
