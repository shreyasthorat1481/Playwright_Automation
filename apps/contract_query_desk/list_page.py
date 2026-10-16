
from playwright.sync_api import Page, expect


class ContractQueryDeskListPage:

    def __init__(self, page: Page):
        self.page = page

    # LIST ICON LOCATOR

    @property
    def list_button(self):
        return self.page.locator(
            "li:nth-child(2) > .cursor-pointer"
        )

    # =====================================================
    # CONTRACT LOCATORS
    # =====================================================

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

    # =====================================================
    # CONTRACT FLOW LOCATORS
    # =====================================================

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
            "Auto-renewal & notice window"
            "Airrived_Cascade-Health-Systems_Subscription-",
            exact=False
        )

    # =====================================================
    # SUMMARY LOCATORS
    # =====================================================

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
            "Summary of files"
            "Airrived_Cascade-Health-Systems_Subscription-Agreement_2025.",
            exact=False
        )

    # =====================================================
    # LIST VIEW ACTION
    # =====================================================

    # OPEN LIST VIEW

    def open_list_view(self):
        expect(
            self.list_button
        ).to_be_visible(timeout=60000)

        self.list_button.click()

    # =====================================================
    # CONTRACT ACTIONS
    # =====================================================

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

    # =====================================================
    # AUTO-RENEWAL ACTIONS
    # =====================================================

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

    # =====================================================
    # CONTRACTS IN SCOPE FILES ACTIONS
    # =====================================================

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
        contract = self.page.get_by_text(
            "Airrived_Cascade-Health-Systems_Subscription-Agreement_2025.docx",
            exact=True
        )

        expect(contract).to_be_visible(timeout=30000)
        contract.click()

    # =====================================================
    # SUMMARY ACTIONS
    # =====================================================

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
        summary_button = self.page.get_by_role(
            "button",
            name="Summary of files",
            exact=True
        )

        expect(summary_button).to_be_visible(timeout=30000)
        summary_button.click()

    def open_summary_of_files_agreement(self):
        # Select the contract
        contract_checkbox = self.page.get_by_role(
            "checkbox",
            name="Select Airrived_Cascade-Health-Systems_Subscription-Agreement_2025.docx"
        )

        expect(contract_checkbox).to_be_visible(timeout=30000)

        if not contract_checkbox.is_checked():
            contract_checkbox.check()

        # Run the Summary of files template
        summary_button = self.page.get_by_role(
            "button",
            name="Summary of files",
            exact=True
        )

        expect(summary_button).to_be_visible(timeout=30000)
        summary_button.click()

        # Verify the query result section is visible
        expect(
            self.page.get_by_text("Query result", exact=True)
        ).to_be_visible(timeout=30000)

    # =====================================================
    # FILTER ACTIONS
    # =====================================================

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
