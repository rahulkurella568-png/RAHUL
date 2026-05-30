# ORACLE FUSION FINANCIALS
# P2P (Procure-to-Pay) & O2C (Order-to-Cash) Cycles
## Comprehensive Data Structures & Process Flow

**Document Date:** May 30, 2026  
**Version:** 1.0  
**Target System:** Oracle Fusion Cloud Financials  
**Modules Covered:** AP, AR, PO, Inventory, GL, SLA  

---

## TABLE OF CONTENTS

1. [Document Overview](#overview)
2. [Procure-to-Pay (P2P) Cycle](#p2p)
3. [Order-to-Cash (O2C) Cycle](#o2c)
4. [Data Structures](#data-structures)
5. [Integration Points](#integration)
6. [Control Points](#controls)
7. [KPIs & Metrics](#kpis)
8. [Configuration Guide](#configuration)
9. [Best Practices](#best-practices)

---

## DOCUMENT OVERVIEW {#overview}

### Purpose
This document provides a detailed breakdown of Procure-to-Pay (P2P) and Order-to-Cash (O2C) cycles in Oracle Fusion Financials, including:

- **Complete process flows and touchpoints**
- **Data structures and table relationships**
- **GL impact and financial reporting implications**
- **Integration points with other modules**
- **Mindmaps for visual process understanding**
- **Best practices and common configuration pitfalls**

### Document Metadata
| Field | Value |
|-------|-------|
| Created Date | May 30, 2026 |
| Version | 1.0 |
| Target System | Oracle Fusion Cloud Financials |
| Modules Covered | AP, AR, PO, Inventory, GL, SLA |

---

## PROCURE-TO-PAY (P2P) CYCLE {#p2p}

### Definition
P2P is the complete procurement lifecycle from supplier identification through payment, encompassing purchase requisitions, purchase orders, goods receipt, invoice matching, approval, and payment processing.

### Key Objectives
✓ Control spend and ensure compliance  
✓ Optimize supplier relationships  
✓ Ensure three-way matching (PO-Receipt-Invoice)  
✓ Minimize payment errors and duplicate invoices  
✓ Maintain audit trail for compliance  
✓ Maximize cash flow optimization through payment terms  

### P2P Process Flow - High Level

| Step | Process | Owner | Key Outcome |
|------|---------|-------|-------------|
| 1 | Requisition Creation | Requestor | Approval for purchase (Req ID) |
| 2 | Purchase Order (PO) Creation | Buyer | Formal commitment (PO Number) |
| 3 | Goods Receipt (GR) | Warehouse/Receiving | Receipt into inventory (GR ID) |
| 4 | Invoice Receipt | AP Clerk | Supplier invoice logged (Invoice ID) |
| 5 | Three-Way Match | System/AP | PO-GR-Invoice validation |
| 6 | Invoice Approval | Manager/Approver | Approved for payment |
| 7 | Payment Processing | Treasurer/AP | Check/ACH/Wire payment |
| 8 | Reconciliation | Accountant | Cash vs. AP cleared |

### P2P Mindmap Visualization

```
PROCURE-TO-PAY (P2P) CYCLE
│
├─ 1. REQUISITION PHASE
│  ├─ Create Purchase Requisition (PUR_REQ)
│  ├─ Approval Workflow (BPM)
│  └─ Requisition Line Items
│
├─ 2. PROCUREMENT PHASE
│  ├─ Create Purchase Order (PO) from Req
│  ├─ PO Header & Lines
│  ├─ Supplier Selection
│  ├─ Terms & Conditions
│  └─ PO Distribution (GL accrual accounts)
│
├─ 3. RECEIPT PHASE
│  ├─ Goods Receipt (Receiving)
│  ├─ Receipt Inspection
│  ├─ Quality Check (if configured)
│  ├─ Inventory Movement
│  └─ GL Impact: Debit Inventory/Asset, Credit Accrual
│
├─ 4. INVOICE PHASE
│  ├─ Invoice Data Entry (Manual/OCR/EDI)
│  ├─ Invoice Line Matching
│  ├─ Three-Way Validation
│  │  ├─ PO ↔ GR ↔ Invoice Match
│  │  └─ Variance Tolerance Check
│  ├─ Hold Rules Applied (if any)
│  └─ GL Impact: Debit COGS/Expense, Credit AP
│
├─ 5. APPROVAL PHASE
│  ├─ Approval Workflows (AMX Rules)
│  ├─ Manager Sign-off
│  ├─ Budget Availability Check
│  └─ Compliance Validation
│
├─ 6. PAYMENT PHASE
│  ├─ Payment Process Request (PPR)
│  ├─ Payment Method Selection (Check/ACH/Wire)
│  ├─ Discount Application (if early payment)
│  ├─ Withholding Tax Calculation
│  ├─ GL Impact: Debit AP, Credit Cash
│  └─ Payment Execution
│
└─ 7. RECONCILIATION PHASE
   ├─ Bank Reconciliation (Cash Mgmt)
   ├─ AP Aging Report
   ├─ Supplier Statement Reconciliation
   └─ Month-End Close
```

---

## ORDER-TO-CASH (O2C) CYCLE {#o2c}

### Definition
O2C is the complete revenue lifecycle from customer order creation through cash collection, encompassing sales orders, shipment, invoicing, revenue recognition, payment collection, and reconciliation.

### Key Objectives
✓ Streamline sales-to-collection process  
✓ Ensure accurate revenue recognition (ASC 606/IFRS 15)  
✓ Minimize Days Sales Outstanding (DSO)  
✓ Manage customer credit and collections  
✓ Maintain accurate receivables aging  
✓ Enable real-time cash forecasting  

### O2C Process Flow - High Level

| Step | Process | Owner | Key Outcome |
|------|---------|-------|-------------|
| 1 | Sales Order Creation | Sales/Order Entry | Customer order confirmed (SO #) |
| 2 | Credit Check | Credit Manager | Credit limit verification |
| 3 | Shipment | Warehouse/Logistics | Goods shipped (Shipment ID) |
| 4 | Invoice Generation | Billing/AR | AR Invoice created (Invoice #) |
| 5 | Revenue Recognition | Revenue/AR | Revenue posted to GL |
| 6 | Invoice Distribution | AR Clerk | Invoice sent to customer |
| 7 | Payment Receipt | Lockbox/AR | Cash received (Receipt #) |
| 8 | Collections | Collector | Follow-up on overdue amounts |
| 9 | Reconciliation | Accountant | AR cleared, DSO measured |

### O2C Mindmap Visualization

```
ORDER-TO-CASH (O2C) CYCLE
│
├─ 1. SALES ORDER PHASE
│  ├─ Customer Creation (CRM/AR)
│  ├─ Sales Order Entry
│  ├─ Order Lines (Item, Qty, Price)
│  ├─ Price List Application
│  └─ Order Booking
│
├─ 2. CREDIT & APPROVAL PHASE
│  ├─ Credit Limit Check
│  ├─ Credit Review (if flagged)
│  ├─ Approval Workflow
│  └─ Order Release
│
├─ 3. FULFILLMENT PHASE
│  ├─ Pick & Pack
│  ├─ Shipment Creation
│  ├─ Delivery/Receipt by Customer
│  ├─ Proof of Delivery (POD)
│  └─ GL Impact: Debit COGS, Credit Inventory
│
├─ 4. INVOICING PHASE
│  ├─ Invoice Auto-Generation from Shipment
│  ├─ Invoice Header & Lines
│  ├─ Tax Calculation
│  ├─ Revenue Schedule (if multi-period)
│  └─ GL Impact: Debit AR, Credit Revenue
│
├─ 5. REVENUE RECOGNITION PHASE
│  ├─ Performance Obligation Assessment (ASC 606)
│  ├─ Revenue Recognition Rules (SLA)
│  ├─ Deferred Revenue Handling (if applicable)
│  └─ GL Impact: Debit AR/Cash, Credit Revenue/Deferred Rev
│
├─ 6. COLLECTION PHASE
│  ├─ Invoice Delivery to Customer
│  ├─ Payment Terms Application
│  ├─ Discount Tracking (Early Pay)
│  ├─ Dunning Management (if overdue)
│  ├─ Lockbox Processing (if configured)
│  └─ Payment Receipt
│
├─ 7. CASH APPLICATION PHASE
│  ├─ Cash Received (Bank Deposit)
│  ├─ Auto-Matching to Invoice
│  ├─ Partial/Overpayment Handling
│  ├─ Discount Adjustment
│  └─ GL Impact: Debit Cash, Credit AR
│
├─ 8. COLLECTIONS PHASE
│  ├─ AR Aging Analysis
│  ├─ Dunning Notices
│  ├─ Write-offs (if uncollectible)
│  ├─ Credit Memo Processing
│  └─ GL Impact: Debit Bad Debt Expense/Write-off, Credit AR
│
└─ 9. RECONCILIATION PHASE
   ├─ AR Sub-Ledger to GL
   ├─ Cash Reconciliation
   ├─ DSO Calculation
   ├─ Aged Balance Reporting
   └─ Month-End Close
```

---

## DATA STRUCTURES {#data-structures}

### P2P DATA STRUCTURES - CORE TABLES

#### Purchasing Module (PO) - Key Tables

| Table Name | Key Fields | Purpose |
|------------|-----------|---------|
| PO_HEADERS_ALL | PO_HEADER_ID, PO_NUMBER, VENDOR_ID, PO_DATE | Master PO header records |
| PO_LINES_ALL | PO_LINE_ID, PO_HEADER_ID, ITEM_ID, QUANTITY, UNIT_PRICE | PO line items |
| PO_DISTRIBUTIONS | PO_DISTRIBUTION_ID, PO_LINE_ID, ACCOUNT, QTY_ORDERED | GL distribution for encumbrance |
| RCV_TRANSACTIONS | TRANSACTION_ID, PO_LINE_ID, QUANTITY_RECEIVED | Goods receipt transactions |
| RCV_SHIPMENT_HEADERS | SHIPMENT_HEADER_ID, PO_HEADER_ID, RECEIPT_DATE | Shipment header |
| RCV_SHIPMENT_LINES | SHIPMENT_LINE_ID, PO_LINE_ID, QUANTITY_SHIPPED | Individual shipment lines |

#### Accounts Payable Module (AP) - Key Tables

| Table Name | Key Fields | Purpose |
|------------|-----------|---------|
| AP_INVOICES_ALL | INVOICE_ID, INVOICE_NUM, VENDOR_ID, INVOICE_DATE | Supplier invoices |
| AP_INVOICE_LINES_ALL | INVOICE_LINE_ID, INVOICE_ID, LINE_TYPE_LOOKUP_CODE | Invoice line items |
| AP_INVOICE_DISTRIBUTIONS_ALL | INVOICE_DISTRIBUTION_ID, INVOICE_ID, DIST_CODE_COMBINATION_ID | GL distribution for expenses |
| AP_MATCHING_SETS | MATCHING_SET_OPTION_ID, PO_ID, RCV_ID, INV_ID | 3-way match validation |
| AP_HOLDS | HOLD_ID, INVOICE_ID, HOLD_REASON | Invoice holds/exceptions |
| AP_PAYMENT_SCHEDULES_ALL | PAYMENT_NUM, INVOICE_ID, DUE_DATE | Payment terms schedule |
| AP_SUPPLIERS | VENDOR_ID, VENDOR_NAME, VENDOR_TYPE_LOOKUP_CODE | Supplier master data |

#### GL Impact - P2P Transaction Flow

| Step | GL Entry | Debit Account | Credit Account | Amount |
|------|----------|---------------|-----------------|--------|
| PO Created (Encumbrance) | Accrual | Encumbrance Liability | Encumbrance Asset | PO Value |
| Goods Receipt | Accrual Reversal + Asset | Inventory/Asset | Accrual Liability | GR Value |
| Invoice Receipt | Expense Recognition | COGS/Expense/Asset | AP Payable | Invoice Value |
| Payment | Cash Out | AP Payable | Cash/Bank | Payment Amount |
| Variance Adjustment | Correction | COGS Variance | AP Payable | Variance Amount |

---

### O2C DATA STRUCTURES - CORE TABLES

#### Sales Order Module (OM) - Key Tables

| Table Name | Key Fields | Purpose |
|------------|-----------|---------|
| ONT_ORDER_HEADERS_ALL | ORDER_ID, ORDER_NUMBER, CUSTOMER_ID, ORDER_DATE | Master sales order |
| ONT_ORDER_LINES_ALL | LINE_ID, ORDER_ID, INVENTORY_ITEM_ID, ORDERED_QUANTITY | Sales order lines |
| WSH_DELIVERY_DETAILS | DELIVERY_DETAIL_ID, LINE_ID, SHIPPED_QUANTITY | Shipment line details |
| WSH_DELIVERY_ASSIGNMENTS | DELIVERY_ASSIGNMENT_ID, DELIVERY_ID, PICKUP_STOP_ID | Delivery logistics |
| ONT_ORDER_HOLDS | HOLD_ID, ORDER_ID, HOLD_REASON | Order holds (credit, etc) |
| AR_CUSTOMERS | CUST_ACCOUNT_ID, CUSTOMER_NAME, PARTY_ID | Customer master data |

#### Accounts Receivable Module (AR) - Key Tables

| Table Name | Key Fields | Purpose |
|------------|-----------|---------|
| RA_CUSTOMER_TRX_ALL | CUSTOMER_TRX_ID, TRX_NUMBER, CUSTOMER_ID, TRX_DATE | AR invoices/transactions |
| RA_CUSTOMER_TRX_LINES_ALL | CUSTOMER_TRX_LINE_ID, CUSTOMER_TRX_ID, LINE_NUMBER | Invoice line items |
| RA_CUST_TRX_LINE_GL_DIST_ALL | CUST_TRX_LINE_GL_DIST_ID, TRX_LINE_ID, CODE_COMBINATION_ID | GL distribution |
| RA_CUSTOMER_RECEIPT_ALL | CASH_RECEIPT_ID, RECEIPT_NUMBER, CUSTOMER_ID, RECEIPT_DATE | Cash receipts |
| AR_RECEIVABLE_APPLICATIONS_ALL | RECEIVABLE_APPLICATION_ID, CASH_RECEIPT_ID, CUSTOMER_TRX_ID | Match receipt to invoice |
| AR_CUSTOMERS_TRX_SUMMARY | CUSTOMER_TRX_SUMMARY_ID, CUSTOMER_ID, CUST_ACCOUNT_ID | Customer AR summary |
| HZ_CUST_ACCOUNTS | CUST_ACCOUNT_ID, ACCOUNT_NUMBER, CUSTOMER_CLASS_CODE | Customer account hierarchy |

#### GL Impact - O2C Transaction Flow

| Step | GL Entry | Debit Account | Credit Account | Amount |
|------|----------|---------------|-----------------|--------|
| Sales Order Created | None | None | None | None (memo only) |
| Shipment | COGS Recognition | COGS of Goods Sold | Finished Goods Inventory | COGS Value |
| Invoice Generated | Revenue Recognition | AR Receivable | Revenue/Sales | Invoice Amount |
| Revenue Recognition | Revenue Accrual | Deferred Revenue / AR | Revenue (when service delivered) | Rev Recognition Amt |
| Cash Receipt | Cash In | Cash/Bank | AR Receivable | Payment Amount |
| Bad Debt Writeoff | Provision | Bad Debt Expense | AR Receivable | Writeoff Amount |

---

## INTEGRATION POINTS {#integration}

### Cross-Module Dependencies

| Integration Point | P2P Module | O2C Module | Business Impact |
|------------------|-----------|-----------|-----------------|
| Inventory Movement | Receipt (GR) | Shipment | GL COGS posting synchronized |
| GL Posting | AP Invoice Distribution | AR Revenue Distribution | Period close dependent |
| Payment Terms | AP Payment Schedule | AR Payment Terms | DSO vs. DPO optimization |
| Customer-Supplier | Supplier Master | Customer Master | Intercompany transactions |
| Subledger Accounting | SLA for P2O Accruals | SLA for Revenue Recognition | Automated GL derivation |
| Withholding Tax | AP Withholding Tax Calc | N/A | Tax compliance & GL posting |
| Multi-Org Transactions | Intercompany PO | Intercompany Sales Order | Consolidated reporting |

### System Integration Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ORACLE FUSION FINANCIALS                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌─ PROCUREMENT (P2P) ────────────────────────────────────────────┐ │
│  │ Requisition → PO → Receipt → Invoice → Approval → Payment     │ │
│  │    ↓           ↓       ↓        ↓         ↓          ↓        │ │
│  │   REQ      PO_HDR  RCV_TXN  AP_INV   AP_HOLD    AP_PMNT      │ │
│  │    ↓           ↓       ↓        ↓         ↓          ↓        │ │
│  │  GL: Encumb → Accrual → Inventory → Expense → AP Liability  │ │
│  └────────────────────────────────────────────────────────────────┘ │
│              ↓                                           ↓            │
│         SUBLEDGER ACCOUNTING (SLA) RULES               CASH MGMT     │
│              ↓                                           ↓            │
│  ┌─ GENERAL LEDGER ──────────────────────────────────────────────┐ │
│  │   Assets | Liabilities | Equity | Revenue | Expenses | Cash │ │
│  │                                                               │ │
│  │   1000: Cash          │  2000: AP Payable   │ 5000: COGS    │ │
│  │   1100: AR Receivable │  3000: Revenue     │ 5100: OpEx    │ │
│  │   1200: Inventory     │  Deferred Revenue  │ 8000: Allocation
│  └───────────────────────────────────────────────────────────────┘ │
│              ↓                                           ↓            │
│         FINANCIAL REPORTING                     BANK RECONCILIATION  │
│              ↓                                           ↓            │
│  ┌─ SALES (O2C) ──────────────────────────────────────────────────┐ │
│  │ Sales Order → Credit Check → Shipment → Invoice → Collection │ │
│  │     ↓            ↓            ↓          ↓           ↓       │ │
│  │   SO_HDR      OM_HOLD    WSHT_DELIVERY  RA_INV    AR_RCPT   │ │
│  │     ↓            ↓            ↓          ↓           ↓       │ │
│  │  GL: None → No Accrual → COGS → Revenue → Cash Received    │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## CONTROL POINTS {#controls}

### P2P Control Framework

| Control Name | Trigger Point | Purpose | Owner |
|------------|---------------|---------|-------|
| 3-Way Matching | Invoice Receipt | Prevent overpayment | AP |
| Approval Workflow | Invoice Amount > Threshold | Segregation of Duties | Manager |
| Hold Rules | Invoice Entry | Vendor Quality/On-time, Budget available | AP/Finance |
| Variance Tolerance | Match Variance | Allow small PO-Invoice variance | Finance |
| Duplicate Check | Invoice Number | Prevent duplicate payments | AP |
| Supplier Validation | Invoice Entry | Ensure active/approved supplier | Procurement |
| Encumbrance Check | PO Release | Prevent over-commitment | Budget Control |
| Withholding Tax | Payment | Tax compliance & GL posting | Tax/AP |

### O2C Control Framework

| Control Name | Trigger Point | Purpose | Owner |
|------------|---------------|---------|-------|
| Credit Limit Check | Sales Order Entry | Prevent exceeding credit exposure | Credit Mgmt |
| Price Validation | Order Line Entry | Prevent unauthorized pricing | Sales Ops |
| Revenue Recognition | Invoice/Shipment | ASC 606/IFRS 15 Compliance | Revenue/AR |
| Invoice Accuracy | Invoice Generation | Ensure correct billing amounts | Billing |
| Collections Aging | AR Aging Report | Monitor DSO, trigger collection action | Collections |
| Discount Validation | Cash Receipt | Prevent unauthorized discounts | AR |
| Write-off Approval | Bad Debt | Prevent unauthorized write-offs | AR Manager |
| Reconciliation | Period End | GL ↔ AR Sub-ledger match | Accountant |

---

## KEY PERFORMANCE INDICATORS (KPIs) {#kpis}

### P2P KPIs

| KPI | Formula | Target | Owner |
|----|---------|--------|-------|
| Purchase Order Cycle Time | Days: PO Created → Invoice | ≤ 10 days | Procurement |
| 3-Way Match Rate | Matched Invoices / Total Invoices | ≥ 95% | AP |
| Invoice Processing Cost | AP Salaries / Number Invoices | ≤ $5/invoice | AP Manager |
| Payment Discount Capture | Discounts Taken / Available | ≥ 80% | Treasurer |
| Duplicate Invoice Rate | Duplicate Invoices / Total | ≤ 0.5% | AP |
| Days Payable Outstanding (DPO) | AP Balance / Daily COGS | 45-60 days | Treasury |
| Variance Rate | PO-Invoice Variances / Total | ≤ 1% | Finance |
| Supplier On-Time Performance | On-Time Receipts / Total | ≥ 95% | Procurement |

### O2C KPIs

| KPI | Formula | Target | Owner |
|----|---------|--------|-------|
| Order Cycle Time | Days: SO → Shipment → Invoice | ≤ 5 days | Sales Ops |
| Cash Conversion Cycle | DIO + DSO - DPO | ≤ 30 days | CFO |
| Days Sales Outstanding (DSO) | AR Balance / Daily Revenue | 30-45 days | AR Manager |
| Invoice Accuracy | Correct Invoices / Total | ≥ 99% | Billing |
| Collection Rate | Cash Collected / Invoiced | ≥ 95% | Collections |
| Credit Limit Utilization | AR / Credit Limit | 60-80% | Credit Mgmt |
| Bad Debt % Revenue | Bad Debt Expense / Revenue | ≤ 2% | AR Manager |
| Order Fulfillment Rate | Fulfilled Orders / Total | ≥ 98% | Warehouse |

---

## CONFIGURATION GUIDE {#configuration}

### Common P2P Pitfalls & Solutions

**1. Three-Way Matching Failures**
- **Problem:** Frequent unmatched invoices due to quantity/price variances
- **Solution:** Configure variance tolerance thresholds (e.g., allow ±2% quantity variance)
- **Config:** Setup & Maintenance > Manage Matching Options

**2. Duplicate Invoice Detection**
- **Problem:** Same invoice posted multiple times
- **Solution:** Enable duplicate invoice check on invoice date + amount + vendor
- **Config:** Setup & Maintenance > Manage Duplicate Invoice Options

**3. Encumbrance Not Clearing**
- **Problem:** PO encumbrance remains even after invoice payment
- **Solution:** Ensure PO Distribution GL accounts align with invoice GL derivation (SLA)
- **Config:** Verify SLA rules derive to correct GL accounts

**4. Payment Discount Not Captured**
- **Problem:** Early payment discounts not automatically applied
- **Solution:** Configure discount terms in AP and validate discount GL accounts
- **Config:** Setup & Maintenance > Manage Payment Terms

**5. Hold Rules Not Triggering**
- **Problem:** Invoices should be on hold but are not
- **Solution:** Verify hold rule conditions (supplier type, amount threshold, etc.)
- **Config:** Setup & Maintenance > Manage Holds Rules

### Common O2C Pitfalls & Solutions

**1. Revenue Recognition Timing Issues**
- **Problem:** Revenue recognized in wrong period (ASC 606 non-compliance)
- **Solution:** Configure revenue recognition rules to trigger on shipment or invoice date
- **Config:** Setup & Maintenance > Manage Revenue Recognition Rules

**2. AR-GL Reconciliation Variance**
- **Problem:** AR sub-ledger doesn't match GL balance
- **Solution:** Verify all RA transactions post through SLA to GL
- **Config:** Run AR-GL Reconciliation Report; investigate open items

**3. Customer Credit Limit Not Enforced**
- **Problem:** Orders bypass credit limit check
- **Solution:** Enable credit hold on SO entry; configure credit rules
- **Config:** Setup & Maintenance > Manage Credit Rules

**4. Lockbox Not Auto-Matching Cash**
- **Problem:** Cash received but not applied to invoices automatically
- **Solution:** Configure lockbox matching rules (PO #, Invoice #, customer ID)
- **Config:** Setup & Maintenance > Manage Lockbox Auto-Matching Rules

**5. Bad Debt Provision Not Calculating**
- **Problem:** Aging > 90 days not triggering bad debt accrual
- **Solution:** Configure bad debt aging rules and run provision batch
- **Config:** Setup & Maintenance > Manage Bad Debt Aging Rules

---

## BEST PRACTICES {#best-practices}

### ✓ P2P Best Practices
1. **Enforce 3-way matching** - Never bypass PO-GR-Invoice validation
2. **Leverage SLA rules** - Auto-derive GL accounts to reduce manual error
3. **Monitor encumbrances** - Close month-end with zero encumbrance balance
4. **Capture early pay discounts** - CFO typically wants 50% capture rate minimum
5. **Centralize holds** - Use hold rules instead of manual review
6. **Implement duplicate checks** - Prevent vendor fraud and overpayments
7. **Regular vendor statement reconciliation** - Catch AP errors early
8. **DPO optimization** - Balance supplier relationships with cash flow

### ✓ O2C Best Practices
1. **Revenue recognition compliance** - Implement ASC 606 properly from day one
2. **Credit policy enforcement** - Prevent bad debt by enforcing credit limits
3. **DSO management** - Target industry-standard DSO (typically 30-45 days)
4. **Lockbox automation** - Reduce days to cash through automated matching
5. **Collection process discipline** - Escalate past-due > 30 days immediately
6. **Bad debt provisioning** - Monthly reserve for high-risk receivables
7. **Customer master governance** - Prevent duplicate customers, maintain data quality
8. **AR-GL reconciliation** - Perform weekly, not just month-end

### ✓ Integrated Process Best Practices
1. **SLA Rule Excellence** - Invest time in SLA configuration; it eliminates 80% of manual GL effort
2. **GL Chart Clarity** - Segment accounts by product/function/BU for better reporting
3. **Workflow Standardization** - Use AMX rules to enforce consistent approval logic
4. **KPI Monitoring** - Track DSO, DPO, and cycle times weekly, not quarterly
5. **Period Close Synchronization** - P2P and O2C close windows should be coordinated
6. **Data Quality** - Invest in data validation rules; garbage in = garbage out
7. **Training & Documentation** - Well-trained users reduce downstream support costs
8. **Continuous Improvement** - Review process metrics quarterly; iterate on rules

### Process Maturity Roadmap

**LEVEL 1 (Manual & Reactive):**
- Manual invoice entry & GL posting
- No 3-way matching automation
- Month-end close = 15+ days
- High AR DSO (60+ days), High AP DPO volatility

**LEVEL 2 (Systematic & Documented):**
- Automated 3-way matching
- Basic SLA rules for GL posting
- Standardized workflows (approval rules)
- Month-end close = 10-12 days
- DSO trend improving, DPO optimizing

**LEVEL 3 (Optimized & Integrated):**
- Full automation: Lockbox, OCR, E-invoicing
- Advanced SLA mapping (multi-dimensional)
- Real-time KPI dashboards
- Month-end close = 5-7 days
- Industry-leading DSO & DPO

**LEVEL 4 (Predictive & Autonomous):**
- Predictive analytics for bad debt, cash forecasting
- Machine learning for invoice exception detection
- Real-time GL consolidation
- Continuous close capabilities
- Strategic partnerships: supplier portals, EDI, API integrations

---

## MONTH-END CLOSE CHECKLIST

### P2P Month-End Close Activities
- [ ] Reconcile AP Sub-ledger to GL
- [ ] Review Outstanding Invoices & Accruals
- [ ] Process Unmatched Receipts (Accrual)
- [ ] Review & Clear AP Holds
- [ ] Process Final Invoices & Payments
- [ ] Reconcile Vendor Statements
- [ ] Review Expense Allocations
- [ ] Validate Withholding Tax Accruals
- [ ] GL period close certification

### O2C Month-End Close Activities
- [ ] Reconcile AR Sub-ledger to GL
- [ ] Review AR Aging & Collections
- [ ] Revenue Recognition Analysis (ASC 606)
- [ ] Process Revenue Accruals/Deferrals
- [ ] Bad Debt Provision Review
- [ ] Reconcile Customer Statements
- [ ] Clear Unmatched Cash
- [ ] Validate Payment Terms Impact
- [ ] GL period close certification

---

**Document End**  
Version 1.0 | Created: May 30, 2026 | Oracle Fusion Financials
