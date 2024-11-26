import FreeSimpleGUI as sg

label = sg.Text("Type a todo:")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

new_window = sg.Window(title='Todo List App', layout=[[label], [input_box, add_button]])
new_window.read()
# new_window.close()