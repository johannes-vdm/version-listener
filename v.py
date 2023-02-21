import requests
import json
import xml.etree.ElementTree as ET
import winsound
import datetime
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

cwd = os.getcwd()

# Set the project name and expected version
project = "com.caseware.za.e.sme.2022"
file_name = "package.json"
package_file = os.path.join(cwd, file_name)

def get_expected_version():
    with open(package_file) as f:
        data = json.load(f)
        return data['version']

# Set the ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
END = "\033[0m"

# Open the log file
with open("vlog.txt", "a") as f:
    f.write("Starting log...\n")

expected_version = get_expected_version()

class PackageFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global expected_version
        if event.src_path.endswith(package_file):
            expected_version = get_expected_version()
            print(f"Expected version updated: {expected_version}")

observer = Observer()
observer.schedule(PackageFileHandler(), os.path.dirname(package_file), recursive=False)
observer.start()

while True:
    # Get the XML data from the URL
    url = "..."
    response = requests.get(url)
    root = ET.fromstring(response.text)

    for plugin_url in root.findall('pluginUrl'):
        url = plugin_url.get("url")
        params = dict(param.split("=") for param in url.split("?")[1].split("&"))

        product = params.get("product")
        version = params.get("version")

        if version is not None:
            version = version.split("-dev")[0]

        if not product or not version:
            continue

        # Check if the version matches the expected version
        if product == project:
            output = f"{product}: current: {version}, expected: {expected_version}"

            if version == expected_version:
                # Print a green message
                print(GREEN + "Version deployed!" + END)
                print(GREEN + output + END)
                # Play a system sound
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

                # Write the output to the log file
                with open("vlog.txt", "a") as f:
                    now = datetime.datetime.now()
                    f.write(f"[{now}] {output}\n")
                break
            else:
                # Print a red message
                print(BLUE + "Searching if version is deployed..." + END)
                print(output)
                # Write the output to the log file
                with open("vlog.txt", "a") as f:
                    now = datetime.datetime.now()
                    f.write(f"[{now}] {output}\n")

    time.sleep(5)
    new_expected_version = get_expected_version()
    if new_expected_version != expected_version:
        expected_version = new_expected_version
        print(f"Expected version updated: {expected_version}")
        continue
