<?xml version="1.0" encoding="Windows-1251"?>
<operator id="{op_id}" cyber_id="{op_id}" ref_id="{op_ito}" out_of_menu="1" rostelecom="1">
  <name>УФК {op_region} {service_name}</name>
  <name_for_cheque>Госпошлина ГИБДД</name_for_cheque>
  <inn_for_cheque />
  <chq_rc_1>{chq_rc_1}</chq_rc_1>
  <chq_rc_2>{chq_rc_2}</chq_rc_2>
  <chq_ls>{chq_ls}</chq_ls>
  <chq_bnk_rc_1>{chq_bnk_rc_1}</chq_bnk_rc_1>
  <chq_bnk_rc_2>{chq_bnk_rc_2}</chq_bnk_rc_2>
  <chq_rs>{chq_rs}</chq_rs>
  <chq_inn>{chq_inn}</chq_inn>
  <chq_kpp>{chq_kpp}</chq_kpp>
  <chq_okato>{chq_okato}</chq_okato>
  <chq_bik>{chq_bik}</chq_bik>
  <chq_kbk>{chq_kbk}</chq_kbk>
  <chq_ptype>{service_name}</chq_ptype>
  <chq_op>ТП</chq_op>
  <chq_tp>ГП</chq_tp>
  <limit min="0" max="15000" />
  <comislimit max="0%" />
  <fields>
    <field id="100" type="text" minlength="1" maxlength="25" klava="rusc">
      <name>ФИО</name>
    </field>
    <field id="101" type="text" minlength="1" maxlength="45" klava="rusc">
      <name>Адрес</name>
    </field>
  </fields>
  <processor type="Cyberplat" id="3" keys_id="0" gate_id="5566" group_id="{op_group}">
    <check amount-value="10">
      <url>/unact_gateway/check/{op_id}</url>
      <request-property name="UNAME" field-rule="[#100]" />
      <request-property name="UADDR" field-rule="[#101]" />
      <request-property name="RC" field-rule="{chq_rc_1}{chq_rc_2}" />
      <request-property name="LS" field-rule="{chq_ls}" />
      <request-property name="BNK_RC" field-rule="{chq_bnk_rc_1}{chq_bnk_rc_2}" />
      <request-property name="RS" field-rule="{chq_rs}" />
      <request-property name="INN" field-rule="{chq_inn}" />
      <request-property name="KPP" field-rule="{chq_kpp}" />
      <request-property name="OKATO" field-rule="{chq_okato}" />
      <request-property name="BIK" field-rule="{chq_bik}" />
      <request-property name="KBK" field-rule="{chq_kbk}" />
      <request-property name="AMOUNT_VALUE" field-rule="{service_amount}" />
    </check>
    <payment with-check="true">
      <url>/unact_gateway/payment/{op_id}</url>
      <request-property name="UNAME" field-rule="[#100]" />
      <request-property name="UADDR" field-rule="[#101]" />
      <request-property name="RC" field-rule="{chq_rc_1}{chq_rc_2}" />
      <request-property name="LS" field-rule="{chq_ls}" />
      <request-property name="BNK_RC" field-rule="{chq_bnk_rc_1}{chq_bnk_rc_2}" />
      <request-property name="RS" field-rule="{chq_rs}" />
      <request-property name="INN" field-rule="{chq_inn}" />
      <request-property name="KPP" field-rule="{chq_kpp}" />
      <request-property name="OKATO" field-rule="{chq_okato}" />
      <request-property name="BIK" field-rule="{chq_bik}" />
      <request-property name="KBK" field-rule="{chq_kbk}" />
      <request-property name="AMOUNT_VALUE" field-rule="{service_amount}" />
    </payment>
    <status>
      <url>/unact_gateway/status/{op_id}</url>
    </status>
    <osmp_format_string>account-number=[#UNAME]\nUADDR=[#UADDR]\nRC=[#RC]\nLS=[#LS]\nBNK_RC=[#BNK_RC]\nRS=[#RS]\nINN=[#INN]\nKPP=[#KPP]\nOKATO=[#OKATO]\nBIK=[#BIK]\nKBK=[#KBK]\nINV_SUM=[#AMOUNT_VALUE]\nDATE_TIME=[#DATE_TIME]\nRECEIPT_NUMBER=[#RECEIPT_NUMBER]</osmp_format_string>
  </processor>
  <menu group="{op_menu_group}" image="" rootmenuimage="" />
</operator>