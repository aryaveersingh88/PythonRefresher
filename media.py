# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:49:05 2018

@author: asingh368
"""
import webbrowser

class Movie():
    
    """This is a class about movies and storing them as objects"""
    
    VALID_RATINGS = ["G", "PG", "PG", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
       
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        