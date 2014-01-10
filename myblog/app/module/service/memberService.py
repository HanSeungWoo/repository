'''
Created on 2014. 1. 10.

@author: dev.s
'''
from app.module.model.memberModel import Member

class MemberService():
    def getMemberList(self):
        query = Member.query.all()
        #query = Member.query.filter_by(memberId = 'admin' )
        entries = [dict(memberId=member.memberId,password=member.password) for member in query]
        
        return entries 