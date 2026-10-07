from nicegui import ui

ui.query('body').classes('bg-yellow-50')

with ui.element("div") as home:
    ui.label("Holy Sonnet X").classes("text-2xl font-bold")
    ui.label("by John Donne").classes("text-2xl font-bold")
    ui.label("Choose your settings in 'Profile Settings' before clicking 'Start'")

saved_name = ""
selected_char = ""
selected_image = ""

def selectCharacter(character, image):
    global selected_char, selected_image
    selected_char = character
    selected_image = image
    ui.notify(f"Selected: {character}")

def save_profile():
    global saved_name
    saved_name = name.value
    settings.close()
    ui.notify("Profile Saved!")

def open_settings():
    name.value = saved_name
    settings.open()

def start():
    home.set_visibility(False)
    settings_button.set_visibility(False)
    start_button.set_visibility(False)
    video.set_visibility(True)

def vidFinish():
    video.set_visibility(False)
    congratulations.set_visibility(True)
    end_name.text = f"Congratulations, {saved_name}, you have made it to the end of the video!"
    end_char.set_source(selected_image)

with ui.dialog() as settings:
    with ui.card().classes("w-96"):
        name = ui.input("Display Name")

        ui.label("Select a Profile Display").classes("text-lg")

        with ui.row().classes("gap-4"):
            ui.image("collar.png").classes("w-20 h-20 cursor-pointer").on("click", lambda: selectCharacter("Duck with Collar", "collar.png"))
            
            ui.image("mustache.png").classes("w-20 h-20 cursor-pointer").on("click", lambda: selectCharacter("Duck with Mustache", "mustache.png"))
            
            ui.image("ribbon.png").classes("w-20 h-20 cursor-pointer").on("click", lambda: selectCharacter("Duck with Ribbon", "ribbon.png"))
       
        ui.button("Save", on_click=save_profile)

with ui.row():
    start_button = ui.button("Start", on_click=start)
    settings_button = ui.button("Profile Settings", on_click=open_settings)

with ui.element("div") as video:
    video_player = ui.video("video.mp4").classes("w-200")
    video_player.on("ended", vidFinish)

video.set_visibility(False)

with ui.element("div").classes("w-full flex flex-col items-center") as congratulations:
    end_name = ui.label("").classes("text-2xl font-bold")
    end_char = ui.image("").classes("w-48 h-48")

video.set_visibility(False)

ui.run()
