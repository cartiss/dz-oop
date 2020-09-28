class Album:
    def __init__(self, name, group, list):
        self.name = name
        self.group = group
        self.list = list

    def get_tracks(self):
        for track in self.list:
            track.show()

    def add_track(self, name_track, time_track):
        new_track = Track(name_track, time_track)
        self.list.append(new_track)
        print(self.list)

    def get_duration(self):
        sum = 0
        for track in self.list:
            sum += track.time
        print(sum)


class Track(Album):
    def __init__(self, name, time):
        self.name = name
        if not isinstance(time, int):
            return
        self.time = time # sec

    def show(self):
        print(self.name, '-', self.time)

album_1 = Album('Rock\'n\'Roll', 'Bits', [Track('Name1', 150), Track('Name2', 160), Track('Name3', 100)])
album_2 = Album('Rock', 'Alebaba', [Track('Rock1', 170), Track('Rock2', 190), Track('Rock3', 120)])

album_1.get_duration()
album_2.get_duration()
