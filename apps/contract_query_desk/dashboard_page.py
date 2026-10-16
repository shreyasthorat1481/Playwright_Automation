
import re

from playwright.sync_api import Page, expect


class ContractQueryDeskDashboardPage:

    def __init__(self, page: Page):
        self.page = page

    # =====================================================
    # APP NAVIGATION LOCATORS
    # =====================================================

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

    # =====================================================
    # DASHBOARD KPI LOCATORS
    # =====================================================

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

    # =====================================================
    # APP NAVIGATION ACTIONS
    # =====================================================

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

    # =====================================================
    # DASHBOARD KPI VALIDATIONS
    # =====================================================

    def verify_total_contracts(self):
        expect(
            self.total_contracts_label
        ).to_be_visible(timeout=60000)

        value = self.total_contracts_label.locator(
            "xpath=preceding-sibling::*[1]"
        )

        expect(value).to_have_text(
            re.compile(r"^\d+$")
        )

    def verify_annual_recurring_revenue(self):
        expect(
            self.annual_recurring_revenue_label
        ).to_be_visible(timeout=60000)

        value = self.annual_recurring_revenue_label.locator(
            "xpath=preceding-sibling::*[1]"
        )

        expect(value).to_have_text(
            re.compile(r"^\$?\d+(?:\.\d+)?[KMB]?$")
        )

    def verify_renewal_at_risk(self):
        expect(
            self.renewal_at_risk_label
        ).to_be_visible(timeout=60000)

        value = self.renewal_at_risk_label.locator(
            "xpath=preceding-sibling::*[1]"
        )

        expect(value).to_have_text(
            re.compile(r"^\d+$")
        )

    def verify_dashboard_kpis(self):
        self.verify_total_contracts()
        self.verify_annual_recurring_revenue()
        self.verify_renewal_at_risk()
