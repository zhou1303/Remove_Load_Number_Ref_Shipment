import re

root_path = 'C:\\Users\\Zhou_Charles\\Desktop\\'

login_userid = None
login_password = None

time_format_military = '%m/%d/%Y %H:%M'
process_name = 'Remove Load Number Ref Shipment'
g_sheets_workbook_id_log = '1Yudm7JfKSgL82zyHXnDKUjJfoI5VGoEsPHgysPXcZ4g'
g_sheets_worksheet_id_log = 0

url_tms_login = 'https://dsclogistics.mercurygate.net/MercuryGate/login/LoginProcess.jsp'
url_list_transports = 'https://dsclogistics.mercurygate.net/MercuryGate/transport/listTransports.jsp'
url_list_shipments = 'https://dsclogistics.mercurygate.net/MercuryGate/shipment/listShipment.jsp'
url_tms_root = 'https://dsclogistics.mercurygate.net'


url_get_request_ref_type_initial = 'https://dsclogistics.mercurygate.net/MercuryGate/common/extClassLoader.jsp?appName=' \
                                  'MG.tms.portlet.enterprise.ReferenceTypesApp'
url_post_request_ref_type = 'https://dsclogistics.mercurygate.net/MercuryGate/extJsPortletData/ReferenceTypesPortlet'

url_post_add_ref = 'https://dsclogistics.mercurygate.net/MercuryGate/common/addReference_process.jsp'
url_prefix_load_html = 'https://dsclogistics.mercurygate.net/MercuryGate/shipment/listTransports.jsp?oidShipment=TO_BE_REPLACE'
url_prefix_ref_html = 'https://dsclogistics.mercurygate.net/MercuryGate/common/listReferences.jsp?sidOwner=(TO_BE_REPLACE,3700,0)'
url_delete_ref = 'https://dsclogistics.mercurygate.net/MercuryGate/common/deleteReference.jsp?oidReference=REF_OID_TO_BE_REPLACE&oidOwner=SHP_OID_TO_BE_REPLACE'

re_pattern_csrf = re.compile('\<meta name\=\"_csrf\" content\=\"([\w\-]*)\" \/\>')
re_pattern_menu_value = re.compile('\<a href\=\"\.\.\/mainframe\/menuLHS\.jsp\?sMenuValue\=([\d\(\)\,]*)'
                                  '\&sMenuSelected\=\*\-\%3EDetail')
re_pattern_oid = re.compile('OID\' class\=\"DetailBodyTableRowOdd \"\>([\d]*)\<\/td\>')
re_pattern_load_ref = re.compile('Load Reference\' class\=\"DetailBodyTableRowOdd \"\>([\d]*) \(Load Number')
re_pattern_url_parse = re.compile('\<script src\=\"([\w\/\.\?\=]*)\" type\=\"text\/javascript\"\>\<\/script\>')
re_pattern_get_load = re.compile('\<a href\=\"javascript\:doDetail\(\d{11}\)\"\>([\w\-]+)</a>')
re_pattern_get_ref_load = re.compile('\<a href\=\"javascript\:doEdit\((\d{11})\)\"\>([\w\-]+)\<\/a\>\s*\<\/td\>\s*\<td style\=\"background\-color\: [\#\w]+\;\" class\=\"type\"\>\s*Load Number')

field_load_number = 'Ref: 1174978200'

oid_enterprise = 54775198209 #ezVision

menu_value_ref_type_trade = '(19217908000,3250,0)'

html_equivalence_and = '&amp;'

