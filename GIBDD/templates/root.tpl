<?xml version="1.0" encoding="Windows-1251"?>
<operator id="{op_id}" cyber_id="{op_id}" op_type="1" ref_id="{op_ref_id}" rostelecom="1">
  <name>{op_region} {service_name}</name>
  <name_for_cheque>{service_name}</name_for_cheque>
  <inn_for_cheque />
  <limit min="1" max="15000" />
  <processor type="Cyberplat" id="3" keys_id="0" gate_id="5564" group_id="{op_group}">
    <check amount-value="10">
      <url>/unact_gateway/check/{op_id}</url>
    </check>
    <payment with-check="true">
      <url>/unact_gateway/payment/{op_id}</url>
    </payment>
    <status>
      <url>/unact_gateway/status/{op_id}</url>
    </status>
    <osmp_format_string />
  </processor>
  <menu group="{op_menu_group}" image="{op_image}" rootmenuimage="" />
</operator>