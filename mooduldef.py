def arithmetic(arv1: float, arv2: float, tehe: str)->any:
    """
    Lihne kalkulaator
    + - liitmine
    - - lahuntamine
    * - korrutamine
    / - jagamine
    ,
    :param float arn1: Sisend kasutajalt, mingi ujukomarv
    :param float arn2: Sisend kasutajalt, mingi ujukomarv
    :param str tehe: aritmeetiline tehe, mis valib kasutaja
    :rtype: var Määrata tüüp(float või str)
    """
    if tehe in ["+", "-", '*', '/']:
        if arv2==0 and tehe=='/':
            vastus = "DIV/0" # на ноль делить нельзя
        else:
            vastus = eval(str(arv1)+tehe+str(arv2))#сeval соберет все и посчитает весь  пример
        return vastus

def is_year_leap(aasta:int)->bool:
    '''kas aasta on liigaasta
    tagastab true kui aasta on liigaasta ja false kui ei ole
    :param int aasta: sisend kasutaja poolt, mingi taisarv
    :rtype: bool tagastab true kui aasta on liigaasta ja false kui ei ole
    '''
    if aasta % 4 == 0 and aasta % 100 != 0 or aasta % 400 == 0:
        vastus=True
    else:
        vastus=False
    return vastus

def square(kulg:float)->any:
    '''
    ruut
    :param float kulg: Sisend kasutajalt, mingi arv
    arvutab ruudu umbermoot, pindala ja diagonaal
    :rtype: float tagastab umbermoot, pindala ja diagonaal
    '''
    umbermoot=kulg*4
    pindala=kulg**2
    diagonaal=(2)**(1/2)*kulg
    return umbermoot, pindala, diagonaal

def season(kuu:int)->str:
    '''
    aastaajad
    :param int kuu: Sisend kasutajalt, mingi arv
    tagastab aastaaja
    :rtype: str tagastab aastaaja
    '''
    if kuu in [12,1,2]:
        vastus="talv"
    elif kuu in [3,4,5]:
        vastus="kevad"
    elif kuu in [6,7,8]:
        vastus="suvi"
    elif kuu in [9,10,11]:
        vastus="sugis"