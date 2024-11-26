import FreeSimpleGUI as sg
import zipfile
import pathlib

# Zipping part
label_zip = sg.Text("Zipping:")
label_zip_from_path = sg.Text("Select files to archive:     ")
input_box_zip_path = sg.InputText(tooltip="Select input files")
label_zip_to_path = sg.Text("Select Zip destination:    ")
input_box_zip_output_path = sg.InputText(tooltip="Select output directory")
button_zip_from = sg.FilesBrowse("Choose", key="zip_files")
button_zip_to = sg.FolderBrowse("Choose", key="zip_folder")
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
button_unzip_from = sg.FilesBrowse("Choose", key="unzip_file")
button_unzip_to = sg.FolderBrowse("Choose", key="unzip_folder")
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


while True:
    event, values = new_window.read()

    if event == "Zip":
        files_input = values['zip_files'].split(';')
        files_to = values['zip_folder']
        output_filename = "archive.zip"
        output_path = pathlib.Path(files_to, output_filename)
        try:
           with zipfile.ZipFile(output_path, mode="w") as archive:
               for path in files_input:
                   archive.write(path)
           sg.popup(f"Archive is created: \n{output_path}")
        except FileNotFoundError:
           sg.popup(f"Specify files and try again!")

    elif event == "Unzip":
        files_input = values['unzip_file']
        dir_output = values['unzip_folder']
        try:
            with zipfile.ZipFile(files_input, 'r') as my_zip:
                my_zip.extractall(dir_output)
            sg.popup(f"Archive is extracted to: \n{dir_output}")
        except FileNotFoundError:
           sg.popup(f"Specify files and try again!")

    elif event == sg.WIN_CLOSED or event == "Exit":
        break

new_window.close()
