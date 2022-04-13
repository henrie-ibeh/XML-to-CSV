import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()


def addXML():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir='./', title='Select File',
                                          filetypes=(('XML Files', '*.xml'), ('all files', '*.*')))
    global files
    files = filename
    label = tk.Label(frame, text=files, bg='white')
    label.pack()
    return files


def testxml():
    import xml.etree.ElementTree as ET

    tree = ET.parse(files)

    root = tree.getroot()

    def xmltodict(xml_tree_root):
        elements = {}
        for root in xml_tree_root:
            elements[root.tag] = root.text

            for child in root:
                elements[child.tag] = child.text

                for element in child:
                    elements[element.tag] = element.text

                    for children in element:
                        elements[children.tag] = children.text

                        for grand in children:
                            elements[grand.tag] = grand.text

                            for great in grand:
                                elements[great.tag] = great.text

                                for greater in great:
                                    elements[greater.tag] = greater.text
        return elements

    dictionary = xmltodict(root)

    variables = ['State', 'LGA', 'DatimCode', 'FacilityName', 'PatientUniqueID', 'PatientHospitalNo',
                 'ANCNoIdentifier',
                 'ANCNoConceptID', 'HTSNo', 'Sex', 'AgeAtStartOfARTYears', 'AgeAtStartOfARTMonths',
                 'CareEntryPoint',
                 'DateTransferredIn',
                 'TransferInStatus', 'ARTStartDate', 'LastPickupDate', 'LastVisitDate', 'DaysOfARVRefil',
                 'CurrentRegimenLine',
                 'CurrentRegimen', 'PregnancyStatus', 'PregnancyStatusDate', 'CurrentViralLoad(c/ml)',
                 'ViralLoadEncounterDate', 'ViralLoadSampleCollectionDate',
                 'ViralLoadReportedDate', 'ViralLoadIndication', 'PatientOutcome', 'PatientOutcomeDate',
                 'CurrentARTStatus',
                 'DateReturnedToCare', 'DateOfTermination', 'CurrentAgeYears', 'CurrentAgeMonths', 'DateOfBirth',
                 'BiometricCaptured', 'BiometricCaptureDate', 'ValidCapture', 'CurrentWeight(Kg)',
                 'CurrentWeightDate',
                 'TBStatus',
                 'TBStatusDate', 'EnrollmentDate']

    for x in variables:
        try:
            label = tk.Label(frame, text=dictionary[x], bg='white')
            label.pack()
        except KeyError:
            continue


canvas = tk.Canvas(root, height=500, width=800, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='grey')
frame.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.1)

openFile = tk.Button(root, text='Open File', padx=10, pady=5, fg='white', bg='#263D42', command=addXML)
openFile.pack()

runApp = tk.Button(root, text='Run', padx=10, pady=5, fg='white', bg='#263D42', command=testxml)
runApp.pack()

root.mainloop()
