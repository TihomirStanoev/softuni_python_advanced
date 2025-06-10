import os


directory_path = '.'
files_by_extension = {}

for item in os.listdir(directory_path):
    item_path = os.path.join(directory_path, item)
    if os.path.isfile(item_path):
        filename = item
        extension = os.path.splitext(filename)[1]
        if not extension:
            continue

        if extension not in files_by_extension:
            files_by_extension[extension] = []
        files_by_extension[extension].append(filename)

    elif os.path.isdir(item_path):
        for sub_item in os.listdir(item_path):
            sub_item_path = os.path.join(item_path, sub_item)
            if os.path.isfile(sub_item_path):
                filename = sub_item
                extension = os.path.splitext(filename)[1]
                if not extension:
                    continue

                if extension not in files_by_extension:
                    files_by_extension[extension] = []
                files_by_extension[extension].append(filename)

report_file_path = os.path.join(directory_path, 'report.txt')

with open(report_file_path, 'w') as report_file:
    sorted_extensions = sorted(files_by_extension.keys())

    for ext in sorted_extensions:
        report_file.write(f"{ext}\n")
        sorted_files = sorted(files_by_extension[ext])

        for file in sorted_files:
            report_file.write(f"- - - {file}\n")

