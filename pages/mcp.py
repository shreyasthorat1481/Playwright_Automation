
from playwright.sync_api import Page, expect
import re


class MCPPage:

    def __init__(self, page: Page):
        self.page = page

    # LOCATORS

    @property
    def apps_menu(self):
        return self.page.locator(".pb-1 > .cursor-pointer").first

    @property
    def search_box(self):
        return self.page.get_by_role(
            "textbox",
            name="Search"
        )

    @property
    def mcp_new_app(self):
        return self.page.get_by_text(
            "MCP new appPrivateN/",
            exact=False
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
    def mcp_new_app_chat(self):
        return self.page.get_by_text(
            "MCP new appHello there, what",
            exact=False
        )

    @property
    def full_page_area(self):
        return self.page.locator(
            ".h-full.min-h-0"
        )

    @property
    def hello_message(self):
        return self.page.get_by_text(
            "Hello there, what can I do for you?",
            exact=True
        )

    @property
    def content_area(self):
        return self.page.locator(
            ".shrink-0.min-w-0"
        )

    @property
    def ask_textbox(self):
        return self.page.get_by_role(
            "textbox",
            name=re.compile(r"Ask me anything about")
        )

    @property
    def ivory_button(self):
        return self.page.locator(
            ".flex.items-center.gap-2.text-ivory700"
        )

    @property
    def rounded_background_button(self):
        return self.page.locator(
            ".inline-flex.items-center.justify-center.rounded-md.bg-background.p-1\\.5"
        )

    @property
    def mcp_details_new_chat(self):
        return self.page.get_by_text(
            "MCP DetailsNew Chat",
            exact=False
        )

    # MCP DETAILS TABS

    @property
    def history_tab(self):
        return self.page.get_by_role(
            "tab",
            name="History"
        )

    @property
    def service_tab(self):
        return self.page.get_by_role(
            "tab",
            name="Service"
        )

    # ACTIONS

    def open_apps(self):
        expect(
            self.apps_menu
        ).to_be_visible(timeout=60000)

        self.apps_menu.click()

    def search_mcp(self):
        expect(
            self.search_box
        ).to_be_visible(timeout=60000)

        self.search_box.fill("MCP")

    def open_mcp_new_app(self):
        expect(
            self.mcp_new_app
        ).to_be_visible(timeout=60000)

        self.mcp_new_app.click()

    def discover_mcp_app(self):
        expect(
            self.discover_button
        ).to_be_visible(timeout=60000)

        self.discover_button.click()

    def launch_mcp_app(self):
        expect(
            self.launch_button
        ).to_be_visible(timeout=60000)

        self.launch_button.click()

    # MCP CHAT

    def open_mcp_chat(self):
        expect(
            self.mcp_new_app_chat
        ).to_be_visible(timeout=60000)

        self.mcp_new_app_chat.click()

    def click_full_page_area(self):
        expect(
            self.full_page_area
        ).to_be_visible(timeout=60000)

        self.full_page_area.click()

    def open_hello_message(self):
        expect(
            self.hello_message
        ).to_be_visible(timeout=60000)

        self.hello_message.click()

    def click_content_area(self):
        expect(
            self.content_area
        ).to_be_visible(timeout=60000)

        self.content_area.click()

    def click_ask_textbox(self):
        expect(
            self.ask_textbox
        ).to_be_visible(timeout=60000)

        self.ask_textbox.click()

    # MCP ACTIONS

    def click_ivory_button(self):
        expect(
            self.ivory_button
        ).to_be_visible(timeout=60000)

        self.ivory_button.click()

    def click_rounded_background_button(self):
        expect(
            self.rounded_background_button
        ).to_be_visible(timeout=60000)

        self.rounded_background_button.click()

    def click_rounded_background_button_again(self):
        expect(
            self.rounded_background_button
        ).to_be_visible(timeout=60000)

        self.rounded_background_button.click()

    # MCP DETAILS

    def open_mcp_details(self):
        expect(
            self.mcp_details_new_chat
        ).to_be_visible(timeout=60000)

        self.mcp_details_new_chat.click()

    def open_history_tab(self):
        expect(
            self.history_tab
        ).to_be_visible(timeout=60000)

        self.history_tab.click()

    def open_service_tab(self):
        expect(
            self.service_tab
        ).to_be_visible(timeout=60000)

        self.service_tab.click()

