
def casear(text, posun):
    '''Funkce, která vytvoří caseraovu šifru - posun o x míst dopředu či dozadu v abecedě. Pro lepší šifrování udělá z 
    velkých písmen malá a přeskakuje mezery'''

    abeceda = 'abcdefghijklmnopqrstuvwxyz'
    indexy_v_abecede = []
    novy_text = ''

    for pismeno in text.lower():
        if pismeno in abeceda:
            indexy_v_abecede.append(abeceda.index(pismeno))
# shift of indexes according to the given shift
    posunute_indexy = []
    for i in indexy_v_abecede:
        if i+posun>25:
            posunute_indexy.append((i + posun) % len(abeceda)) # shift over zero 
        else:
            posunute_indexy.append(i + posun)

    for ind in posunute_indexy:
        novy_text = novy_text + abeceda[ind]
    return novy_text


message = 'My name is Matej'
print(casear(message, 1))
