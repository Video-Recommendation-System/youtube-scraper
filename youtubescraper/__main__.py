import numpy as np
import sys
import yapi

def main():
    input_file = sys.argv[1]
    api_key = sys.argv[2]
    contents = readfile(input_file)

    api = yapi.YoutubeAPI(api_key)

    print contents

    for video_id in contents:
        print video_id
        video = grab_video(api, video_id)
        info = get_video_info(video)
        for x in info:
            print x

def readfile(filepath):
    with open(filepath) as f:
        content = [x.strip() for x in f.readlines()]
        return content

def grab_video(api, video_id):
    return api.get_video_info(video_id)

def get_video_info(video):
    return [
        get_video_title(video),
        get_video_description(video),
        str(get_video_tags(video)),
        get_channel_title(video),
        get_video_thumbnail(video)
    ]

def get_video_title(video):
    return video.items[0].snippet.title

def get_video_description(video):
    return video.items[0].snippet.description

def get_video_tags(video):
    return video.items[0].snippet.tags

def get_channel_title(video):
    return video.items[0].snippet.channelTitle

def get_video_thumbnail(video):
    return video.items[0].snippet.thumbnails.default.url

if __name__ == "__main__":
    main()
