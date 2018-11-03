from audio_metadata import MP3
from audio_metadata.formats.tables import ID3PictureType
from google_music import MusicManager
import google_music
import random
import glob
import sys

from tenacity import RetryError

CREDENTIAL = './'


def main():
    args = sys.argv
    target = '.'
    max_num = 1000
    print(args)
    if len(args) > 2:
        print(len(args))
        target = args[1]
        max_num = int(args[2])
    monkey_patch()
    google_music.session.TOKEN_DIR = CREDENTIAL
    manager = MusicManager()
    list = glob.glob(f"{target}/**/*.mp3", recursive=True)
    if len(list) <= 0:
        print('list empty')
        sys.exit()
    for i in range(1, max_num):
        path = list[random.randint(1, len(list))]
        try:
            print(f"try [{path}]")
            manager.upload(path)
            print(f"success [{path}]")
        except RetryError as e:
            print(f"failed [{path}]")



def monkey_patch():
    org = MP3.load

    def load(data):
        r = org(data)
        if len(r.pictures) > 0 and r.pictures[0].type == ID3PictureType.OTHER:
            r.pictures[0].type = ID3PictureType.COVER_FRONT
        return r

    MP3.load = load


if __name__ == '__main__':
    main()
