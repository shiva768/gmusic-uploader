from gmusicapi import Musicmanager

CREDENTIAL = './credential'

def main():
    manager = Musicmanager()
    login(manager)
    manager.upload('/home/shibata/downloads/130cm - true eternity／instrumental.mp3')

def login(manager:Musicmanager):
     if not manager.login(CREDENTIAL):
        manager.perform_oauth(storage_filepath=CREDENTIAL, open_browser=True)


if __name__ == '__main__':
    main()