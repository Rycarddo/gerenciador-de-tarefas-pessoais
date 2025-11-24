import flet as ft

def main(page: ft.Page):

    # Window settings
    page.title = "Gerenciador de Tarefas Pessoais"
    page.window.width = 400
    page.window.height = 650
    page.theme_mode = ft.ThemeMode.LIGHT

    # Functions
    def add_task(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()
    
    # Creating items
    welcome_msg = ft.Text(value="Bem-vindo, Rycarddo!")
    new_task = ft.TextField(hint_text="Insira uma tarefa", expand=True, on_submit= add_task)
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click= add_task)

    column = ft.Column(
        width=400,
                controls=[
                    ft.Row(
                        controls=[
                            new_task,
                            new_button
                        ]
                    )
                ]
    )

    # Adding items
    page.add(welcome_msg, column)

ft.app(target= main)