class Media:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def give_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f'Name: {self.name} - Year {self.year} - {self.likes} Likes'


class Movie(Media):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'Movie: {self.name} - Year {self.year} - Duration {self.duration} - {self.likes} Likes'


class Serie(Media):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Serie: {self.name} - Year {self.year} - Seasons {self.seasons} - {self.likes} Likes'


class Playlist():
    def __init__(self, name, medias):
        self.name = name
        self._medias = medias

    def __getitem__(self, item):
        return self._medias[item]

    def __len__(self):
        return len(self._medias)


avengers = Movie('avengers - ininity war', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
scream = Movie('scream', 1999, 120)
daredevil = Serie('daredevil', 2003, 3)

avengers.give_like
scream.give_like
avengers.give_like
avengers.give_like
daredevil.give_like
scream.give_like
avengers.give_like
daredevil.give_like
scream.give_like
avengers.give_like
avengers.give_like
avengers.give_like
avengers.give_like
daredevil.give_like
atlanta.give_like
atlanta.give_like
daredevil.give_like


medias = [avengers, atlanta, daredevil, scream]
weekend_playlist = Playlist('Weekend', medias)

# This is a polymorphism/polimorfismo
# for media in medias:
#    duration = media.duration if hasattr(media, 'duration') else None
#    seasons = media.seasons if hasattr(media, 'seasons') else None
#    if duration:
#        print(
#            f"The Movie: {media.name} has {media.duration} minutes ({media.year}) | {media.likes} Likes")
#    elif seasons:
#        print(
#            f"The Serie: {media.name} has {media.seasons} seasons ({media.year}) | {media.likes} Likes")

# simplifying a bit more
print(
    f"Playlist: weekend_playlist.name - Size: {len(weekend_playlist)} Medias")

for media in weekend_playlist:
    print(f"  => {media}")
