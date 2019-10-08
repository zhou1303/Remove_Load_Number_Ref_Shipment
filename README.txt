To use this executable program to remove extra Ref: Load Number, follow below steps before running the .exe file:

I.	Save Credentials for Login:

1.	Save Mercury Gate TMS login username to 'username.txt'. Do not leave space at the beginning or the end.
2.	Save Mercury Gate TMS login password to 'password.txt'. Do not leave space at the beginning or the end.

II.	Identify Shipments and Format File:

1.	Go to TMS -> Shipment report -> Include Primary Reference, OID, Ref: Load Number, Loads as columns -> Setup filters -> Download as .xls -> Use Excel filter to remove normal shipments and only keep exceptions (i.e. shipments whose Loads = 1 while having > 1 Ref: Load Number, etc) -> Save the file.
2.	Transfer file from .xls to .xlsx by: Open Excel file -> File -> Info -> Convert -> Yes.
3.	Rename the file to 'Dynamic.xlsx' if it is named something else. Do not name it as 'Dynamic.xlsx.xlsx' as .xlsx is a suffix of Excel file that will be automatically applied.
4.	Make sure the tab in the spreadsheet is either the ONLY tab or the FIRST tab. Otherwise, the program will capture whatever the first tab is and malfunction.
5.	Note that this program works with any .xlsx file named 'Dynamic' who should have column OID from a shipment report. All the other columns mentioned above are for identifying and operation convenience. Therefore, in the extreme case, one 'Dynamic.xlsx' file with only one column OID works fine.
6.	Save 'Dynamic.xlsx' file in the same folder where this .exe program is saved. Now the program is ready to run.

How it works:
This program captures shipment OIDs provided by the 'Dynamic.xlsx' file, logs in to Mercury Gate TMS using credentials provided in .txt files, finds loads attached to each shipment object, compares the results with the references attached to this shipment object and finally removes any extra Ref: Load Number from it. 

Keep in mind:
1.	An user is responsible for identifying shipment with incorrect number of Ref: Load Number and following above-mentioned steps to save the information to an Excel file. The program will then correct them automatically in the system.
2.	Feeding the program a list of normal shipment OID won't let it make any changes. The only reason it requires OID input is that it completes faster when having a target among thousands and millions of shipments.