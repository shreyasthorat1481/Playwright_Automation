
from playwright.sync_api import Page, expect
import re


class ContractQueryDesk:

    def __init__(self, page: Page):
        self.page = page

    # LOCATORS

    @property
    def apps_menu(self):
        return self.page.locator(
            ".pb-1 > .cursor-pointer"
        ).first

    @property
    def search_box(self):
        return self.page.get_by_role(
            "textbox",
            name="Search"
        )

    @property
    def discover_button(self):
        return self.page.get_by_role(
            "button",
            name="Discover now"
        ).first

    @property
    def launch_button(self):
        return self.page.get_by_role(
            "button",
            name="Launch"
        )

    @property
    def contracts_menu(self):
        return self.page.locator(
            "li:nth-child(2) > .cursor-pointer"
        )

    @property
    def select_all_contracts(self):
        return self.page.get_by_role(
            "checkbox",
            name="Select all contracts"
        )

    @property
    def auto_renewal_button(self):
        return self.page.get_by_role(
            "button",
            name="Auto-renewal & notice window",
            exact=True
        )

    @property
    def open_filters_button(self):
        return self.page.get_by_role(
            "button",
            name="Open filters"
        )

    # DASHBOARD CARD LOCATORS

    @property
    def total_contracts_label(self):
        return self.page.get_by_text(
            "Total Contracts",
            exact=True
        )

    @property
    def annual_recurring_revenue_label(self):
        return self.page.get_by_text(
            "Annual Recurring Revenue (ARR)",
            exact=True
        )

    @property
    def renewal_at_risk_label(self):
        return self.page.get_by_text(
            "Renewal At Risk",
            exact=True
        )

    # CONTRACT FLOW LOCATORS

    @property
    def contracts_in_scope_files(self):
        return self.page.get_by_text(
            "Contracts in Scope Files",
            exact=True
        )

    @property
    def renewals(self):
        return self.page.get_by_text(
            "Renewals",
            exact=True
        )

    @property
    def auto_renewal_section(self):
        return self.page.get_by_role(
            "complementary"
        ).locator("div").filter(
            has_text="Auto-renewal & notice window"
        ).nth(3)

    @property
    def query_result(self):
        return self.page.get_by_text(
            "Query result",
            exact=True
        )

    @property
    def auto_renewal_contract(self):
        return self.page.get_by_text(
            "Auto-renewal & notice windowAirrived_Cascade-Health-Systems_Subscription-",
            exact=False
        )

    # SUMMARY LOCATORS

    @property
    def summary_button(self):
        return self.page.get_by_text(
            "Summary",
            exact=True
        )

    @property
    def summary_of_files_button(self):
        return self.page.get_by_role(
            "button",
            name="Summary of files",
            exact=True
        )

    @property
    def summary_of_files_text(self):
        return self.page.get_by_text(
            "Summary of files",
            exact=True
        )

    @property
    def summary_of_files_agreement(self):
        return self.page.get_by_text(
            "Summary of filesAirrived_Cascade-Health-Systems_Subscription-Agreement_2025.",
            exact=False
        )


    # GENERAL ACTIONS

    def open_home_page(self):

        self.page.goto(
            "https://acme.ui.dev.airrived.ai/home",
            wait_until="domcontentloaded",
            timeout=60000
        )

    def open_apps(self):

        expect(
            self.apps_menu
        ).to_be_visible(timeout=60000)

        self.apps_menu.click()

    def search_contract_query_desk(self):

        expect(
            self.search_box
        ).to_be_visible(timeout=60000)

        self.search_box.click()

        self.search_box.fill(
            "contract query desk"
        )

    def discover_contract_query_desk(self):

        expect(
            self.discover_button
        ).to_be_visible(timeout=30000)

        self.discover_button.click()

    def launch_contract_query_desk(self):

        expect(
            self.launch_button
        ).to_be_visible(timeout=30000)

        self.launch_button.click()

    # DASHBOARD VALIDATIONS

    def verify_total_contracts(self):
        expect(
            self.total_contracts_label
        ).to_be_visible(timeout=60000)

        value = self.total_contracts_label.locator(
            "xpath=preceding-sibling::*[1]"
        )

        expect(
            value
        ).to_have_text(
            re.compile(r"^\d+$")
        )

    def verify_annual_recurring_revenue(self):
        expect(
            self.annual_recurring_revenue_label
        ).to_be_visible(timeout=60000)

        value = self.annual_recurring_revenue_label.locator(
            "xpath=preceding-sibling::*[1]"
        )

        expect(
            value
        ).to_have_text(
            re.compile(
                r"^\$?\d+(?:\.\d+)?[KMB]?$"
            )
        )

    def verify_renewal_at_risk(self):
        expect(
            self.renewal_at_risk_label
        ).to_be_visible(timeout=60000)

        value = self.renewal_at_risk_label.locator(
            "xpath=preceding-sibling::*[1]"
        )

        expect(
            value
        ).to_have_text(
            re.compile(r"^\d+$")
        )

    def verify_dashboard_kpis(self):


        self.verify_total_contracts()

        self.verify_annual_recurring_revenue()

        self.verify_renewal_at_risk()

    # CONTRACTS

    def open_contracts(self):

        expect(
            self.contracts_menu
        ).to_be_visible(timeout=60000)

        self.contracts_menu.click()

    def select_all_contracts_checkbox(self):

        expect(
            self.select_all_contracts
        ).to_be_visible(timeout=60000)

        self.select_all_contracts.click()

    # AUTO RENEWAL

    def open_auto_renewal(self):

        expect(
            self.auto_renewal_button
        ).to_be_visible(timeout=60000)

        self.auto_renewal_button.click()

        contract_text = self.page.get_by_text(
            "Airrived_Cascade-Health-Systems_Subscription-",
            exact=False
        )

        expect(
            contract_text
        ).to_be_visible(timeout=60000)

        contract_text.click()


    # CONTRACTS IN SCOPE FILES

    def open_contracts_in_scope_files(self):

        expect(
            self.contracts_in_scope_files
        ).to_be_visible(timeout=60000)

        self.contracts_in_scope_files.click()

    def open_renewals(self):

        expect(
            self.renewals
        ).to_be_visible(timeout=60000)

        self.renewals.click()

    def open_auto_renewal_section(self):

        expect(
            self.auto_renewal_section
        ).to_be_visible(timeout=60000)

        self.auto_renewal_section.click()

    def open_query_result(self):

        expect(
            self.query_result
        ).to_be_visible(timeout=60000)

        self.query_result.click()

    def open_auto_renewal_contract(self):

        expect(
            self.auto_renewal_contract
        ).to_be_visible(timeout=60000)

        self.auto_renewal_contract.click()

    # SUMMARY

    def open_summary(self):

        expect(
            self.summary_button
        ).to_be_visible(timeout=60000)

        self.summary_button.click()

    def open_first_summary_of_files(self):

        expect(
            self.summary_of_files_button
        ).to_be_visible(timeout=60000)

        self.summary_of_files_button.click()

    def open_second_summary_of_files(self):

        summary_text = self.summary_of_files_text

        expect(
            summary_text.nth(1)
        ).to_be_visible(timeout=60000)

        summary_text.nth(1).click()

    def open_summary_of_files_agreement(self):

        expect(
            self.summary_of_files_agreement
        ).to_be_visible(timeout=60000)

        self.summary_of_files_agreement.click()

    # FILTERS

    def open_filters(self):

        expect(
            self.open_filters_button
        ).to_be_visible(timeout=60000)

        self.open_filters_button.click()

        status_filter = self.page.get_by_text(
            "StatusAllNASourceAllMicrosoft"
        )

        expect(
            status_filter
        ).to_be_visible(timeout=60000)

        status_filter.click()