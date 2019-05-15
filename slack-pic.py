"""
Primary function for changing profile picture
"""
import glob
import os
import random
import subprocess

AUTH_TOKEN = "YOUR TOKEN HERE"
PIC_DIRECTORY = "/path/to/your/image/folder"
WAIT_TIME = 60 * 5

def main():
    """
    Main func for selecting random image and setting Slack
    display pic to it
    """

    path = os.path.join(PIC_DIRECTORY, "*")
    all_files = glob.glob(path)

    image = random.choice(all_files)
    args = [
        "curl", "https://slack.com/api/users.setPhoto",
        "-F", "token={}".format(AUTH_TOKEN),
        "-F", "image=@{}".format(image),
    ]
    subprocess.check_call(args=args)

if __name__ == "__main__":
    main()
