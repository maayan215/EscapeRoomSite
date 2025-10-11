from nicegui import ui

items = ['1', '2', '3']
selection = ui.select(options=items)

def update_values():
    new_items = ['4', '5']
    selection.options = new_items
    selection.update()

# ui.button('update', on_click=lambda: selection.bind_value_from(globals(), 'items'))
ui.button('update', on_click=lambda: update_values())
ui.run()