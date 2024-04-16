def valytiByla(byla):
    with open(byla, 'w', encoding='utf-8') as f:
        pass

def skaitytiByla(byla):
    duomenys = {}
    with open(byla, 'r', encoding='utf-8') as f:
        eilutes = f.readlines()
        for eilute in eilutes:
            vardas = eilute.split(' ')[0]
            duomenys[vardas] = float(eilute.strip().split(' ')[1])
    return duomenys

def atrinktiMokinius(sarasas):
    bendrasVid = sum(sarasas.values()) / len(sarasas)
    atrinktiMokiniai = {}
    for mokinys, vidurkis in sarasas.items():
        if vidurkis >= bendrasVid:
            atrinktiMokiniai[mokinys] = vidurkis
    #atrinktiMokiniai = {mokinys: vidurkis for mokinys, vidurkis in sarasas.items() if vidurkis >= bendrasVid}
    return atrinktiMokiniai

def surikiuotiMokinius(sarasas):
    surikiuotiMokiniai = dict(sorted(sarasas.items(), key=lambda kv: (-kv[1], kv[0])))
    return surikiuotiMokiniai

def rasytiIByla(byla, sarasas, tekstas):
    with open(byla, 'a', encoding='utf-8') as f:
        f.write('----------------------\n')
        f.write(f'{tekstas}\n')
        for vardas, vid in sarasas.items():
            f.write(f' {vardas:12} {vid:>6.2f}\n')


valytiByla('02uzdDictRez.txt')
klases = ['duom3_1.txt', 'duom3_2.txt', 'duom3_3.txt', 'duom3_4.txt']

visosKlases = {}
n = 1
for klase in klases:
    klasesDuomenys = skaitytiByla(klase)
    atrinktiIrSurikiuoti = atrinktiMokinius(surikiuotiMokinius(klasesDuomenys))
    rasytiIByla('02uzdDictRez.txt', atrinktiIrSurikiuoti, f'Klasė {n}:')
    n += 1
    visosKlases.update(atrinktiIrSurikiuoti)

rezultatas = atrinktiMokinius(surikiuotiMokinius(visosKlases))
rasytiIByla('02uzdDictRez.txt', rezultatas, 'Rezultatas:')