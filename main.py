#!/usr/bin/env python3
from nicegui import ui
import CalendarFunctions
import os
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def top_panel():
    ui.dark_mode(True)
    with ui.row().classes('w-full justify-between items-center p-6 bg-gradient-to-r from-[#1a1a1a] to-[#2a2a2a] shadow-2xl border-b border-[#00b4d8]/20 sticky top-0 z-50'):
            ui.label('חדרי הבריחה שלנו').classes('text-3xl font-bold text-[#00b4d8] glow')
            with ui.row().classes('gap-4 text-lg'):
                ui.link("הזמנה", '/order').classes('hover:text-[#ffb703] bg-gradient-to-r from-[#ffb703] to-[#ff9900] px-6 py-3 rounded-xl text-black font-bold hover-lift transition-all duration-300 mr-5')
                # ui.link('על המשחק', '#about').classes('hover:text-[#ffb703] bg-gradient-to-r from-[#00b4d8] to-[#0090b0] px-6 py-3 rounded-xl text-white font-medium hover-lift transition-all duration-300')
                ui.link('אודות', '/about').classes('hover:text-[#ffb703] bg-gradient-to-r from-[#00b4d8] to-[#0090b0] px-6 py-3 rounded-xl text-white font-medium hover-lift transition-all duration-300')
                ui.link('בית', '/').classes('hover:text-[#ffb703] bg-gradient-to-r from-[#00b4d8] to-[#0090b0] px-6 py-3 rounded-xl text-white font-medium hover-lift transition-all duration-300')

@ui.page('/')
def home_page():
    ui.query('body').classes('bg-gradient-to-br from-[#0a0a0a] via-[#0e0e0e] to-[#1a1a1a] text-white min-h-screen')
    ui.dark_mode().enable()
    # Add custom CSS for animations and effects
    ui.add_head_html('''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700&display=swap');
            * { font-family: 'Heebo', sans-serif; }
            
            .fade-in { animation: fadeIn 0.8s ease-in-out; }
            .slide-up { animation: slideUp 0.6s ease-out; }
            .glow { box-shadow: 0 0 20px rgba(0, 180, 216, 0.3); }
            .hover-lift { transition: transform 0.3s ease, box-shadow 0.3s ease; }
            .hover-lift:hover { transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); }
            
            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
            @keyframes slideUp { from { transform: translateY(30px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
            @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
            .pulse { animation: pulse 2s infinite; }
        </style>
    ''')

    with ui.column().classes('items-center w-full min-h-screen justify-between fade-in'):
        top_panel()
        
        #hero image + text

        with ui.element('div').classes(
            'relative w-full h-[600px] max-w-6xl overflow-hidden shadow-2xl hover-lift '
        ):
            ui.image('hero image.png').classes('w-full h-full object-cover')

            with ui.column().classes(
                'absolute inset-0 flex items-center justify-center text-center py-24 slide-up'
            ):
                ui.label('משמרת לילה').classes(
                    'text-9xl font-bold bg-gradient-to-r from-[#00b4d8] to-[#ffb703] '
                    'bg-clip-text text-transparent drop-shadow-xl'
                )
        
        with ui.column().classes('items-center text-center py-24 px-6 bg-gradient-to-br from-[#141414] to-[#1a1a1a] w-full border-t border-b border-[#00b4d8]/20') as about:
            ui.label('על המשחק').classes('text-4xl font-bold text-[#ffb703] mb-8 slide-up')
            
            with ui.row().classes('w-full max-w-6xl justify-center items-center gap-12'):
                with ui.column().classes('flex-1 text-right'):
                    ui.label('ממש פשוט: בזמן הפנוי לקחנו חדר פנוי אצל מעיין והפכנו אותו לחדר בריחה').classes('text-xl text-gray-300 mb-6 leading-relaxed')
                    ui.label('בנינו הכל בעצמנו – מהחידות ועד המנגנונים – כחלק מפרויקט שיצא משליטה לטובה').classes('text-lg text-gray-400 leading-relaxed')
                
                ui.image('https://placehold.co/500x300?text=Family+Playing+Escape+Room').classes('rounded-2xl shadow-2xl hover-lift transition-all duration-500 flex-1')

        # 🧩 אזור "איך משחקים?" משופר
        with ui.column().classes('items-center text-center py-24 px-6 w-full bg-gradient-to-br from-[#0e0e0e] to-[#141414]'):
            ui.label('?אז איך זה עובד').classes('text-4xl font-bold text-[#00b4d8] mb-8 slide-up')
            
            with ui.row().classes('w-full max-w-6xl justify-center items-center gap-12'):
                ui.image('https://placehold.co/500x300?text=Family+Playing+Escape+Room').classes('rounded-2xl shadow-2xl hover-lift transition-all duration-500 flex-1 ')
                
                with ui.column().classes('flex-1 text-right'):
                    ui.label('מגיעים לבית של מעיין, נכנסים בקבוצות של 2–3 אנשים ומשחקים בחדר').classes('text-xl text-gray-300 leading-relaxed text-right')
                    ui.label('בסוף, אחרי שכולם שיחקו, עושים סיור קצר ומראים איך הכל עובד מאחורי הקלעים').classes('text-lg text-gray-400 leading-relaxed text-right')
        # ☎️ אזור צור קשר משופר
        with ui.column().classes('items-center text-center py-24 px-6 bg-gradient-to-br from-[#1a1a1a] to-[#2a2a2a] w-full border-t border-[#00b4d8]/20') as contact:
            ui.label('יצירת קשר').classes('text-4xl font-bold text-[#ffb703] mb-8 slide-up')
            ui.label('רוצים לכתוב לנו, לספר בדיחה, או לשלוח לנו איומי מוות? אנחנו זמינים').classes('text-xl text-gray-300 mb-2 max-w-2xl leading-relaxed')
            
            ui.add_head_html("""
            <style>
            .q-table td, .q-table th {
                font-size: 18px !important;
            }
            </style>
            """)

            with ui.row().classes('gap-3 mt-2 justify-center items-center flex-wrap text-right'):
                ui.table(rows=[
                    {'name': 'מעיין', 'phone': '053-822-3997', 'mail': 'maayan.aharonn@gmail.com'},
                    {'name': 'אור', 'phone': '054-937-7664', 'mail': 'oror224@gmail.com'},
                    {'name': 'גיא', 'phone': '050-244-8111', 'mail': 'goldenbergguy@gmail.com'},
                ], columns=[
                    {'name': 'mail', 'label': 'מייל', 'field': 'mail'},
                    {'name': 'phone', 'label': 'טלפון', 'field': 'phone'},
                    {'name': 'name', 'label': 'שם', 'field': 'name'},
                ], column_defaults={
                    'align': 'center',
                    'headerClasses': 'text-primary',
                    'classes': 'text-gray-300 text-lg text-center', 

                }).classes('w-full max-w-4xl bg-[#2a2a2a] rounded-2xl shadow-2xl border border-[#ffb703]/20 hover-lift text-3xl text-right' )
        # ⚙️ תחתית האתר משופר
        with ui.row().classes('w-full justify-center items-center py-8 bg-gradient-to-r from-[#0e0e0e] to-[#1a1a1a] text-gray-400 text-sm border-t border-[#00b4d8]/10'):
            ui.label('© 2025 חדרי הבריחה שלנו | פיתוח ועיצוב: מעיין, אור וגיא').classes('text-center')
#TODO: add tanks
@ui.page('/about')
def about_page():
    
    top_panel()

    ui.query('body').classes('bg-gradient-to-br from-[#0a0a0a] via-[#0e0e0e] to-[#1a1a1a] text-white min-h-screen')
    
    # Add the same custom CSS
    ui.add_head_html('''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700&display=swap');
            * { font-family: 'Heebo', sans-serif; }
            
            .fade-in { animation: fadeIn 0.8s ease-in-out; }
            .slide-up { animation: slideUp 0.6s ease-out; }
            .glow { box-shadow: 0 0 20px rgba(0, 180, 216, 0.3); }
            .hover-lift { transition: transform 0.3s ease, box-shadow 0.3s ease; }
            .hover-lift:hover { transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); }
            
            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
            @keyframes slideUp { from { transform: translateY(30px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
        </style>
    ''')

    with ui.column().classes('items-center w-full min-h-screen justify-start py-20 px-6 fade-in'):
        # Enhanced header
        ui.label('מי אנחנו?').classes('text-5xl font-bold text-[#00b4d8] mb-8 slide-up bg-gradient-to-r from-[#00b4d8] to-[#ffb703] bg-clip-text text-transparent')
        
        # Team photo with enhanced styling
        ui.image('https://placehold.co/600x300?text=Team+Photo').classes('rounded-3xl shadow-2xl mb-12 hover-lift transition-all duration-500')
        
        # Enhanced team description
        ui.label('אנחנו מעיין, אור וגיא – שלושה חברים וסטודנטים להנדסת אלקטרוניקה שהחליטו לקחת את הפרויקט צעד קדימה: לבנות חדר בריחה שלם אצלנו בבית.').classes('text-xl text-center max-w-4xl mb-12 text-gray-300 leading-relaxed slide-up')
        
        # Technology section with enhanced styling
        with ui.column().classes('w-full max-w-4xl items-center text-center mb-12'):
            ui.label('הצצה לטכנולוגיה').classes('text-3xl font-bold text-[#ffb703] mb-8 slide-up')
            
            with ui.row().classes('w-full gap-8 justify-center items-start flex-wrap'):
                with ui.column().classes('flex-1 min-w-300px bg-gradient-to-br from-[#1a1a1a] to-[#2a2a2a] p-6 rounded-2xl border border-[#00b4d8]/20 hover-lift'):
                    ui.label('חומרה').classes('text-2xl font-bold text-[#00b4d8] mb-4')
                    ui.label('המערכת שלנו משלבת רכיבי Arduino ו־ESP32, חיישני תנועה, מנגנוני מנעולים חשמליים, תאורת לד חכמה, ובקרי סאונד.').classes('text-gray-300 leading-relaxed')
                
                with ui.column().classes('flex-1 min-w-300px bg-gradient-to-br from-[#1a1a1a] to-[#2a2a2a] p-6 rounded-2xl border border-[#ffb703]/20 hover-lift'):
                    ui.label('תוכנה').classes('text-2xl font-bold text-[#ffb703] mb-4')
                    ui.label('בנינו ממשק מחשב ידידותי בעזרת NiceGUI שמאפשר לנו לשלוט בכל החידות, להפעיל מנגנונים ולהציג רמזים לשחקנים.').classes('text-gray-300 leading-relaxed')
        
        # Fun fact with enhanced styling
        ui.label('פרויקט שדרש הרבה שעות, קפה, ובעיקר עבודת צוות.').classes('text-center text-gray-400 mt-8 text-lg italic')
        
        # Enhanced back button
        ui.link('חזרה לדף הבית', '/').classes('mt-12 text-[#00b4d8] hover:text-[#ffb703] text-xl font-medium bg-gradient-to-r from-[#00b4d8]/20 to-[#ffb703]/20 px-8 py-4 rounded-xl hover-lift transition-all duration-300')

@ui.page('/order')
def reservation_page():
    top_panel()
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
    
    DEFAULT_SLOT_TEXT = 'נא לבחור תאריך'
    NO_SLOTS_TEXT = 'אין שעות פנויות בתאריך זה'

    def updateSlots(date, select):
        global slots
        slots = CalendarFunctions.get_open_on_Day(date) if date else [DEFAULT_SLOT_TEXT]
        select.options = slots
        if(len(slots) == 0):
            select.options = [NO_SLOTS_TEXT]
            select.value = NO_SLOTS_TEXT
        else:
            select.value = slots[0]
        select.update()
    
    def order():
        event = CalendarFunctions.create_event(demo.name, demo.email, demo.phone, demo.amount, demo.date, demo.time, demo.difficulty)
        ui.notify(f'event created at time {event.get("start").get("dateTime")}', position='top-left')
        stepper.next()
    
    ui.query('body').classes('bg-gradient-to-br from-[#0a0a0a] via-[#0e0e0e] to-[#1a1a1a] text-white min-h-screen')
    
    ui.add_head_html('''
        <style>
             .fade-in { animation: fadeIn 0.8s ease-in-out; }
             .slide-up { animation: slideUp 0.6s ease-out; }
             .glow { box-shadow: 0 0 20px rgba(0, 180, 216, 0.3); }
             .hover-lift { transition: transform 0.3s ease, box-shadow 0.3s ease; }
             .hover-lift:hover { transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); }
           
             @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
             @keyframes slideUp { from { transform: translateY(30px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
        </style>
    ''')

    with ui.column().classes('items-center justify-center min-h-screen w-full py-12 px-6 fade-in'):
        ui.label('הזמנת מקום').classes('text-8xl font-bold text-[#00b4d8] mb-10 slide-up bg-gradient-to-r from-[#00b4d8] to-[#ffb703] bg-clip-text text-transparent')
        with ui.row(wrap=True, align_items='center').classes('w-full justify-center'):            
            
            with ui.stepper().props('vertical').classes('w-full md:w-2/3 lg:w-1/2 bg-gradient-to-br from-[#1a1a1a] to-[#2a2a2a] p-8 rounded-3xl shadow-2xl border border-[#00b4d8]/20') as stepper:                
                with ui.step('פרטים אישיים', icon="person").classes('text-right text-white'):
                    stepper.next
                    with ui.card().classes('items-center w-full mt-4 rounded-xl border border-[#00b4d8]/30 bg-gradient-to-r from-[#23272F] to-[#141a28] text-white text-xl shadow-lg hover-lift'):
                        ui.label(':בחרו מספר משתתפים').classes('mr-4 text-lg text-[#5898d4] font-semibold')
                        value_label = ui.label(f"{1}").classes('ml-4 text-3xl font-bold text-[#ffb703] ')
                        slide = ui.slider(min=1, max=5, step=1, value=1).bind_value_to(demo, 'amount').props('color=#5898d4').classes('flex-1 mx-4')
                        value_label.bind_text_from(slide, 'value')
                    name = ui.input('שם המזמין', on_change=lambda: validate_inputs(next_btn)).bind_value_to(demo, 'name').classes('w-full px-2 py-2 text-right rounded-xl border border-[#00b4d8]/30 bg-gradient-to-r from-[#23272F] to-[#141a28] text-white text-xl shadow-lg hover-lift')
                    phone = ui.input('טלפון', on_change=lambda: validate_inputs(next_btn)).bind_value_to(demo, 'phone').classes('w-full px-2 py-2 text-right rounded-xl border border-[#00b4d8]/30 bg-gradient-to-r from-[#23272F] to-[#141a28] text-white text-xl shadow-lg hover-lift')
                    email = ui.input('אימייל', on_change=lambda: validate_inputs(next_btn)).bind_value_to(demo, 'email').classes('w-full px-2 py-2 text-right rounded-xl border border-[#00b4d8]/30 bg-gradient-to-r from-[#23272F] to-[#141a28] text-white text-xl shadow-lg hover-lift')
                    
                    next_btn = ui.button('הבא', on_click=stepper.next).classes('mt-4 bg-gradient-to-r from-[#00b4d8] to-[#0090b0] hover:from-[#0090b0] hover:to-[#00b4d8] text-white rounded-xl px-8 py-3 text-lg shadow-lg hover-lift transition-all duration-300 font-medium')
                    # next_btn.disable()

                    def validate_inputs(button):
                        all_filled = all(field.value.strip() for field in [name, phone, email])
                        if all_filled:
                            button.enable()
                        else:
                            button.disable()

                with ui.step('פרטי הזמנה', icon="person").classes('text-right text-white'):
                    ui.label('בחרו תאריך, שעה ורמת קושי.').classes('text-lg text-gray-300 mb-4 text-right')
                    with ui.column().classes('w-full ml-6 items-center text-right'):
                        chooseDate = ui.date('תאריך הזמנה', on_change=lambda: updateSlots(chooseDate.value, select)).bind_value_to(demo, 'date').classes('text-right bg-[#2a2a2a] bg-gradient-to-r from-[#23272F] to-[#141a28] rounded-lg text-white items-left hover-lift')
                        select = ui.select([DEFAULT_SLOT_TEXT], label='בחרו שעה', value=DEFAULT_SLOT_TEXT).bind_value_to(demo, 'time').classes('w-full text-right bg-gradient-to-r from-[#23272F] to-[#141a28] border border-[#00b4d8]/30 rounded-xl px-4 py-3 text-white focus:border-[#00b4d8] focus:ring-2 focus:ring-[#00b4d8]/20 transition-all duration-300 hover-lift')
                        # ui.select(['מתחילים', 'מתקדמים', 'מאתגר'], label='רמת קושי', value='מתחילים', on_change=lambda: validate_order_inputs()).bind_value_to(demo, 'difficulty').classes('w-full text-right bg-gradient-to-r from-[#2a2a2a] to-[#3a3a3a] border border-[#00b4d8]/30 rounded-xl px-4 py-3 text-white focus:border-[#00b4d8] focus:ring-2 focus:ring-[#00b4d8]/20 transition-all duration-300')
                        ui.label(':בחרו רמת קושי').classes('text-xl font-semibold text-[#ffb703] mr-1 slide-up')
                        ui.radio(
                            {1: 'מתחילים', 2:'מתקדמים', 3:'מאתגר'},
                            on_change=lambda: validate_order_inputs()
                        ).props(
                            'inline color=cyan'
                        ).classes(
                            'px-6 py-3 mx-2 text-white text-xl bg-gradient-to-r from-[#23272F] to-[#141a28] border border-[#00b4d8]/30 rounded-xl focus:border-[#00b4d8] focus:ring-2 focus:ring-[#00b4d8]/20 transition-all duration-300 hover-lift'
                        ).bind_value_to(demo, 'difficulty')
                            

                    with ui.row().classes('justify-between mt-6 text-right'):
                        ui.button('אחורה', on_click=stepper.previous).props('flat').classes('mt-4 text-white border border-[#00b4d8]/30 rounded-xl px-8 py-3 text-lg shadow-lg hover-lift transition-all duration-300 font-medium')
                        next_button = ui.button('הבא', on_click=stepper.next).classes('mt-4 bg-gradient-to-r from-[#00b4d8] to-[#0090b0] hover:from-[#0090b0] hover:to-[#00b4d8] text-white rounded-xl px-8 py-3 text-lg shadow-lg hover-lift transition-all duration-300 font-medium')                    
                    # next_button.disable()

                    def validate_order_inputs():
                        all_filled = chooseDate.value is not None and demo.time not in [DEFAULT_SLOT_TEXT, NO_SLOTS_TEXT] != ''
                        if all_filled:
                            next_button.enable()
                        else:
                            next_button.disable()

                with ui.step('סיכום הזמנה').props('icon=assignment').classes('text-right text-white'):
                    ui.label('בדקו שהפרטים נכונים לפני האישור הסופי').classes('text-lg text-gray-300 mb-4 text-right')

                    with ui.card().classes('w-full bg-gradient-to-r from-[#23272F] to-[#141a28] border border-[#00b4d8]/30 rounded-xl focus:border-[#00b4d8] focus:ring-2 focus:ring-[#00b4d8]/20 transition-all duration-300 hover-lift p-4'):
                        with ui.grid(columns=2).classes('w-full text-right gap-2'):
                            ui.label().bind_text_from(demo, 'name')
                            ui.label(':שם המזמין').classes('text-[#ffb703]')

                            ui.label().bind_text_from(demo, 'phone')
                            ui.label(':טלפון').classes('text-[#ffb703]')

                            ui.label().bind_text_from(demo, 'amount')
                            ui.label(':מספר אנשים').classes('text-[#ffb703]')

                            ui.label().bind_text_from(demo, 'email')
                            ui.label(':אימייל').classes('text-[#ffb703]')

                            ui.label().bind_text_from(demo, 'difficulty')
                            ui.label(':רמת קושי').classes('text-[#ffb703]')

                            ui.label().bind_text_from(demo, 'date')
                            ui.label(':תאריך הזמנה').classes('text-[#ffb703]')

                            ui.label().bind_text_from(demo, 'time')
                            ui.label(':שעת הזמנה').classes('text-[#ffb703]')

                    with ui.row().classes('justify-center gap-4 mt-6'):
                        ui.button('אחורה', on_click=stepper.previous).props('flat').classes('mt-4 text-white border border-[#00b4d8]/30 rounded-xl px-8 py-3 text-lg shadow-lg hover-lift transition-all duration-300 font-medium')
                        ui.button('אשר הזמנה', on_click=lambda: order()).classes('mt-4 bg-gradient-to-r from-[#00b4d8] to-[#0090b0] hover:from-[#0090b0] hover:to-[#00b4d8] text-white rounded-xl px-8 py-3 text-lg shadow-lg hover-lift transition-all duration-300 font-medium')
                        ui.button("go go go", on_click=stepper.next)

                with ui.step('הזמנה נקלטה!').props('icon=thumb_up').classes('text-right text-white'):
                    with ui.card().classes('w-full items-center bg-gradient-to-r from-[#23272F] to-[#141a28] border border-[#00b4d8]/30 rounded-xl focus:border-[#00b4d8] focus:ring-2 focus:ring-[#00b4d8]/20 transition-all duration-300 hover-lift p-4'):
                        ui.label('תודה רבה! ההזמנה שלכם אושרה').classes('text-2xl font-semibold mb-2 text-[#00b4d8]')
                        ui.label('מייל אישור עם כל הפרטים בדרך אליכם').classes('text-lg text-gray-300')
                        ui.button('צפייה בלוח השנה', on_click=lambda: ui.navigate.to(CalendarFunctions.make_public_google_calendar_link(demo.date, demo.time))).classes('mt-4 hover:text-[#ffb703] bg-gradient-to-r from-[#00b4d8] to-[#0090b0] text-white rounded-xl px-8 py-3 text-lg shadow-lg hover-lift transition-all duration-300 font-medium')
                        ui.link(text='חזרה', target='/').props('flat').classes('mt-4 text-white border border-[#00b4d8]/30 rounded-xl px-8 py-3 text-lg shadow-lg hover-lift transition-all duration-300 font-medium')

# ✅ Create the FastAPI app manually
from fastapi import FastAPI
fastapi_app = FastAPI()

# ✅ Attach NiceGUI to this FastAPI app
ui.configure(app=fastapi_app)

# ✅ Make this visible for gunicorn
app = fastapi_app

if __name__ == "__main__":
    ui.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 8080)),
        reload=False
    )
                
