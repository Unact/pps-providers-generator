# -*- coding: utf-8 -*-

menu_tree="""<group id="{{menu_base}}00" image="gup_reg.png" title="Регистрационные действия ({{op_region}})">
{menu_groups[10]}</group>
{menu_groups[20]}</group>
{menu_groups[30]}</group>
{menu_groups[0]}</group>
{menu_groups[40]}</group>
"""

menu_groups={
10:'<group id="{menu_base}10" image="gup_reg_rg.png" title="Регистрация ТС">\n',
20:'<group id="{menu_base}20" image="gup_reg_unrg.png" title="Снятие ТС с учета">\n',
30:'<group id="{menu_base}30" image="gup_reg_izm.png" title="Дубликаты, Замена, Изменения">\n',
40:'<group id="{menu_base}40" image="gup_exam.png" title="Экзаменационные действия  ({op_region})">\n',
0:''
}