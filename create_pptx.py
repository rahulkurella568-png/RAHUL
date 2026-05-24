"""
Create a PowerPoint (.pptx) file manually without python-pptx.
A .pptx is a ZIP file containing XML files following the OOXML standard.
"""
import zipfile
import os

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Primary_Ledger_Presentation.pptx")

# EMU conversions
def inches(val):
    return int(val * 914400)

def pt(val):
    return int(val * 12700)


SLIDE_WIDTH = inches(13.333)
SLIDE_HEIGHT = inches(7.5)

# Colors
DARK_BLUE = "1B2A4A"
MEDIUM_BLUE = "2C5F8A"
LIGHT_BLUE = "3A7CBD"
ACCENT_ORANGE = "E86C00"
WHITE = "FFFFFF"
LIGHT_GRAY = "F0F2F5"
DARK_GRAY = "333333"
GREEN = "27AE60"
RED = "E74C3C"

def make_shape_xml(id_num, name, left, top, width, height, fill_color, text="",
                   font_size=1800, bold=False, font_color="333333", align="ctr"):
    bold_xml = '<a:rPr lang="en-US" sz="{}" b="1" dirty="0"><a:solidFill><a:srgbClr val="{}"/></a:solidFill><a:latin typeface="Segoe UI"/></a:rPr>'.format(font_size, font_color) if bold else '<a:rPr lang="en-US" sz="{}" dirty="0"><a:solidFill><a:srgbClr val="{}"/></a:solidFill><a:latin typeface="Segoe UI"/></a:rPr>'.format(font_size, font_color)

    paras = ""
    if text:
        lines = text.split("\n")
        for line in lines:
            paras += '<a:p><a:pPr algn="{}"/><a:r>{}<a:t>{}</a:t></a:r></a:p>'.format(align, bold_xml, escape_xml(line))
    else:
        paras = '<a:p><a:endParaRPr lang="en-US"/></a:p>'

    return '''<p:sp>
  <p:nvSpPr><p:cNvPr id="{}" name="{}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
  <p:spPr>
    <a:xfrm><a:off x="{}" y="{}"/><a:ext cx="{}" cy="{}"/></a:xfrm>
    <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
    <a:solidFill><a:srgbClr val="{}"/></a:solidFill>
    <a:ln><a:noFill/></a:ln>
  </p:spPr>
  <p:txBody>
    <a:bodyPr wrap="square" lIns="91440" tIns="45720" rIns="91440" bIns="45720" anchor="ctr"/>
    <a:lstStyle/>
    {}
  </p:txBody>
</p:sp>'''.format(id_num, name, left, top, width, height, fill_color, paras)

def escape_xml(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def make_slide_xml(shapes_xml):
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
       xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
       xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld><p:spTree>
    <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
    <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/>
    <a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
    {}
  </p:spTree></p:cSld>
</p:sld>'''.format(shapes_xml)

def make_bullet_text(bullets, font_size=1600, font_color="333333"):
    paras = ""
    for b in bullets:
        paras += '<a:p><a:pPr algn="l" marL="457200" indent="-228600"><a:buChar char="\u2022"/></a:pPr><a:r><a:rPr lang="en-US" sz="{}" dirty="0"><a:solidFill><a:srgbClr val="{}"/></a:solidFill><a:latin typeface="Segoe UI"/></a:rPr><a:t>{}</a:t></a:r></a:p>'.format(font_size, font_color, escape_xml(b))
    return paras

def make_textbox(id_num, name, left, top, width, height, text_paras_xml):
    return '''<p:sp>
  <p:nvSpPr><p:cNvPr id="{}" name="{}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
  <p:spPr>
    <a:xfrm><a:off x="{}" y="{}"/><a:ext cx="{}" cy="{}"/></a:xfrm>
    <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
    <a:noFill/>
    <a:ln><a:noFill/></a:ln>
  </p:spPr>
  <p:txBody>
    <a:bodyPr wrap="square" lIns="91440" tIns="45720" rIns="91440" bIns="45720"/>
    <a:lstStyle/>
    {}
  </p:txBody>
</p:sp>'''.format(id_num, name, left, top, width, height, text_paras_xml)


# ===== BUILD SLIDES =====
slides = []

# --- SLIDE 1: Title ---
s1 = ""
s1 += make_shape_xml(2, "bg", 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT, DARK_BLUE)
s1 += make_shape_xml(3, "line", 0, inches(5.5), SLIDE_WIDTH, inches(0.08), ACCENT_ORANGE)
s1 += make_shape_xml(4, "title", inches(1), inches(1.5), inches(11), inches(1.2),
                     DARK_BLUE, "PRIMARY LEDGER", 4400, True, WHITE)
s1 += make_shape_xml(5, "sub", inches(1), inches(3), inches(11), inches(0.8),
                     DARK_BLUE, "Oracle Fusion Cloud Financials - General Ledger", 2400, False, WHITE)
s1 += make_shape_xml(6, "info", inches(1), inches(4.2), inches(11), inches(0.6),
                     DARK_BLUE, "Functional Consultant Training", 1800, False, LIGHT_BLUE)
s1 += make_shape_xml(7, "date", inches(1), inches(6), inches(11), inches(0.6),
                     DARK_BLUE, "Prepared by: Rahul | Date: May 2026", 1400, False, WHITE)
slides.append(s1)

# --- SLIDE 2: What is a Primary Ledger ---
s2 = ""
s2 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s2 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                     DARK_BLUE, "What is a Primary Ledger?", 3200, True, WHITE, "l")
s2 += make_shape_xml(4, "def", inches(0.8), inches(1.4), inches(11.5), inches(0.8),
                     WHITE, "A Primary Ledger is the MAIN accounting record for a Legal Entity in Oracle Fusion.", 2000, True, DARK_BLUE, "l")
bullets2 = [
    "It is the single source of truth for all financial transactions",
    "Every Legal Entity MUST have exactly ONE Primary Ledger",
    "Records transactions in the functional (local) currency",
    "Used for statutory reporting, tax compliance, and management reporting",
    "All subledger journals (AP, AR, FA) post to the Primary Ledger",
    "Cannot be deleted once transactions are posted"
]
bp2 = make_bullet_text(bullets2, 1800, DARK_GRAY)
s2 += make_textbox(5, "bullets", inches(0.8), inches(2.5), inches(11.5), inches(3.5), bp2)
s2 += make_shape_xml(6, "key", inches(0.8), inches(6.2), inches(11.5), inches(0.8),
                     LIGHT_GRAY, "KEY: Primary Ledger = COA + Calendar + Currency + Convention", 1600, True, MEDIUM_BLUE)
slides.append(s2)


# --- SLIDE 3: 4 Mandatory Components ---
s3 = ""
s3 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s3 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                     DARK_BLUE, "4 Mandatory Components of a Primary Ledger", 3000, True, WHITE, "l")
components = [
    ("1. Chart of Accounts\n(COA)", "Defines account\nstructure & segments"),
    ("2. Accounting\nCalendar", "Defines fiscal year\nand periods"),
    ("3. Currency", "Functional currency\nfor the ledger\n(USD, INR, GBP)"),
    ("4. Accounting\nConvention", "Accrual or Cash\nbasis accounting")
]
for i, (title, desc) in enumerate(components):
    left = inches(0.5 + i * 3.2)
    s3 += make_shape_xml(4+i*2, f"box{i}", left, inches(1.8), inches(2.9), inches(2), LIGHT_GRAY, title, 1500, True, MEDIUM_BLUE)
    s3 += make_shape_xml(5+i*2, f"desc{i}", left, inches(3.9), inches(2.9), inches(1.8), LIGHT_GRAY, desc, 1300, False, DARK_GRAY)

s3 += make_shape_xml(20, "center", inches(3), inches(6), inches(7), inches(1), DARK_BLUE,
                     "PRIMARY LEDGER = COA + Calendar + Currency + Convention", 1800, True, WHITE)
slides.append(s3)

# --- SLIDE 4: Primary vs Secondary vs Reporting ---
s4 = ""
s4 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s4 += make_shape_xml(3, "header", inches(0.3), inches(0.15), inches(12.5), inches(1),
                     DARK_BLUE, "Primary vs Secondary Ledger vs Reporting Currency", 2600, True, WHITE, "l")

table_data = [
    ["", "Primary Ledger", "Secondary Ledger", "Reporting Currency"],
    ["Purpose", "Main statutory ledger", "Alternate GAAP (IFRS)", "Same ledger, diff currency"],
    ["COA", "Own COA", "Can differ from primary", "Same as Primary"],
    ["Calendar", "Own Calendar", "Can differ", "Same as Primary"],
    ["Currency", "Local (e.g., INR)", "Can differ", "Group (e.g., USD)"],
    ["Mandatory?", "YES - Required", "NO - Optional", "NO - Optional"],
    ["Use Case", "Statutory reporting", "Dual GAAP compliance", "Group consolidation"],
]

y_start = inches(1.5)
row_h = inches(0.7)
col_w = inches(3.1)
for r, row in enumerate(table_data):
    for c, cell in enumerate(row):
        left = inches(0.3) + c * col_w
        top = y_start + r * row_h
        if r == 0:
            color = MEDIUM_BLUE
            fc = WHITE
            b = True
        else:
            color = LIGHT_GRAY if r % 2 == 0 else WHITE
            fc = DARK_BLUE if c == 0 else DARK_GRAY
            b = (c == 0)
        s4 += make_shape_xml(10 + r*4 + c, f"cell_{r}_{c}", left, top, col_w, row_h,
                             color, cell, 1200, b, fc)
slides.append(s4)


# --- SLIDE 5: Enterprise Structure ---
s5 = ""
s5 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s5 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                     DARK_BLUE, "Where Primary Ledger Fits in Enterprise Structure", 2800, True, WHITE, "l")
# Enterprise
s5 += make_shape_xml(4, "ent", inches(4.5), inches(1.5), inches(4.3), inches(0.7), DARK_BLUE,
                     "ENTERPRISE (ABC Group)", 1400, True, WHITE)
# Legal Entities
s5 += make_shape_xml(5, "le1", inches(1.5), inches(2.8), inches(4), inches(0.7), MEDIUM_BLUE,
                     "Legal Entity: ABC Inc. (US)", 1300, True, WHITE)
s5 += make_shape_xml(6, "le2", inches(7.5), inches(2.8), inches(4), inches(0.7), MEDIUM_BLUE,
                     "Legal Entity: ABC Ltd. (UK)", 1300, True, WHITE)
# Primary Ledgers
s5 += make_shape_xml(7, "pl1", inches(1.5), inches(4), inches(4), inches(1.2), ACCENT_ORANGE,
                     "PRIMARY LEDGER\nUS Ledger | COA: Corp | USD", 1300, True, WHITE)
s5 += make_shape_xml(8, "pl2", inches(7.5), inches(4), inches(4), inches(1.2), ACCENT_ORANGE,
                     "PRIMARY LEDGER\nUK Ledger | COA: Corp | GBP", 1300, True, WHITE)
# Business Units
s5 += make_shape_xml(9, "bu1", inches(1.5), inches(5.8), inches(1.8), inches(0.6), LIGHT_BLUE,
                     "BU: US AP", 1100, True, WHITE)
s5 += make_shape_xml(10, "bu2", inches(3.7), inches(5.8), inches(1.8), inches(0.6), LIGHT_BLUE,
                     "BU: US AR", 1100, True, WHITE)
s5 += make_shape_xml(11, "bu3", inches(7.5), inches(5.8), inches(1.8), inches(0.6), LIGHT_BLUE,
                     "BU: UK AP", 1100, True, WHITE)
s5 += make_shape_xml(12, "bu4", inches(9.7), inches(5.8), inches(1.8), inches(0.6), LIGHT_BLUE,
                     "BU: UK AR", 1100, True, WHITE)
slides.append(s5)


# --- SLIDE 6: Steps to Create ---
s6 = ""
s6 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s6 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                     DARK_BLUE, "Steps to Create a Primary Ledger", 3200, True, WHITE, "l")
s6 += make_shape_xml(4, "nav", inches(0.8), inches(1.35), inches(11), inches(0.5),
                     WHITE, 'Navigation: Setup and Maintenance > "Manage Primary Ledgers" > Create', 1400, False, MEDIUM_BLUE, "l")
steps = [
    "Step 1: Enter Ledger Name and Description",
    "Step 2: Select Chart of Accounts (must be deployed first)",
    "Step 3: Select Accounting Calendar (must have periods defined)",
    "Step 4: Select Functional Currency (e.g., USD, INR, GBP)",
    "Step 5: Select Accounting Convention (Accrual / Cash)",
    "Step 6: Assign Subledger Accounting Method (Standard Accrual)",
    "Step 7: Configure Ledger Options (Retained Earnings, Suspense)",
    "Step 8: Save and Complete Accounting Configuration",
]
bp6 = make_bullet_text(steps, 1700, DARK_GRAY)
s6 += make_textbox(5, "steps", inches(0.8), inches(2.0), inches(11.5), inches(5), bp6)
slides.append(s6)

# --- SLIDE 7: Screen Fields ---
s7 = ""
s7 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s7 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                     DARK_BLUE, "Create Primary Ledger - Screen Fields", 3000, True, WHITE, "l")
s7 += make_shape_xml(4, "form_bg", inches(1), inches(1.5), inches(11), inches(5.5), LIGHT_GRAY)

fields = [
    ("* Name:", "ABC US Primary Ledger"),
    ("  Description:", "Primary ledger for US operations"),
    ("* Chart of Accounts:", "Corporate COA"),
    ("* Accounting Calendar:", "Monthly Calendar FY2026"),
    ("* Currency:", "USD - US Dollar"),
    ("* Accounting Convention:", "Accrual"),
    ("  Subledger Acctg Method:", "Standard Accrual (Seeded)"),
]
for i, (label, value) in enumerate(fields):
    y = inches(1.7 + i * 0.7)
    s7 += make_shape_xml(10+i*2, f"lbl{i}", inches(1.2), y, inches(3.5), inches(0.5),
                         LIGHT_GRAY, label, 1300, True, DARK_BLUE, "r")
    s7 += make_shape_xml(11+i*2, f"val{i}", inches(5), y+inches(0.05), inches(5.8), inches(0.4),
                         WHITE, value, 1300, False, DARK_GRAY, "l")
s7 += make_shape_xml(30, "note", inches(1.5), inches(6.7), inches(10), inches(0.4),
                     LIGHT_GRAY, "* = Mandatory fields | All prerequisites must be completed first", 1200, False, RED, "l")
slides.append(s7)


# --- SLIDE 8: Ledger Options ---
s8 = ""
s8 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s8 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                     DARK_BLUE, "Ledger Options - Mandatory Configurations", 2800, True, WHITE, "l")

opts = [
    ["Option", "Account / Value", "Purpose"],
    ["Retained Earnings", "01-000-31000-000-00", "Year-end P&L close account"],
    ["Suspense Account", "01-000-99000-000-00", "Catches unbalanced entries"],
    ["Rounding Account", "01-000-99100-000-00", "Currency rounding diffs"],
    ["Enable Suspense", "Yes / No", "Allow unbalanced journals?"],
    ["Journal Approval", "Yes (Recommended)", "Approval before posting"],
    ["Reversals", "Yes", "Allow journal reversals"],
]
for r, row in enumerate(opts):
    for c, cell in enumerate(row):
        w = [inches(3.2), inches(4), inches(4.5)][c]
        left = inches(0.5) + sum([inches(3.2), inches(4), inches(4.5)][:c])
        top = inches(1.5) + r * inches(0.7)
        if r == 0:
            bg, fc, b = MEDIUM_BLUE, WHITE, True
        else:
            bg = LIGHT_GRAY if r % 2 == 0 else WHITE
            fc, b = DARK_GRAY, False
        s8 += make_shape_xml(10+r*3+c, f"opt_{r}_{c}", left, top, w, inches(0.65), bg, cell, 1200, b, fc)
slides.append(s8)

# --- SLIDE 9: Accounting Configuration ---
s9 = ""
s9 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s9 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                     DARK_BLUE, "Accounting Configuration", 3200, True, WHITE, "l")
bullets9 = [
    "Oracle auto-generates an Accounting Configuration when you create a Primary Ledger",
    "It links: Primary Ledger + Secondary Ledgers + Reporting Currencies",
    "Status MUST be COMPLETED before you can open periods or post journals",
    "Navigation: Setup and Maintenance > Manage Accounting Configurations > Complete",
    "Validates: COA deployed, Calendar has periods, Currency enabled, Retained Earnings set",
    "If Secondary Ledger or Reporting Currency needed, add them BEFORE completing",
    "Once completed, structural changes (COA, Calendar) cannot be modified",
]
bp9 = make_bullet_text(bullets9, 1600, DARK_GRAY)
s9 += make_textbox(4, "bullets", inches(0.8), inches(1.5), inches(11.5), inches(4.5), bp9)
s9 += make_shape_xml(5, "status", inches(3), inches(6.2), inches(7), inches(0.8), GREEN,
                     "Status: COMPLETED (Required before transacting)", 1600, True, WHITE)
slides.append(s9)


# --- SLIDE 10: Prerequisites ---
s10 = ""
s10 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s10 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                      DARK_BLUE, "Prerequisites Before Creating Primary Ledger", 2800, True, WHITE, "l")
prereqs = [
    "1. Chart of Accounts created and deployed (GL# Key Flexfield)",
    "2. Value Sets created with values (Account Types assigned - Revenue/Expense/Asset/Liability/Equity)",
    "3. Accounting Calendar created with period type and periods defined",
    "4. Currency enabled in the system (USD, INR, GBP, EUR, etc.)",
    "5. Retained Earnings account exists in value set (Account Type = Equity)",
    "6. Segment Labels assigned (GL_BALANCING and GL_ACCOUNT are mandatory)",
    "7. Legal Entity created (optional at this stage - can assign later)",
]
bp10 = make_bullet_text(prereqs, 1600, DARK_GRAY)
s10 += make_textbox(4, "prereqs", inches(0.8), inches(1.5), inches(11.5), inches(5), bp10)
s10 += make_shape_xml(5, "warn", inches(0.8), inches(6.2), inches(11.5), inches(0.8), ACCENT_ORANGE,
                      "IMPORTANT: Complete ALL prerequisites before attempting ledger creation!", 1500, True, WHITE)
slides.append(s10)

# --- SLIDE 11: Subledger Accounting ---
s11 = ""
s11 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s11 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                      DARK_BLUE, "Subledger Accounting Method", 3200, True, WHITE, "l")
bullets11 = [
    "Every Primary Ledger needs a Subledger Accounting Method (SLAM)",
    "Defines HOW subledger transactions create GL journal entries",
    "Subledgers: AP Invoices/Payments, AR Invoices/Receipts, FA Depreciation, Cash Mgmt, Expenses",
    "Default: Standard Accrual (Oracle seeded - works for 90% of implementations)",
    "Custom methods can be created for complex accounting requirements",
    "Navigation: Setup and Maintenance > Manage Subledger Accounting Methods",
    "Assigned during Ledger creation or via Ledger Options",
    "Contains: Journal Entry Rule Sets, Account Derivation Rules, Mapping Sets",
]
bp11 = make_bullet_text(bullets11, 1600, DARK_GRAY)
s11 += make_textbox(4, "bullets", inches(0.8), inches(1.5), inches(11.5), inches(5.5), bp11)
slides.append(s11)


# --- SLIDE 12: Real-World Examples ---
s12 = ""
s12 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s12 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                      DARK_BLUE, "Real-World Examples", 3200, True, WHITE, "l")
# Example boxes
s12 += make_shape_xml(4, "ex1_bg", inches(0.5), inches(1.5), inches(3.8), inches(3.5), LIGHT_GRAY)
s12 += make_shape_xml(5, "ex1_title", inches(0.5), inches(1.5), inches(3.8), inches(0.6), MEDIUM_BLUE,
                      "Single-Country (US)", 1300, True, WHITE)
s12 += make_shape_xml(6, "ex1", inches(0.6), inches(2.2), inches(3.6), inches(2.7), LIGHT_GRAY,
                      "Company: XYZ Corp\nLedger: XYZ US Primary\nCOA: XYZ COA\nCalendar: Jan-Dec\nCurrency: USD\nConvention: Accrual", 1200, False, DARK_GRAY, "l")

s12 += make_shape_xml(7, "ex2_bg", inches(4.6), inches(1.5), inches(3.8), inches(3.5), LIGHT_GRAY)
s12 += make_shape_xml(8, "ex2_title", inches(4.6), inches(1.5), inches(3.8), inches(0.6), MEDIUM_BLUE,
                      "Multi-Country (India)", 1300, True, WHITE)
s12 += make_shape_xml(9, "ex2", inches(4.7), inches(2.2), inches(3.6), inches(2.7), LIGHT_GRAY,
                      "Legal Entity: ABC India\nLedger: India Primary\nCOA: Corporate COA\nCalendar: Apr-Mar\nCurrency: INR\n+ Reporting: USD", 1200, False, DARK_GRAY, "l")

s12 += make_shape_xml(10, "ex3_bg", inches(8.7), inches(1.5), inches(4.1), inches(3.5), LIGHT_GRAY)
s12 += make_shape_xml(11, "ex3_title", inches(8.7), inches(1.5), inches(4.1), inches(0.6), MEDIUM_BLUE,
                      "Dual-GAAP (Saudi)", 1300, True, WHITE)
s12 += make_shape_xml(12, "ex3", inches(8.8), inches(2.2), inches(3.9), inches(2.7), LIGHT_GRAY,
                      "Primary: KSA Local GAAP\nCurrency: SAR\nSecondary: KSA IFRS\nReporting: USD (Group)", 1200, False, DARK_GRAY, "l")

s12 += make_shape_xml(13, "rule", inches(0.5), inches(5.5), inches(12.3), inches(1), DARK_BLUE,
                      "Rule: Different currency or calendar = Separate Primary Ledger | Same COA = Easy consolidation", 1400, True, WHITE)
slides.append(s12)


# --- SLIDE 13: Key Design Decisions ---
s13 = ""
s13 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s13 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                      DARK_BLUE, "Key Design Decisions", 3200, True, WHITE, "l")
decisions = [
    ["Decision", "Recommendation"],
    ["One ledger per country or shared?", "Separate - different currencies need separate ledgers"],
    ["Share COA across ledgers?", "Yes - enables easy consolidation"],
    ["Accrual or Cash basis?", "Accrual (99% of implementations)"],
    ["Enable Suspense?", "Yes in Test/Dev, No in Production"],
    ["Enable Journal Approval?", "Yes - internal control and audit trail"],
    ["Need multi-GAAP?", "Add Secondary Ledger"],
    ["Need group currency?", "Add Reporting Currency"],
]
for r, row in enumerate(decisions):
    for c, cell in enumerate(row):
        w = inches(6) if c == 0 else inches(6)
        left = inches(0.5) + c * inches(6)
        top = inches(1.5) + r * inches(0.7)
        if r == 0:
            bg, fc, b = MEDIUM_BLUE, WHITE, True
        else:
            bg = LIGHT_GRAY if r % 2 == 0 else WHITE
            fc = DARK_GRAY
            b = (c == 0)
        s13 += make_shape_xml(10+r*2+c, f"d_{r}_{c}", left, top, w, inches(0.65), bg, cell, 1300, b, fc)
slides.append(s13)

# --- SLIDE 14: Common Errors ---
s14 = ""
s14 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s14 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                      DARK_BLUE, "Common Errors During Ledger Creation", 2800, True, WHITE, "l")
errs = [
    ["Error", "Solution"],
    ["COA not available for selection", "Deploy GL# Flexfield first"],
    ["No calendar available", "Create Accounting Calendar with periods"],
    ["Retained Earnings account required", "Create account with type = Equity"],
    ["Accounting Config not complete", "Manage Acctg Config > Click Complete"],
    ["No balancing segment defined", "Assign GL_BALANCING label to segment"],
    ["No natural account segment", "Assign GL_ACCOUNT label to segment"],
]
for r, row in enumerate(errs):
    for c, cell in enumerate(row):
        w = inches(6)
        left = inches(0.5) + c * inches(6)
        top = inches(1.5) + r * inches(0.75)
        if r == 0:
            bg = RED if c == 0 else GREEN
            fc, b = WHITE, True
        else:
            bg = LIGHT_GRAY if r % 2 == 0 else WHITE
            fc = RED if c == 0 else GREEN
            b = False
        s14 += make_shape_xml(10+r*2+c, f"e_{r}_{c}", left, top, w, inches(0.7), bg, cell, 1300, b, fc)
slides.append(s14)


# --- SLIDE 15: Next Steps ---
s15 = ""
s15 += make_shape_xml(2, "header_bg", 0, 0, SLIDE_WIDTH, inches(1.2), DARK_BLUE)
s15 += make_shape_xml(3, "header", inches(0.5), inches(0.15), inches(12), inches(1),
                      DARK_BLUE, "After Creating the Primary Ledger - Next Steps", 2800, True, WHITE, "l")
next_steps = [
    "1. Complete Accounting Configuration (status = COMPLETED)",
    "2. Create Legal Entity and assign to the Ledger",
    "3. Create Business Units and assign to Legal Entity",
    "4. Open first Accounting Period",
    "5. Configure Subledger Options (AP, AR, FA, Cash Mgmt)",
    "6. Set up Security Roles (data access by Business Unit)",
    "7. Load Opening Balances (if migrating from legacy system)",
    "8. Start Transacting!",
]
bp15 = make_bullet_text(next_steps, 1700, DARK_GRAY)
s15 += make_textbox(4, "next", inches(0.8), inches(1.5), inches(11.5), inches(5.5), bp15)
slides.append(s15)

# --- SLIDE 16: Summary / Thank You ---
s16 = ""
s16 += make_shape_xml(2, "bg", 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT, DARK_BLUE)
s16 += make_shape_xml(3, "line", 0, inches(3.5), SLIDE_WIDTH, inches(0.06), ACCENT_ORANGE)
s16 += make_shape_xml(4, "title", inches(1), inches(0.5), inches(11), inches(0.8),
                      DARK_BLUE, "Summary - Key Takeaways", 3200, True, WHITE, "l")
takeaways = [
    "Primary Ledger = COA + Calendar + Currency + Convention",
    "Every Legal Entity must have exactly ONE Primary Ledger",
    "Complete ALL prerequisites before creating the ledger",
    "Accounting Configuration must be COMPLETED before transacting",
    "Use Secondary Ledger for multi-GAAP needs",
    "Use Reporting Currency for group currency reporting",
    "Design on paper first - structure CANNOT change after go-live",
]
bp16 = make_bullet_text(takeaways, 1500, WHITE)
s16 += make_textbox(5, "take", inches(1), inches(1.5), inches(11), inches(2.8), bp16)
s16 += make_shape_xml(6, "q", inches(1), inches(5), inches(11), inches(1),
                      DARK_BLUE, "Questions?", 4000, True, ACCENT_ORANGE)
s16 += make_shape_xml(7, "ty", inches(1), inches(6.2), inches(11), inches(0.8),
                      DARK_BLUE, "Thank You!", 2400, False, WHITE)
slides.append(s16)


# ===== ASSEMBLE THE PPTX (ZIP) FILE =====
content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  {}
</Types>'''

slide_overrides = ""
for i in range(len(slides)):
    slide_overrides += '<Override PartName="/ppt/slides/slide{}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>\n'.format(i+1)
content_types = content_types.format(slide_overrides)

rels_root = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
</Relationships>'''

# Presentation relationships
pres_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  {}
</Relationships>'''
slide_rels_entries = ""
for i in range(len(slides)):
    slide_rels_entries += '<Relationship Id="rId{}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{}.xml"/>\n'.format(i+1, i+1)
pres_rels = pres_rels.format(slide_rels_entries)

# Presentation XML
slide_id_list = ""
for i in range(len(slides)):
    slide_id_list += '<p:sldId id="{}" r:id="rId{}"/>'.format(256+i, i+1)

presentation_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
                xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
                xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst/>
  <p:sldIdLst>{}</p:sldIdLst>
  <p:sldSz cx="{}" cy="{}" type="custom"/>
  <p:notesSz cx="{}" cy="{}"/>
</p:presentation>'''.format(slide_id_list, SLIDE_WIDTH, SLIDE_HEIGHT, SLIDE_WIDTH, SLIDE_HEIGHT)


# Write the ZIP file
with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr('[Content_Types].xml', content_types)
    zf.writestr('_rels/.rels', rels_root)
    zf.writestr('ppt/presentation.xml', presentation_xml)
    zf.writestr('ppt/_rels/presentation.xml.rels', pres_rels)

    for i, slide_shapes in enumerate(slides):
        slide_xml = make_slide_xml(slide_shapes)
        zf.writestr(f'ppt/slides/slide{i+1}.xml', slide_xml)
        # Each slide needs a rels file (empty is fine)
        slide_rel = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
</Relationships>'''
        zf.writestr(f'ppt/slides/_rels/slide{i+1}.xml.rels', slide_rel)

print(f"PowerPoint created successfully: {output_path}")
print(f"Total slides: {len(slides)}")
print(f"File size: {os.path.getsize(output_path) / 1024:.1f} KB")
