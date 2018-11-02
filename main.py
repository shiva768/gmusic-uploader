from audio_metadata import MP3
from audio_metadata.formats.tables import ID3PictureType
from google_music import MusicManager
import random
import glob
import sys

CREDENTIAL = './credential'


def main():
    args = sys.argv
    target = '.'
    if len(args) > 0:
        target = args[0]
    monkey_patch()
    manager = MusicManager()
    list = glob.glob(f"{target}/*/*.mp3", recursive=True)
    for i in range(1, 1000):
        path = list[random.randint(1, len(list))]
        manager.upload(path)


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
