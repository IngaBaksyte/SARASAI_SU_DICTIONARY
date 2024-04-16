# 1 užduotis. Parašykite programą, kuri sukurtų bylą sarasas.txt, kurioje būtų saugomi duomenys (duomenis
# saugoti programoje naudokite dict duomenų tipą, kur indeksas yra mokinio vardas, o reikšmė – ženkliukų,
# kurios reikia pagaminti su šiuo vardu, kiekis. Duomenims išrinkti naudokite set tipą. Taip pat galite naudoti
# ir list tipo duomenis.).

def valytiByla(byla):
    with open(byla, 'w', encoding='utf-8') as f:
        pass

def skaitytiByla(*klases):
    sarasas = []
    for klase in klases:
        with open(klase, 'r', encoding='utf-8') as f:
            sarasas.extend([vardas.strip() for vardas in f])
    return sarasas

def skaičiuotiZenkliukus(sarasas):
    sutvarkytasSarasas = dict()
    unikalusSarasas = set(sarasas)
    for vardas in unikalusSarasas:
        kiekis = sarasas.count(vardas)
        sutvarkytasSarasas[vardas] = kiekis
        #sutvarkytasSarasas[vardas] = {'kiekis': kiekis}
    return sutvarkytasSarasas

def rasytiSarasa(byla, sarasas):
    with open(byla, 'a', encoding='utf-8') as f:
        f.write('---------------------------\n')
        f.write('| Vardas         | Kiekis |\n')
        f.write('---------------------------\n')
        for vardas, kiekis in sarasas.items():
            f.write(f'| {vardas:14} | {kiekis:4}   |\n')
        f.write('---------------------------\n')

def skaiciuotiKaina(sarasas):
    for k, v in sarasas.items():
        kiekis = v
        if kiekis <= 3:
            kaina = 5 * kiekis
        elif kiekis <= 5:
            kaina = (5 * 3) + 4 + 3 * (kiekis - 4)
        else:
            kaina = (5 * 3) + (3 + kiekis)
        #print(kaina)
        sarasas[k] = [v, kaina]
        #sarasas[k] = {'kiekis': v, 'kaina': kaina}
    return sarasas

def rasytiSaskaita(byla, sarasas):
    with open(byla, 'a', encoding='utf-8') as f:
        f.write('-----------------------------------\n')
        f.write('| Vardas         | Kiekis | Kaina |\n')
        f.write('-----------------------------------\n')
        for vardas, info in sarasas.items():
            f.write(f'| {vardas:14} | {info[0]:4}   | {info[1]:4}  |\n')
            #f.write(f'| {vardas:14} | {info["kiekis"]:4}   | {info["kaina"]:4}  |\n')
        f.write('-----------------------------------\n')


valytiByla('01uzdDictSarasas.txt')
valytiByla('01uzdDictSaskaita.txt')

klasiuSarasas = skaitytiByla('12a.txt', '12b.txt', '12c.txt', '12d.txt', '12e.txt', '12f.txt', '12g.txt')

klasiuSarasasSuskaicuota = skaičiuotiZenkliukus(klasiuSarasas)
#klasiuSarasasPagalVarda = dict(sorted(klasiuSarasasSuskaicuota.items(), key = lambda kv: kv[0]))
#rasytiSarasa('01uzdDictSarasas.txt', klasiuSarasasPagalVarda)

klasiuSarasasPagalZenkl = dict(sorted(klasiuSarasasSuskaicuota.items(), key = lambda kv: -kv[1]))
rasytiSarasa('01uzdDictSarasas.txt', klasiuSarasasPagalZenkl)

saskaita = skaiciuotiKaina(klasiuSarasasPagalZenkl)
rasytiSaskaita('01uzdDictSaskaita.txt', saskaita)