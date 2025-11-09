from nicegui import ui

ui.label('Hello, Escape Room Site!')
ui.button('Click me', on_click=lambda: ui.notify('Button clicked!'))


if __name__ in {"__main__", "__mp_main__"}:
    ui.run()