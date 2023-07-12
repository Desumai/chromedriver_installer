### py script to install the selenium chrome driver for the user's chrome version
### Creator: Desumai
### Date Created: 2023/7/12
### Date Modified: 2023/7/12

from bs4 import BeautifulSoup
from urllib.error import HTTPError
import requests, os


URL = "https://chromedriver.storage.googleapis.com/"
fileExt = "chromedriver_win32.zip"

try:
    print("Enter Chrome Version (e.g. 114.0.5735.199):")
    version = input()

    # check if input is in correct format (4 period seperated integers)
    checkStrs = version.split(".")
    if len(checkStrs) != 4:
        raise ValueError(
            "Improper chrome version. See chrome://settings/help to find your chrome version."
        )
    for checkStr in checkStrs:
        try:
            int(checkStr)
        except ValueError:
            raise ValueError(
                "Improper chrome version. See chrome://settings/help to find your chrome version."
            )

    # get file path
    idURL = URL + "LATEST_RELEASE_" + version[: version.rindex(".")]
    page = requests.get(idURL)
    soup = BeautifulSoup(page.content, "html.parser")
    filePath = soup.prettify().replace("\n", "")

    # TODO: get other OS chrome drivers
    fileURL = URL + filePath
    fileURL = fileURL + "/" + fileExt
    print(fileURL)
    page = requests.get(fileURL)
    if page.status_code != 200:
        raise HTTPError(code=page.status_code, url=fileURL)
    print("Driver found. Downloading...")
    downloadPath = os.getcwd() + "\\downloads\\" + version + "_" + fileExt
    with open(downloadPath, "wb") as file:
        file.write(page.content)
    print("Finished.")
    print("Saved to " + downloadPath)
    print("Press ENTER to exit...")

except ValueError as e:
    print(e)
except HTTPError as e:
    if e.code == 404:
        print("Error: url '" + e.url + "' not found.")
    else:
        print(e.code + " Error. Could not get driver.")
except Exception as e:
    print(e)
