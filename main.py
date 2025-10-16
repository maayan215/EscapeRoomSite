#!/usr/bin/env python3
from nicegui import ui
import CalendarFunctions
SCOPES = ["https://www.googleapis.com/auth/calendar"]

with ui.header().classes(replace='row items-center w-full') as header:
    ui.image('logo.jpeg').classes('w-12 h-12 mr-auto')
    with ui.tabs() as tabs:
        ui.tab('אודות')
        ui.tab('הזמנות')
        ui.tab('בית')
global name, amount, email

class Demo:
    def __init__(self):
        self.name = ''
        self.email = ''
        self.amount = 0
        self.phone = ''
        self.date = ''
        self.time = ''
        self.difficulty = ''

demo = Demo()
slots= ["no slots yet"]
selection = None
def updateSlots(date, select):
    global slots
    print(f'date: {date}')
    # ui.notify(f'Available slots updated for {date}', position='top-left')
    slots = CalendarFunctions.get_open_on_Day(date) if date else ['אין תורים היום טיפש']
    select.options = slots
    if(len(slots) == 0):
        select.options = ['אין תורים היום טיפש']
        select.value = 'אין תורים היום טיפש'
    else:
        select.value = slots[0]
    select.update()

def order():
    event = CalendarFunctions.create_event(demo.name, demo.email, demo.phone, demo.amount, demo.date, demo.time, demo.difficulty)
    ui.notify(f'event created at time {event.get("start").get("dateTime")}', position='top-left')
    stepper.next()
    
with ui.tab_panels(tabs, value='הזמנות',).classes('w-full h-full '):
    with ui.tab_panel('בית'):
        ui.label('תוכן של בית').classes('self-end text-right w-full')
    with ui.tab_panel('הזמנות'):
        with ui.row(wrap=True, align_items='center').classes('w-full justify-center'):
            
            with ui.stepper().props('vertical').classes('w-1/2') as stepper:
                with ui.step('פרטים אישיים').props('icon=person').classes('text-right'):

                    name = ui.input('שם המזמין',on_change= lambda: validate_inputs()).bind_value_to(demo, 'name').classes('w-full text-right')
                    phone = ui.input('טלפון',on_change= lambda: validate_inputs()).bind_value_to(demo, 'phone').classes('w-full text-right')
                    # amount = ui.number('כמה אנשים אתם?').bind_value_to(demo, 'amount').classes('w-full text-right')
                    amount = ui.select([1, 2, 3],label="כמה אנשים אתם?", value=1).bind_value_to(demo, 'amount').classes('w-full text-right')
                    email = ui.input('אימייל',on_change= lambda: validate_inputs()).bind_value_to(demo, 'email').classes('w-full text-right')
                    v = False
                    next_btn = ui.button('הבא', on_click=stepper.next).props('color=primary disabled')
                    def validate_inputs():
                        all_filled = all(field.value.strip() for field in [name, phone, amount, email])
                        if all_filled:
                            next_btn.enable()

                    
                    

                with ui.step('פרטי הזמנה').props('icon=calendar').classes('text-right'):
                    with ui.row():
                        # date = "2025-10-16"
                        chooseDate = ui.date('תאריך הזמנה', on_change = lambda: updateSlots(chooseDate.value, select)).bind_value_to(demo, 'date').classes('text-right')
                        ui.separator().props('vertical')
                        with ui.column():
                            select = ui.select(['אין תורים היום טיפש'], label='תורים', value='אין תורים היום טיפש').bind_value_to(demo, 'time').classes('w-auto')
                            ui.select(['מתחילים', 'מתקדמים', 'סופר חנונים'], label='רמת קושי', value='מתחילים').bind_value_to(demo, 'difficulty').classes('text-center')
                    with ui.row():
                        ui.button('הבא', on_click=stepper.next)
                        ui.button('אחורה', on_click=stepper.previous)
                with ui.step('סיכום הזמנה').props('icon=check').classes('text-right'):
                    with ui.card().classes('w-full align-center').style("background-color: rgba(130, 130, 130, 0.2); backdrop-filter: blur(10px); border-radius: 10px; padding: 20px;"):
                        with ui.grid(columns=2).classes('w-full'):
                            ui.label().bind_text_from(demo, 'name').classes('text-left')
                            ui.label(':שם המזמין').classes('text-right')

                            ui.label().bind_text_from(demo, 'phone').classes('text-left')
                            ui.label(':טלפון').classes('text-right')

                            ui.label().bind_text_from(demo, 'amount').classes('text-left')
                            ui.label(':מספר אנשים').classes('text-right')

                            ui.label().bind_text_from(demo, 'difficulty').classes('text-left')
                            ui.label(':רמת קושי').classes('text-right')

                            ui.label().bind_text_from(demo, 'email').classes('text-left')
                            ui.label(':אימייל').classes('text-right')
                            
                            ui.separator().props('span')
                            ui.separator().props('span')

                            ui.label().bind_text_from(demo, 'date').classes('text-left')
                            ui.label(':תאריך הזמנה').classes('text-right')

                            ui.label().bind_text_from(demo, 'time').classes('text-left')
                            ui.label(':שעת הזמנה').classes('text-right')



                    with ui.row():
                        # ui.button('הזמן', on_click=stepper.next, onclick=lambda: )
                        # ui.button('הזמן', on_click=lambda: CalendarFunctions.create_event(demo.name, demo.email, demo.phone, demo.amount, demo.date, demo.time, demo.difficulty), on_click = stepper.next).props('color=primary')
                        ui.button('הזמן', on_click= lambda: order()).props('color=primary')
                        # ui.button('test', on_click=lambda: print(CalendarFunctions.get_Specific_Event(demo.date, demo.time)))
                        ui.button('אחורה', on_click=stepper.previous)
                with ui.step('הזמנתך נקלטה!').props('icon=thumb_up').classes('text-right'):
                    ui.label('תודה רבה שהזמנתם אצלנו! נתראה בקרוב :)').classes('self-end text-right w-full')
                    ui.button('קישור להזמנה', on_click=lambda: ui.navigate.to(CalendarFunctions.make_public_google_calendar_link(demo.date, demo.time))).props('color=primary')
                    # ui.button('חזרה להתחלה', on_click=stepper.reset).props('color=primary')
                    ui.button('back', on_click=stepper.previous)
    with ui.tab_panel('אודות'):
        ui.label('תוכן של אודות ').classes('self-end text-right w-full')
ui.run(host='0.0.0.0', port=8080, title='Escape Room MT Digital', favicon='logo.jpeg')