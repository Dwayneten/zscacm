from flask import Flask, request, render_template
from getnum import *

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
  return render_template('/index.html')

@app.route('/rank')
def rank():
  poj1 = get_poj_ac_num('Dwayne')
  hdu1 = get_hdu_ac_num('Dwayne')
  zsc1 = get_zsc_ac_num('2013030403029')
  tol1 = int(poj1) + int(hdu1) + int(zsc1)

  poj2 = get_poj_ac_num('2013030403027')
  hdu2 = get_hdu_ac_num('2013030403027')
  zsc2 = get_zsc_ac_num('2013030403027')
  tol2 = int(poj2) + int(hdu2) + int(zsc2)

  poj3 = get_poj_ac_num('T47X')
  hdu3 = get_hdu_ac_num('T47X')
  zsc3 = get_zsc_ac_num('2013031102013')
  tol3 = int(poj3) + int(hdu3) + int(zsc3)
    
  poj4 = get_poj_ac_num('2013031102007')
  hdu4 = get_hdu_ac_num('2013031102007')
  zsc4 = get_zsc_ac_num('2013031102007')
  tol4 = int(poj4) + int(hdu4) + int(zsc4)
  
  poj5 = get_poj_ac_num('2013031001011')
  hdu5 = get_hdu_ac_num('2013031001011')
  zsc5 = get_zsc_ac_num('2013031001011')
  tol5 = int(poj5) + int(hdu5) + int(zsc5)
    
  poj6 = get_poj_ac_num('862044553')
  hdu6 = get_hdu_ac_num('862044553')
  zsc6 = get_zsc_ac_num('2013031101022')
  tol6 = int(poj6) + int(hdu6) + int(zsc6)

  poj7 = get_poj_ac_num('491561501')
  hdu7 = get_hdu_ac_num('2013030402042')
  zsc7 = get_zsc_ac_num('2013030402042')
  tol7 = int(poj7) + int(hdu7) + int(zsc7)
    
  poj8 = get_poj_ac_num('midsummer')
  hdu8 = get_hdu_ac_num('midsummer')
  zsc8 = get_zsc_ac_num('2013031001009')
  tol8 = int(poj8) + int(hdu8) + int(zsc8)
    
  poj9 = get_poj_ac_num('2013030402008')
  hdu9 = get_hdu_ac_num('2013030402008')
  zsc9 = get_zsc_ac_num('2013030402008')
  tol9 = int(poj9) + int(hdu9) + int(zsc9)

  poj10 = get_poj_ac_num('2013031102067')
  hdu10 = get_hdu_ac_num('2013031102067')
  zsc10 = get_zsc_ac_num('2013031102067')
  tol10 = int(poj10) + int(hdu10) + int(zsc10)

  return render_template('/index.html', showRank = 1,
                        POJ_1 = poj1,
                        HDU_1 = hdu1,
                        ZSC_1 = zsc1,
                        TOL_1 = tol1,
                        CF_1 = get_cf_rank('Dwayne'),
                        BC_1 = get_bc_rank('Dwayne'),

                        POJ_2 = poj2,
                        HDU_2 = hdu2,
                        ZSC_2 = zsc2,
                        TOL_2 = tol2,
                        CF_2 = get_cf_rank('2013030403027'),
                        BC_2 = get_bc_rank('2013030403027'),

                        POJ_3 = poj3,
                        HDU_3 = hdu3,
                        ZSC_3 = zsc3,
                        TOL_3 = tol3,
                        CF_3 = get_cf_rank('T47X'),
                        BC_3 = get_bc_rank('T47X'),
                        
                        POJ_4 = poj4,
                        HDU_4 = hdu4,
                        ZSC_4 = zsc4,
                        TOL_4 = tol4,
                        CF_4 = get_cf_rank('2013031102007'),
                        BC_4 = get_bc_rank('2013031102007'),

                        POJ_5 = poj5,
                        HDU_5 = hdu5,
                        ZSC_5 = zsc5,
                        TOL_5 = tol5,
                        CF_5 = get_cf_rank('2013031001011'),
                        BC_5 = get_bc_rank('2013031001011'),
                        
                        POJ_6 = poj6,
                        HDU_6 = hdu6,
                        ZSC_6 = zsc6,
                        TOL_6 = tol6,
                        CF_6 = get_cf_rank('2013031101022'),
                        BC_6 = get_bc_rank('2013031101022'),

                        POJ_7 = poj7,
                        HDU_7 = hdu7,
                        ZSC_7 = zsc7,
                        TOL_7 = tol7,
                        CF_7 = get_cf_rank('2013030402042'),
                        BC_7 = get_bc_rank('2013030402042'),
                        
                        POJ_8 = poj8,
                        HDU_8 = hdu8,
                        ZSC_8 = zsc8,
                        TOL_8 = tol8,
                        CF_8 = get_cf_rank('ZSC2013031001009'),
                        BC_8 = get_bc_rank('2013031001009'),
                        
                        POJ_9 = poj9,
                        HDU_9 = hdu9,
                        ZSC_9 = zsc9,
                        TOL_9 = tol9,
                        CF_9 = get_cf_rank('2013030402008'),
                        BC_9 = get_bc_rank('2013030402008'),

                        POJ_10 = poj10,
                        HDU_10 = hdu10,
                        ZSC_10 = zsc10,
                        TOL_10 = tol10,
                        CF_10 = get_cf_rank('FightingJ'),
                        BC_10 = get_bc_rank('2013031102067'),)

@app.route('/about')
def about():
  return render_template('/index.html', showAbout = 1)

@app.route('/query', methods=['GET'])
def query_form():
    return render_template('/index.html')

@app.route('/query', methods=['POST'])
def query():
    POJ = request.form['POJ']
    HDU = request.form['HDU']
    ZSC = request.form['ZSC']
    CF = request.form['CF']
    BC = request.form['BC']
    checkUsername = ''
    if POJ:
        checkUsername = POJ
    elif HDU:
        checkUsername = HDU
    elif ZSC:
        checkUsername = ZSC
    elif CF:
        checkUsername = CF
    elif BC:
        checkUsername = BC
    tPOJnum = int(get_poj_ac_num(POJ))
    tHDUnum = int(get_hdu_ac_num(HDU))
    tZSCnum = int(get_zsc_ac_num(ZSC))
    # tCFnum = 
    tCFrank = int(get_cf_rank(CF))
    tCFmax = int(get_cf_max(CF))
    tBCrank = int(get_bc_rank(BC))
    tBCmax = int(get_bc_max(BC))
    tTOLnum = tPOJnum + tHDUnum + tZSCnum
    return render_template('/index.html', username = checkUsername,
                           POJnum = tPOJnum,
                           HDUnum = tHDUnum,
                           ZSCnum = tZSCnum,
                           # CFnum = ,
                           CFrank = tCFrank,
                           CFmax = tCFmax,
                           BCrank = tBCrank,
                           BCmax = tBCmax,
                           TOLnum = tTOLnum)

  
if __name__ == '__main__':
        app.run()