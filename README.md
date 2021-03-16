# Space Webflow Homepage
This repo contains an python script that transform a webflow exported site into a valid fleek site

## Requirements:

- Python 3.8+

## How to use:

- Copy the exported files from webflow inside `src` directory
- Run the build file: `python build.py`
- A `dist` folder will be created with the transformed files

## Config file:
`config.json` file contains all the transforms and files that the script is going to work with:

- `project.src_path`: the source path.
- `project.build_path`: the build path where transformed files are going to be saved.
- `project.root_file_name`: name that is going to take a file if you specify the `move_to_subfolder: true` property into the `transforms` section for a specific file.
- `links_replacements`: common config to replace the `target` value by `replace_by` (used for links)
- `file_links_replacement`: common config to replace the `target` value by `replace_by` (used for file links)
- `transforms`: specify the files that should be transformed
