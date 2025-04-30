# fix_pom.py
import xml.dom.minidom

# Read the original pom
with open("pom.xml", "r", encoding="utf-8") as f:
    xml_string = f.read()

# Parse and pretty-print with 2-space indents
dom = xml.dom.minidom.parseString(xml_string)
pretty = dom.toprettyxml(indent="  ")

# Remove any blank lines added by toprettyxml
lines = [ln for ln in pretty.split("\n") if ln.strip()]
cleaned = "\n".join(lines)

# Overwrite the original pom.xml
with open("pom.xml", "w", encoding="utf-8") as f:
    f.write(cleaned)

print("[✔] pom.xml indentation fixed.")

