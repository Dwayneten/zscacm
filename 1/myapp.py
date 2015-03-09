from flask import Flask, request, render_template
from getnum import *

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
  return render_template('/index.html')

@app.route('/rank')
def rank():
  return render_template('/index.html', showRank = 1)

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