## Import libraries
import json
from os import walk
import shutil
from zipfile import ZipFile
from datetime import date, datetime
import zipfile
import glob
import os

## Read config json
with open("config.json") as config_file:
    config = json.load(config_file)
conf = config
folder = config["folder"]
destination = config["destination"]
last_date = datetime.strptime(config["last_date"], "%Y-%m-%d").strftime("%Y-%m-%d")

def main():
    print("")

    ## calculate date

    now_date = date.today().strftime("%Y-%m-%d")
    if now_date > last_date:

        # names
        zip_destination = destination + "\\" + last_date + ".zip"

        ## Create Zip File
        zip_file = ZipFile(zip_destination, "w")
        print("\nZIP CREATED")

        ## Add content from folder
        for content in glob.iglob(folder + "\\" + '**\\*.*', recursive=True):
            if content.endswith('desktop.ini'):
                    continue
            print("    ADD: " + content.replace(folder + "\\", ""))
            zip_file.write(content, content.replace(folder + "\\", ""), zipfile.ZIP_DEFLATED)

        ## Close Zip File
        zip_file.close()
        print("ZIP CLOSED\n")

        ## Delete folder content
        for the_file in os.listdir(folder):
            if the_file.endswith('desktop.ini'):
                continue
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(e)

        with open("config.json", 'w') as config_file:
            conf["last_date"] = now_date
            json.dump(conf, config_file, indent=4)
    
    ## If last date equals to now date
    elif last_date == now_date:
        print("\nTRY TOMORROW")
    ## If no content in folder
    else:
        print("\nNO CONTENT IN FOLDER")

## For main function
if __name__ == "__main__":
    main()