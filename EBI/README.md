## EBI indexing

This folder contains

* `pathogens_portal_index.json` - a JSON file which is used by EBI to index provided information/datset from our website
* `update_index_json.py` - a python script that is used by github workflow (`update_index_json`) to update relavant information whenever a release is made.
* `index_json_template.py` - a python script with a JSON template that is imported and used in the `update_index_json.py` script
