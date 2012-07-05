# -*- coding: utf-8 -*-
from services import services
providers=[
#=======================================================================


{ 	"op_name":"Экат", 									#Название провайдера. Шаблоны будут сохраниены в каталоге result/_Название оператора_
	"op_id_start":1100510,								#ID первого оператора
	"op_menu_group":13600,								#ID группы меню
	"op_gate":"5569",									#ID шлюза
	"chq_rc":"ЗАО Экат",								#Полное название для чека
	"chq_ks":"30101810400000000225",					#КС
	"chq_bnk_rc":"Сбербанк России ОАО, г. Москва",		#Банк получателя
	"chq_rs":"40702810838040114536",					#РС
	"chq_inn":"7714665081",								#ИНН
	"chq_kpp":"771401001",								#КПП
	"chq_bik":"044525225",								#БИК
	#Список услуг провайдера задавется в формате 
	#{"service":services["_Индекс услуги_"],"service_amount":"_Стоимость услуги_"},
	#индексы услуг можно посмотреть в services.py
	#для услуги Доплата в качестве _Стоимость услуги_ необходимо указать [#102]
	#Шаблоны будут сгенерированы тольколь для перечисленых услуг оператора
	#Список услуг можно расширить в services.xml
	"services":[
		{"service":services["legkovie"],"service_amount":"720"},
		{"service":services["gruzovye_am_l3t"],"service_amount":"770"},
		{"service":services["gruzovye_am_l12t"],"service_amount":"1510"},
		{"service":services["gruzovye_am_g12t"],"service_amount":"1630"},
		{"service":services["avtobusy_l5t"],"service_amount":"1290"},
		{"service":services["avtobusy_g5t"],"service_amount":"1560"},
		{"service":services["pricepy_do3t"],"service_amount":"600"},
		{"service":services["pricepy_g3t"],"service_amount":"1050"},
		{"service":services["mototransport"],"service_amount":"240"},
		{"service":services["doplata"],"service_amount":"[#102]"},
	]
},

#--------------------------------------------Московская область--------
{ 	"op_name":"Экат-А",
	"op_id_start":1100522, 
	"op_menu_group":14000,
	"op_gate":"5576",
	"chq_rc":"ООО Экат-А",
	"chq_ks":"30101810900000000181",
	"chq_bnk_rc":"Банк Возрождение (ОАО)",
	"chq_rs":"40702810505700141162",
	"chq_inn":"5048026060",
	"chq_kpp":"504801001",
	"chq_bik":"044525181",
	"services":[
		{"service":services["legkovie"],"service_amount":"680"},
		{"service":services["gruzovye_am_l3t"],"service_amount":"770"},
		{"service":services["gruzovye_am_l12t"],"service_amount":"1030"},
		{"service":services["gruzovye_am_g12t"],"service_amount":"1100"},
		{"service":services["avtobusy_l5t"],"service_amount":"880"},
		{"service":services["avtobusy_g5t"],"service_amount":"1050"},
		{"service":services["pricepy_do3t"],"service_amount":"430"},
		{"service":services["pricepy_3-10t"],"service_amount":"540"},
		{"service":services["mototransport"],"service_amount":"220"},
		{"service":services["doplata"],"service_amount":"[#102]"},
	]
},

#--------------------------------------------Московская область--------
{ 	"op_name":"Академконтроль",
	"op_id_start":1100820, 
	"op_menu_group":14100,
	"op_gate":"5577",
	"chq_rc":"ООО Академконтроль",
	"chq_ks":"30101810900000000278",
	"chq_bnk_rc":"Банк Возрождение (ОАО)",
	"chq_rs":"40702810300000004709",
	"chq_inn":"7736178927",
	"chq_kpp":"773601001",
	"chq_bik":"044579278",
	"services":[
		{"service":services["legkovie"],"service_amount":"720"},
		{"service":services["gruzovye_am_l3t"],"service_amount":"770"},
		{"service":services["gruzovye_am_l12t"],"service_amount":"1510"},
		{"service":services["gruzovye_am_g12t"],"service_amount":"1630"},
		{"service":services["avtobusy_l5t"],"service_amount":"1290"},
		{"service":services["avtobusy_g5t"],"service_amount":"1560"},
		{"service":services["pricepy_do3t"],"service_amount":"600"},
		{"service":services["pricepy_3-10t"],"service_amount":"1050"},
		{"service":services["mototransport"],"service_amount":"240"},
		{"service":services["doplata"],"service_amount":"[#102]"},
	]
},

#=======================================================================
{ 	"op_name":"Автотест",
	"op_id_start":1100550, 
	"op_menu_group":13620,
	"op_gate":"5578",
	"chq_rc":"ООО Автотест",
	"chq_ks":"30101810500000000219",
	"chq_bnk_rc":"ОАО БАНК МОСКВЫ, г. Москва",
	"chq_rs":"40702810300410001175",
	"chq_inn":"7735558612",
	"chq_kpp":"773501001",
	"chq_bik":"044525219",
	"services":[
		{"service":services["legkovie"],"service_amount":"720"},
		{"service":services["gruzovye_am_l3t"],"service_amount":"770"},
		{"service":services["pricepy_do3t"],"service_amount":"600"},
		{"service":services["mototransport"],"service_amount":"240"},
		{"service":services["doplata"],"service_amount":"[#102]"},
	]
},
#===================================================================
]
