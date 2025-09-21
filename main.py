import os
from nicegui import ui, app
from starlette.middleware.sessions import SessionMiddleware

SECRET = os.getenv('APP_SECRET', 'change-me')
PASSWORD = os.getenv('APP_PASSWORD', 'letmein')
PORT = int(os.getenv('PORT', '8080'))

app.add_middleware(SessionMiddleware, secret_key=SECRET)

def signed_in() -> bool:
    return app.storage.user.get('signed_in', False)

@ui.page('/')
def index():
    if not signed_in():
        with ui.card().classes('max-w-sm mx-auto mt-20'):
            ui.label('כניסה').classes('text-xl')
            pwd = ui.input('סיסמה', password=True, password_toggle_button=True)
            ui.button('התחבר', on_click=lambda: try_login(pwd.value))
            ui.label('רמז: תשנה את APP_PASSWORD בסביבה').classes('text-xs text-gray-500')
        return
    ui.label('שלום! האתר פעיל 😊')
    ui.button('התנתק', on_click=logout)

def try_login(p: str):
    if p == PASSWORD:
        app.storage.user['signed_in'] = True
        ui.navigate.reload()
    else:
        ui.notify('סיסמה שגויה', color='negative')

def logout():
    app.storage.user['signed_in'] = False
    ui.navigate.reload()
ui.run(host='0.0.0.0', port=PORT)
