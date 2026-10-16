
from apps.contract_query_desk.login_page import LoginPage
from apps.contract_query_desk.dashboard_page import (ContractQueryDeskDashboardPage)
from apps.contract_query_desk.list_page import (ContractQueryDeskListPage)


def test_contract_query_desk(page):

    login_page = LoginPage(page)
    dashboard_page = ContractQueryDeskDashboardPage(page)
    list_page = ContractQueryDeskListPage(page)

    login_page.open_login_page()
    login_page.login("johndoe@airrived.ai", "GJ39qZ$K@nL99S8")

    dashboard_page = ContractQueryDeskDashboardPage(page)
    list_page = ContractQueryDeskListPage(page)


    dashboard_page.open_home_page()
    dashboard_page.open_apps()
    dashboard_page.search_contract_query_desk()
    dashboard_page.discover_contract_query_desk()
    dashboard_page.launch_contract_query_desk()

    dashboard_page.verify_dashboard_kpis()
    list_page.open_list_view()

    list_page.open_contracts()
    list_page.select_all_contracts_checkbox()

    list_page.open_auto_renewal()

    list_page.open_contracts_in_scope_files()
    list_page.open_renewals()
    list_page.open_auto_renewal_section()
    list_page.open_query_result()
    list_page.open_auto_renewal_contract()

    list_page.open_summary()
    list_page.open_first_summary_of_files()
    list_page.open_second_summary_of_files()
    list_page.open_summary_of_files_agreement()

    list_page.open_filters()
