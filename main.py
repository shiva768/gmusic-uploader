from audio_metadata import MP3
from audio_metadata.formats.tables import ID3PictureType
from google_music import MusicManager
CREDENTIAL = './credential'



org = MP3.load
def load(data):
    r = org(data)
    if len(r.pictures) > 0 and r.pictures[0].type == ID3PictureType.OTHER:
        r.pictures[0].type = ID3PictureType.COVER_FRONT
    return r

MP3.load = load

def main():
    manager = MusicManager()
    manager.upload('/home/shibata/downloads/130cm - せせりのテーマ.mp3')


if __name__ == '__main__':
    main()