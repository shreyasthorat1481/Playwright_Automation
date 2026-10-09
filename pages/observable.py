import re
from playwright.sync_api import Page, expect


class ObservablePage:

    def __init__(self, page: Page):
        self.page = page

    # APP LOCATORS

    @property
    def apps_menu(self):
        return self.page.locator(".pb-1 > .cursor-pointer").first

    @property
    def search_box(self):
        return self.page.get_by_role("textbox", name="Search")

    @property
    def observable_app(self):
        return self.page.get_by_text(
            "ObservablePrivateObservable",
            exact=False
        ).first

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

    # TEXT INTERFACE

    @property
    def text_tab(self):
        return self.page.get_by_role(
            "tab",
            name="Text"
        )

    @property
    def text_box(self):
        return self.page.get_by_role(
            "textbox",
            name="Enter text here..."
        )

    @property
    def text_tabpanel(self):
        return self.page.get_by_role(
            "tabpanel",
            name="Text"
        )

    # OBSERVABLE DETAILS

    @property
    def observable_details_tabpanel(self):
        return self.page.get_by_role(
            "tabpanel",
            name="Observable Details"
        )

    @property
    def iocs_overview(self):
        return self.observable_details_tabpanel.get_by_text(
            "IOCs Overview",
            exact=True
        )

    @property
    def provider_details(self):
        return self.observable_details_tabpanel.get_by_text(
            "Provider details",
            exact=True
        )

    @property
    def verdict_details(self):
        return self.observable_details_tabpanel.get_by_text(
            "Verdict details",
            exact=True
        )

    # IOCs DETAILS

    @property
    def iocs_details_tab(self):
        return self.page.get_by_role(
            "tab",
            name="IOCs Details"
        )

    @property
    def iocs_details_tabpanel(self):
        return self.page.get_by_role(
            "tabpanel",
            name="IOCs Details"
        )

    # APP ACTIONS

    def open_apps(self):
        self.apps_menu.click()

    def search_observable(self):
        expect(self.search_box).to_be_visible(timeout=60000)

        self.search_box.click()
        self.search_box.fill("obser")

    def search_observable_again(self):
        expect(self.search_box).to_be_visible(timeout=60000)

        self.search_box.fill("observable")

    def open_observable_app(self):
        expect(self.observable_app).to_be_visible(timeout=60000)

        self.observable_app.click()

    def discover_observable(self):
        expect(self.discover_button).to_be_visible(timeout=60000)

        self.discover_button.click()

    def launch_observable(self):
        expect(self.launch_button).to_be_visible(timeout=60000)

        self.launch_button.click()

    # TEXT ACTIONS

    def open_text_interface(self):
        button = self.page.get_by_role("main").get_by_role(
            "button"
        ).filter(has_text=re.compile(r"^$")).first

        expect(button).to_be_visible(timeout=60000)

        button.click()

    def select_text_tab(self):
        expect(self.text_tab).to_be_visible(timeout=60000)

        self.text_tab.click()

    def enter_observable_text(self, observable_text):
        expect(self.text_box).to_be_visible(timeout=60000)

        self.text_box.fill(observable_text)

    def submit_text(self):
        button = self.text_tabpanel.get_by_role("button").last

        expect(button).to_be_visible(timeout=60000)

        button.click()

    # IOC OVERVIEW

    def open_iocs_overview(self):
        expect(
            self.iocs_overview
        ).to_be_visible(timeout=60000)

    def verify_ioc_count(self, ioc_label):

        label = self.observable_details_tabpanel.get_by_text(
            ioc_label,
            exact=True
        )

        expect(label).to_be_visible(timeout=60000)

        numeric_values = (
            self.observable_details_tabpanel
            .get_by_text(re.compile(r"^\d+$"))
        )

        expect(
            numeric_values.first
        ).to_be_visible(timeout=60000)

        print(f"{ioc_label} count is available")

    def verify_hash(self):
        self.verify_ioc_count("Hash")

    def verify_ip(self):
        self.verify_ioc_count("IP")

    def verify_url(self):
        self.verify_ioc_count("URL")

    def verify_domain(self):
        self.verify_ioc_count("Domain")

    # PROVIDER

    def open_provider_details(self):
        expect(
            self.provider_details
        ).to_be_visible(timeout=60000)

        self.provider_details.click()

    def open_verdict_details(self):
        expect(
            self.verdict_details
        ).to_be_visible(timeout=60000)

        self.verdict_details.click()

    # IOC DETAILS

    def open_iocs_details(self):

        expect(
            self.iocs_details_tab
        ).to_be_visible(timeout=60000)

        self.iocs_details_tab.click()

        expect(
            self.iocs_details_tabpanel
        ).to_be_visible(timeout=60000)

    def check_ioc_detail(self, ioc_type):

        locator = self.iocs_details_tabpanel.get_by_text(
            ioc_type,
            exact=True
        )

        if locator.count() > 0:

            expect(
                locator.first
            ).to_be_visible(timeout=60000)

            locator.first.click()

            print(
                f"{ioc_type} found in IOCs Details"
            )

        else:

            print(
                f"{ioc_type} not found in IOCs Details - skipping"
            )

    def open_domain_details(self):
        self.check_ioc_detail("DOMAIN")

    def open_ip_details(self):
        self.check_ioc_detail("IP")