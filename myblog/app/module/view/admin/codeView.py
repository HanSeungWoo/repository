'''
Created on 2014. 1. 10.

@author: dev.s
'''
from flask import render_template
from flask import url_for
from app import app
from app.module.service.codeService import CodeService 

@app.route('/code/codeList')
def codeList():
    codeService = CodeService()
    entries = codeService.getCodeTypeList()
    return render_template(
                            "/admin/code/codeList.html"
                            ,entries=entries
                            )


with app.test_request_context():
    None
    #codeService = CodeService()
    #entries = codeService.getCodeTypeList()
    #print(entries)