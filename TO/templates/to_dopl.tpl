<?xml version="1.0" encoding="Windows-1251"?>
<operator id="{op_id}" cyber_id="{op_id}" rostelecom="1">
  <name>{op_name} {service_name}</name>
  <chq_rc>{chq_rc}</chq_rc>
  <chq_ks>{chq_ks}</chq_ks>
  <chq_bnk_rc>{chq_bnk_rc}</chq_bnk_rc>
  <chq_rs>{chq_rs}</chq_rs>
  <chq_inn>{chq_inn}</chq_inn>
  <chq_kpp>{chq_kpp}</chq_kpp>
  <chq_bik>{chq_bik}</chq_bik>
  <chq_op>ТП</chq_op>
  <chq_tp>ГП</chq_tp>
  <name_for_cheque>Технический осмотр {chq_rc} - {service_name}</name_for_cheque>
  <chq_ptype>За проверку тех-состояния АТС ({service_name})</chq_ptype>
  <limit min="1" max="15000" />
  <fields>
    <field id="100" type="text" minlength="1" maxlength="25" klava="rusc">
      <name>ФИО</name>
    </field>
    <field id="101" type="text" minlength="1" maxlength="45" klava="rusc">
      <name>Адрес</name>
    </field>
    <field id="102" type="integer" minlength="1" maxlength="9">
      <name>Точная сумма платежа</name>
      <comment>[b]Внимание![/b] Введите точную сумму.</comment>
      <regexp>\\d{{1,4}}</regexp>
    </field>
  </fields>
  <processor type="Cyberplat" id="3" keys_id="0" gate_id="{op_gate}" group_id="{op_group}">
    <check amount-value="10">
      <url>/unact_gateway/check/{op_id}</url>
      <request-property name="UNAME" field-rule="[#100]" />
      <request-property name="UADDR" field-rule="[#101]" />
      <request-property name="KS" field-rule="{chq_ks}" />
      <request-property name="RC" field-rule="{chq_bnk_rc}" />
      <request-property name="RS" field-rule="{chq_rs}" />
      <request-property name="INN" field-rule="{chq_inn}" />
      <request-property name="KPP" field-rule="{chq_kpp}" />
      <request-property name="BIK" field-rule="{chq_bik}" />
      <request-property name="AMOUNT_VALUE" field-rule="{service_amount}" />
    </check>
    <payment with-check="true">
      <url>/unact_gateway/payment/{op_id}</url>
      <request-property name="UNAME" field-rule="[#100]" />
      <request-property name="UADDR" field-rule="[#101]" />
      <request-property name="KS" field-rule="{chq_ks}" />
      <request-property name="RC" field-rule="{chq_bnk_rc}" />
      <request-property name="RS" field-rule="{chq_rs}" />
      <request-property name="INN" field-rule="{chq_inn}" />
      <request-property name="KPP" field-rule="{chq_kpp}" />
      <request-property name="BIK" field-rule="{chq_bik}" />
      <request-property name="AMOUNT_VALUE" field-rule="{service_amount}" />
    </payment>
    <status>
      <url>/unact_gateway/status/{op_id}</url>
    </status>
    <osmp_format_string>account-number=[#UNAME]\nUADDR=[#UADDR]\nKS=[#KS]\nRC=[#RC]\nRS=[#RS]\nINN=[#INN]\nKPP=[#KPP]\nBIK=[#BIK]\nINV_SUM=[#AMOUNT_VALUE]</osmp_format_string>
  </processor>
  <menu group="{op_menu_group}" image="{op_image}" rootmenuimage="" />
</operator>