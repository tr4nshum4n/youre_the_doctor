def meta_vial():
    """Runs vial trials. Prints results when they are interesting."""
    for i in range(100000):
        vial_status = {'vial_a_level':0,
                       'vial_b_level':0,
                       'vial_a_medicine_grams':0,
                       'vial_b_medicine_grams':0
                       }
        
        vial_status = vial_main(vial_status)


def vial_main(vial_status):
    """Performs operations to obtain desired concentrations of medicine."""
    from random import randint
    funclist = ""
    functions = {1: fill_a,
                 2: fill_b,
                 3: dump_a,
                 4: dump_b,
                 5: pour_a_b,
                 6: pour_b_a,
                 7: pill_a,
                 8: pill_b}

    pill_in = False
    mymaxfun = 8
    for i in range(100000):
        myrand = randint(1,mymaxfun)
        if(myrand == 7 or myrand == 8):
            pill_in = True
        if(myrand > 6 ):
            mymaxfun = 6
        func = functions[myrand]
        funclist = funclist+ ", \n"+ func.__name__
        func(vial_status)
        if(vial_status['vial_a_medicine_grams'] > .1299 and vial_status['vial_a_medicine_grams'] < .131):
            print(vial_status, funclist)
        if(pill_in == True and vial_status['vial_a_medicine_grams'] == 0 and vial_status['vial_b_medicine_grams'] == 0):
            break
    return vial_status
        
    
def fill_a(vial_status):
    """Fills vial A up to maximum with water."""
    if(vial_status['vial_a_level'] < 5):
        vial_status['vial_a_level'] = 5

    
def fill_b(vial_status):
    """Fills vial B up to maximum with water."""
    if(vial_status['vial_b_level'] < 3):
        vial_status['vial_b_level'] = 3


def dump_a(vial_status):
    """Dumps contents of vial a."""
    if(vial_status['vial_a_level'] > 0):
        vial_status['vial_a_level'] = 0
        vial_status['vial_a_medicine_grams'] = 0


def dump_b(vial_status):
    """Dumps contents of vial b."""
    if(vial_status['vial_b_level'] > 0):
        vial_status['vial_b_level'] = 0
        vial_status['vial_b_medicine_grams'] = 0

        
def pill_a(vial_status):
    """Puts pill in vial a."""
    vial_status['vial_a_medicine_grams'] = 1

    
def pill_b(vial_status):
    """Puts pill in vial b."""
    vial_status['vial_b_medicine_grams'] = 1


def pour_a_b(vial_status):
    """Pours contents of vial a into vial b."""
    if(vial_status['vial_a_level'] > 0 and vial_status['vial_b_level'] < 3):
        dif = min(vial_status['vial_a_level'], 3 - vial_status['vial_b_level'])
        vial_status['vial_b_medicine_grams']=round(vial_status['vial_b_medicine_grams'] + vial_status['vial_a_medicine_grams'] * dif / vial_status['vial_a_level'],3)
        vial_status['vial_b_level'] = vial_status['vial_b_level'] + dif
        vial_status['vial_a_medicine_grams'] = round(vial_status['vial_a_medicine_grams'] - vial_status['vial_a_medicine_grams'] * dif/vial_status['vial_a_level'],3)
        vial_status['vial_a_level'] = vial_status['vial_a_level'] - dif


def pour_b_a(vial_status):
    """Pours contents of vial b into vial a."""
    if(vial_status['vial_b_level'] > 0 and vial_status['vial_a_level'] < 5):
        dif = min(vial_status['vial_b_level'], 5 - vial_status['vial_a_level'])
        vial_status['vial_a_medicine_grams']=round(vial_status['vial_a_medicine_grams'] + vial_status['vial_b_medicine_grams'] * dif / vial_status['vial_b_level'],3)
        vial_status['vial_a_level'] = vial_status['vial_a_level'] + dif
        vial_status['vial_b_medicine_grams'] = round(vial_status['vial_b_medicine_grams'] - vial_status['vial_b_medicine_grams'] * dif/vial_status['vial_b_level'],3)
        vial_status['vial_b_level'] = vial_status['vial_b_level'] - dif

