# https://python.plainenglish.io/how-to-automatically-download-bulk-images-for-your-dataset-using-python-f1efffba7a03
# https://github.com/theDreamer911/image_downloader
# https://www.youtube.com/watch?v=t2k5Lsbpj8Y&t=1s

# pip install requests
# pip install bs4

# unlimited download
# specifying new folder path !

"""
# https://bobbyhadz.com/blog/python-attributeerror-module-collections-has-no-attribute-mutablemapping
try:
    #  using Python 3.10+
    from collections.abc import MutableMapping
except ImportError:
    # ️ using Python 3.10-
    from collections import MutableMapping

#  <class 'collections.abc.MutableMapping'>
print(MutableMapping)

"""

import os
import requests
from bs4 import BeautifulSoup
import collections


# First Section: Importing Libraries
import os
import requests
from bs4 import BeautifulSoup

# Second Section: Declare important variables
google_image = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

# Third Section: Build the main function
saved_folder = 'images'

def main():
    if not os.path.exists(saved_folder):
        os.mkdir(saved_folder)
    download_images()


def download_images():
    data = input('What are you looking for? ')
    n_images = int(input('How many images do you want? '))
    new_folder = input('Enter the new folder path: ')
    
    if not new_folder:
        new_folder = saved_folder

    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    print('searching...')

    page = 0
    counter = 0
    while counter < n_images:
        search_url = google_image + 'q=' + data + '&start=' + str(page * 100)

        response = requests.get(search_url, headers=user_agent)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        results = soup.findAll('img', {'class': 'rg_i Q4LuWd'})

        links = []
        for result in results:
            try:
                link = result['data-src']
                links.append(link)
                counter += 1
                if counter == n_images:
                    break
            except KeyError:
                continue

        print(f"Downloading {len(links)} images...")

        for i, link in enumerate(links):
            response = requests.get(link)
            image_name = os.path.join(new_folder, data + str(i + page * 80) + '.jpg')
            with open(image_name, 'wb') as fh:
                fh.write(response.content)

        if len(links) == 0 or counter == n_images:
            break
        page += 1


# Fifth Section: Run your code
if __name__ == "__main__":
    main()
