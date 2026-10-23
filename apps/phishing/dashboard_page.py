import re

from playwright.sync_api import Page, expect


class PhishingDashboardPage:

    def __init__(self, page: Page):
        self.page = page

    # LOCATORS

    @property
    def app_menu(self):
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
    def phishing_app_text(self):
        return self.page.get_by_text(
            re.compile(
                r"Phishing \(Don't Delete\)\s+QA Team"
            ),
            exact=False
        ).first

    @property
    def app_primary_action_button(self):
        return self.page.locator(
            "button.bg-primary.h-8"
        ).first

    @property
    def discover_button(self):
        return self.page.get_by_role(
            "button",
            name="Discover now"
        )

    @property
    def launch_button(self):
        return self.page.get_by_role(
            "button",
            name="Launch"
        )

    @property
    def preview_button(self):
        return self.page.get_by_role(
            "button",
            name="Preview"
        )

    @property
    def phishing_summary_section(self):
        return self.page.locator("section").filter(
            has_text="Phishing Summary"
        ).first

    @property
    def total_email_label(self):
        return self.phishing_summary_section.get_by_text(
            "Emails",
            exact=True
        )

    @property
    def total_classification_label(self):
        return self.phishing_summary_section.get_by_text(
            "Total classification",
            exact=True
        )

    @property
    def last_job_run_label(self):
        return self.page.get_by_text(
            re.compile(
                r"[A-Z][a-z]{2} \d{1,2}, \d{4} "
                r"\d{1,2}:\d{2} [AP]M"
            )
        ).first

    @property
    def category_details_section(self):
        return self.page.locator("section").filter(
            has=self.page.get_by_text(
                "Category Details",
                exact=True
            )
        ).first

    @property
    def summary_of_email_section(self):
        return self.page.locator("section").filter(
            has=self.page.get_by_text(
                "Summary of Emails",
                exact=True
            )
        ).first

    @property
    def classification_section(self):
        return self.page.get_by_text(
            "Classification",
            exact=True
        ).first

    # NAVIGATION AND APP LAUNCH

    def open_home_page(self):
        self.page.goto(
            "https://acme.ui.dev.airrived.ai/home",
            wait_until="domcontentloaded",
            timeout=60000
        )

    def open_apps(self):
        expect(self.app_menu).to_be_visible(
            timeout=60000
        )
        self.app_menu.click()

        expect(self.search_box).to_be_visible(
            timeout=60000
        )

    def search_phishing_app(self):
        # Match the initial search action in the new script.
        self.search_box.click()
        self.search_box.fill("phishi")

        # Navigate to the Apps page with the initial query.
        self.page.goto(
            "https://acme.ui.dev.airrived.ai/apps?q=phishi",
            wait_until="domcontentloaded",
            timeout=60000
        )

        # Wait for the search field and perform the final search.
        expect(self.search_box).to_be_visible(
            timeout=60000
        )
        self.search_box.fill("phishing")

    def open_phishing_app(self):
        expect(self.phishing_app_text).to_be_visible(
            timeout=60000
        )
        self.phishing_app_text.click()

    def click_app_primary_action(self):
        expect(
            self.app_primary_action_button
        ).to_be_visible(timeout=60000)

        self.app_primary_action_button.click()

    def launch_app(self):
        expect(self.launch_button).to_be_visible(
            timeout=60000
        )
        self.launch_button.click()

    def open_dashboard_preview(self):
        expect(self.preview_button).to_be_visible(
            timeout=60000
        )
        self.preview_button.click()

    # DASHBOARD VERIFICATIONS

    def verify_numeric_data(self, section):
        expect(section).to_be_visible(
            timeout=60000
        )

        # Wait until loading finishes.
        expect(section).not_to_contain_text(
            "Loading stats...",
            timeout=60000
        )

        # Verify that numeric data is displayed.
        expect(section).to_contain_text(
            re.compile(r"\d+"),
            timeout=10000
        )

    def verify_phishing_summary(self):
        self.verify_numeric_data(
            self.phishing_summary_section
        )

    def verify_total_emails(self):
        expect(
            self.total_email_label
        ).to_be_visible(timeout=60000)

        expect(
            self.phishing_summary_section
        ).to_contain_text(
            re.compile(
                r"\d+\s*Emails",
                re.IGNORECASE
            ),
            timeout=10000
        )

    def verify_total_classifications(self):
        expect(
            self.total_classification_label
        ).to_be_visible(timeout=60000)

        expect(
            self.phishing_summary_section
        ).to_contain_text(
            re.compile(
                r"\d+\s*Total classification",
                re.IGNORECASE
            ),
            timeout=10000
        )

    def verify_last_job_run(self):
        expect(
            self.last_job_run_label
        ).to_be_visible(timeout=60000)

    def verify_category_details(self):
        self.verify_numeric_data(
            self.category_details_section
        )

    def verify_summary_of_emails(self):
        expect(
            self.summary_of_email_section
        ).to_be_visible(timeout=60000)

        expect(
            self.summary_of_email_section.get_by_role(
                "columnheader",
                name="Name"
            )
        ).to_be_visible(timeout=60000)

        expect(
            self.summary_of_email_section.get_by_role(
                "row"
            ).nth(1)
        ).to_be_visible(timeout=60000)

    def verify_classification(self):
        expect(
            self.classification_section
        ).to_be_visible(timeout=60000)

    def verify_dashboard_data(self):
        self.verify_phishing_summary()
        self.verify_total_emails()
        self.verify_total_classifications()
        self.verify_last_job_run()
        self.verify_category_details()
        self.verify_summary_of_emails()
        self.verify_classification()
