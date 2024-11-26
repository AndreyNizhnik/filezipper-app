import FreeSimpleGUI as sg

# Zipping part
label_zip = sg.Text("Zipping:")
label_zip_from_path = sg.Text("Select files to archive:     ")
input_box_zip_path = sg.InputText(tooltip="Select input files")
label_zip_to_path = sg.Text("Select Zip destination:    ")
input_box_zip_output_path = sg.InputText(tooltip="Select output directory")
button_zip_from = sg.Button("Choose")
button_zip_to = sg.Button("Choose")
button_zip = sg.Button("Zip")

# Overheads
label_blank1 = sg.Text("----------------------------------"*4)
label_blank2 = sg.Text("----------------------------------"*4)
button_exit = sg.Button("Exit")

# Unzipping part
label_unzip = sg.Text("Unzipping:")
label_unzip_from_path = sg.Text("Select files to unarchive:  ")
input_box_unzip_path = sg.InputText(tooltip="Select input files")
label_unzip_to_path = sg.Text("Select output destination:")
input_box_unzip_output_path = sg.InputText(tooltip="Select output directory")
button_unzip_from = sg.Button("Choose")
button_unzip_to = sg.Button("Choose")
button_unzip = sg.Button("Unzip")

# Window interface
title = "FileZipper App"
new_window = sg.Window(title=title, layout=[
    [label_zip],
    [label_zip_from_path, input_box_zip_path, button_zip_from],
    [label_zip_to_path, input_box_zip_output_path, button_zip_to],
    [button_zip],
    [label_blank1],
    [label_unzip],
    [label_unzip_from_path, input_box_unzip_path, button_unzip_from],
    [label_unzip_to_path, input_box_unzip_output_path, button_unzip_to],
    [button_unzip],
    [label_blank2],
    [button_exit]
])
new_window.read()
new_window.close()