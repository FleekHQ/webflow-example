import os
import json
import shutil

print("building files:")

print("reading config file...")
with open("config.json") as f:
    config = json.load(f)

print("config file: ok")

if os.path.exists(config["project"]["build_path"]):
    print("deleting \"" + config["project"]["build_path"] + "\" path")
    shutil.rmtree(config["project"]["build_path"])

print("copying files...")
shutil.copytree(config["project"]["src_path"], config["project"]["build_path"], dirs_exist_ok=True)

for file in config["transforms"]:
    print("transforming \"" + file["filepath"] + "\"")
    filepath = os.path.join(config["project"]["build_path"], file["filepath"])

    with open(filepath, "r+") as f:
        content = f.read()

        if "inserts" in file:
            for insert in file["inserts"]:
                content = content.replace(insert["target"], insert["target"] + insert["text"])

        if file["apply_links_replacements"]:
            for replacement in config["links_replacements"]:
                content = content.replace(replacement["target"], replacement["replace_by"])

        if file["apply_file_links_replacements"]:
            for replacement in config["file_links_replacement"]:
                content = content.replace(replacement["target"], replacement["replace_by"])

        f.seek(0)
        f.write(content)
        f.truncate()

    if file["move_to_subfolder"]:
        dir_path = os.path.join(config["project"]["build_path"], file["name"])
        target_path = os.path.join(dir_path, config["project"]["root_file_name"])

        os.mkdir(dir_path)
        os.replace(filepath, target_path)

print("build completed successfully")
