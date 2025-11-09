from nicegui import ui

ui.label('Hello, Escape Room Site!')
ui.button('Click me', on_click=lambda: ui.notify('Button clicked!'))


ui.run()