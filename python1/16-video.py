car0={
    'model':'lacetti',
    'rang':'oq',
    'narx':10000,
    'yil':2010,
    'korobka':'avtomat'
}
car1={
    'model':'nexia3',
    'rang':'qora',
    'narx':9000,
    'yil':2015,
    'korobka':'mexanika'
}
cars=[car0, car1]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang,"
          f"{car['yil']} -yil,"
          f"{car['narx']}$")
dasturchilar={
            'ali':['python', 'c++'],
            'vali':['html', 'css', 'js'],
            'bakir':['python', 'php'],
            'nigora':['sql', 'php'],
            'karim':['c++', 'c#']
          }
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(f'{til.upper()}', end='')