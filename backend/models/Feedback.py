from typing import List


class Feedback:
    liked: list
    disliked: list

    def __init__(self, likes: list, dislikes: list):
        self.liked = likes
        self.disliked = dislikes


