"""
    This script is used to update JSON file used by EBI to index pathogens portal.
    At every release, the triggered workflow will run this to update relevant info.
"""

import argparse
import requests
import os
from index_json_template import json_templete

def get_last_modified(url):
    response = requests.get(url)
    # For all files in blobserver, the info.json should have modified field in speciifc format
    return response.json()["modified"][2:10]

def check_and_update_content(index_file_path, info_to_update):
    index_content_new = json_templete.format(**info_to_update)
    # check if the content is same as old, then do not write again
    if os.path.exists(index_file_path):
        with open(index_file_path, "r") as index_file:
            if index_content_new == index_file.read():
                print("Content is same, not updating")
                return
    # write if the file doesn't exist or the content is updated
    with open(index_file_path, "w") as index_file:
        index_file.write(index_content_new)
        print("updated")
    return

if __name__ == "__main__":
    # define commadline parameters to easily pass release info
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", required=True)
    parser.add_argument("--release-date", required=True)
    args = parser.parse_args()

    # save the passed info in a dict
    info_to_update = {
        "release" : args.release,
        "release_date": args.release_date
    }
    
    # dataset for which frequent updates are made
    info_urls = {
        "dataset7" : "https://blobserver.dc.scilifelab.se/blob/swedishpop_subplot_button.json/info.json",
        "dataset8" : "https://blobserver.dc.scilifelab.se/blob/lineage_four_recent.json/info.json",
        "dataset10" : "https://blobserver.dc.scilifelab.se/blob/wastewater_data_gu_allviruses.xlsx/info.json",
        "dataset14" : "https://blobserver.dc.scilifelab.se/blob/SLU_wastewater_data.csv/info.json",
        "dataset16" : "https://blobserver.dc.scilifelab.se/blob/wastewater_data_gu_allviruses.xlsx/info.json",
        "dataset18": "https://blobserver.dc.scilifelab.se/blob/SLU_wastewater_data.csv/info.json"
    }

    # iterate thorugh the above dict and get recent modifed dates
    for key, url in info_urls.items():
        info_to_update[key + "_modified"] = get_last_modified(url)

    # the output file should in same folder as this script
    index_file_path = os.path.join(os.path.dirname(__file__), "pathogens_portal_index.json")
    check_and_update_content(index_file_path, info_to_update)
