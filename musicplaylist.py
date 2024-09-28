class Song_add():
    def __init__(self,singer,song_name,duration):
        self.song_name=song_name
        self.singer= singer
        self.durt = duration

    def details(self):
        return [self.song_name,self.singer,self.durt]
    

class Music_pl():
    def __init__(self):
        self.all_song = []

    def add_playlist(self,music_details):
        self.all_song.append(music_details())
        print()
        return self.all_song

    def show_up(self):
        return self.all_song
    
    def searchWmusicName(self,musicname_add):
        result=[]
        for i in self.all_song:
            if musicname_add.lower() == i[0].lower():
                result.append(i)

        if result:
            for a in result:  # Sadece sonuçlar varsa yazdır
                print(f"Music Name: {a[0]}, Singer: {a[1]}, Duration: {a[2]}")
        else:
            print("Not found")  # Eğer sonuç yoksa, "Not found" mesajı döndür
        
            
    def searchWSinger(self,singer_name):
        result = []
        for i in self.all_song:
            if singer_name.lower() == i[1].lower():
                result.append(i)
        if result:
            for a in result:  # Sadece sonuçlar varsa yazdır
                print(f"Music Name: {a[0]}, Singer: {a[1]}, Duration: {a[2]}")
        else:
            print("Not found")  # Eğer sonuç yoksa, "Not found" mesajı döndür
