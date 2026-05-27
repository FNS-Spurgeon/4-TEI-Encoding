from lxml import etree
from datetime import date
import csv
import os

file = "../../3-DataEnrichment/2-DataEnriched/vol2-1876-1900-allusions-enriched.csv"

ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

with open(file, 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for row in csvreader:
        print(row[0])

        root = etree.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")
        root.set("{http://www.w3.org/XML/1998/namespace}id", row[0])
        teiHeader = etree.SubElement(root, "teiHeader")

        fileDesc = etree.SubElement(teiHeader, "fileDesc")
        titleStmt = etree.SubElement(fileDesc, "titleStmt")
        title = etree.SubElement(titleStmt, "title")
        title.text = row[5] + ", " + row[9] + ". " + row[12]

        respStmt1 = etree.SubElement(titleStmt, "respStmt")
        name1 = etree.SubElement(respStmt1, "name")
        name1.set("{http://www.w3.org/XML/1998/namespace}id", "DS")
        name1.text = "Devani Singh"
        resp1 = etree.SubElement(respStmt1, "resp")
        resp1.text = "Principal investigator of the project. Supervision of the workflow and control of data quality."

        respStmt2 = etree.SubElement(titleStmt, "respStmt")
        name2 = etree.SubElement(respStmt2, "name")
        name2.set("{http://www.w3.org/XML/1998/namespace}id", "EL")
        name2.text = "Elina Leblanc"
        resp2 = etree.SubElement(respStmt2, "resp")
        resp2.text = "Data modelling, OCR correction, text encoding and uploading in the database."

        respStmt3 = etree.SubElement(titleStmt, "respStmt")
        name3 = etree.SubElement(respStmt3, "name")
        name3.set("{http://www.w3.org/XML/1998/namespace}id", "JS")
        name3.text = "Jordan Skinner"
        resp3 = etree.SubElement(respStmt3, "resp")
        resp3.text = "Corpus enhacement and verification of data accuracy. Control of data quality."

        pubStmt = etree.SubElement(fileDesc, "publicationStmt")
        publisher = etree.SubElement(pubStmt, "publisher")
        publisher.text = 'Project SNSF "Caroline Spurgeon: Chaucer Allusions, Shakespeare\'s Imagery, and the Digital Humanities" (n°225925)'

        authority = etree.SubElement(pubStmt, "authority")
        authority.text = "Department of English Language and Literature, Faculty of Humanities, University of Geneva"

        address = etree.SubElement(pubStmt, "address")
        addrline1 = etree.SubElement(address, "addrLine")
        addrline1.text = "12, boulevard des Philosophes"
        addrline2 = etree.SubElement(address, "addrLine")
        addrline2.text = "1205 Genève"

        availability = etree.SubElement(pubStmt, "availability")
        licence = etree.SubElement(availability, "licence", target="https://creativecommons.org/licenses/by/4.0/")
        licence.text = "CC BY"

        sourceDesc = etree.SubElement(fileDesc, "sourceDesc")
        biblStruct = etree.SubElement(sourceDesc, "biblStruct")
        analytic = etree.SubElement(biblStruct, "analytic")

        if row[9] == "Unknown":
            author1 = etree.SubElement(analytic, "author")
            author1.text = row[9]
        else:
            author1 = etree.SubElement(analytic, "author", cert=row[8], role=row[10][0].upper(), ref="http://viaf.org/viaf/" + row[11])
            author1.text = row[9]

        date1 = etree.SubElement(analytic, "date", cert=row[6], when=row[5])
        date1.text = row[5]

        title1 = etree.SubElement(analytic, "title", level="a")
        title1.text = row[12]

        monogr = etree.SubElement(biblStruct, "monogr")
        title2 = etree.SubElement(monogr, "title", level="m")
        title2.text = "Five Hundred Years of Chaucer Criticism and Allusion"

        author2 = etree.SubElement(monogr, "author")
        author2.text = "Spurgeon, Caroline"

        note = etree.SubElement(monogr, "note")
        note.text = "We used the digitizations made by Google for the University of Michigan (Public Domain, Google-Digitized). The facsimile can be found on HathiTrust."
        if row[1] == "Vol.1":
            ptr = etree.SubElement(note, "ptr", target="https://hdl.handle.net/2027/mdp.39015016921887")
        elif row[1] == "Vol.2":
            ptr = etree.SubElement(note, "ptr", target="https://hdl.handle.net/2027/mdp.39015066185086")
        else:
            ptr = etree.SubElement(note, "ptr", target="https://hdl.handle.net/2027/mdp.39015066184931")

        imprint = etree.SubElement(monogr, "imprint")
        pubPlace = etree.SubElement(imprint, "pubPlace")
        pubPlace.text = "Cambridge"
        publisher = etree.SubElement(imprint, "publisher")
        publisher.text = "University Press"
        date2 = etree.SubElement(imprint, "date")
        date2.text = "1925"

        vol = etree.SubElement(monogr, "biblScope", unit="volume")
        vol.text = row[1][-1]
        part = etree.SubElement(monogr, "biblScope", unit="part")
        part.text = row[2][-1]
        pages = etree.SubElement(monogr, "biblScope", unit="page")
        pages.text = row[3][1:]

        encodingDesc = etree.SubElement(teiHeader, "encodingDesc")
        projectDesc = etree.SubElement(encodingDesc, "projectDesc")
        projectPara = etree.SubElement(projectDesc, "p")
        projectPara.text = "The digital part of the SNSF project 'Caroline Spurgeon: Chaucer Allusions, Shakespeare's Imagery, and the Digital Humanities' aims to create the first open-access database dedicated to the criticism and reception of Chaucer throughout history. It draws on the compilation and cataloguing work carried out by Professor Caroline Spurgeon (1869–1942) and collected in 'Five Hundred Years of Chaucer Criticism and Allusion'. This work consists of three volumes and a supplement, which will be systematically transcribed, corrected, enriched, encoded and published online, in order to facilitate future research and bring new perspectives to light."

        editorialDecl = etree.SubElement(encodingDesc, "editorialDecl")
        editorialPara = etree.SubElement(editorialDecl, "p")
        editorialPara.text = "The original spelling and punctuation are retained. Meaningful layouts are reproduced, i.e. verses, printed marginalia, dots lines, tables, etc. However, we do not consider, the line breaks for prose, the columns or the curly brackets. The same rules apply for special characters and glyphs. Otiose letters are normalised, as well as spaces before punctuation marks."

        appInfo = etree.SubElement(encodingDesc, "appInfo")
        application = etree.SubElement(appInfo, "application", ident="FoNDUE", version="0.1")
        label = etree.SubElement(application, "label")
        label.text = "FoNDUE"
        ptr_app = etree.SubElement(application, "ptr", target="https://fondue.unige.ch/")

        profileDesc = etree.SubElement(teiHeader, "profileDesc")
        langUsage = etree.SubElement(profileDesc, "langUsage")
        if row[17] == "fr":
            language = etree.SubElement(langUsage, "language", ident=row[17])
            language.text = "French"
        elif row[17] == "frm":
            language = etree.SubElement(langUsage, "language", ident=row[17])
            language.text = "Moyen français"
        elif row[17] == "en":
            language = etree.SubElement(langUsage, "language", ident=row[17])
            language.text = "English"
        else:
            language = etree.SubElement(langUsage, "language", ident="#")

        textClass = etree.SubElement(profileDesc, 'textClass')
        if "/" in row[16]:
            kList = row[16].split("/")
            for kL in kList:
                k = kL.split(",")
                catRef = etree.SubElement(textClass, 'catRef', scheme="#"+k[0], target="#"+k[-1])
        elif row[16] == "":
            pass
        else:
            kList = row[16].split(",")
            catRef = etree.SubElement(textClass, 'catRef', scheme="#"+kList[0], target="#"+kList[-1])

        revisionDesc = etree.SubElement(teiHeader, "revisionDesc")
        when = date.today().strftime("%Y-%m-%d")
        change =etree.SubElement(revisionDesc, "change", when=when, who="#EL")
        change.text = "Creation of the TEI file and enrichment of data"

        text = etree.SubElement(root, 'text')
        body = etree.SubElement(text, 'body')
        div = etree.SubElement(body, 'div', type="allusion")

        if "-" in row[3][1:]:
            pages = row[3][1:].split("-")
            milestone = etree.SubElement(div, 'milestone', unit="page", n=pages[0])
        else:
            milestone = etree.SubElement(div, 'milestone', unit="page", n=row[3][1:])

        ab_Imprint = etree.SubElement(div, 'ab', type="imprint")
        ab_Imprint.text = row[4] + " " + row[7] + " " + row[12] + " " + row[13]

        if row[14] != "":
            ab_Quotation = etree.SubElement(div, 'ab', type="quotation")
            seg = etree.SubElement(ab_Quotation, 'seg')
            seg.text = row[14]

        if row[15] != "":
            footnote = etree.SubElement(ab_Quotation, 'note', type="footnote")
            footnote.text = "Spurgeon's note: " + row[15]

        # print(etree.tostring(div, xml_declaration=True, encoding='UTF-8', pretty_print=True))

        tree = etree.ElementTree(root)

        path_tei = '../tei-files/vol2-1876-1900-xml'  # New folder to save the files
        if not os.path.isdir(path_tei):
            os.mkdir(path_tei)

        filename = row[0] + ".xml"
        filename_path = os.path.join(path_tei, filename)

        if not os.path.isfile(filename_path):
            tree.write(filename_path, xml_declaration=True, encoding='UTF-8', pretty_print=True)
