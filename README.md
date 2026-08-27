# TEI Encoding

This repository contains the digital editions of Chaucer allusions, encoded in XML TEI:

- The TEI files are stored in "tei-files".
- The ODD used by the project is available in "odd".
- "scripts" contains the Python scripts used to create and enhance the TEI files:
    - [csv2tei.py](https://github.com/FNS-Spurgeon/4-TEI-Encoding/blob/main/scripts/csv2tei.py): Creates a first TEI encoding from the CSV files produced in the step 3 of the workflow. This encoding is then manually checked and corrected, if needed.
    - [pageLink_additions](https://github.com/FNS-Spurgeon/4-TEI-Encoding/blob/main/scripts/pageLink_additions.py): Adds HathiTrust page links to the TEI files.
    - [authorsList](https://github.com/FNS-Spurgeon/4-TEI-Encoding/blob/main/scripts/authorsList.py): Generates a TEI list of authors names.
   
## Licence

All data are published under the licence [CC-BY](https://creativecommons.org/licenses/by/4.0/).

