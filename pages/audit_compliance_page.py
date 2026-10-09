from playwright.sync_api import Page, expect


class AuditCompliancePage:
    """
    Page Object: User Audit Log.

    Covers:
    - User Audit Log
    - Activity Overview
    - Key Performance Indicators cards
    - Action Distribution
    - Top Active Users
    - Daily Activity Timeline
    """

    TITLE = "User Audit Log"

    ACTIVITY_OVERVIEW = "Activity Overview"

    TOTAL_EVENTS = "Total Events"
    UNIQUE_USERS = "Unique Users"
    ACTION_TYPES = "Action Types"
    DAYS_TRACKED = "Days Tracked"

    ACTION_DISTRIBUTION = "Action Distribution"
    TOP_ACTIVE_USERS = "Top Active Users"
    DAILY_ACTIVITY_TIMELINE = "Daily Activity Timeline"

    def __init__(self, page: Page):
        self.page = page

    # LOCATORS

    @property
    def main(self):
        return self.page.get_by_role("main")

    @property
    def user_audit_log_heading(self):
        return self.page.get_by_text(
            self.TITLE,
            exact=True
        ).first

    @property
    def activity_overview(self):
        return self.page.get_by_text(
            self.ACTIVITY_OVERVIEW,
            exact=True
        ).first

    # USER AUDIT LOG BUTTON

    @property
    def view_user_audit_logs_button(self):
        return self.page.get_by_role(
            "button",
            name="View User Audit Logs"
        )

    # KPI CARDS

    @property
    def total_events(self):
        return self.page.get_by_text(
            self.TOTAL_EVENTS,
            exact=True
        ).first

    @property
    def unique_users(self):
        return self.page.get_by_text(
            self.UNIQUE_USERS,
            exact=True
        ).first

    @property
    def action_types(self):
        return self.page.get_by_text(
            self.ACTION_TYPES,
            exact=True
        ).first

    @property
    def days_tracked(self):
        return self.page.get_by_text(
            self.DAYS_TRACKED,
            exact=True
        ).first

    # CHARTS

    @property
    def action_distribution(self):
        return self.page.get_by_text(
            self.ACTION_DISTRIBUTION,
            exact=True
        ).first

    @property
    def top_active_users(self):
        return self.page.get_by_text(
            self.TOP_ACTIVE_USERS,
            exact=True
        ).first

    @property
    def top_active_users_chart(self):
        return self.page.locator(
            ".col-span-12.flex.flex-col.gap-4.md\\:col-span-7"
        ).first

    @property
    def daily_activity_timeline(self):
        return self.page.get_by_text(
            self.DAILY_ACTIVITY_TIMELINE,
            exact=True
        ).first

    # ACTIONS

    def open_user_audit_log(self):
    

        expect(
            self.view_user_audit_logs_button
        ).to_be_visible(timeout=20_000)

        self.view_user_audit_logs_button.click()

    # PAGE VALIDATION

    def expect_page_loaded(self):
        """
        Validates that the User Audit Log page is loaded.
        """

        expect(
            self.user_audit_log_heading
        ).to_be_visible(timeout=30_000)

        expect(
            self.activity_overview
        ).to_be_visible(timeout=20_000)

    # KPI VALIDATION

    def expect_kpi_cards_visible(self):
        """
        Validates all Activity Overview KPI cards.

        Values are NOT checked because they are dynamic.
        """

        expect(
            self.total_events
        ).to_be_visible(timeout=15_000)

        expect(
            self.unique_users
        ).to_be_visible(timeout=15_000)

        expect(
            self.action_types
        ).to_be_visible(timeout=15_000)

        expect(
            self.days_tracked
        ).to_be_visible(timeout=15_000)

    # ACTION DISTRIBUTION

    def expect_action_distribution_visible(self):
        """
        Validates that Action Distribution is displayed.
        """

        expect(
            self.action_distribution
        ).to_be_visible(timeout=15_000)

    # TOP ACTIVE USERS VALIDATION

    def expect_top_active_users_visible(self):
        """
        Validates Top Active Users section and chart.
        """

        expect(
            self.top_active_users
        ).to_be_visible(timeout=15_000)

        expect(
            self.top_active_users_chart
        ).to_be_visible(timeout=20_000)

    # DAILY ACTIVITY TIMELINE VALIDATION

    def expect_daily_activity_timeline_visible(self):
        """
        Validates Daily Activity Timeline section and chart.
        """

        expect(
            self.daily_activity_timeline
        ).to_be_visible(timeout=15_000)

        timeline_chart = self.page.get_by_role(
            "application"
        ).last

        expect(
            timeline_chart
        ).to_be_visible(timeout=20_000)

    # COMPLETE DASHBOARD VALIDATION

    def expect_complete_dashboard(self):
        """
        Validates the complete User Audit Log dashboard.
        """

        self.expect_page_loaded()

        self.expect_kpi_cards_visible()

        self.expect_action_distribution_visible()

        self.expect_top_active_users_visible()

        self.expect_daily_activity_timeline_visible()