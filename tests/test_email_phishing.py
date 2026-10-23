
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from apps.phishing.email_management_page import EmailManagementPage


def test_email_management(page: Page):

    login_page = LoginPage(page)
    email_page = EmailManagementPage(page)

    login_page.open_login_page()
    login_page.login(
        "johndoe@airrived.ai",
        "GJ39qZ$K@nL99S8"
    )

    page.goto(
        "https://acme.ui.dev.airrived.ai/apps?appId=7340&view=email-management&agentId=49",
        wait_until="domcontentloaded",
        timeout=60000
    )

    email_page.open_email_management()

    email_page.open_first_phishing_email()

    email_page.verify_summary_section()

    email_page.verify_email_detail_buttons()

    email_page.verify_email_preview()

    email_page.verify_email_headers()

    email_page.verify_observables()

    email_page.verify_remediation()

    email_page.verify_conversational_ai()

    print("Email Management test completed successfully.")
