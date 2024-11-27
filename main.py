import FreeSimpleGUI as sg
import zipfile
import pathlib
import os

# Front End - Zipping
label_zip = sg.Text("Zipping:", size=(20, 1))
label_zip_from_path = sg.Text("Select files to archive:", size=(20, 1))
input_box_zip_path = sg.InputText(tooltip="Select input files", size=(40, 1))
label_zip_to_path = sg.Text("Select Zip destination:", size=(20, 1))
input_box_zip_output_path = sg.InputText(tooltip="Select output directory", size=(40, 1))
button_zip_from = sg.FilesBrowse("Choose", key="zip_files")
button_zip_to = sg.FolderBrowse("Choose", key="zip_folder")
button_zip = sg.Button("Zip", size=(7, 1), button_color=('white', 'green'))
label_archive_name = sg.Text("Archive name:", size=(20, 1))
file_name = sg.InputText(default_text='archive.zip', tooltip="File name", key='file_name', size=(40, 1))

# Front End - Overheads
label_blank1 = sg.Text("-" * 130)

# Front End - Unzipping
label_unzip = sg.Text("Unzipping:", size=(20, 1))
label_unzip_from_path = sg.Text("Select files to unarchive:", size=(20, 1))
input_box_unzip_path = sg.InputText(tooltip="Select input files", size=(40, 1))
label_unzip_to_path = sg.Text("Select output destination:", size=(20, 1))
input_box_unzip_output_path = sg.InputText(tooltip="Select output directory", size=(40, 1))
button_unzip_from = sg.FilesBrowse("Choose", key="unzip_file")
button_unzip_to = sg.FolderBrowse("Choose", key="unzip_folder")
button_unzip = sg.Button("Unzip", size=(7, 1), button_color=('white', 'green'))

# Front End - Window Interface
title = "FileZipper App"
new_window = sg.Window(title=title, layout=[
    [label_zip],
    [label_zip_from_path, input_box_zip_path, button_zip_from],
    [label_zip_to_path, input_box_zip_output_path, button_zip_to],
    [label_archive_name, file_name],
    [button_zip],
    [label_blank1],
    [label_unzip],
    [label_unzip_from_path, input_box_unzip_path, button_unzip_from],
    [label_unzip_to_path, input_box_unzip_output_path, button_unzip_to],
    [button_unzip]
])

while True:
    event, values = new_window.read()

    # Back End - Zipping
    if event == "Zip":
        files_input = values['zip_files'].split(';')
        files_to = values['zip_folder']
        output_filename = values['file_name']
        output_path = pathlib.Path(files_to, output_filename)
        try:
            with zipfile.ZipFile(output_path, mode="w") as archive:
                for path in files_input:
                    archive.write(path, os.path.basename(path))
            sg.popup(f"Archive is created: \n{output_path}")
        except FileNotFoundError:
            sg.popup(f"Specify files and try again!")

    # Back End - Unzipping
    elif event == "Unzip":
        files_input = values['unzip_file']
        dir_output = values['unzip_folder']
        try:
            with zipfile.ZipFile(files_input, 'r') as my_zip:
                my_zip.extractall(dir_output)
            sg.popup(f"Archive is extracted to: \n{dir_output}")
        except FileNotFoundError:
            sg.popup(f"Specify files and try again!")

    # Back End - Closing
    elif event == sg.WIN_CLOSED:
        break

new_window.close()
