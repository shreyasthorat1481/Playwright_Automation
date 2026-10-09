
from pages.login_page import LoginPage
from pages.mcp import MCPPage

def test_mcp(page):

    login_page = LoginPage(page)
    mcp_page = MCPPage(page)

    # LOGIN
    login_page.open_login_page()

    login_page.login(
        "johndoe@airrived.ai",
        "GJ39qZ$K@nL99S8"
    )

    # OPEN APPS
    mcp_page.open_apps()

    # SEARCH MCP
    mcp_page.search_mcp()

    # OPEN MCP APP
    mcp_page.open_mcp_new_app()
    mcp_page.discover_mcp_app()
    mcp_page.launch_mcp_app()

    # MCP CHAT
    mcp_page.open_mcp_chat()
    mcp_page.click_full_page_area()
    mcp_page.open_hello_message()
    mcp_page.click_content_area()
    mcp_page.click_ask_textbox()

    # MCP ACTIONS
    mcp_page.click_ivory_button()
    mcp_page.click_rounded_background_button()
    mcp_page.click_rounded_background_button_again()

    # MCP DETAILS
    mcp_page.open_mcp_details()
    mcp_page.open_history_tab()
    mcp_page.open_service_tab()



