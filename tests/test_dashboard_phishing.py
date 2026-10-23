from playwright.sync_api import Page, expect

from apps.phishing.dashboard_page import PhishingDashboardPage
from pages.login_page import LoginPage


def test_phishing_dashboard(page: Page):

    login_page = LoginPage(page)
    phishing_page = PhishingDashboardPage(page)

    # Login
    login_page.open_login_page()
    login_page.login(
        "johndoe@airrived.ai",
        "GJ39qZ$K@nL99S8"
    )

    # Open the Apps page and search for the phishing app
    phishing_page.open_home_page()
    phishing_page.open_apps()
    phishing_page.search_phishing_app()

    # Select the Phishing app
    phishing_page.open_phishing_app()

    # Click the app's primary action button
    phishing_page.click_app_primary_action()

    # Launch the app
    phishing_page.launch_app()

    # Verify that the dashboard is visible
    expect(
        phishing_page.phishing_summary_section
    ).to_be_visible(timeout=60000)

    # Verify dashboard data
    phishing_page.verify_dashboard_data()