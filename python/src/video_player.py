"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.currently_playing = "none"
        self.playing = False
        self.playlists = {}

        self.video_titles = [video.title for video in self._video_library.get_all_videos()]
        self.video_ids = [video.video_id for video in self._video_library.get_all_videos()]
        self.video_tags = [list(video.tags) for video in self._video_library.get_all_videos()]

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for i in range(len(self.video_titles)):
            print(f"{self.video_titles[i]} ({self.video_ids[i]}) {self.video_tags[i]}")

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        for i in range(len(self.video_titles)):
            if self.video_ids[i] == video_id:
                print(f"Playing video: {self.video_titles[i]}")
                self.playing = True
                self.currently_playing = self.video_titles[i]
                return
        print("Cannot play video: Video does not exist")
            
        
    def stop_video(self):
        """Stops the current video."""
        if (self.currently_playing != "none") :
            print(f"Stopping video: {self.currently_playing}")
            self.currently_playing = "none"
            self.playing = False
            return
        print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""
        num_videos = len(self.video_titles)

        if num_videos != 0 :
            if self.currently_playing == "none":
                self.play_video(self.video_ids[random.randint(0, num_videos - 1)])
                return
            else:
                print(f"Stopping video: {self.currently_playing}")
                self.play_video(self.video_ids[random.randint(0, num_videos - 1)])
                return
        print("No Videos in library.")

    def pause_video(self):
        """Pauses the current video."""
        if self.playing:
            print(f"Pausing video: {self.currently_playing}")
            self.playing = False
        elif self.currently_playing == "none":
            print("Cannot pause video: No video is currently playing")
        else:
            print(f"Video already paused: {self.currently_playing}")


    def continue_video(self):
        """Resumes playing the current video."""
        if (self.playing == False):
            if (self.currently_playing != "none"):
                print(f"Continuing video: {self.currently_playing}")
                self.playing = True
            else:
                print("Cannot continue video: No video is currently playing")
        else:
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""

        for i in range(len(self.video_titles)):
            if self.playing:
                if self.currently_playing == self.video_titles[i]:
                    print(f"{self.video_titles[i]} ({self.video_ids[i]}) {self.video_tags[i]}")
                    return
            else:
                if self.currently_playing == self.video_titles[i]:
                    print(f"{self.video_titles[i]} ({self.video_ids[i]}) {self.video_tags[i]} - PAUSED")
                    return
        print("No video is currently playing")
        

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        if playlist_name.upper() in self.playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
            return
        print(f"Successfully created new playlist: {playlist_name}")
        self.playlists[playlist_name.upper()] = Playlist(playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.upper() not in self.playlists:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return
        if video_id not in self.video_ids:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        if self.video_titles[self.video_ids.index(video_id)] in self.playlists[playlist_name.upper()].videos:
            print(f"Cannot add video to {playlist_name}: Video already added")
            return
        video_name = self.video_titles[self.video_ids.index(video_id)]
        print(f"Added video to {playlist_name}: {video_name}")
        self.playlists[playlist_name.upper()].videos.append(video_name)

    def show_all_playlists(self):
        """Display all playlists."""
        if not self.playlists:
            print("No playlists created yet.")
            return
        print("Showing all playlists:")
        for playlist in sorted(self.playlists):
            print(self.playlists[playlist].playlist_name)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() not in self.playlists:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist") 
            return
        if not self.playlists[playlist_name.upper()].videos:
            print(f"Showing playlist: {playlist_name}\n  No videos here yet")
            return
        print("Showing playlist: {playlist_name}")
        for video in self.playlists[playlist_name.upper()].videos:
            if video in self.video_titles:
                print(f"  {video} ({self.video_ids[self.video_titles.index(video)]}) {self.video_tags[self.video_titles.index(video)]}")    

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.upper() not in self.playlists:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
            return
        if video_id not in self.video_ids:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            return
        for video_title in self.video_titles:
            if video_id == self.video_ids[self.video_titles.index(video_title)]:
                if video_title not in self.playlists[playlist_name.upper()].videos:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
                    return
                self.playlists[playlist_name.upper()].videos.remove(video_title)
                print(f"Removed video from {playlist_name}: {video_title}")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() not in self.playlists:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
            return
        print(f"Successfully removed all videos from {playlist_name}")
        self.playlists[playlist_name.upper()].videos = []

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() not in self.playlists:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
            return
        
        print(f"Deleted playlist: {playlist_name}")
        self.playlists.pop(playlist_name.upper())        

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        i = 1
        results = []
        result_ids = []
        for video_title in sorted(self.video_titles):
            if search_term.upper() in video_title.upper():
                results.append(f"{i}) {video_title} ({self.video_ids[self.video_titles.index(video_title)]}) {self.video_tags[self.video_titles.index(video_title)]}")
                result_ids.append(self.video_ids[self.video_titles.index(video_title)])
                i += 1
        if i == 1:
            print(f"No search results for {search_term}")
            return
        print(f"Here are the results for {search_term}:")
        for result in results:
            print(result)
        print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
        try:
            play_number = int(input())
        except:
            return
        if play_number == i:
            return
        if play_number:
            self.play_video(result_ids[play_number-1])

    def search_videos_tag(self, search_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        i = 1
        results = []
        result_ids = []
        for video_tag_list in self.video_tags:
            if search_tag.lower() in video_tag_list:
                results.append(f"{i}) {self.video_titles[self.video_tags.index(video_tag_list)]} ({self.video_ids[self.video_tags.index(video_tag_list)]}) {video_tag_list}")
                result_ids.append(self.video_ids[self.video_tags.index(video_tag_list)])
                i += 1
        if i == 1:
            print(f"No search results for {search_tag}")
            return
        print(f"Here are the results for {search_tag}:")
        for result in results:
            print(result)
        print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
        try:
            play_number = int(input())
        except:
            return
        if play_number == i:
            return
        if play_number:
            self.play_video(result_ids[play_number-1])

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
