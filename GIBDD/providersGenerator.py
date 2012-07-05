#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path, sys
from providers import providers
from menu import *

#Retrieving script path
HOME_DIR=os.path.abspath(os.path.dirname(sys.argv[0]))
TPL_DIR=os.path.join(HOME_DIR,"templates")
RESULT_DIR=os.path.join(HOME_DIR,"result")

#Generate operator profiles
for prv in providers:
	sid=-1 #starting op_id offset
	print prv["op_region"]
	
	prv_menu_groups=menu_groups.copy()
	
	op_dir=os.path.join(RESULT_DIR,prv["op_region"])
	
	try:
		os.makedirs(op_dir)
	except:
		pass
	
	#menu_tpl=""
	for s in prv["services"]:
		print s["service"]["name"]
		sid=sid+1
		cur_ufk_id=str(prv["op_id_start"]+sid)
		cur_root_id=str(int(cur_ufk_id)+50)
		
		#menu_tpl+="".join(['<operator_id id="',cur_op_id,'" image="',s["service"]["image"],'" visible="0" />\n'])
		
		
		ufk_tpl_path=os.path.join(TPL_DIR,s["service"]["ufk_tpl"])
		root_tpl_path=os.path.join(TPL_DIR,s["service"]["root_tpl"])
		
		F=open(ufk_tpl_path,"r")
		ufk_tpl_data=F.read()
		F.close()
		
		F=open(root_tpl_path,"r")
		root_tpl_data=F.read()
		F.close()
		
		ufk_result=ufk_tpl_data.format(	
							op_id=cur_ufk_id,
							op_ito=s["service"]["op_ito"],
							op_region=prv["op_region"],
							op_menu_group=prv["op_menu_group"]+s["service"]["menu_subgrp"],
							service_name=s["service"]["name"],
							chq_rc_1=prv["chq_rc_1"],
							chq_rc_2=prv["chq_rc_2"],
							chq_ls=prv["chq_ls"],
							chq_bnk_rc_1=prv["chq_bnk_rc_1"],
							chq_bnk_rc_2=prv["chq_bnk_rc_2"],
							chq_rs=prv["chq_rs"],
							chq_inn=prv["chq_inn"],
							chq_kpp=prv["chq_kpp"],
							chq_okato=prv["chq_okato"],
							chq_bik=prv["chq_bik"],
							chq_kbk=prv["chq_kbk"],
							op_group=s["service"]["op_group"],
							service_amount=s["service_amount"]
						)
		
		root_result=root_tpl_data.format(	
							op_id=cur_root_id,
							op_ref_id=cur_ufk_id,
							op_region=prv["op_region"],
							op_menu_group=prv["op_menu_group"]+s["service"]["menu_subgrp"],
							op_image=s["service"]["image"],
							service_name=s["service"]["name"],
							op_group=cur_root_id
						)
						
		#Add provider to menu_group
		prv_menu_groups[s["service"]["menu_subgrp"]]+="".join(['<operator_id id="',cur_root_id,'" name=" " image="',s["service"]["image"],'" rootmenuimage="" visible="0" />\n'])
		
		
		ufk_res_cp1251=ufk_result.decode('utf-8').encode('cp1251')
		root_res_cp1251=root_result.decode('utf-8').encode('cp1251')
		
		ufk_result_filename=os.path.join(op_dir,cur_ufk_id+".xml")
		root_result_filename=os.path.join(op_dir,cur_root_id+".xml")
		
		#Save operator template
		F=open(ufk_result_filename,"w")
		F.write(ufk_res_cp1251)
		F.close()
		
		F=open(root_result_filename,"w")
		F.write(root_res_cp1251)
		F.close()
	
	#Generate menu
	tmp_menu=menu_tree.format(menu_groups=prv_menu_groups)
	result_menu=tmp_menu.format(op_region=prv["op_region"],menu_base=str(prv["op_menu_group"])[:-2])	
	#Save menu template
	F=open(os.path.join(op_dir,"menu.xml"),"w")
	F.write(result_menu)
	F.close()
