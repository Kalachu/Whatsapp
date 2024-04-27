import requests
from bs4 import BeautifulSoup
import random
import string
import time

while True:
    # Open or create a text file to log valid invite links
    with open("valid_invite_links.txt", "a") as valid_file:
        # Open or create a text file to log invalid invite links
        with open("invalid_invite_links.txt", "a") as invalid_file:
            # Generate a random invite link
            invite_link = "https://chat.whatsapp.com/{}".format(''.join(random.choices(string.ascii_letters + string.digits, k=22)))
            
            #debug
            #invite_link = "https://chat.whatsapp.com/DAsQl6BNMJLAG8KtbCkHI0"

            # Use requests to fetch the HTML source code of the invite link
            response = requests.get(invite_link)

            # Parse the source code using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the <h3> tag
            h3_tag = soup.find('h3', {'class': '_9vd5 _9scr'})

            # Check whether the tag contains text or not
            if h3_tag and h3_tag.text:
                print("Invite link is valid!")
                valid_file.write(invite_link + " " + h3_tag.text + "\n")
            else:
                print("Invite link is invalid!" + " " + invite_link + "\n")
                invalid_file.write(invite_link + "\n")

    time.sleep(3)
