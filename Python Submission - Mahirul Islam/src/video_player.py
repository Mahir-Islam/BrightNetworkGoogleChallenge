"""A video player class."""
import random
from .video_library import VideoLibrary

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.all_videos = self._video_library._videos #dictionary
        self.current_video = ""
        self.paused = False
        self.playlists = {}
        self.listen_for_number = False
        self.tag_listen_for_number = False
        self.vidlist = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):

        print("Here's a list of all available videos:")
        for video_id in self.all_videos:
            video = self.all_videos.get(video_id, None)
            print(f"{video.title} ({video_id}) [{' '.join(video.tags)}]")

    def play_video(self, video_id):

        exist = False
        for v_id in self.all_videos:
            if v_id == video_id:
                title = self.all_videos.get(v_id, None).title
                exist = True

        if exist:
            if self.current_video != "":
                print(f"Stopping video: {self.all_videos.get(self.current_video, None).title}")

            self.current_video = video_id
            print(f"Playing video: {self.all_videos.get(self.current_video, None).title}")
            self.paused = False

        elif not exist:
            print("Cannot play video: Video does not exist")

    def stop_video(self):

        if self.current_video == "":
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self.all_videos.get(self.current_video, None).title}")
            self.current_video = ""

    def play_random_video(self):

        num_videos = len(self._video_library.get_all_videos())

        if num_videos == 0:
            print("No videos available")
        else:
            w = random.choice( list( self.all_videos.keys() ))
            while w == self.current_video: 
                w = random.choice( list( self.all_videos.keys() ) )
            self.play_video(w)

    def pause_video(self):
        if self.current_video == "":
            print("Cannot pause video: No video is currently playing")
        else:
            if self.paused:
                print(f"Video already paused: {self.all_videos.get(self.current_video, None).title}")
            elif not self.paused:
                print(f"Pausing video: {self.all_videos.get(self.current_video, None).title}")
                self.paused = True

    def continue_video(self):
        if self.current_video == "":
            print("Cannot continue video: No video is currently playing")
        else:
            if not self.paused:
                print(f"Cannot continue video: Video is not paused")
            elif self.paused:
                print(f"Continuing video: {self.all_videos.get(self.current_video, None).title}")
                self.paused = False

    def show_playing(self):

        P = ""
        if self.paused:
            P = "- PAUSED"

        if self.current_video == "":
            print("No video is currently playing")
        else:
            print(f"{self.all_videos.get(self.current_video, None).title} ({self.current_video}) [{' '.join(self.all_videos.get(self.current_video, None).tags)}] {P}")

    def create_playlist(self, playlist_name):
        name = playlist_name.upper()
        if name in self.playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlists[name] = []
            print(f"Successfully created new playlist: {name}")


    def add_to_playlist(self, playlist_name, video_id):

        title = ""
        exist = False
        name = playlist_name.upper()

        for v_id in self.all_videos:
            if v_id == video_id:
                title = self.all_videos.get(v_id, None).title
                exist = True

        if not exist:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        elif exist:
            if name not in self.playlists:
                print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            elif video_id in self.playlists[name]:
                print(f"Cannot add video to {playlist_name}: Video already added")
            else:
                self.playlists[name].append(video_id)
                print(f"Added video to {playlist_name}: {title}")

    def show_all_playlists(self):
        linebreak = "\n"
        print(f"Showing all playlists: {linebreak}{f' {linebreak}'.join(list(self.playlists.keys()) )}")

    def show_playlist(self, playlist_name):

        vidlist = ""
        linebreak = "\n"
        name = playlist_name.upper()

        if name not in self.playlists:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            return
        elif self.playlists[name] == []:
            vidlist = "No videos here yet"
        else:
            for v_id in self.playlists[name]:
                video = self.all_videos.get(v_id, None)
                vidlist += f"{video.title} ({v_id}) [{f' '.join(video.tags)}] {linebreak}"

        print(f"""Showing playlist: {playlist_name}: {linebreak} {vidlist}""")

    def remove_from_playlist(self, playlist_name, video_id):
        title = ""
        exist = False
        name = playlist_name.upper()

        for v_id in self.all_videos:
            if v_id == video_id:
                title = self.all_videos.get(v_id, None).title
                exist = True

        if not exist:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
        elif exist:
            if name not in self.playlists:
                print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
            elif video_id in self.playlists[name]:
                self.playlists[name].remove(video_id)
                print(f"Removed video from {playlist_name}: {title}")
            else:
                print(f"Cannot remove video from {playlist_name}: Video is not in playlist")

    def clear_playlist(self, playlist_name):
        name = playlist_name.upper()

        if name not in self.playlists:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        elif self.playlists[name] == []:
            print(f"Cannot clear playlist {playlist_name}: Playlist is already empty")
        else:
            print(f"Successfully removed all videos from: {playlist_name}")
            self.playlists[name] = []


    def delete_playlist(self, playlist_name):
        name = playlist_name.upper()

        if name not in self.playlists:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            print(f"Deleted playlist: {playlist_name}")
            self.playlists.pop(name)


    def search_videos(self, search_term, number = -1):

        search_term = search_term.lower()
        linebreak = "\n"
        self.all_videos
        self.vidlist = []
        titles = []

        for video_id in self.all_videos:
            if search_term in self.all_videos.get(video_id, None).title.lower():
                self.vidlist.append(video_id)
                titles.append(self.all_videos.get(video_id, None).title)

        titles = sorted(titles)

        list_str = f"Here are the results for {search_term}:"
        i = 0
        for title in titles:
            list_str += f"{linebreak}{i+1}) {title} ({self.vidlist[i]}) [{' '.join(self.all_videos.get(self.vidlist[i], None).tags)}]"
            i+=1

        list_str += f"{linebreak}Would you like to play any of the above? If yes, specify the number of the video. If your answer is not a valid number, we will assume it's a no."
        if titles == []:
            list_str = f"No search results for {search_term}"
        print(list_str)

        self.listen_for_number = True

    def search_videos_tag(self, video_tag):

        video_tag = video_tag.lower()
        linebreak = "\n"
        self.all_videos
        self.vidlist = []
        titles = []

        for video_id in self.all_videos:
            if video_tag in self.all_videos.get(video_id, None).tags:
                self.vidlist.append(video_id)
                titles.append(self.all_videos.get(video_id, None).title)

        titles = sorted(titles)

        list_str = f"Here are the results for {video_tag}:"
        i = 0
        for title in titles:
            list_str += f"{linebreak}{i+1}) {title} ({self.vidlist[i]}) [{' '.join(self.all_videos.get(self.vidlist[i], None).tags)}] "
            i+=1

        list_str += f"{linebreak}Would you like to play any of the above? If yes, specify the number of the video. If your answer is not a valid number, we will assume it's a no."
        if titles == []:
            list_str = f"No search results for {video_tag}"
        print(list_str)

        self.tag_listen_for_number = True

    def index_value(self, number):
        number = abs(int(number))

        if self.listen_for_number:
            self.play_video(self.vidlist[number-1])
            self.listen_for_number = False
        elif self.tag_listen_for_number:
            self.play_video(self.vidlist[number-1])
            self.tag_listen_for_number = False