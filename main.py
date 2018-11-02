from google_music import MusicManager

CREDENTIAL = './credential'

def main():
    manager = MusicManager()
    manager.upload('/home/shibata/downloads/130cm - true eternity／instrumental.mp3')


if __name__ == '__main__':
    main()