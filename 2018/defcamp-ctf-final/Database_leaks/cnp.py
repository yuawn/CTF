from pwn import *
import itertools
from collections import namedtuple
from concurrent.futures import ProcessPoolExecutor
import hashlib

User = namedtuple('User', ['id', 'name', 'md5', 'salt', 'msgs'], defaults=[None] * 4 + [[]])
Message = namedtuple('Message', ['id', 'content', 'date'])


def enum_cnp(birthday=None, gender=None):
    if gender is not None:
        if gender == 'male':
            S = [1, 5, 7, 3]
        elif gender == 'female':
            S = [2, 6, 8, 4]
    else:
        S = [1,2,5,6,7,8,3,4]
    AA = [list(map(int, f'{i:02d}')) for i in reversed(range(100))]
    if birthday is not None:
        month, day = map(int, birthday.split('/'))
        LL = [list(map(int, f'{month:02d}'))]
        DD = [list(map(int, f'{day:02d}'))]
    else:
        LL = [list(map(int, f'{i+1:02d}')) for i in range(12)]
        DD = [list(map(int, f'{i+1:02d}')) for i in range(31)]
    JJ = [list(map(int, f'{i+1:02d}')) for i in range(52)]
    NNN = [list(map(int, f'{i:03d}')) for i in range(1000)]
    
    # i = 0
    for s, aa, ll, dd, jj, nnn in itertools.product(S, AA, LL, DD, JJ, NNN):
        # i += 1
        # if i % 1000000 == 0:
        #     print(i)
        # print(s, aa, ll, dd, jj, nnn)
        c = (s * 2 + aa[0] * 7 + aa[1] * 9 + ll[0] * 1 + ll[1] * 4 + dd[0] * 6 + dd[1] * 3 + jj[0] * 5 + jj[1] * 8 + nnn[0] * 2 + nnn[1] * 7 + nnn[2] * 9) % 11 % 10
        yield '{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(s, *aa, *ll, *dd, *jj, *nnn, c)


user_genders = {'VLAD': None, 'ILEANA': 'female', 'DINU': None, 'TATIANA': 'female', 'BOGDAN': None, 'DANIEL': 'male', 'VIOLETA': 'female', 'CONSTANTIN': 'male', 'IRINA': None, 'CORNEL': 'male', 'ISABELA': None, 'OANA': 'female', 'DIONISIE': None, 'ADAM': 'male', 'OTILIA': None, 'CRISTINA': 'female', 'AUGUSTIN': None, 'FLORINA': None, 'CRISTIAN': 'male', 'VICTOR': 'male', 'SERGIU': 'male', 'NELU': 'male', 'GEORGIANA': None, 'FLAVIA': None, 'VALERIA': 'female', 'CEZAR': 'male', 'IONELA': 'female', 'NICOLAE': None, 'LUMINITA': 'female', 'MONICA': 'female', 'ILINCA': 'female', 'PAUL': 'male', 'CORNELIA': 'female', 'RODICA': 'female', 'IANCU': 'male', 'RAHELA': None, 'CLAUDIU': 'male', 'EMANUEL': 'male', 'ELENA': 'female', 'VIRGINIA': 'female', 'VEACESLAV': None, 'DAN': 'male', 'TIMOTEI': None, 'TOMA': None, 'IOAN': 'male', 'LAVINIA': None, 'MANUELA': 'female', 'NATALIA': 'female', 'SERGHEI': 'male', 'EUGENIA': 'female', 'IONEL': 'male', 'MARIN': None, 'ION': 'male', 'RADU': 'male', 'TRAIAN': None, 'LIDIA': 'female', 'CATALINA': 'female', 'ALINA': 'female', 'ADRIANA': 'female', 'FELICIA': 'female', 'NARCISA': 'female', 'MANUEL': 'male', 'ELISABETA': 'female', 'BENIAMIN': 'male', 'PETRICA': 'male', 'ANDRADA': None, 'STELIAN': 'male', 'ANDRA': None, 'DARIUS': 'male', 'ILIE': 'male', 'IULIANA': 'female', 'ADELA': 'female', 'BIANCA': 'female', 'DEMETRA': None, 'VERA': 'female', 'MARCELA': None, 'DUMITRA': None, 'VERONICA': 'female', 'COSTICA': 'male', 'ANI': None, 'EUSEBIU': None, 'CAROL': 'male', 'POMPILIU': 'male', 'SOFIA': 'female', 'CLAUDIA': 'female', 'NICU': 'male', 'DAVID': 'male', 'ROZALIA': None, 'SIMON': 'male', 'IONUT': 'male', 'STEFANIA': None, 'COSTACHE': None, 'DANA': 'female', 'DECEBAL': 'male', 'AURELIA': 'female', 'VIRGILIU': 'male', 'TEREZA': None, 'CRINA': 'female', 'IULIU': 'male', 'ANCA': 'female', 'ADELINA': None, 'COSTEL': 'male', 'CIPRIAN': 'male', 'VALERIU': 'male', 'SILVIA': 'female', 'ANGELA': 'female', 'CATALIN': None, 'MARIA': 'female', 'MITICA': 'male', 'STEFAN': 'male', 'ADINA': None, 'ANTONIU': None, 'LUCIAN': 'male', 'ADRIAN': 'female', 'MINODORA': None, 'GRIGORE': 'male', 'SANDRA': 'female', 'MIRON': None, 'DENIS': 'male', 'VIORICA': 'female', 'MAGDALENA': 'female', 'PAULA': 'female', 'CAMELIA': 'female', 'OLIMPIA': None, 'VALENTINA': None, 'FLORIN': 'male', 'GABRIEL': 'male', 'LAURENTIU': 'male', 'COSMINA': 'female', 'MARGARETA': None, 'TUDOR': None, 'BRANDUSA': None, 'SIMION': None, 'ATANASE': None, 'SIMONA': None, 'MAGDA': None, 'LIANA': None, 'CORNELIU': 'male', 'LUCIA': 'female', 'DACIANA': 'female', 'ARTUR': None, 'AMALIA': 'female', 'SERAFIM': None, 'LAURA': 'female', 'COSTIN': 'male', 'TEODORA': None, 'LUCA': None, 'EMILIAN': 'male', 'RUXANDRA': 'female', 'STELA': 'female', 'VALI': 'male', 'ANA': 'female', 'THEODOR': None, 'LIVIA': None, 'FILIP': None, 'DORINA': 'female', 'NECULAI': 'male', 'CORINA': 'female', 'CARMEN': 'female', 'COSMIN': 'male', 'PETRU': 'male', 'SEBASTIAN': 'male', 'CECILIA': 'female', 'LIVIU': 'male', 'ALEX': 'male', 'IULIAN': 'male', 'ALEXANDRA': 'female', 'HORIA': None, 'AURORA': 'female', 'ECATERINA': 'female', 'BOGDANA': None, 'EDUARD': None, 'LUIZA': None, 'IULIA': None, 'LARISA': None, 'EUGEN': 'male', 'GEORGE': 'male', 'SANDA': 'female', 'ALBERT': 'male', 'ALEXANDRU': 'male', 'GHENADIE': 'male', 'SORIN': 'male', 'MIHAITA': 'male', 'HARALAMB': 'male', 'VIOREL': 'male', 'GAVRIL': 'male', 'GHEORGHE': 'male', 'IOLANDA': None, 'STAN': 'male', 'ALIN': 'male', 'LOREDANA': None, 'MIRELA': 'female', 'ANTON': 'male', 'IOSIF': 'male', 'CONSTANTA': 'female', 'GEORGETA': 'female', 'ANGELICA': 'female', 'ANTONIA': 'female', 'RAMONA': 'female', 'LENUTA': 'female', 'MARTIN': 'male', 'ANDREEA': 'female', 'FLAVIU': 'male', 'EMANUELA': None, 'IOANA': 'female', 'ANDREI': 'male', 'MARIAN': 'male', 'NICUSOR': 'male', 'DIANA': 'female', 'DORU': 'male', 'DRAGOS': None, 'DOINA': 'female', 'MARIUS': None, 'REMUS': None, 'HOREA': None, 'ANGHEL': None, 'VASILE': 'male', 'EMILIA': 'female', 'MIHAIL': None, 'DENISA': None, 'AUREL': 'male', 'HORATIU': 'male', 'RALUCA': None, 'LILIANA': 'female', 'MIHAELA': 'female', 'EMIL': 'male', 'ROXANA': None, 'OLGA': 'female', 'VIRGIL': 'male', 'DELIA': 'female', 'MARINA': 'female', 'MARTA': 'female', 'ISABELLA': 'female', 'MIHAI': 'male', 'DARIA': None, 'CEZARA': None, 'MADALINA': 'female', 'NICOLETA': 'female', 'IACOB': None, 'MATEI': None, 'CATINA': None, 'VASILICA': 'male', 'RAZVAN': None, 'DANIELA': None, 'OCTAVIAN': None, 'MARCEL': 'male', 'ANAMARIA': None, 'ROBERT': 'female', 'MIRUNA': 'female', 'PETRONELA': None, 'DORIN': 'male', 'FELIX': 'male', 'MARILENA': None, 'SORINA': 'female', 'STELIANA': None, 'VALENTIN': 'male', 'CLARA': 'female', 'FANE': 'male', 'MARIANA': 'female', 'DRAGOMIR': 'male', 'DUMITRU': 'male', 'IGNAT': None, 'MIRCEA': 'male', 'SONIA': 'female', 'OVIDIU': 'male', 'VALERIAN': None, 'ADI': None, 'PETRE': 'male', 'GABI': None, 'TIBERIU': 'male', 'SILVIU': 'male', 'VICTORIA': 'female', 'SANDU': 'male', 'SABINA': None, 'TEODOR': None, 'DANUT': None, 'CRISTI': 'male'}

# user_genders = {'VLAD': None, 'ILEANA': None, 'DINU': None, 'TATIANA': None, 'BOGDAN': None, 'DANIEL': 'male', 'VIOLETA': None, 'CONSTANTIN': None, 'IRINA': None, 'CORNEL': None, 'ISABELA': None, 'OANA': None, 'DIONISIE': None, 'ADAM': 'male', 'OTILIA': None, 'CRISTINA': 'female', 'AUGUSTIN': None, 'FLORINA': None, 'CRISTIAN': None, 'VICTOR': 'male', 'SERGIU': None, 'NELU': None, 'GEORGIANA': None, 'FLAVIA': None, 'VALERIA': 'female', 'CEZAR': None, 'IONELA': None, 'NICOLAE': None, 'LUMINITA': None, 'MONICA': 'female', 'ILINCA': None, 'PAUL': 'male', 'CORNELIA': 'female', 'RODICA': None, 'IANCU': None, 'RAHELA': None, 'CLAUDIU': None, 'EMANUEL': 'male', 'ELENA': 'female', 'VIRGINIA': 'female', 'VEACESLAV': None, 'DAN': 'male', 'TIMOTEI': None, 'TOMA': None, 'IOAN': None, 'LAVINIA': None, 'MANUELA': 'female', 'NATALIA': 'female', 'SERGHEI': None, 'EUGENIA': 'female', 'IONEL': None, 'MARIN': None, 'ION': None, 'RADU': None, 'TRAIAN': None, 'LIDIA': 'female', 'CATALINA': 'female', 'ALINA': None, 'ADRIANA': 'female', 'FELICIA': 'female', 'NARCISA': None, 'MANUEL': 'male', 'ELISABETA': None, 'BENIAMIN': None, 'PETRICA': None, 'ANDRADA': None, 'STELIAN': None, 'ANDRA': None, 'DARIUS': 'male', 'ILIE': None, 'IULIANA': None, 'ADELA': 'female', 'BIANCA': 'female', 'DEMETRA': None, 'VERA': 'female', 'MARCELA': None, 'DUMITRA': None, 'VERONICA': 'female', 'COSTICA': None, 'ANI': None, 'EUSEBIU': None, 'CAROL': 'female', 'POMPILIU': None, 'SOFIA': 'female', 'CLAUDIA': 'female', 'NICU': None, 'DAVID': 'male', 'ROZALIA': None, 'SIMON': 'male', 'IONUT': None, 'STEFANIA': None, 'COSTACHE': None, 'DANA': 'female', 'DECEBAL': None, 'AURELIA': 'female', 'VIRGILIU': None, 'TEREZA': None, 'CRINA': None, 'IULIU': None, 'ANCA': None, 'ADELINA': None, 'COSTEL': None, 'CIPRIAN': None, 'VALERIU': None, 'SILVIA': 'female', 'ANGELA': 'female', 'CATALIN': None, 'MARIA': 'female', 'MITICA': None, 'STEFAN': 'male', 'ADINA': None, 'ANTONIU': None, 'LUCIAN': None, 'ADRIAN': 'female', 'MINODORA': None, 'GRIGORE': None, 'SANDRA': 'female', 'MIRON': None, 'DENIS': 'male', 'VIORICA': None, 'MAGDALENA': 'female', 'PAULA': 'female', 'CAMELIA': None, 'OLIMPIA': None, 'VALENTINA': None, 'FLORIN': None, 'GABRIEL': 'male', 'LAURENTIU': None, 'COSMINA': None, 'MARGARETA': None, 'TUDOR': None, 'BRANDUSA': None, 'SIMION': None, 'ATANASE': None, 'SIMONA': None, 'MAGDA': None, 'LIANA': None, 'CORNELIU': None, 'LUCIA': 'female', 'DACIANA': None, 'ARTUR': None, 'AMALIA': 'female', 'SERAFIM': None, 'LAURA': 'female', 'COSTIN': None, 'TEODORA': None, 'LUCA': None, 'EMILIAN': None, 'RUXANDRA': None, 'STELA': None, 'VALI': None, 'ANA': 'female', 'THEODOR': None, 'LIVIA': None, 'FILIP': None, 'DORINA': None, 'NECULAI': None, 'CORINA': 'female', 'CARMEN': 'female', 'COSMIN': None, 'PETRU': None, 'SEBASTIAN': 'male', 'CECILIA': 'female', 'LIVIU': None, 'ALEX': 'male', 'IULIAN': None, 'ALEXANDRA': 'female', 'HORIA': None, 'AURORA': 'female', 'ECATERINA': None, 'BOGDANA': None, 'EDUARD': None, 'LUIZA': None, 'IULIA': None, 'LARISA': None, 'EUGEN': None, 'GEORGE': 'male', 'SANDA': None, 'ALBERT': 'male', 'ALEXANDRU': None, 'GHENADIE': None, 'SORIN': None, 'MIHAITA': None, 'HARALAMB': None, 'VIOREL': None, 'GAVRIL': None, 'GHEORGHE': None, 'IOLANDA': None, 'STAN': 'male', 'ALIN': None, 'LOREDANA': None, 'MIRELA': None, 'ANTON': 'male', 'IOSIF': None, 'CONSTANTA': None, 'GEORGETA': None, 'ANGELICA': 'female', 'ANTONIA': 'female', 'RAMONA': 'female', 'LENUTA': None, 'MARTIN': 'male', 'ANDREEA': None, 'FLAVIU': None, 'EMANUELA': None, 'IOANA': None, 'ANDREI': None, 'MARIAN': 'female', 'NICUSOR': None, 'DIANA': 'female', 'DORU': None, 'DRAGOS': None, 'DOINA': None, 'MARIUS': None, 'REMUS': None, 'HOREA': None, 'ANGHEL': None, 'VASILE': None, 'EMILIA': 'female', 'MIHAIL': None, 'DENISA': None, 'AUREL': None, 'HORATIU': None, 'RALUCA': None, 'LILIANA': 'female', 'MIHAELA': None, 'EMIL': 'male', 'ROXANA': None, 'OLGA': 'female', 'VIRGIL': 'male', 'DELIA': 'female', 'MARINA': 'female', 'MARTA': 'female', 'ISABELLA': 'female', 'MIHAI': None, 'DARIA': None, 'CEZARA': None, 'MADALINA': None, 'NICOLETA': None, 'IACOB': None, 'MATEI': None, 'CATINA': None, 'VASILICA': None, 'RAZVAN': None, 'DANIELA': None, 'OCTAVIAN': None, 'MARCEL': 'male', 'ANAMARIA': None, 'ROBERT': 'female', 'MIRUNA': None, 'PETRONELA': None, 'DORIN': None, 'FELIX': 'male', 'MARILENA': None, 'SORINA': None, 'STELIANA': None, 'VALENTIN': 'male', 'CLARA': 'female', 'FANE': None, 'MARIANA': 'female', 'DRAGOMIR': None, 'DUMITRU': None, 'IGNAT': None, 'MIRCEA': None, 'SONIA': 'female', 'OVIDIU': None, 'VALERIAN': None, 'ADI': None, 'PETRE': None, 'GABI': None, 'TIBERIU': None, 'SILVIU': None, 'VICTORIA': 'female', 'SANDU': None, 'SABINA': None, 'TEODOR': None, 'DANUT': None, 'CRISTI': None}

# import sexmachine.detector

# detector = sexmachine.detector.Detector()
# for name in user_genders:
#     if user_genders[name] is None:
#         user_genders[name] = detector.get_gender(name)
#         print(user_genders[name])



def get():
    r = remote('dbleaks.dctf18-finals.def.camp', 13021)
    r.recvuntil('([')
    users = eval('[{}]'.format(r.recvuntil(']]')[:-1].decode()))
    r.recvuntil('[')
    msgs = eval('[{}]'.format(r.recvuntil(']]')[:-1].decode()))
    users = [User(*u) for u in users]
    msgs = [Message(*m) for m in msgs]        
    r.close()
    return users, msgs

def join(users, msgs):
    for u in users:
        for m in msgs.copy():
            if m.id == u.id:
                u.msgs.append(m)
                msgs.remove(m)

def get_birthday(user):
    for msg in user.msgs:
        if 'Birthday' in msg.content:
            return msg.date

def get_gender(user):
    return user_genders.get(user.name, None)

def get_users():
    users, msgs = get()
    join(users, msgs)
    return users

def fuck(user):
    print(user.name)
    birthday = get_birthday(user)
    gender = get_gender(user)
    # print(gender)
    if gender is None:
        return
    for i, cnp in enumerate(enum_cnp(birthday=birthday, gender=gender)):
        # if i == 1000000:
        #     return
        md5 = hashlib.md5((user.salt + cnp).encode()).hexdigest()
        # print(user.md5, md5, cnp)
        if md5 == user.md5:
            print(f'!!!!!! ---> {user.name} {cnp}')
            return user, cnp


with ProcessPoolExecutor(max_workers=8) as ex:
    users = get_users()
    # from IPython import embed
    # embed()
    results = list(ex.map(fuck, users))


