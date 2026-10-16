
from playwright.sync_api import Page

from apps.phishing.dashboard_page import PhishingDashboardPage
from pages.login_page import LoginPage


def test_phishing_dashboard(page: Page):

    # 1. Create page objects
    login_page = LoginPage(page)
    phishing_page = PhishingDashboardPage(page)

    # 2. Login
    login_page.open_login_page()
    login_page.login(
        "johndoe@airrived.ai",
        "GJ39qZ$K@nL99S8"
    )

    # 3. Open Phishing app
    phishing_page.open_home_page()
    phishing_page.open_apps()
    phishing_page.search_phishing_app()

    # 4. Discover and launch the app
    phishing_page.open_phishing_app()

    # 5. Open dashboard and validate data
    phishing_page.open_dashboard_preview()
    phishing_page.verify_dashboard_data()
