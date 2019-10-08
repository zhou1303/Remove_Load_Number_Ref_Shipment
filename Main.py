import pandas as pd
import Post_Data
import Constant
import time
import G_API
import Get_Data


if __name__ == '__main__':

    # START COUNTING RUNNING TIME
    start = time.time()

    # LOGIN TMS
    Get_Data.read_login_credentials()
    session_requests, csrf = Post_Data.login_tms()

    # Extract data from the spreadsheet.
    df_shipment = pd.read_excel('Dynamic.xlsx', dtype=str)
    oids = df_shipment['OID'].tolist()

    for oid in oids:

        # Concatenate the load page.
        url_load_html = Constant.url_prefix_load_html
        url_load_html = url_load_html.replace('TO_BE_REPLACE', oid)

        # Concatenate the reference page.
        url_ref_html = Constant.url_prefix_ref_html
        url_ref_html = url_ref_html.replace('TO_BE_REPLACE', oid)

        # Parse the html script of the load page and find the load attached.
        load_html = session_requests.get(url_load_html).text
        linked_loads = Constant.re_pattern_get_load.findall(load_html)
        print('The loads attached to shipment object (OID):', oid, 'are:')

        for linked_load in linked_loads:
            print(linked_load)

        # Parse the htmel script of the reference page and find all Ref: Load Number.
        ref_html = session_requests.get(url_ref_html).text
        ref_loads = Constant.re_pattern_get_ref_load.findall(ref_html)

        # Loop all Ref: Load Number, if any of them not in attached loads, remove them.
        for ref_load in ref_loads:
            if ref_load[1] not in linked_loads:
                print('Ref: Load Number', ref_load[1], 'is removed for shipment object (OID):', oid)
                ref_oid = ref_load[0]
                # Send request to TMS and remove Ref: Load Number.
                url_del_ref = Constant.url_delete_ref
                url_del_ref = url_del_ref.replace('REF_OID_TO_BE_REPLACE', ref_oid)
                url_del_ref = url_del_ref.replace('SHP_OID_TO_BE_REPLACE', oid)

                session_requests.get(url_del_ref)

    print('Process is completed and will be logged. This window will be closed automatically in 30 seconds.')

    # END TIME
    end = time.time()

    # UPDATE LOG REPORT ON GOOGLE SHEETS
    duration = end - start
    workbook_log = G_API.get_workbook_by_id(Constant.g_sheets_workbook_id_log)
    worksheet_log = G_API.get_worksheet_by_id(workbook_log, Constant.g_sheets_worksheet_id_log)
    Post_Data.log_event(worksheet_log, duration)

    time.sleep(30)