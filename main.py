def sayi_al(alt_sinir,ust_sinir):
    sayi = input(f"{alt_sinir} ile {ust_sinir} arasında bir değer giriniz: ")
    while not(sayi.isdigit() and int(sayi)>=alt_sinir and int(sayi)<=ust_sinir):
        sayi = input(f"{alt_sinir} ile {ust_sinir} arasında bir değer giriniz: ")
    return int(sayi)

def oyun_alani_goster(satir_sayisi,satirdaki_sayilar,sutun_harfleri,oyun_alani_bosluklar):
    sutun_harfleri = sutun_harfleri[:satir_sayisi+1]
    print(' ',end='')
    for i in range(satir_sayisi):
        print(sutun_harfleri[i],end='   ')
    print(sutun_harfleri[satir_sayisi],end=' ')
    print()
    for j in range(satir_sayisi-1):
        print(satirdaki_sayilar[j],end='')
        for k in range(satir_sayisi):
            print(oyun_alani_bosluklar[j][k],end='')
            print('---',end='')
        print(oyun_alani_bosluklar[j][satir_sayisi],end='')
        print(satirdaki_sayilar[j])
        print(' |',end='')
        for a in range(satir_sayisi):
            print('   ',end='|')
        print()
    print(satirdaki_sayilar[satir_sayisi-1],end='')
    for b in range(satir_sayisi):
        print(oyun_alani_bosluklar[satir_sayisi-1][b],end='')
        print('---',end='')
    print(oyun_alani_bosluklar[satir_sayisi-1][satir_sayisi],end='')
    print(satirdaki_sayilar[satir_sayisi-1])
    print(' ', end='')
    for l in range(satir_sayisi):
        print(sutun_harfleri[l], end='   ')
    print(sutun_harfleri[satir_sayisi])


def tas_konumu_al(satir_sayisi,satirdaki_sayilar,sutun_harfleri):
    tas_konum = input('Taş yerleştirmek  istediğiniz konumu giriniz(2D): ')
    tas_konum = tas_konum.upper()
    while not (tas_konum[0].isdigit() and int(tas_konum[0]) in (satirdaki_sayilar[:satir_sayisi]) and tas_konum[1] in sutun_harfleri[:satir_sayisi+1] and len(tas_konum)==2):
        tas_konum = input('İşlem yapmak istediğiniz konumu giriniz: ')
        tas_konum = tas_konum.upper()
    return tas_konum

def tas_yerlestir(satir_sayisi,satirdaki_sayilar,sutun_harfleri,tas_rengi,oyun_alani_bosluklar):
    tas_konum = tas_konumu_al(satir_sayisi,satirdaki_sayilar,sutun_harfleri)
    while oyun_alani_bosluklar[int(tas_konum[0])-1][sutun_harfleri.index(tas_konum[1])] != ' ':
        print('Taş yerleştirmek istediğiniz yerde başka bir taş bulunmakta.Lütfen boş olan bir konuma hamle yapınız.')
        tas_konum = tas_konumu_al(satir_sayisi, satirdaki_sayilar, sutun_harfleri)
    oyun_alani_bosluklar[int(tas_konum[0]) - 1][sutun_harfleri.index(tas_konum[1])] = tas_rengi[0]
    oyun_alani_goster(satir_sayisi,satirdaki_sayilar,sutun_harfleri,oyun_alani_bosluklar)
    #print(oyun_alani_bosluklar)

def kare_kontrol(satir_sayisi,tas_rengi,oyun_alani_bosluklar,renk_kare_say):
    for i in range(int(satir_sayisi)-1):
        for j in range(int(satir_sayisi)):
            if oyun_alani_bosluklar[i][j] == oyun_alani_bosluklar[i][j+1] == oyun_alani_bosluklar[i+1][j] == oyun_alani_bosluklar[i+1][j+1] == tas_rengi[0]:
                renk_kare_say += 1
    return renk_kare_say

def tas_cikar(oyun_alani_bosluklar,tas_rengi,silinecek_tas_rengi,renk_kare_say,satir_sayisi,satirdaki_sayilar,sutun_harfleri):

    tas_konum = tas_konumu_al(satir_sayisi,satirdaki_sayilar,sutun_harfleri)
    while oyun_alani_bosluklar[int(tas_konum[0])-1][sutun_harfleri.index(tas_konum[1])] != silinecek_tas_rengi[0]:
        print("Rakibin taşını çıkarmak istediğiniz alanda rakibin taşı bulunmamaktadır.")
        tas_konum = tas_konumu_al(satir_sayisi, satirdaki_sayilar, sutun_harfleri)
    if sutun_harfleri.index(tas_konum[1]) != sutun_harfleri.index(sutun_harfleri[satir_sayisi]):
        while oyun_alani_bosluklar[int(tas_konum[0])-2][sutun_harfleri.index(tas_konum[1])] == oyun_alani_bosluklar[int(tas_konum[0])-1][sutun_harfleri.index(tas_konum[1])] == oyun_alani_bosluklar[int(tas_konum[0])-2][sutun_harfleri.index(tas_konum[1])+1] == oyun_alani_bosluklar[int(tas_konum[0])-1][sutun_harfleri.index(tas_konum[1])+1] or oyun_alani_bosluklar[int(tas_konum[0])-1][sutun_harfleri.index(tas_konum[1])]==oyun_alani_bosluklar[int(tas_konum[0])-2][sutun_harfleri.index(tas_konum[1])]== oyun_alani_bosluklar[int(tas_konum[0])-1][sutun_harfleri.index(tas_konum[1])-1]== oyun_alani_bosluklar[int(tas_konum[0])-2][sutun_harfleri.index(tas_konum[1])-1]:

            print("Çıkarmak istediğiniz rakip taş rakibin kare oluşturan taşlarından biri olduğu için bu taş çıkarılamaz.")
            tas_konum = tas_konumu_al(satir_sayisi, satirdaki_sayilar, sutun_harfleri)
        oyun_alani_bosluklar[int(tas_konum[0]) - 1][sutun_harfleri.index(tas_konum[1])] = ' '
        silinecek_tas_rengi.remove(silinecek_tas_rengi[-1])
        oyun_alani_goster(satir_sayisi,satirdaki_sayilar,sutun_harfleri,oyun_alani_bosluklar)
    else:
        while oyun_alani_bosluklar[int(tas_konum[0])-2][sutun_harfleri.index(tas_konum[1])] == oyun_alani_bosluklar[int(tas_konum[0])-1][sutun_harfleri.index(tas_konum[1])] == oyun_alani_bosluklar[int(tas_konum[0])-2][sutun_harfleri.index(tas_konum[1])-1] == oyun_alani_bosluklar[int(tas_konum[0])-1][sutun_harfleri.index(tas_konum[1])-1]:
            print(
                "Çıkarmak istediğiniz rakip taş rakibin kare oluşturan taşlarından biri olduğu için bu taş çıkarılamaz.")
            tas_konum = tas_konumu_al(satir_sayisi, satirdaki_sayilar, sutun_harfleri)
        oyun_alani_bosluklar[int(tas_konum[0]) - 1][sutun_harfleri.index(tas_konum[1])] = ' '
        silinecek_tas_rengi.remove(silinecek_tas_rengi[-1])
        oyun_alani_goster(satir_sayisi, satirdaki_sayilar, sutun_harfleri, oyun_alani_bosluklar)


def hamle_konumu_al(satir_sayisi,satirdaki_sayilar,sutun_harfleri,tas_rengi,oyun_alani_bosluklar,renk_kare_say):
    starting_point = input(f"{tas_rengi[0]} oyuncusunun hareket ettirmek istediği taşın konumunu giriniz(örnek 2D): ")
    starting_point = starting_point.upper()
    while not (starting_point[0].isdigit() and int(starting_point[0]) in satirdaki_sayilar[:satir_sayisi] and starting_point[1] in sutun_harfleri[:satir_sayisi+1] and oyun_alani_bosluklar[int(starting_point[0])-1][sutun_harfleri.index(starting_point[1])] == tas_rengi[0] ):
        starting_point = input(f"{tas_rengi[0]} oyuncusunun hareket ettirmek istediği taşın konumunu doğru giriniz(örnek 2D): ")
        starting_point = starting_point.upper()
    last_point = input(f"{tas_rengi[0]} oyuncusunun taşını hareket ettirmek istediği boş konumu giriniz (örnek 3D): ")
    last_point = last_point.upper()
    while not (
            last_point[0].isdigit() and int(last_point[0]) in satirdaki_sayilar[:satir_sayisi] and last_point[
        1] in sutun_harfleri[:satir_sayisi + 1] and oyun_alani_bosluklar[int(last_point[0]) - 1][
                sutun_harfleri.index(last_point[1])] == ' '):
        last_point = input(f"{tas_rengi[0]} oyuncusunun taşını hareket ettirmek istediği boş konumu doğru giriniz (örnek 3D): ")
        last_point = last_point.upper()
    while not(last_point[0]== starting_point[0] or last_point[1]==starting_point[1]):
        starting_point = input(
            f"{tas_rengi[0]} oyuncusunun hareket ettirmek istediği taşın konumunu doğru giriniz(örnek 2D): ")
        starting_point = starting_point.upper()
        last_point = input(
            f"{tas_rengi[0]} oyuncusunun taşını hareket ettirmek istediği boş konumu doğru giriniz (örnek 3D): ")
        last_point = last_point.upper()

    if starting_point[0] == last_point[0]:
        if max(sutun_harfleri.index(last_point[1]),sutun_harfleri.index(starting_point[1])) - min(sutun_harfleri.index(last_point[1]),sutun_harfleri.index(starting_point[1])) != 1:
            for i in range(min(sutun_harfleri.index(starting_point[1]),sutun_harfleri.index(last_point[1]))+1,max(sutun_harfleri.index(starting_point[1]),sutun_harfleri.index(last_point[1]))):
                while oyun_alani_bosluklar[satirdaki_sayilar.index(int(starting_point[0]))][i] != ' ':
                    print("Hareket ettirmek istediğiniz taş ile boş konum arasında başka bir taş bulunmaktadır.")
                    starting_point = input(f"{tas_rengi[0]} oyuncusunun hareket ettirmek istediği taşın konumunu doğru giriniz(örnek 2D): ")
                    starting_point = starting_point.upper()
                    last_point = input(f"{tas_rengi[0]} oyuncusunun taşını hareket ettirmek istediği boş konumu doğru giriniz (örnek 3D): ")
                    last_point = last_point.upper()
    elif starting_point[1] == last_point[1]:
        if max(satirdaki_sayilar.index(int(last_point[0])),satirdaki_sayilar.index(int(starting_point[0]))) - min(satirdaki_sayilar.index(int(last_point[0])),satirdaki_sayilar.index(int(starting_point[0]))) != 1:
            for i in range(min(satirdaki_sayilar.index(int(starting_point[0])),satirdaki_sayilar.index(int(last_point[0])))+1,max(satirdaki_sayilar.index(int(starting_point[0])),satirdaki_sayilar.index(int(last_point[0])))):
                while oyun_alani_bosluklar[i][sutun_harfleri.index(starting_point[1])] != ' ':
                    print("Hareket ettirmek istediğiniz taş ile boş konum arasında başka bir taş bulunmaktadır.")
                    starting_point = input(
                        f"{tas_rengi[0]} oyuncusunun hareket ettirmek istediği taşın konumunu doğru giriniz(örnek 2D): ")
                    starting_point = starting_point.upper()
                    last_point = input(
                        f"{tas_rengi[0]} oyuncusunun taşını hareket ettirmek istediği boş konumu doğru giriniz (örnek 3D): ")
                    last_point = last_point.upper()

    return starting_point,last_point


def hamle_yap(satir_sayisi,satirdaki_sayilar,sutun_harfleri,tas_rengi,oyun_alani_bosluklar,renk_kare_say,silinecek_tas_rengi):
    ilk_kare_say = kare_kontrol(satir_sayisi,tas_rengi,oyun_alani_bosluklar,renk_kare_say)
    ilk_konum,son_konum = hamle_konumu_al(satir_sayisi,satirdaki_sayilar,sutun_harfleri,tas_rengi,oyun_alani_bosluklar,renk_kare_say)
    oyun_alani_bosluklar[int(ilk_konum[0])-1][sutun_harfleri.index(ilk_konum[1])] = ' '
    oyun_alani_goster(satir_sayisi, satirdaki_sayilar, sutun_harfleri, oyun_alani_bosluklar)
    son_kare_say = kare_kontrol(satir_sayisi,tas_rengi,oyun_alani_bosluklar,renk_kare_say)
    if son_kare_say < ilk_kare_say:
        renk_kare_say -= 1
    oyun_alani_bosluklar[satirdaki_sayilar.index(int(son_konum[0]))][sutun_harfleri.index(son_konum[1])] = tas_rengi[0]
    kare_kontrol(satir_sayisi,tas_rengi,oyun_alani_bosluklar,renk_kare_say)
    if ilk_kare_say == renk_kare_say:
        tas_cikar(oyun_alani_bosluklar,tas_rengi,silinecek_tas_rengi,renk_kare_say,satir_sayisi,satirdaki_sayilar,sutun_harfleri)
    oyun_alani_goster(satir_sayisi,satirdaki_sayilar,sutun_harfleri,oyun_alani_bosluklar)


def main():
    satirdaki_sayilar = [1,2,3,4,5,6,7]
    sutun_harfleri = ['A','B','C','D','E','F','G','H']
    satir_sayisi = int(sayi_al(3,7))
    sutun_sayisi = int(satir_sayisi) + 1
    oyun_alani_bosluklar = []
    beyaz_kare_say = 0
    siyah_kare_say = 0
    for i in range(int(satir_sayisi)):
        oyun_alani_bosluklar.append([' ']* sutun_sayisi)
    oyun_alani_goster(satir_sayisi,satirdaki_sayilar,sutun_harfleri,oyun_alani_bosluklar)
    toplam_tas_say = satir_sayisi*sutun_sayisi
    beyaz_taslar = ['B']*(toplam_tas_say//2)
    siyah_taslar = ['S']*(toplam_tas_say//2)
    for i in range(satir_sayisi*sutun_sayisi//2):
        tas_yerlestir(satir_sayisi,satirdaki_sayilar,sutun_harfleri,beyaz_taslar,oyun_alani_bosluklar)
        tas_yerlestir(satir_sayisi, satirdaki_sayilar, sutun_harfleri, siyah_taslar, oyun_alani_bosluklar)
    beyaz_kare_say = kare_kontrol(satir_sayisi,beyaz_taslar,oyun_alani_bosluklar,beyaz_kare_say)
    siyah_kare_say = kare_kontrol(satir_sayisi,  siyah_taslar, oyun_alani_bosluklar,siyah_kare_say)
    print(beyaz_kare_say,siyah_kare_say)
    for i in range(beyaz_kare_say):
        tas_cikar(oyun_alani_bosluklar,beyaz_taslar,siyah_taslar,beyaz_kare_say,satir_sayisi,satirdaki_sayilar,sutun_harfleri)
    for j in range(siyah_kare_say):
        tas_cikar(oyun_alani_bosluklar,siyah_taslar,beyaz_taslar,siyah_kare_say,satir_sayisi,satirdaki_sayilar,sutun_harfleri)
    onceki_beyaz_kare_say = kare_kontrol(satir_sayisi,beyaz_taslar,oyun_alani_bosluklar,beyaz_kare_say)
    onceki_siyah_kare_say = kare_kontrol(satir_sayisi,siyah_taslar,oyun_alani_bosluklar,siyah_kare_say)
    while len(beyaz_taslar) >3 and len(siyah_taslar)>3:
        hamle_yap(satir_sayisi,satirdaki_sayilar,sutun_harfleri,beyaz_taslar,oyun_alani_bosluklar,beyaz_kare_say,siyah_taslar)
        kare_kontrol(satir_sayisi,beyaz_taslar,oyun_alani_bosluklar,beyaz_kare_say)
        if kare_kontrol(satir_sayisi,beyaz_taslar,oyun_alani_bosluklar,beyaz_kare_say) < onceki_beyaz_kare_say:
            onceki_beyaz_kare_say -= 1
        kare_kontrol(satir_sayisi, beyaz_taslar, oyun_alani_bosluklar, beyaz_kare_say)
        if kare_kontrol(satir_sayisi,beyaz_taslar,oyun_alani_bosluklar,beyaz_kare_say) > onceki_beyaz_kare_say:
            onceki_beyaz_kare_say += 1
            tas_cikar(oyun_alani_bosluklar,beyaz_taslar,siyah_taslar,beyaz_kare_say,satir_sayisi,satirdaki_sayilar,sutun_harfleri)

        hamle_yap(satir_sayisi,satirdaki_sayilar,sutun_harfleri,siyah_taslar,oyun_alani_bosluklar,siyah_kare_say,beyaz_taslar)
        kare_kontrol(satir_sayisi, siyah_taslar, oyun_alani_bosluklar, siyah_kare_say)
        if kare_kontrol(satir_sayisi,siyah_taslar,oyun_alani_bosluklar,siyah_kare_say)<onceki_siyah_kare_say:
            onceki_siyah_kare_say -= 1
        if kare_kontrol(satir_sayisi,siyah_taslar,oyun_alani_bosluklar,siyah_kare_say) > onceki_siyah_kare_say:
            onceki_siyah_kare_say += 1
            tas_cikar(oyun_alani_bosluklar,siyah_taslar,beyaz_taslar,siyah_kare_say,satir_sayisi,satirdaki_sayilar,sutun_harfleri)
    if len(beyaz_taslar) == 3:
        print(f"kazanan oyuncu {siyah_taslar[0]}")
    if len(siyah_taslar) == 3:
        print(f"kazanan oyuncu {beyaz_taslar[0]}")

if __name__ == '__main__':
    main()