#!/usr/bin/env python3
from nicegui import ui

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

with ui.header().classes(replace='row items-center w-full') as header:
    ui.image('logo.jpeg').classes('w-12 h-12 mr-auto')
    with ui.tabs() as tabs:
        ui.tab('אודות')
        ui.tab('הזמנות')
        ui.tab('בית')


with ui.tab_panels(tabs, value='בית',).classes('w-full h-full '):
    with ui.tab_panel('בית'):
        ui.label('תוכן של ביתv').classes('self-end text-right w-full')
    with ui.tab_panel('הזמנות'):
        # with ui.row(wrap=True, align_items='center').classes('w-full justify-center'):
        ui.label("1")
            # with ui.stepper().props('vertical').classes('w-1/2') as stepper:
                # with ui.step('פרטים אישיים').props('icon=person').classes('text-right'):
                    # ui.input('שם המזמין').classes('w-full text-right')
                    # ui.number('כמה אנשים אתם?').classes('w-full text-right')
                    # ui.input('אימייל').classes('w-full text-right')
                    # ui.button('Next', on_click=stepper.next)
                # with ui.step('פרטי הזמנה').props('icon=calendar').classes('text-right'):
                    # ui.date('תאריך הזמנה').classes('text-right')
                    # ui.time('שעת הזמנה').classes('text-right')
                    # with ui.dropdown_button("ניסיון", auto_close=True).classes('w-full text-right'):
                        # ui.item('מתחילים')
                        # ui.item('מתקדמים')
                        # ui.item('סופר חנונים')
            # ui.label("2")
    with ui.tab_panel('אודות'):
        ui.label('תוכן של אודות ').classes('self-end text-right w-full')

ui.run()
