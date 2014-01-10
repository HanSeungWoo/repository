'''
Created on 2014. 1. 10.

@author: dev.s
'''
from app.module.model.codeTypeModel import CodeType

class CodeService():
    
    '''
        @note: tb_code_type (코드타입값) 리스트
    '''
    def getCodeTypeList(self):
        query = CodeType.query.all()
        entries = [dict(
                        code_type=codeType.code_type
                        ,value=codeType.value
                        ,description=codeType.description
                        ) for codeType in query]
        
        return entries