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
                        BC_3 = get_bc_rank('T47X'),)

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