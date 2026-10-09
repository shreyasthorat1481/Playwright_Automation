from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.contract_query_desk import ContractQueryDesk


def test_contract_query_desk(page: Page):

    login_page = LoginPage(page)
    contract_page = ContractQueryDesk(page)

    login_page.open_login_page()

    login_page.login(
        "johndoe@airrived.ai",
        "GJ39qZ$K@nL99S8"
    )

    # APPS

    contract_page.open_apps()
    contract_page.search_contract_query_desk()
    contract_page.discover_contract_query_desk()
    contract_page.launch_contract_query_desk()

    # DASHBOARD  VALIDATIOn

    contract_page.verify_dashboard_kpis()

    # CONTRACTS

    contract_page.open_contracts()
    contract_page.select_all_contracts_checkbox()
    contract_page.open_auto_renewal()

    # CONTRACTS IN SCOPE FILES

    contract_page.open_contracts_in_scope_files()
    contract_page.select_all_contracts_checkbox()
    contract_page.open_renewals()
    contract_page.open_auto_renewal_section()
    contract_page.open_query_result()
    contract_page.open_auto_renewal_contract()

    # SUMMARY

    contract_page.open_summary()
    contract_page.open_first_summary_of_files()
    contract_page.open_second_summary_of_files()
    contract_page.open_summary_of_files_agreement()

    # FILTER
    contract_page.open_filters()