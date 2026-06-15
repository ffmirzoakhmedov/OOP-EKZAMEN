import flet as ft

class TodoWindow:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Лабораторная работа"
        
        # Самое простое поле и кнопка без лишних выкрутасов
        self.input_field = ft.TextField(label="Новая задача")
        self.add_btn = ft.TextButton("Добавить", on_click=self.add_item)
        
        self.main_layout = ft.Column()
        
        self.page.add(
            ft.Text("Список задач"),
            self.input_field,
            self.add_btn,
            ft.Divider(),
            self.main_layout
        )

    def add_item(self, e):
        if self.input_field.value != "":
            # Текст задачи и кнопка удаления рядом
            task_text = ft.Text(self.input_field.value)
            del_btn = ft.TextButton("Удалить", on_click=lambda x: self.delete_item(row_container))
            
            row_container = ft.Row([task_text, del_btn])
            
            self.main_layout.controls.append(row_container)
            self.input_field.value = ""
            self.page.update()

    def delete_item(self, row_to_remove):
        self.main_layout.controls.remove(row_to_remove)
        self.page.update()

if __name__ == "__main__":
    ft.app(target=TodoWindow)