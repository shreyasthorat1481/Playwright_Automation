
from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    # LOCATORS

    @property
    def email_input(self):
        return self.page.get_by_role(
            "textbox",
            name="email@domain.com"
        )

    @property
    def password_input(self):
        return self.page.locator(
            'input[name="password"]'
        )

    @property
    def login_button(self):
        return self.page.get_by_role(
            "button",
            name="Login",
            exact=True
        )

    def open_login_page(self):

        self.page.goto(
            "https://acme.ui.dev.airrived.ai/login",
            wait_until="domcontentloaded",
            timeout=60000
        )

        expect(
            self.email_input
        ).to_be_visible(timeout=60000)

        expect(
            self.password_input
        ).to_be_visible(timeout=60000)

    def login(self, email, password):

        expect(
            self.email_input
        ).to_be_visible(timeout=60000)

        expect(
            self.password_input
        ).to_be_visible(timeout=60000)

        self.email_input.fill(email)

        self.password_input.fill(password)

        print("Email entered")

        # Click Login
        self.login_button.click()

        print("Login button clicked")

        self.page.wait_for_timeout(3000)

        print(
            "URL after login:",
            self.page.url
        )

        if self.login_button.is_visible():

            print("LOGIN PAGE IS STILL OPEN")

            # Print visible page text
            print(
                self.page.locator("body").inner_text()
            )

        else:

            print("LOGIN PAGE CLOSED")

        self.page.wait_for_timeout(2000)
