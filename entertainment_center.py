# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:11:17 2018

@author: asingh368
"""

import media 
import fresh_oranges

toy_story = media.Movie("Toy Story", "A story about a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


#print(toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien planet",
                     r"https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     r"https://www.youtube.com/watch?v=6ziBFh3V1aM")

#print(avatar.storyline)
#avatar.show_trailer()

#https://www.youtube.com/watch?v=R0feRJtDj4c
lion_king = media.Movie("Lion King", "Story Of Simba", 
             "https://en.wikipedia.org/wiki/The_Lion_King_(2019_film)#/media/File:Disney_The_Lion_King_2019.jpg", 
             r"https://www.youtube.com/watch?v=R0feRJtDj4c")

#lion_king.show_trailer()
midnight_in_paris = media.Movie("Midnight in paris", "Love story about a Midnight in paris", 
                                "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg", 
                                r"https://www.youtube.com/watch?v=FAfR8omt-CY")


movies = [toy_story, avatar, lion_king, midnight_in_paris]
#fresh_oranges.open_movies_page(movies)

##print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)