# -*- coding: utf-8 -*-
from services import services
providers=[
#=======================================================================


{ 	"op_region":"Щелково", 								#Название провайдера. Шаблоны будут сохраниены в каталоге result/_Название оператора_
	"op_id_start":1100600,								#ID первого оператора
	"op_menu_group":13700,								#ID группы меню
	"chq_rc_1":"УФК по МО (УГИБДД ГУ МВД России по Московской области)",	#Полное название для чека
	"chq_rc_2":"",
	"chq_ls":"04731440640",								#ЛС
	"chq_bnk_rc_1":"Отделение N1 МГТУ Банка России г. Москва 705",	#Банк получателя
	"chq_bnk_rc_2":"",
	"chq_rs":"40101810600000010102",					#РС
	"chq_inn":"7702300872",								#ИНН
	"chq_kpp":"770201001",								#КПП
	"chq_okato":"46259000000",							#ОКАТО
	"chq_bik":"044583001",								#БИК
	"chq_kbk":"18810807141011000110",					#КБК
	#Список услуг провайдера задается в формате 
	#{"service":services["_Индекс услуги_"],"service_amount":"_Стоимость услуги_"},
	#индексы услуг можно посмотреть в services.py
	#для услуги Доплата в качестве _Стоимость услуги_ необходимо указать [#102]
	#Шаблоны будут сгенерированы тольколь для перечисленых услуг оператора
	#Список услуг можно расширить в services.xml
	"services":[
		{"service":services["reg_bdc"],"service_amount":"2000"},
		{"service":services["reg_ae"],"service_amount":"1500"},
		{"service":services["reg_bdc_pts"],"service_amount":"2500"},
		{"service":services["reg_ae_pts"],"service_amount":"2000"},
		{"service":services["unreg_bum"],"service_amount":"300"},
		{"service":services["unreg_bum_pts"],"service_amount":"800"},
		{"service":services["unreg_met"],"service_amount":"1300"},
		{"service":services["dubl_sts"],"service_amount":"500"},
		{"service":services["dubl_pts"],"service_amount":"800"},
		{"service":services["dubl_svid"],"service_amount":"200"},
		{"service":services["dubl_izm"],"service_amount":"200"},
		{"service":services["ex_ud"],"service_amount":"800"},
		{"service":services["ex_temp_ud"],"service_amount":"400"},
		{"service":services["ex_mn_ud"],"service_amount":"1000"},
		{"service":services["reg_bdc_to"],"service_amount":"2300"},
		{"service":services["reg_ae_to"],"service_amount":"1800"},
		{"service":services["reg_bcd_pts_to"],"service_amount":"2800"},
		{"service":services["reg_ae_pts_to"],"service_amount":"2300"},
		{"service":services["dolp"],"service_amount":"[#102]"},
		{"service":services["gto"],"service_amount":"300"},	
	]
},

#-------------------------------------------

{ 	"op_region":"Кимры", 								#Название провайдера. Шаблоны будут сохраниены в каталоге result/_Название оператора_
	"op_id_start":1100700,								#ID первого оператора
	"op_menu_group":14000,								#ID группы меню
	"chq_rc_1":"УФК по Тверской области (Межмуниципальный",	#Полное название для чека
	"chq_rc_2":"отдел МВД Российской Федерации 'Кимрский')",
	"chq_ls":"04731440640",								#ЛС
	"chq_bnk_rc_1":"В ГРКЦ ГУ Банка России по Тверской области",	#Банк получателя
	"chq_bnk_rc_2":"",
	"chq_rs":"40101810600000010005",					#РС
	"chq_inn":"6910005298",								#ИНН
	"chq_kpp":"691001001",								#КПП
	"chq_okato":"28426000000",							#ОКАТО
	"chq_bik":"042809001",								#БИК
	"chq_kbk":"18811630020016000140",					#КБК
	#Список услуг провайдера задается в формате 
	#{"service":services["_Индекс услуги_"],"service_amount":"_Стоимость услуги_"},
	#индексы услуг можно посмотреть в services.py
	#для услуги Доплата в качестве _Стоимость услуги_ необходимо указать [#102]
	#Шаблоны будут сгенерированы тольколь для перечисленых услуг оператора
	#Список услуг можно расширить в services.xml
	"services":[
		{"service":services["reg_bdc"],"service_amount":"2000"},
		{"service":services["reg_ae"],"service_amount":"1500"},
		{"service":services["reg_bdc_pts"],"service_amount":"2500"},
		{"service":services["reg_ae_pts"],"service_amount":"2000"},
		{"service":services["unreg_bum"],"service_amount":"300"},
		{"service":services["unreg_bum_pts"],"service_amount":"600"},
		{"service":services["unreg_met"],"service_amount":"1200"},
		{"service":services["dubl_sts"],"service_amount":"300"},
		{"service":services["dubl_pts"],"service_amount":"500"},
		{"service":services["dubl_svid"],"service_amount":"200"},
		{"service":services["dubl_izm"],"service_amount":"200"},
		{"service":services["ex_ud"],"service_amount":"800"},
		{"service":services["ex_temp_ud"],"service_amount":"500"},
		{"service":services["ex_mn_ud"],"service_amount":"1000"},
		{"service":services["reg_bdc_to"],"service_amount":"2300"},
		{"service":services["reg_ae_to"],"service_amount":"1800"},
		{"service":services["reg_bcd_pts_to"],"service_amount":"2800"},
		{"service":services["reg_ae_pts_to"],"service_amount":"2300"},
		{"service":services["dolp"],"service_amount":"[#102]"},
		{"service":services["gto"],"service_amount":"300"},	
	]
},

#-------------------------------------------

{ 	"op_region":"Москва", 								#Название провайдера. Шаблоны будут сохраниены в каталоге result/_Название оператора_
	"op_id_start":1100900,								#ID первого оператора
	"op_menu_group":14200,								#ID группы меню
	"chq_rc_1":"УФК по г.Москве (Управление ГИБДД ГУВД по г.Москве)",	#Полное название для чека
	"chq_rc_2":"",
	"chq_ls":"04731440640",								#ЛС
	"chq_bnk_rc_1":"Отделение N1 МГТУ Банка России г. Москва 705",	#Банк получателя
	"chq_bnk_rc_2":"",
	"chq_rs":"40101810800000010041",					#РС
	"chq_inn":"7707089101",								#ИНН
	"chq_kpp":"770731005",								#КПП
	"chq_okato":"45286585000",							#ОКАТО
	"chq_bik":"044583001",								#БИК
	"chq_kbk":"18810807141011000110",					#КБК
	#Список услуг провайдера задается в формате 
	#{"service":services["_Индекс услуги_"],"service_amount":"_Стоимость услуги_"},
	#индексы услуг можно посмотреть в services.py
	#для услуги Доплата в качестве _Стоимость услуги_ необходимо указать [#102]
	#Шаблоны будут сгенерированы тольколь для перечисленых услуг оператора
	#Список услуг можно расширить в services.xml
	"services":[
		{"service":services["reg_bdc"],"service_amount":"2000"},
		{"service":services["reg_ae"],"service_amount":"1500"},
		{"service":services["reg_bdc_pts"],"service_amount":"2500"},
		{"service":services["reg_ae_pts"],"service_amount":"2000"},
		{"service":services["unreg_bum"],"service_amount":"300"},
		{"service":services["unreg_bum_pts"],"service_amount":"600"},
		{"service":services["unreg_met"],"service_amount":"1200"},
		{"service":services["dubl_sts"],"service_amount":"300"},
		{"service":services["dubl_pts"],"service_amount":"500"},
		{"service":services["dubl_svid"],"service_amount":"200"},
		{"service":services["dubl_izm"],"service_amount":"200"},
		{"service":services["ex_ud"],"service_amount":"800"},
		{"service":services["ex_temp_ud"],"service_amount":"500"},
		{"service":services["ex_mn_ud"],"service_amount":"1000"},
		{"service":services["reg_bdc_to"],"service_amount":"2300"},
		{"service":services["reg_ae_to"],"service_amount":"1800"},
		{"service":services["reg_bcd_pts_to"],"service_amount":"2800"},
		{"service":services["reg_ae_pts_to"],"service_amount":"2300"},
		{"service":services["dolp"],"service_amount":"[#102]"},
		{"service":services["gto"],"service_amount":"300"},
		{"service":services["gos_nomer_sts"],"service_amount":"1800"},	
		{"service":services["bum_transit"],"service_amount":"100"},	
		{"service":services["unreg_met_ae_pts"],"service_amount":"700"},	
		{"service":services["reg_bez_nomer"],"service_amount":"500"},	
	]
},

{ 	"op_region":"Подольск", 								#Название провайдера. Шаблоны будут сохраниены в каталоге result/_Название оператора_
	"op_id_start":1101000,								#ID первого оператора
	"op_menu_group":14300,								#ID группы меню
	"chq_rc_1":"УФК по МО (УГИБДД ГУ МВД России по Московской области)",	#Полное название для чека
	"chq_rc_2":"",
	"chq_ls":"04731440640",								#ЛС
	"chq_bnk_rc_1":"Отделение N1 МГТУ Банка России г. Москва 705",	#Банк получателя
	"chq_bnk_rc_2":"",
	"chq_rs":"40101810600000010102",					#РС
	"chq_inn":"7702300872",								#ИНН
	"chq_kpp":"770201001",								#КПП
	"chq_okato":"46460000000",							#ОКАТО
	"chq_bik":"044583001",								#БИК
	"chq_kbk":"18810807141011000110",					#КБК
	#Список услуг провайдера задается в формате 
	#{"service":services["_Индекс услуги_"],"service_amount":"_Стоимость услуги_"},
	#индексы услуг можно посмотреть в services.py
	#для услуги Доплата в качестве _Стоимость услуги_ необходимо указать [#102]
	#Шаблоны будут сгенерированы тольколь для перечисленых услуг оператора
	#Список услуг можно расширить в services.xml
	"services":[
		{"service":services["reg_bdc"],"service_amount":"2000"},
		{"service":services["reg_ae"],"service_amount":"1500"},
		{"service":services["reg_bdc_pts"],"service_amount":"2500"},
		{"service":services["reg_ae_pts"],"service_amount":"2000"},
		{"service":services["unreg_bum"],"service_amount":"300"},
		{"service":services["unreg_bum_pts"],"service_amount":"800"},
		{"service":services["unreg_met"],"service_amount":"1300"},
		{"service":services["dubl_sts"],"service_amount":"500"},
		{"service":services["dubl_pts"],"service_amount":"500"},
		{"service":services["dubl_svid"],"service_amount":"200"},
		{"service":services["dubl_izm"],"service_amount":"200"},
		{"service":services["ex_ud"],"service_amount":"800"},
		{"service":services["ex_temp_ud"],"service_amount":"500"},
		{"service":services["ex_mn_ud"],"service_amount":"1000"},
		{"service":services["reg_bdc_to"],"service_amount":"2300"},
		{"service":services["reg_ae_to"],"service_amount":"1800"},
		{"service":services["reg_bcd_pts_to"],"service_amount":"2800"},
		{"service":services["reg_ae_pts_to"],"service_amount":"2300"},
		{"service":services["dolp"],"service_amount":"[#102]"},
		{"service":services["gto"],"service_amount":"300"},	
	]
},

#=======================================================================
]