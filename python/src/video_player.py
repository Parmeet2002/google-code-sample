"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self._pause = False
        self._play = True

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        
        print("Here's a list of all available vidoes:")
        video_list = (self._video_library.get_all_videos())     #Create a variable with video title contents
        video_list.sort(key=lambda x: x.title)

        for video in video_list:                                #for every item in the list
            tagstring = str(video.tags)                         #Turn the tag into a string
            print(video.title,"(" ,video.video_id,")","[", tagstring.strip("()"),"]" ) #print the item

    def play_video(self, video_id):
     "Plays the respective video"

     video = self._video_library.get_video(video_id)
     
     if not video: 
        print("Cannot play video: Video does not exist")    ##If video id entered is not valid then video doesnt exist
        return 
    
     if self._current_video != None:
        print("Stopping video:" ,self._current_video.title) ##Stops current video
        print("Playing video:" ,video.title)                ##Starts playing next video
        self._current_video = video
        return 

     print("Playing video:" ,video.title)
     self._current_video = video

    def stop_video(self):
        """Stops the current video."""
    
        if self._current_video != None:
           print("Stopping video:", self._current_video.title)  ##If there is a video playing stop it
           self._current_video = None

        elif self._current_video == None:                       ##If there is no video playing display the message below
           print("Cannot stop video: No video is currently playing")
         

    def play_random_video(self):
        """Plays a random video from the video library."""
    
        if self._current_video != None:
           print("Stopping video: ", self._current_video.title) 
           random_vid = random.choice(self._video_library.get_all_videos()) ##Chooses a random video from the list
           print("Playing Video: ", random_vid.title)                       ##Plays the random video
           self._current_video = random_vid
           return
           
        elif self._current_video == None:
             random_vid = random.choice(self._video_library.get_all_videos())
             print("Playing Video: ", random_vid.title)
             self._current_video = random_vid
             return

    def pause_video(self):
        """Pauses the current video."""

        if self._current_video != None and self._pause == False:    ##For the case when video is playing
           print("Pausing video: ", self._current_video.title)
           self._pause = True
           self._play = False
           return

        elif self._pause == True:                                   ## For the case when video is already paused
            print("Video already paused: ", self._current_video.title)
            self._play = False
            return

        elif self._current_video == None:                           ##For the case when there is no video playing
             print("Cannot pause video: No video is currently playing")
             return
           

    def continue_video(self):
        """Resumes playing the current video."""

        if self._current_video != None and self._pause == True:     ##For the case when a video is paused
           print("Continuing video: ", self._current_video.title)
           self._pause = False
           self._play = True
           return

        elif self._current_video != None and self._play == True:    ##For the case when video is already playing
            print("Cannot continue video: Video is not paused")
            return

        elif self._current_video == None:                           ##For the case when no video is playing
            print("Cannot continue video: No video is currently playing")
            return


    def show_playing(self):
        """Displays video currently playing."""

        if self._current_video != None and self._pause == True:
            tagstring = str(self._current_video.tags)
            print("Currently playing: ", self._current_video.title, "(", self._current_video.video_id ,")", "[", tagstring.strip("()") ,"]", " - PAUSED")
            return

        elif self._current_video != None and self._play == True:
            tagstring = str(self._current_video.tags)
            print("Currently playing: ", self._current_video.title, "(", self._current_video.video_id ,")", "[", tagstring.strip("()") ,"]",)
            return
            
        elif self._current_video == None:
            print("No video is currently playing")
            return


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

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
