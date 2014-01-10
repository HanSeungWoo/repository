'''
Created on 2014. 1. 9.

@author: dev.s
'''

from flask import render_template
from app import app
from app.module.service.memberService import MemberService
from flask import request

#@app.route('/<path:path>')
#def catch_all(path):
#    return path #  => member/memberList
    
@app.route('/member/memberList' , methods=['GET'])
def memberListGet():
    #a = request.args.get("name")
    #users_query = memberModel.Member.query.all()
    memberService = MemberService()
    entries = memberService.getMemberList()
    
    #entries = dict(memberId=Member.memberId,password=Member.password)
    return render_template("/admin/member/memberList.html",entries=entries)
