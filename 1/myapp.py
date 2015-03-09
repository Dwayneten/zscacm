from flask import Flask, request, render_template
from getnum import *

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
  return render_template('/index.html')

@app.route('/query', methods=['GET'])
def query_form():
    return render_template('/index.html')

@app.route('/query', methods=['POST'])
def query():
    POJ = request.form['POJ']
    HDU = request.form['HDU']
    CF = request.form['CF']
    BC = request.form['BC']
    checkUsername = ''
    if POJ:
        checkUsername = POJ
    elif HDU:
        checkUsername = HDU
    elif CF:
        checkUsername = CF
    elif BC:
        checkUsername = BC
    return render_template('/index.html', username = checkUsername,
                           POJnum = get_poj_ac_num(POJ),
                           HDUnum = get_hdu_ac_num(HDU),
                           # CFnum = ,
                           CFrank = get_cf_rank(CF),
                           CFmax = get_cf_max(CF),
                           BCrank = get_bc_rank(BC),
                           BCmax = get_bc_max(BC))

  
if __name__ == '__main__':
        app.run()