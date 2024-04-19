import math

class BangunRuang:
    def luas(self):
        pass

    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return 6 * self.sisi ** 2

    def volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def luas(self):
        return 2 * ((self.panjang * self.lebar) + (self.panjang * self.tinggi) + (self.lebar * self.tinggi))

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class Bola(BangunRuang):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 4 * math.pi * self.jari_jari ** 2

    def volume(self):
        return (4/3) * math.pi * self.jari_jari ** 3

class Silinder(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def luas(self):
        return 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)

    def volume(self):
        return math.pi * self.jari_jari ** 2 * self.tinggi

class PrismaSegitiga(BangunRuang):
    def __init__(self, alas, tinggi_alas, tinggi_prisma):
        self.alas = alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_prisma = tinggi_prisma

    def luas(self):
        return 0.5 * self.alas * self.tinggi_alas + (self.alas * self.tinggi_prisma)

    def volume(self):
        return 0.5 * self.alas * self.tinggi_alas * self.tinggi_prisma

def main():
    # Membuat objek-objek bangun ruang
    kubus = Kubus(5)
    balok = Balok(3, 4, 5)
    bola = Bola(7)
    silinder = Silinder(4, 6)
    prisma = PrismaSegitiga(6, 8, 10)

    # Menampilkan luas dan volume dari masing-masing bangun ruang
    print("Luas dan Volume Bangun Ruang:")
    print("1. Luas Kubus:  ",kubus.luas())
    print("   Volume Kubus: ", kubus.volume())
    print("2. Luas Balok: ", balok.luas())
    print("   Volume Balok: ", balok.volume())
    print("3. Luas Bola: ", bola.luas())
    print("   Volume Bola: ", bola.volume())
    print("4. Luas Silinder: ", silinder.luas())
    print("   Volume Silinder: ", silinder.volume())
    print("5. Luas Prisma Segitga: ", prisma.luas())
    print("   Volume prisma Segitga: ", prisma.volume())

if __name__ == "__main__":
    main()