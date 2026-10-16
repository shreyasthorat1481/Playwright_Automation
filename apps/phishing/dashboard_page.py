
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

    def search_phishing_app(self):
        expect(self.search_box).to_be_visible(
            timeout=60000
        )
        self.search_box.fill("Phishing")

    def open_phishing_app(self):
        phishing_app_link = self.page.locator(
            'a[href="/apps?appId=6606&agentId=49"]'
        ).first

        expect(phishing_app_link).to_be_visible(
            timeout=30000
        )

        phishing_app_link.click()

        expect(self.page).to_have_url(
            re.compile(
                r"https://acme\.ui\.dev\.airrived\.ai/"
                r"apps\?appId=6606"
                r"(?:&view=dashboard)?"
                r"&agentId=49"
            ),
            timeout=30000
        )

    def open_dashboard_preview(self):
        expect(self.preview_button).to_be_visible(
            timeout=60000
        )
        self.preview_button.click()


    def verify_numeric_data(self, section):
        expect(section).to_be_visible(
            timeout=60000
        )

        # Wait until loading finishes
        expect(section).not_to_contain_text(
            "Loading stats...",
            timeout=60000
        )

        # Verify that numeric data is displayed
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
