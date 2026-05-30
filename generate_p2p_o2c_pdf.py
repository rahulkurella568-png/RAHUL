#!/usr/bin/env python3
"""
Generate comprehensive P2P and O2C cycle PDF with mindmaps and data structures
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import io
from datetime import datetime

# Create PDF
pdf_path = "/projects/sandbox/RAHUL/P2P_O2C_Cycles_with_DataStructures.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)

# Story to hold all PDF elements
story = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1a3a5c'),
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#2e5090'),
    spaceAfter=8,
    spaceBefore=8,
    fontName='Helvetica-Bold'
)

subheading_style = ParagraphStyle(
    'CustomSubHeading',
    parent=styles['Heading3'],
    fontSize=11,
    textColor=colors.HexColor('#3d5a80'),
    spaceAfter=6,
    fontName='Helvetica-Bold'
)

normal_style = ParagraphStyle(
    'CustomNormal',
    parent=styles['Normal'],
    fontSize=9,
    alignment=TA_JUSTIFY,
    spaceAfter=4
)

# ============================================================================
# PAGE 1: TITLE & OVERVIEW
# ============================================================================

story.append(Paragraph("ORACLE FUSION FINANCIALS", title_style))
story.append(Paragraph("P2P (Procure-to-Pay) & O2C (Order-to-Cash) Cycles", title_style))
story.append(Paragraph("Comprehensive Data Structures & Process Flow", heading_style))
story.append(Spacer(1, 0.2*inch))

overview_text = """
<b>Document Purpose:</b> This document provides a detailed breakdown of Procure-to-Pay (P2P) and Order-to-Cash (O2C) 
cycles in Oracle Fusion Financials, including:<br/>
• Complete process flows and touchpoints<br/>
• Data structures and table relationships<br/>
• GL impact and financial reporting implications<br/>
• Integration points with other modules<br/>
• Mindmaps for visual process understanding<br/>
• Best practices and common configuration pitfalls
"""

story.append(Paragraph(overview_text, normal_style))
story.append(Spacer(1, 0.3*inch))

# Document metadata
meta_data = [
    ["Created Date:", datetime.now().strftime("%B %d, %Y")],
    ["Version:", "1.0"],
    ["Target System:", "Oracle Fusion Cloud Financials"],
    ["Modules Covered:", "AP, AR, PO, Inventory, GL, SLA"]
]

meta_table = Table(meta_data, colWidths=[2*inch, 3*inch])
meta_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e8f0f7')),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cccccc'))
]))

story.append(meta_table)
story.append(PageBreak())

# ============================================================================
# PAGE 2: P2P OVERVIEW & MINDMAP
# ============================================================================

story.append(Paragraph("PROCURE-TO-PAY (P2P) CYCLE", heading_style))
story.append(Spacer(1, 0.1*inch))

p2p_overview = """
<b>Definition:</b> P2P is the complete procurement lifecycle from supplier identification through payment, 
encompassing purchase requisitions, purchase orders, goods receipt, invoice matching, approval, and payment processing.<br/><br/>

<b>Key Objectives:</b><br/>
✓ Control spend and ensure compliance<br/>
✓ Optimize supplier relationships<br/>
✓ Ensure three-way matching (PO-Receipt-Invoice)<br/>
✓ Minimize payment errors and duplicate invoices<br/>
✓ Maintain audit trail for compliance<br/>
✓ Maximize cash flow optimization through payment terms
"""

story.append(Paragraph(p2p_overview, normal_style))
story.append(Spacer(1, 0.2*inch))

# P2P Process Steps
story.append(Paragraph("P2P Process Flow - High Level", subheading_style))

p2p_steps = [
    ["Step", "Process", "Owner", "Key Outcome"],
    ["1", "Requisition Creation", "Requestor", "Approval for purchase (Req ID)"],
    ["2", "Purchase Order (PO) Creation", "Buyer", "Formal commitment (PO Number)"],
    ["3", "Goods Receipt (GR)", "Warehouse/Receiving", "Receipt into inventory (GR ID)"],
    ["4", "Invoice Receipt", "AP Clerk", "Supplier invoice logged (Invoice ID)"],
    ["5", "Three-Way Match", "System/AP", "PO-GR-Invoice validation"],
    ["6", "Invoice Approval", "Manager/Approver", "Approved for payment"],
    ["7", "Payment Processing", "Treasurer/AP", "Check/ACH/Wire payment"],
    ["8", "Reconciliation", "Accountant", "Cash vs. AP cleared"]
]

p2p_table = Table(p2p_steps, colWidths=[0.6*inch, 1.8*inch, 1.4*inch, 1.8*inch])
p2p_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5090')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f5fa')])
]))

story.append(p2p_table)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("P2P Mindmap Visualization", subheading_style))
p2p_mindmap = """
<b>PROCURE-TO-PAY (P2P) CYCLE</b><br/>
<br/>
┌─ <b>1. REQUISITION PHASE</b><br/>
│  ├─ Create Purchase Requisition (PUR_REQ)<br/>
│  ├─ Approval Workflow (BPM)<br/>
│  └─ Requisition Line Items<br/>
│<br/>
├─ <b>2. PROCUREMENT PHASE</b><br/>
│  ├─ Create Purchase Order (PO) from Req<br/>
│  ├─ PO Header & Lines<br/>
│  ├─ Supplier Selection<br/>
│  ├─ Terms & Conditions<br/>
│  └─ PO Distribution (GL accrual accounts)<br/>
│<br/>
├─ <b>3. RECEIPT PHASE</b><br/>
│  ├─ Goods Receipt (Receiving)<br/>
│  ├─ Receipt Inspection<br/>
│  ├─ Quality Check (if configured)<br/>
│  ├─ Inventory Movement<br/>
│  └─ GL Impact: Debit Inventory/Asset, Credit Accrual<br/>
│<br/>
├─ <b>4. INVOICE PHASE</b><br/>
│  ├─ Invoice Data Entry (Manual/OCR/EDI)<br/>
│  ├─ Invoice Line Matching<br/>
│  ├─ Three-Way Validation<br/>
│  │  ├─ PO ↔ GR ↔ Invoice Match<br/>
│  │  └─ Variance Tolerance Check<br/>
│  ├─ Hold Rules Applied (if any)<br/>
│  └─ GL Impact: Debit COGS/Expense, Credit AP<br/>
│<br/>
├─ <b>5. APPROVAL PHASE</b><br/>
│  ├─ Approval Workflows (AMX Rules)<br/>
│  ├─ Manager Sign-off<br/>
│  ├─ Budget Availability Check<br/>
│  └─ Compliance Validation<br/>
│<br/>
├─ <b>6. PAYMENT PHASE</b><br/>
│  ├─ Payment Process Request (PPR)<br/>
│  ├─ Payment Method Selection (Check/ACH/Wire)<br/>
│  ├─ Discount Application (if early payment)<br/>
│  ├─ Withholding Tax Calculation<br/>
│  ├─ GL Impact: Debit AP, Credit Cash<br/>
│  └─ Payment Execution<br/>
│<br/>
└─ <b>7. RECONCILIATION PHASE</b><br/>
   ├─ Bank Reconciliation (Cash Mgmt)<br/>
   ├─ AP Aging Report<br/>
   ├─ Supplier Statement Reconciliation<br/>
   └─ Month-End Close<br/>
"""

story.append(Paragraph(p2p_mindmap, ParagraphStyle(
    'Monospace', parent=styles['Normal'], fontName='Courier', fontSize=7.5, 
    spaceAfter=4, leftIndent=0.1*inch
)))

story.append(PageBreak())

# ============================================================================
# PAGE 3: O2C OVERVIEW & MINDMAP
# ============================================================================

story.append(Paragraph("ORDER-TO-CASH (O2C) CYCLE", heading_style))
story.append(Spacer(1, 0.1*inch))

o2c_overview = """
<b>Definition:</b> O2C is the complete revenue lifecycle from customer order creation through cash collection, 
encompassing sales orders, shipment, invoicing, revenue recognition, payment collection, and reconciliation.<br/><br/>

<b>Key Objectives:</b><br/>
✓ Streamline sales-to-collection process<br/>
✓ Ensure accurate revenue recognition (ASC 606/IFRS 15)<br/>
✓ Minimize Days Sales Outstanding (DSO)<br/>
✓ Manage customer credit and collections<br/>
✓ Maintain accurate receivables aging<br/>
✓ Enable real-time cash forecasting
"""

story.append(Paragraph(o2c_overview, normal_style))
story.append(Spacer(1, 0.2*inch))

# O2C Process Steps
story.append(Paragraph("O2C Process Flow - High Level", subheading_style))

o2c_steps = [
    ["Step", "Process", "Owner", "Key Outcome"],
    ["1", "Sales Order Creation", "Sales/Order Entry", "Customer order confirmed (SO #)"],
    ["2", "Credit Check", "Credit Manager", "Credit limit verification"],
    ["3", "Shipment", "Warehouse/Logistics", "Goods shipped (Shipment ID)"],
    ["4", "Invoice Generation", "Billing/AR", "AR Invoice created (Invoice #)"],
    ["5", "Revenue Recognition", "Revenue/AR", "Revenue posted to GL"],
    ["6", "Invoice Distribution", "AR Clerk", "Invoice sent to customer"],
    ["7", "Payment Receipt", "Lockbox/AR", "Cash received (Receipt #)"],
    ["8", "Collections", "Collector", "Follow-up on overdue amounts"],
    ["9", "Reconciliation", "Accountant", "AR cleared, DSO measured"]
]

o2c_table = Table(o2c_steps, colWidths=[0.6*inch, 1.8*inch, 1.4*inch, 1.8*inch])
o2c_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5090')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f5fa')])
]))

story.append(o2c_table)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("O2C Mindmap Visualization", subheading_style))
o2c_mindmap = """
<b>ORDER-TO-CASH (O2C) CYCLE</b><br/>
<br/>
┌─ <b>1. SALES ORDER PHASE</b><br/>
│  ├─ Customer Creation (CRM/AR)<br/>
│  ├─ Sales Order Entry<br/>
│  ├─ Order Lines (Item, Qty, Price)<br/>
│  ├─ Price List Application<br/>
│  └─ Order Booking<br/>
│<br/>
├─ <b>2. CREDIT & APPROVAL PHASE</b><br/>
│  ├─ Credit Limit Check<br/>
│  ├─ Credit Review (if flagged)<br/>
│  ├─ Approval Workflow<br/>
│  └─ Order Release<br/>
│<br/>
├─ <b>3. FULFILLMENT PHASE</b><br/>
│  ├─ Pick & Pack<br/>
│  ├─ Shipment Creation<br/>
│  ├─ Delivery/Receipt by Customer<br/>
│  ├─ Proof of Delivery (POD)<br/>
│  └─ GL Impact: Debit COGS, Credit Inventory<br/>
│<br/>
├─ <b>4. INVOICING PHASE</b><br/>
│  ├─ Invoice Auto-Generation from Shipment<br/>
│  ├─ Invoice Header & Lines<br/>
│  ├─ Tax Calculation<br/>
│  ├─ Revenue Schedule (if multi-period)<br/>
│  └─ GL Impact: Debit AR, Credit Revenue<br/>
│<br/>
├─ <b>5. REVENUE RECOGNITION PHASE</b><br/>
│  ├─ Performance Obligation Assessment (ASC 606)<br/>
│  ├─ Revenue Recognition Rules (SLA)<br/>
│  ├─ Deferred Revenue Handling (if applicable)<br/>
│  └─ GL Impact: Debit AR/Cash, Credit Revenue/Deferred Rev<br/>
│<br/>
├─ <b>6. COLLECTION PHASE</b><br/>
│  ├─ Invoice Delivery to Customer<br/>
│  ├─ Payment Terms Application<br/>
│  ├─ Discount Tracking (Early Pay)<br/>
│  ├─ Dunning Management (if overdue)<br/>
│  ├─ Lockbox Processing (if configured)<br/>
│  └─ Payment Receipt<br/>
│<br/>
├─ <b>7. CASH APPLICATION PHASE</b><br/>
│  ├─ Cash Received (Bank Deposit)<br/>
│  ├─ Auto-Matching to Invoice<br/>
│  ├─ Partial/Overpayment Handling<br/>
│  ├─ Discount Adjustment<br/>
│  └─ GL Impact: Debit Cash, Credit AR<br/>
│<br/>
├─ <b>8. COLLECTIONS PHASE</b><br/>
│  ├─ AR Aging Analysis<br/>
│  ├─ Dunning Notices<br/>
│  ├─ Write-offs (if uncollectible)<br/>
│  ├─ Credit Memo Processing<br/>
│  └─ GL Impact: Debit Bad Debt Expense/Write-off, Credit AR<br/>
│<br/>
└─ <b>9. RECONCILIATION PHASE</b><br/>
   ├─ AR Sub-Ledger to GL<br/>
   ├─ Cash Reconciliation<br/>
   ├─ DSO Calculation<br/>
   ├─ Aged Balance Reporting<br/>
   └─ Month-End Close<br/>
"""

story.append(Paragraph(o2c_mindmap, ParagraphStyle(
    'Monospace', parent=styles['Normal'], fontName='Courier', fontSize=7.5, 
    spaceAfter=4, leftIndent=0.1*inch
)))

story.append(PageBreak())

print("PDF generation in progress... (Part 1 of 2)")


# ============================================================================
# PAGE 4: P2P DATA STRUCTURES & TABLES
# ============================================================================

story.append(Paragraph("P2P DATA STRUCTURES - CORE TABLES", heading_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("Purchasing Module (PO) - Key Tables", subheading_style))

po_tables = [
    ["Table Name", "Key Fields", "Purpose"],
    ["PO_HEADERS_ALL", "PO_HEADER_ID, PO_NUMBER, VENDOR_ID, PO_DATE", "Master PO header records"],
    ["PO_LINES_ALL", "PO_LINE_ID, PO_HEADER_ID, ITEM_ID, QUANTITY, UNIT_PRICE", "PO line items"],
    ["PO_DISTRIBUTIONS", "PO_DISTRIBUTION_ID, PO_LINE_ID, ACCOUNT, QTY_ORDERED", "GL distribution for encumbrance"],
    ["RCV_TRANSACTIONS", "TRANSACTION_ID, PO_LINE_ID, QUANTITY_RECEIVED", "Goods receipt transactions"],
    ["RCV_SHIPMENT_HEADERS", "SHIPMENT_HEADER_ID, PO_HEADER_ID, RECEIPT_DATE", "Shipment header"],
    ["RCV_SHIPMENT_LINES", "SHIPMENT_LINE_ID, PO_LINE_ID, QUANTITY_SHIPPED", "Individual shipment lines"]
]

po_table = Table(po_tables, colWidths=[1.8*inch, 2.2*inch, 1.5*inch])
po_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5090')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f5fa')])
]))

story.append(po_table)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("Accounts Payable Module (AP) - Key Tables", subheading_style))

ap_tables = [
    ["Table Name", "Key Fields", "Purpose"],
    ["AP_INVOICES_ALL", "INVOICE_ID, INVOICE_NUM, VENDOR_ID, INVOICE_DATE", "Supplier invoices"],
    ["AP_INVOICE_LINES_ALL", "INVOICE_LINE_ID, INVOICE_ID, LINE_TYPE_LOOKUP_CODE", "Invoice line items"],
    ["AP_INVOICE_DISTRIBUTIONS_ALL", "INVOICE_DISTRIBUTION_ID, INVOICE_ID, DIST_CODE_COMBINATION_ID", "GL distribution for expenses"],
    ["AP_MATCHING_SETS", "MATCHING_SET_OPTION_ID, PO_ID, RCV_ID, INV_ID", "3-way match validation"],
    ["AP_HOLDS", "HOLD_ID, INVOICE_ID, HOLD_REASON", "Invoice holds/exceptions"],
    ["AP_PAYMENT_SCHEDULES_ALL", "PAYMENT_NUM, INVOICE_ID, DUE_DATE", "Payment terms schedule"],
    ["AP_SUPPLIERS", "VENDOR_ID, VENDOR_NAME, VENDOR_TYPE_LOOKUP_CODE", "Supplier master data"]
]

ap_table = Table(ap_tables, colWidths=[1.8*inch, 2.2*inch, 1.5*inch])
ap_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8B0000')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ffe8e8')])
]))

story.append(ap_table)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("GL Impact - P2P Transaction Flow", subheading_style))

p2p_gl = [
    ["Step", "GL Entry", "Debit Account", "Credit Account", "Amount"],
    ["PO Created (Encumbrance)", "Accrual", "Encumbrance Liability", "Encumbrance Asset", "PO Value"],
    ["Goods Receipt", "Accrual Reversal + Asset", "Inventory/Asset", "Accrual Liability", "GR Value"],
    ["Invoice Receipt", "Expense Recognition", "COGS/Expense/Asset", "AP Payable", "Invoice Value"],
    ["Payment", "Cash Out", "AP Payable", "Cash/Bank", "Payment Amount"],
    ["Variance Adjustment", "Correction", "COGS Variance", "AP Payable", "Variance Amount"]
]

p2p_gl_table = Table(p2p_gl, colWidths=[1.1*inch, 1.1*inch, 1.2*inch, 1.2*inch, 1.1*inch])
p2p_gl_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a472a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#e8f0e8')])
]))

story.append(p2p_gl_table)
story.append(PageBreak())

# ============================================================================
# PAGE 5: O2C DATA STRUCTURES & TABLES
# ============================================================================

story.append(Paragraph("O2C DATA STRUCTURES - CORE TABLES", heading_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("Sales Order Module (OM) - Key Tables", subheading_style))

so_tables = [
    ["Table Name", "Key Fields", "Purpose"],
    ["ONT_ORDER_HEADERS_ALL", "ORDER_ID, ORDER_NUMBER, CUSTOMER_ID, ORDER_DATE", "Master sales order"],
    ["ONT_ORDER_LINES_ALL", "LINE_ID, ORDER_ID, INVENTORY_ITEM_ID, ORDERED_QUANTITY", "Sales order lines"],
    ["WSH_DELIVERY_DETAILS", "DELIVERY_DETAIL_ID, LINE_ID, SHIPPED_QUANTITY", "Shipment line details"],
    ["WSH_DELIVERY_ASSIGNMENTS", "DELIVERY_ASSIGNMENT_ID, DELIVERY_ID, PICKUP_STOP_ID", "Delivery logistics"],
    ["ONT_ORDER_HOLDS", "HOLD_ID, ORDER_ID, HOLD_REASON", "Order holds (credit, etc)"],
    ["AR_CUSTOMERS", "CUST_ACCOUNT_ID, CUSTOMER_NAME, PARTY_ID", "Customer master data"]
]

so_table = Table(so_tables, colWidths=[1.8*inch, 2.2*inch, 1.5*inch])
so_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5090')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f5fa')])
]))

story.append(so_table)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("Accounts Receivable Module (AR) - Key Tables", subheading_style))

ar_tables = [
    ["Table Name", "Key Fields", "Purpose"],
    ["RA_CUSTOMER_TRX_ALL", "CUSTOMER_TRX_ID, TRX_NUMBER, CUSTOMER_ID, TRX_DATE", "AR invoices/transactions"],
    ["RA_CUSTOMER_TRX_LINES_ALL", "CUSTOMER_TRX_LINE_ID, CUSTOMER_TRX_ID, LINE_NUMBER", "Invoice line items"],
    ["RA_CUST_TRX_LINE_GL_DIST_ALL", "CUST_TRX_LINE_GL_DIST_ID, TRX_LINE_ID, CODE_COMBINATION_ID", "GL distribution"],
    ["RA_CUSTOMER_RECEIPT_ALL", "CASH_RECEIPT_ID, RECEIPT_NUMBER, CUSTOMER_ID, RECEIPT_DATE", "Cash receipts"],
    ["AR_RECEIVABLE_APPLICATIONS_ALL", "RECEIVABLE_APPLICATION_ID, CASH_RECEIPT_ID, CUSTOMER_TRX_ID", "Match receipt to invoice"],
    ["AR_CUSTOMERS_TRX_SUMMARY", "CUSTOMER_TRX_SUMMARY_ID, CUSTOMER_ID, CUST_ACCOUNT_ID", "Customer AR summary"],
    ["HZ_CUST_ACCOUNTS", "CUST_ACCOUNT_ID, ACCOUNT_NUMBER, CUSTOMER_CLASS_CODE", "Customer account hierarchy"]
]

ar_table = Table(ar_tables, colWidths=[1.8*inch, 2.2*inch, 1.5*inch])
ar_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8B0000')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ffe8e8')])
]))

story.append(ar_table)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("GL Impact - O2C Transaction Flow", subheading_style))

o2c_gl = [
    ["Step", "GL Entry", "Debit Account", "Credit Account", "Amount"],
    ["Sales Order Created", "None", "None", "None", "None (memo only)"],
    ["Shipment", "COGS Recognition", "COGS of Goods Sold", "Finished Goods Inventory", "COGS Value"],
    ["Invoice Generated", "Revenue Recognition", "AR Receivable", "Revenue/Sales", "Invoice Amount"],
    ["Revenue Recognition", "Revenue Accrual", "Deferred Revenue / AR", "Revenue (when service delivered)", "Rev Recognition Amt"],
    ["Cash Receipt", "Cash In", "Cash/Bank", "AR Receivable", "Payment Amount"],
    ["Bad Debt Writeoff", "Provision", "Bad Debt Expense", "AR Receivable", "Writeoff Amount"]
]

o2c_gl_table = Table(o2c_gl, colWidths=[1.1*inch, 1.1*inch, 1.2*inch, 1.2*inch, 1.1*inch])
o2c_gl_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a472a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#e8f0e8')])
]))

story.append(o2c_gl_table)
story.append(PageBreak())

print("PDF generation in progress... (Part 2 of 2)")


# ============================================================================
# PAGE 6: P2P & O2C INTEGRATION & TOUCHPOINTS
# ============================================================================

story.append(Paragraph("P2P & O2C INTEGRATION POINTS", heading_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("Cross-Module Dependencies", subheading_style))

integration_data = [
    ["Integration Point", "P2P Module", "O2C Module", "Business Impact"],
    ["Inventory Movement", "Receipt (GR)", "Shipment", "GL COGS posting synchronized"],
    ["GL Posting", "AP Invoice Distribution", "AR Revenue Distribution", "Period close dependent"],
    ["Payment Terms", "AP Payment Schedule", "AR Payment Terms", "DSO vs. DPO optimization"],
    ["Customer-Supplier", "Supplier Master", "Customer Master", "Intercompany transactions"],
    ["Subledger Accounting", "SLA for P2O Accruals", "SLA for Revenue Recognition", "Automated GL derivation"],
    ["Withholding Tax", "AP Withholding Tax Calc", "N/A", "Tax compliance & GL posting"],
    ["Multi-Org Transactions", "Intercompany PO", "Intercompany Sales Order", "Consolidated reporting"]
]

integration_table = Table(integration_data, colWidths=[1.5*inch, 1.4*inch, 1.4*inch, 1.4*inch])
integration_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5090')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f5fa')])
]))

story.append(integration_table)
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph("System Integration Architecture", subheading_style))

integration_arch = """
<b>End-to-End Business Process Integration:</b><br/>
<br/>
┌─────────────────────────────────────────────────────────────────────┐<br/>
│                    ORACLE FUSION FINANCIALS                         │<br/>
├─────────────────────────────────────────────────────────────────────┤<br/>
│                                                                       │<br/>
│  ┌─ PROCUREMENT (P2P) ────────────────────────────────────────────┐ │<br/>
│  │ Requisition → PO → Receipt → Invoice → Approval → Payment     │ │<br/>
│  │    ↓           ↓       ↓        ↓         ↓          ↓        │ │<br/>
│  │   REQ      PO_HDR  RCV_TXN  AP_INV   AP_HOLD    AP_PMNT      │ │<br/>
│  │    ↓           ↓       ↓        ↓         ↓          ↓        │ │<br/>
│  │  GL: Encumb → Accrual → Inventory → Expense → AP Liability  │ │<br/>
│  └────────────────────────────────────────────────────────────────┘ │<br/>
│              ↓                                           ↓            │<br/>
│         SUBLEDGER ACCOUNTING (SLA) RULES               CASH MGMT     │<br/>
│              ↓                                           ↓            │<br/>
│  ┌─ GENERAL LEDGER ──────────────────────────────────────────────┐ │<br/>
│  │   Assets | Liabilities | Equity | Revenue | Expenses | Cash │ │<br/>
│  │                                                               │ │<br/>
│  │   1000: Cash          │  2000: AP Payable   │ 5000: COGS    │ │<br/>
│  │   1100: AR Receivable │  3000: Revenue     │ 5100: OpEx    │ │<br/>
│  │   1200: Inventory     │  Deferred Revenue  │ 8000: Allocation
│  └───────────────────────────────────────────────────────────────┘ │<br/>
│              ↓                                           ↓            │<br/>
│         FINANCIAL REPORTING                     BANK RECONCILIATION  │<br/>
│              ↓                                           ↓            │<br/>
│  ┌─ SALES (O2C) ──────────────────────────────────────────────────┐ │<br/>
│  │ Sales Order → Credit Check → Shipment → Invoice → Collection │ │<br/>
│  │     ↓            ↓            ↓          ↓           ↓       │ │<br/>
│  │   SO_HDR      OM_HOLD    WSHT_DELIVERY  RA_INV    AR_RCPT   │ │<br/>
│  │     ↓            ↓            ↓          ↓           ↓       │ │<br/>
│  │  GL: None → No Accrual → COGS → Revenue → Cash Received    │ │<br/>
│  └────────────────────────────────────────────────────────────────┘ │<br/>
│                                                                       │<br/>
└─────────────────────────────────────────────────────────────────────┘<br/>
"""

story.append(Paragraph(integration_arch, ParagraphStyle(
    'Monospace', parent=styles['Normal'], fontName='Courier', fontSize=6.5, 
    spaceAfter=4, leftIndent=0.05*inch
)))

story.append(PageBreak())

# ============================================================================
# PAGE 7: CONTROL POINTS & COMPLIANCE
# ============================================================================

story.append(Paragraph("CONTROL POINTS & COMPLIANCE", heading_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("P2P Control Framework", subheading_style))

p2p_controls = [
    ["Control Name", "Trigger Point", "Purpose", "Owner"],
    ["3-Way Matching", "Invoice Receipt", "Prevent overpayment", "AP"],
    ["Approval Workflow", "Invoice Amount > Threshold", "Segregation of Duties", "Manager"],
    ["Hold Rules", "Invoice Entry", "Vendor Quality/On-time, Budget available", "AP/Finance"],
    ["Variance Tolerance", "Match Variance", "Allow small PO-Invoice variance", "Finance"],
    ["Duplicate Check", "Invoice Number", "Prevent duplicate payments", "AP"],
    ["Supplier Validation", "Invoice Entry", "Ensure active/approved supplier", "Procurement"],
    ["Encumbrance Check", "PO Release", "Prevent over-commitment", "Budget Control"],
    ["Withholding Tax", "Payment", "Tax compliance & GL posting", "Tax/AP"]
]

p2p_controls_table = Table(p2p_controls, colWidths=[1.4*inch, 1.3*inch, 1.4*inch, 1.2*inch])
p2p_controls_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5090')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f5fa')])
]))

story.append(p2p_controls_table)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("O2C Control Framework", subheading_style))

o2c_controls = [
    ["Control Name", "Trigger Point", "Purpose", "Owner"],
    ["Credit Limit Check", "Sales Order Entry", "Prevent exceeding credit exposure", "Credit Mgmt"],
    ["Price Validation", "Order Line Entry", "Prevent unauthorized pricing", "Sales Ops"],
    ["Revenue Recognition", "Invoice/Shipment", "ASC 606/IFRS 15 Compliance", "Revenue/AR"],
    ["Invoice Accuracy", "Invoice Generation", "Ensure correct billing amounts", "Billing"],
    ["Collections Aging", "AR Aging Report", "Monitor DSO, trigger collection action", "Collections"],
    ["Discount Validation", "Cash Receipt", "Prevent unauthorized discounts", "AR"],
    ["Write-off Approval", "Bad Debt", "Prevent unauthorized write-offs", "AR Manager"],
    ["Reconciliation", "Period End", "GL ↔ AR Sub-ledger match", "Accountant"],
    ["Customer Validation", "Order Entry", "Active customer, correct terms", "Sales"]
]

o2c_controls_table = Table(o2c_controls, colWidths=[1.4*inch, 1.3*inch, 1.4*inch, 1.2*inch])
o2c_controls_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8B0000')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ffe8e8')])
]))

story.append(o2c_controls_table)
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph("Month-End Close Checklist", subheading_style))

close_checklist = """
<b>P2P Month-End Close Activities:</b><br/>
□ Reconcile AP Sub-ledger to GL<br/>
□ Review Outstanding Invoices & Accruals<br/>
□ Process Unmatched Receipts (Accrual)<br/>
□ Review & Clear AP Holds<br/>
□ Process Final Invoices & Payments<br/>
□ Reconcile Vendor Statements<br/>
□ Review Expense Allocations<br/>
□ Validate Withholding Tax Accruals<br/>
□ GL Period close certification<br/>
<br/>
<b>O2C Month-End Close Activities:</b><br/>
□ Reconcile AR Sub-ledger to GL<br/>
□ Review AR Aging & Collections<br/>
□ Revenue Recognition Analysis (ASC 606)<br/>
□ Process Revenue Accruals/Deferrals<br/>
□ Bad Debt Provision Review<br/>
□ Reconcile Customer Statements<br/>
□ Clear Unmatched Cash<br/>
□ Validate Payment Terms Impact<br/>
□ GL period close certification<br/>
"""

story.append(Paragraph(close_checklist, normal_style))

story.append(PageBreak())

# ============================================================================
# PAGE 8: KEY METRICS & KPIs
# ============================================================================

story.append(Paragraph("KEY PERFORMANCE INDICATORS (KPIs)", heading_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("P2P KPIs", subheading_style))

p2p_kpis = [
    ["KPI", "Formula", "Target", "Owner"],
    ["Purchase Order Cycle Time", "Days: PO Created → Invoice", "≤ 10 days", "Procurement"],
    ["3-Way Match Rate", "Matched Invoices / Total Invoices", "≥ 95%", "AP"],
    ["Invoice Processing Cost", "AP Salaries / Number Invoices", "≤ $5/invoice", "AP Manager"],
    ["Payment Discount Capture", "Discounts Taken / Available", "≥ 80%", "Treasurer"],
    ["Duplicate Invoice Rate", "Duplicate Invoices / Total", "≤ 0.5%", "AP"],
    ["Days Payable Outstanding (DPO)", "AP Balance / Daily COGS", "45-60 days", "Treasury"],
    ["Variance Rate", "PO-Invoice Variances / Total", "≤ 1%", "Finance"],
    ["Supplier On-Time Performance", "On-Time Receipts / Total", "≥ 95%", "Procurement"]
]

p2p_kpis_table = Table(p2p_kpis, colWidths=[1.5*inch, 1.8*inch, 1.2*inch, 1.3*inch])
p2p_kpis_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5090')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f5fa')])
]))

story.append(p2p_kpis_table)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("O2C KPIs", subheading_style))

o2c_kpis = [
    ["KPI", "Formula", "Target", "Owner"],
    ["Order Cycle Time", "Days: SO → Shipment → Invoice", "≤ 5 days", "Sales Ops"],
    ["Cash Conversion Cycle", "DIO + DSO - DPO", "≤ 30 days", "CFO"],
    ["Days Sales Outstanding (DSO)", "AR Balance / Daily Revenue", "30-45 days", "AR Manager"],
    ["Invoice Accuracy", "Correct Invoices / Total", "≥ 99%", "Billing"],
    ["Collection Rate", "Cash Collected / Invoiced", "≥ 95%", "Collections"],
    ["Credit Limit Utilization", "AR / Credit Limit", "60-80%", "Credit Mgmt"],
    ["Bad Debt % Revenue", "Bad Debt Expense / Revenue", "≤ 2%", "AR Manager"],
    ["Order Fulfillment Rate", "Fulfilled Orders / Total", "≥ 98%", "Warehouse"]
]

o2c_kpis_table = Table(o2c_kpis, colWidths=[1.5*inch, 1.8*inch, 1.2*inch, 1.3*inch])
o2c_kpis_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8B0000')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ffe8e8')])
]))

story.append(o2c_kpis_table)

story.append(PageBreak())

# ============================================================================
# PAGE 9: COMMON CONFIGURATIONS & TROUBLESHOOTING
# ============================================================================

story.append(Paragraph("CONFIGURATION & TROUBLESHOOTING", heading_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("Common P2P Pitfalls & Solutions", subheading_style))

p2p_pitfalls = """
<b>1. Three-Way Matching Failures</b><br/>
   Problem: Frequent unmatched invoices due to quantity/price variances<br/>
   Solution: Configure variance tolerance thresholds (e.g., allow ±2% quantity variance)<br/>
   Config: Setup & Maintenance > Manage Matching Options<br/>
<br/>
<b>2. Duplicate Invoice Detection</b><br/>
   Problem: Same invoice posted multiple times<br/>
   Solution: Enable duplicate invoice check on invoice date + amount + vendor<br/>
   Config: Setup & Maintenance > Manage Duplicate Invoice Options<br/>
<br/>
<b>3. Encumbrance Not Clearing</b><br/>
   Problem: PO encumbrance remains even after invoice payment<br/>
   Solution: Ensure PO Distribution GL accounts align with invoice GL derivation (SLA)<br/>
   Config: Verify SLA rules derive to correct GL accounts<br/>
<br/>
<b>4. Payment Discount Not Captured</b><br/>
   Problem: Early payment discounts not automatically applied<br/>
   Solution: Configure discount terms in AP and validate discount GL accounts<br/>
   Config: Setup & Maintenance > Manage Payment Terms<br/>
<br/>
<b>5. Hold Rules Not Triggering</b><br/>
   Problem: Invoices should be on hold but are not<br/>
   Solution: Verify hold rule conditions (supplier type, amount threshold, etc.)<br/>
   Config: Setup & Maintenance > Manage Holds Rules<br/>
"""

story.append(Paragraph(p2p_pitfalls, normal_style))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("Common O2C Pitfalls & Solutions", subheading_style))

o2c_pitfalls = """
<b>1. Revenue Recognition Timing Issues</b><br/>
   Problem: Revenue recognized in wrong period (ASC 606 non-compliance)<br/>
   Solution: Configure revenue recognition rules to trigger on shipment or invoice date<br/>
   Config: Setup & Maintenance > Manage Revenue Recognition Rules<br/>
<br/>
<b>2. AR-GL Reconciliation Variance</b><br/>
   Problem: AR sub-ledger doesn't match GL balance<br/>
   Solution: Verify all RA transactions post through SLA to GL<br/>
   Config: Run AR-GL Reconciliation Report; investigate open items<br/>
<br/>
<b>3. Customer Credit Limit Not Enforced</b><br/>
   Problem: Orders bypass credit limit check<br/>
   Solution: Enable credit hold on SO entry; configure credit rules<br/>
   Config: Setup & Maintenance > Manage Credit Rules<br/>
<br/>
<b>4. Lockbox Not Auto-Matching Cash</b><br/>
   Problem: Cash received but not applied to invoices automatically<br/>
   Solution: Configure lockbox matching rules (PO #, Invoice #, customer ID)<br/>
   Config: Setup & Maintenance > Manage Lockbox Auto-Matching Rules<br/>
<br/>
<b>5. Bad Debt Provision Not Calculating</b><br/>
   Problem: Aging > 90 days not triggering bad debt accrual<br/>
   Solution: Configure bad debt aging rules and run provision batch<br/>
   Config: Setup & Maintenance > Manage Bad Debt Aging Rules<br/>
"""

story.append(Paragraph(o2c_pitfalls, normal_style))

story.append(PageBreak())

# ============================================================================
# PAGE 10: SUMMARY & BEST PRACTICES
# ============================================================================

story.append(Paragraph("BEST PRACTICES & SUMMARY", heading_style))
story.append(Spacer(1, 0.1*inch))

best_practices = """
<b>✓ P2P Best Practices:</b><br/>
1. <b>Enforce 3-way matching</b> - Never bypass PO-GR-Invoice validation<br/>
2. <b>Leverage SLA rules</b> - Auto-derive GL accounts to reduce manual error<br/>
3. <b>Monitor encumbrances</b> - Close month-end with zero encumbrance balance<br/>
4. <b>Capture early pay discounts</b> - CFO typically wants 50% capture rate minimum<br/>
5. <b>Centralize holds</b> - Use hold rules instead of manual review<br/>
6. <b>Implement duplicate checks</b> - Prevent vendor fraud and overpayments<br/>
7. <b>Regular vendor statement reconciliation</b> - Catch AP errors early<br/>
8. <b>DPO optimization</b> - Balance supplier relationships with cash flow<br/>
<br/>
<b>✓ O2C Best Practices:</b><br/>
1. <b>Revenue recognition compliance</b> - Implement ASC 606 properly from day one<br/>
2. <b>Credit policy enforcement</b> - Prevent bad debt by enforcing credit limits<br/>
3. <b>DSO management</b> - Target industry-standard DSO (typically 30-45 days)<br/>
4. <b>Lockbox automation</b> - Reduce days to cash through automated matching<br/>
5. <b>Collection process discipline</b> - Escalate past-due > 30 days immediately<br/>
6. <b>Bad debt provisioning</b> - Monthly reserve for high-risk receivables<br/>
7. <b>Customer master governance</b> - Prevent duplicate customers, maintain data quality<br/>
8. <b>AR-GL reconciliation</b> - Perform weekly, not just month-end<br/>
<br/>
<b>✓ Integrated Process Best Practices:</b><br/>
1. <b>SLA Rule Excellence</b> - Invest time in SLA configuration; it eliminates 80% of manual GL effort<br/>
2. <b>GL Chart Clarity</b> - Segment accounts by product/function/BU for better reporting<br/>
3. <b>Workflow Standardization</b> - Use AMX rules to enforce consistent approval logic<br/>
4. <b>KPI Monitoring</b> - Track DSO, DPO, and cycle times weekly, not quarterly<br/>
5. <b>Period Close Synchronization</b> - P2P and O2C close windows should be coordinated<br/>
6. <b>Data Quality</b> - Invest in data validation rules; garbage in = garbage out<br/>
7. <b>Training & Documentation</b> - Well-trained users reduce downstream support costs<br/>
8. <b>Continuous Improvement</b> - Review process metrics quarterly; iterate on rules<br/>
"""

story.append(Paragraph(best_practices, normal_style))
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph("Process Maturity Roadmap", subheading_style))

maturity = """
<b>LEVEL 1 (Manual & Reactive):</b><br/>
• Manual invoice entry & GL posting<br/>
• No 3-way matching automation<br/>
• Month-end close = 15+ days<br/>
• High AR DSO (60+ days), High AP DPO volatility<br/>
<br/>
<b>LEVEL 2 (Systematic & Documented):</b><br/>
• Automated 3-way matching<br/>
• Basic SLA rules for GL posting<br/>
• Standardized workflows (approval rules)<br/>
• Month-end close = 10-12 days<br/>
• DSO trend improving, DPO optimizing<br/>
<br/>
<b>LEVEL 3 (Optimized & Integrated):</b><br/>
• Full automation: Lockbox, OCR, E-invoicing<br/>
• Advanced SLA mapping (multi-dimensional)<br/>
• Real-time KPI dashboards<br/>
• Month-end close = 5-7 days<br/>
• Industry-leading DSO & DPO<br/>
<br/>
<b>LEVEL 4 (Predictive & Autonomous):</b><br/>
• Predictive analytics for bad debt, cash forecasting<br/>
• Machine learning for invoice exception detection<br/>
• Real-time GL consolidation<br/>
• Continuous close capabilities<br/>
• Strategic partnerships: supplier portals, EDI, API integrations<br/>
"""

story.append(Paragraph(maturity, normal_style))

# ============================================================================
# BUILD PDF
# ============================================================================

# Build the PDF
doc.build(story)

print(f"\n✓ PDF successfully created: {pdf_path}")
print(f"✓ Document contains comprehensive P2P & O2C cycle documentation")
print(f"✓ Includes mindmaps, data structures, integration points, and best practices")
