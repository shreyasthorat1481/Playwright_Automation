
import re

from playwright.sync_api import Page, expect


class EmailManagementPage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def email_list_icon(self):
        return self.page.locator(
            "li:nth-child(2) > .cursor-pointer"
        )

    @property
    def summary_of_emails_heading(self):
        return self.page.get_by_text(
            "Summary of Emails", exact=False
        )

    @property
    def email_cards(self):
        return self.page.get_by_role(
            "button",
            name=re.compile(r"Potential Phish:", re.IGNORECASE)
        )

    @property
    def summary_tab(self):
        return self.page.get_by_role(
            "tab", name="Summary"
        )

    @property
    def what_happened_heading(self):
        return self.page.get_by_text(
            "What Happened", exact=True
        )

    @property
    def sender_emails_button(self):
        return self.page.get_by_role(
            "button",
            name=re.compile(r"Sender Emails", re.IGNORECASE)
        )

    @property
    def recipients_button(self):
        return self.page.get_by_role(
            "button",
            name=re.compile(r"Recipients", re.IGNORECASE)
        )

    @property
    def domain_button(self):
        return self.page.get_by_role(
            "button",
            name=re.compile(r"Domain", re.IGNORECASE)
        )

    @property
    def reporter_button(self):
        return self.page.get_by_role(
            "button",
            name=re.compile(r"Reporter", re.IGNORECASE)
        )

    @property
    def attachments_button(self):
        return self.page.get_by_role(
            "button",
            name=re.compile(r"Attachments", re.IGNORECASE)
        )

    @property
    def email_preview_heading(self):
        return self.page.get_by_text(
            "Email Preview", exact=True
        )

    @property
    def email_headers_tab(self):
        return self.page.get_by_role(
            "tab", name="Email Headers"
        )

    @property
    def email_headers_panel(self):
        return self.page.get_by_role(
            "tabpanel", name="Email Headers"
        )

    @property
    def email_headers_search(self):
        return self.email_headers_panel.get_by_placeholder(
            "Search"
        )

    @property
    def observables_tab(self):
        return self.page.get_by_role(
            "tab", name="Observables"
        )

    @property
    def iocs_details_heading(self):
        return self.page.get_by_text(
            "IOCs Details", exact=False
        )

    @property
    def remediation_tab(self):
        return self.page.get_by_role(
            "tab", name="Remediation"
        )

    @property
    def remediation_panel(self):
        return self.page.get_by_role(
            "tabpanel", name="Remediation"
        )

    @property
    def remediation_summary_button(self):
        return self.page.get_by_role(
            "button",
            name=re.compile(
                r"Remediation Summary", re.IGNORECASE
            )
        )

    @property
    def conversational_ai_tab(self):
        return self.page.get_by_role(
            "tab", name="Conversational AI"
        )

    @property
    def conversational_ai_panel(self):
        return self.page.get_by_role(
            "tabpanel", name="Conversational AI"
        )

    #VALIDATION METHODS

    def verify_visible_text(self, locator, section_name):
        expect(locator).to_be_visible(timeout=30000)

        text_content = locator.inner_text(
            timeout=30000
        ).strip()

        assert text_content, (
            f"{section_name} is visible but contains no text."
        )

        print(
            f"PASS: {section_name} contains visible text: "
            f"{text_content[:200]!r}"
        )

    def verify_visible_control(self, locator, section_name):
        expect(locator.first).to_be_visible(timeout=30000)

        print(
            f"PASS: {section_name} is visible."
        )


    # EMAIL MANAGEMENT NAVIGATION

    def open_email_management(self):
        expect(
            self.email_list_icon
        ).to_be_visible(timeout=60000)

        self.email_list_icon.click()

        expect(
            self.summary_of_emails_heading
        ).to_be_visible(timeout=60000)

        self.verify_visible_text(
            self.summary_of_emails_heading,
            "Summary of Emails"
        )

    def open_first_phishing_email(self):
        expect(
            self.email_cards.first
        ).to_be_visible(timeout=60000)

        self.email_cards.first.click()

        expect(
            self.summary_tab
        ).to_be_visible(timeout=30000)

        print("PASS: Opened a phishing email.")

    # SUMMARY

    def verify_summary_section(self):
        expect(
            self.summary_tab
        ).to_be_visible(timeout=30000)

        self.summary_tab.click()

        expect(
            self.what_happened_heading
        ).to_be_visible(timeout=30000)

        print(
            "PASS: Summary and What Happened are visible."
        )


    # EMAIL DETAILS

    def verify_email_detail_buttons(self):
        detail_buttons = [
            (self.sender_emails_button, "Sender Emails"),
            (self.recipients_button, "Recipients"),
            (self.domain_button, "Domain"),
            (self.reporter_button, "Reporter"),
            (self.attachments_button, "Attachments"),
        ]

        for locator, section_name in detail_buttons:
            self.verify_visible_control(
                locator, section_name
            )

            locator.first.click()

            print(
                f"PASS: {section_name} control responds to a click."
            )

    def verify_email_preview(self):
        self.verify_visible_control(
            self.email_preview_heading,
            "Email Preview"
        )

    # =====================================================
    # EMAIL HEADERS
    # =====================================================

    def verify_email_headers(self):
        self.email_headers_tab.click()

        expect(
            self.email_headers_panel
        ).to_be_visible(timeout=30000)

        panel_text = self.email_headers_panel.inner_text(
            timeout=30000
        ).strip()

        if panel_text:
            print(
                "PASS: Email Headers displays text: "
                f"{panel_text[:200]!r}"
            )
        elif self.email_headers_search.count() > 0:
            expect(
                self.email_headers_search
            ).to_be_visible(timeout=30000)

            print(
                "PASS: Email Headers search control is visible."
            )
        else:
            raise AssertionError(
                "Email Headers panel has no visible text "
                "or search control."
            )


    # OBSERVABLES

    def verify_observables(self):
        self.observables_tab.click()

        expect(
            self.iocs_details_heading
        ).to_be_visible(timeout=30000)

        self.verify_visible_text(
            self.iocs_details_heading,
            "IOCs Details"
        )

        print("PASS: Observables section is displayed.")

    # REMEDIATION

    def verify_remediation(self):
        self.remediation_tab.click()

        expect(
            self.remediation_panel
        ).to_be_visible(timeout=30000)

        expect(
            self.remediation_summary_button
        ).to_be_visible(timeout=30000)

        self.remediation_summary_button.click()

        expect(
            self.remediation_panel
        ).to_be_visible(timeout=30000)

        panel_text = self.remediation_panel.inner_text(
            timeout=30000
        ).strip()

        assert panel_text, (
            "Remediation tab is open, but no text result "
            "is displayed in the Remediation panel."
        )

        print(
            "PASS: Remediation panel displays text: "
            f"{panel_text[:300]!r}"
        )


    # CONVERSATIONAL AI

    def verify_conversational_ai(self):
        self.conversational_ai_tab.click()

        expect(
            self.conversational_ai_tab
        ).to_be_visible(timeout=30000)

        print("PASS: Conversational AI tab is accessible.")

        if self.conversational_ai_panel.count() > 0:
            expect(
                self.conversational_ai_panel
            ).to_be_visible(timeout=30000)

            panel_text = (
                self.conversational_ai_panel
                .inner_text(timeout=30000)
                .strip()
            )

            if panel_text:
                print(
                    "PASS: Conversational AI displays text: "
                    f"{panel_text[:200]!r}"
                )
            else:
                print(
                    "INFO: Conversational AI panel is visible "
                    "but currently has no text."
                )

    # COMPLETE EMAIL MANAGEMENT VALIDATION

    def verify_email_management(self):
        self.open_email_management()
        self.open_first_phishing_email()
        self.verify_summary_section()
        self.verify_email_detail_buttons()
        self.verify_email_preview()
        self.verify_email_headers()
        self.verify_observables()
        self.verify_remediation()
        self.verify_conversational_ai()
