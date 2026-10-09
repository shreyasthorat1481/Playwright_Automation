from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.observable import ObservablePage


def test_observable(page: Page):

    # LOGIN
    login_page = LoginPage(page)
    observable_page = ObservablePage(page)

    login_page.open_login_page()

    login_page.login(
        "johndoe@airrived.ai",
        "GJ39qZ$K@nL99S8"
    )

    # OPEN APPS
    observable_page.open_apps()

    # SEARCH OBSERVABLE APP
    observable_page.search_observable()
    observable_page.search_observable_again()


    # OPEN OBSERVABLE APP
    observable_page.open_observable_app()

    # DISCOVER
    observable_page.discover_observable()

    # LAUNCH
    observable_page.launch_observable()

    # OPEN TEXT INTERFACE
    observable_page.open_text_interface()
    observable_page.select_text_tab()

    # TEST DATA
    observable_text = """
    Tata Marcopolo is an Indian automobile manufacturing company.
    Website: WWW.TATA.COM
    IP: 1.129.39.1
    """

    observable_page.enter_observable_text(
        observable_text
    )

    # SUBMIT
    observable_page.submit_text()

    # IOC OVERVIEW
    observable_page.open_iocs_overview()
    observable_page.verify_hash()
    observable_page.verify_ip()
    observable_page.verify_url()
    observable_page.verify_domain()

    # PROVIDER DETAILS
    observable_page.open_provider_details()

    # VERDICT DETAILS
    observable_page.open_verdict_details()

    # IOC DETAILS
    observable_page.open_iocs_details()
    observable_page.open_domain_details()
    observable_page.open_ip_details()