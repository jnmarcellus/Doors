#+------------------------------------------------------------+
# | Module Name:        Create XML                             |
# | Module Purpose:     Create XML Files                       |
# | Module Modifier:    John Marcellus                         |
# | Module Date:        8/31/2017                              |
# +------------------------------------------------------------

# Import modules
import xml.etree.cElementTree as ET

# Definitions

#------------------------------------------------------------------------------------------------------------------------------------------------------#

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("filename.xml")