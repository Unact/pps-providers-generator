#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path, sys
from providers import providers

#Retrieving script path
HOME_DIR=os.path.abspath(os.path.dirname(sys.argv[0]))
TPL_DIR=os.path.join(HOME_DIR,"templates")
RESULT_DIR=os.path.join(HOME_DIR,"result")

for prv in providers:
	sid=-1 #starting op_id offset
	print prv["op_name"]
	
	op_dir=os.path.join(RESULT_DIR,prv["op_name"])
	
	try:
		os.makedirs(op_dir)
	except:
		pass
	
	menu_tpl=""
	for s in prv["services"]:
		print s["service"]["name"]
		sid=sid+1
		cur_op_id=str(prv["op_id_start"]+sid)
		
		menu_tpl+="".join(['<operator_id id="',cur_op_id,'" image="',s["service"]["image"],'" visible="0" />\n'])
		
		
		template=os.path.join(TPL_DIR,s["service"]["tpl"])
		F=open(template,"r")
		tpl_data=F.read()
		F.close()
		result=tpl_data.format(	op_id=cur_op_id,
							op_name=prv["op_name"],
							op_menu_group=prv["op_menu_group"],
							service_name=s["service"]["name"],
							chq_rc=prv["chq_rc"],
							chq_ks=prv["chq_ks"],
							chq_bnk_rc=prv["chq_bnk_rc"],
							chq_rs=prv["chq_rs"],
							chq_inn=prv["chq_inn"],
							chq_kpp=prv["chq_kpp"],
							chq_bik=prv["chq_bik"],
							op_gate=prv["op_gate"],
							op_group=prv["op_id_start"],
							service_amount=s["service_amount"],
							op_image=s["service"]["image"]
						)
		
		res_cp1251=result.decode('utf-8').encode('cp1251')
		
		result_filename=os.path.join(op_dir,cur_op_id+".xml")
		
		#Save operator template
		F=open(result_filename,"w")
		F.write(res_cp1251)
		F.close()
		
	#Save menu template
	F=open(os.path.join(op_dir,"menu.xml"),"w")
	F.write(menu_tpl)
	F.close()
	
