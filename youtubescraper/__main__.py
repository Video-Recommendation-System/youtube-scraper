import numpy as np
import sys
import yapi

def main():
    input_file = sys.argv[1]
    api_key = readfile(sys.argv[2])[0]
    contents = readfile(input_file)

    api = yapi.YoutubeAPI(api_key)

    print contents


    channel_playlist_id = get_channel_playlist_id(api, "MatthewPatrick13")
    print channel_playlist_id
    channel_videos = get_channel_videos(api, channel_playlist_id)

    print channel_videos

    for video_id in channel_videos:
        video = grab_video(api, video_id)
        info = get_video_info(video_id, video)
        for x in info:
            print x

        print "~~~~~~~~~~~~~~~~~~~~"
        print "~~~~~~~~~~~~~~~~~~~~"
        print "~~~~~~~~~~~~~~~~~~~~"


def readfile(filepath):
    with open(filepath) as f:
        content = [x.strip() for x in f.readlines()]
        return content

def grab_video(api, video_id):
    return api.get_video_info(video_id)

def get_video_info(video_id, video):
    return [
        video_id,
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

def get_channel_id(api, channel_name):
    return api.get_channel_by_name(channel_name).items[0].id

def get_channel_playlist_id(api, channel_name):
    return api.get_channel_by_name(channel_name).items[0].contentDetails.relatedPlaylists.uploads

def get_channel_videos(api, channel_playlist_id):
    return [x.contentDetails.videoId for x in api.get_playlist_items_by_playlist_id(channel_playlist_id, max_results=10).items]

if __name__ == "__main__":
    main()
