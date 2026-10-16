
from playwright.sync_api import Page, expect

from apps.phishing.dashboard_page import PhishingDashboardPage
from pages.login_page import LoginPage


def test_phishing_dashboard(page: Page):

    login_page = LoginPage(page)
    phishing_page = PhishingDashboardPage(page)

    login_page.open_login_page()

    login_page.login(
        "johndoe@airrived.ai",
        "GJ39qZ$K@nL99S8"
    )

    phishing_page.open_home_page()
    phishing_page.open_apps()
    phishing_page.search_phishing_app()

    phishing_page.open_phishing_app()

    phishing_page.open_dashboard_preview()

    expect(
        phishing_page.phishing_summary_section
    ).to_be_visible(timeout=60000)

    phishing_page.verify_dashboard_data()
