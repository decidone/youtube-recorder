import requests
from bs4 import BeautifulSoup as bs
import subprocess
import time
import datetime

class YoutubeRecorder:
    def __init__(self):
        self.channel_id = 'channel-id' #channel id. not channel name
        self.quality = 'best'
        self.loop_time = 10.0
        self.file_path = 'C:/Users/user-name/Videos/'    #use '/' not '\'
        self.file_name = datetime.datetime.now().strftime('[%Y-%m-%d]%H%M%S')
        self.file_type = '.ts'

    def run(self):
        while True:
            self.file_name = datetime.datetime.now().strftime('[%Y-%m-%d]%H%M%S')
            response = requests.get('https://www.youtube.com/channel/'+ self.channel_id + '/live')
            soup = bs(response.content, 'html.parser')
            stream_link = soup.find('link', attrs={'rel':'canonical'})
            print(datetime.datetime.now().strftime('[%Y-%m-%d] %H:%M:%S'))
            if '/watch?v=' in stream_link['href']:
                print('Stream reservation found. Waiting for the stream is on')
                title = soup.find('meta', attrs={'name':'title'})
                print('Stream title : ' + title['content'])
                subprocess.call(['streamlink', stream_link['href'], self.quality, '-o', self.file_path + self.file_name + self.file_type])
            else:
                print('No stream reservation was found')

            time.sleep(self.loop_time)

if __name__ == '__main__':
    def main():
        yr = YoutubeRecorder()
        yr.run()

    main()
