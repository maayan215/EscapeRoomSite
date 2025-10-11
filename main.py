#!/usr/bin/env python3
from nicegui import ui
import CalendarFunctions
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

with ui.header().classes(replace='row items-center w-full') as header:
    ui.image('logo.jpeg').classes('w-12 h-12 mr-auto')
    with ui.tabs() as tabs:
        ui.tab('אודות')
        ui.tab('הזמנות')
        ui.tab('בית')


class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
slots= ["no slots yet", ""]
selection = None
def updateSlots(date):
    global slots
    global selection
    selection = ui.select(options=slots)
    
    # global selection
    slots = CalendarFunctions.get_open_on_Day(date) if date else ['no slots today you fool']
    selection.bind_value(slots)
    # selection.value = slots[0] if slots else None
    # selection = ui.select(options=slots)
    # for i in range(len(slots)):
    #     ui.button(text=f'{slots[i]}')
    ui.notify(f'Available slots updated for {date}', position='top-left')

with ui.tab_panels(tabs, value='בית',).classes('w-full h-full '):
    with ui.tab_panel('בית'):
        ui.label('תוכן של ביתv').classes('self-end text-right w-full')
    with ui.tab_panel('הזמנות'):
        with ui.row(wrap=True, align_items='center').classes('w-full justify-center'):
        # ui.label("1")
            
            with ui.stepper().props('vertical').classes('w-1/2') as stepper:
                with ui.step('פרטים אישיים').props('icon=person').classes('text-right'):
                    ui.input('שם המזמין').classes('w-full text-right')
                    ui.number('כמה אנשים אתם?').classes('w-full text-right')
                    ui.input('אימייל').classes('w-full text-right')
                    ui.button('Next', on_click=stepper.next)
                with ui.step('פרטי הזמנה').props('icon=calendar').classes('text-right'):
                    with ui.row():
                        date = "2025-10-16"
                        ui.date('תאריך הזמנה', on_change=lambda: updateSlots(date)).bind_value(globals(), 'date').classes('text-right')
                        ui.separator().props('vertical')
                    with ui.dropdown_button("ניסיון", auto_close=True).classes('w-full text-right'):
                        ui.item('מתחילים')
                        ui.item('מתקדמים')
                        ui.item('סופר חנונים')
    with ui.tab_panel('אודות'):
        ui.label('תוכן של אודות ').classes('self-end text-right w-full')

ui.run()
