## Install Pytube
pip install pytube

import pytube

## Provide the Youtube video link
video_url=input('Please provide Youtube URL: ')
## Output Path
path='/sample_data/'

pytube.YouTube(video_url).streams.get_highest_resolution().download(path)