import xlsxwriter
import os
import datetime
import win32com.client as win32

today = datetime.date.today().strftime("%d-%m-%Y")
now = datetime.datetime.now().strftime("%H.%M.%S")

def logOperazioni(log):
    """Scrittura dei log su apposito Txt,
    il parametro da passare è una stringa."""

    fileLog = open("Log.txt", "a")
    if log == "":
        if os.stat("Log.txt").st_size == 0:
            logOperazioni("Scorrere in basso per avere i log piu' recenti.\nI Log vengono registrati ogni volta che viene lanciato il programma.")
        logOperazioni("\n\n\nI seguenti Log fanno riferimento al giorno " + today + " alle ore " + now + "\n")
    fileLog.write(log)
    fileLog.close()

def logExcel(colonne):
    """Scrittura dei log su apposito Excel,
    il parametro da passare è una stringa."""

    nomeExcel = "Log.xlsx"
    workbook = xlsxwriter.Workbook(nomeExcel)
    worksheet = workbook.add_worksheet()

    for colonna in colonne:
        compilaColonnaExcel(worksheet, colonna, int(colonne.index(colonna)))

    workbook.close()
    riadattaColonneExcel(nomeExcel)
    logOperazioni("\n\n" + nomeExcel + " creato con successo!")

def riadattaColonneExcel(nomeExcel):
    """Inserendo il nome del file Excel,
    questa funzione allargherà le colonne,
    rendendole meglio consultabili."""

    currentDirectory = os.getcwd()
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(currentDirectory + '\\' + nomeExcel)
    ws = wb.Worksheets("Sheet1")
    ws.Columns.AutoFit()
    wb.Save()
    excel.Application.Quit()

def compilaColonnaExcel(worksheet, colonna, nColonna):
    """Questa funzione dovrebbe essere utilizzata in un loop su un array,
    che contiene i contenuti di ciascuna riga di una determinata colonna.
    Il worksheet è:
    nomeExcel = "Log.xlsx";
    workbook = xlsxwriter.Workbook(nomeExcel);
    worksheet = workbook.add_worksheet();
    La colonna è un array con il contenuto di ciascuna riga,
    Il nColonna è il numero della colonna nell'excel, si parte da zero."""

    row = 0
    for cella in colonna:
        worksheet.write(row, nColonna, cella)
        row += 1
