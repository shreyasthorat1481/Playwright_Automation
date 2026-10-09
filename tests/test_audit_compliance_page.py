from playwright.sync_api import Page

from pages.audit_compliance_page import AuditCompliancePage



def test_audit_compliance_dashboard(page: Page):

    page.goto("https://acme.ui.dev.airrived.ai/audit")
    audit_page = AuditCompliancePage(page)
    audit_page.expect_complete_dashboard()

    