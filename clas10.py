class YouTube:
    def __init__(self, kanal, obuna):
        self.kanal = kanal
        self.obuna = obuna

    def add_sub(self, son):
        self.obuna += son
        print(f"▶️ {son} ta obunachi qoshildi")

    def info(self):
        print(f"📺 Kanal: {self.kanal}")
        print(f"👥 Obunachi: {self.obuna}")


yt = YouTube("Coder UZ", 1000)

yt.add_sub(500)
yt.add_sub(1200)

yt.info()