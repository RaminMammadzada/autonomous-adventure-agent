import os
import requests
from google.adk.agents.llm_agent import Agent
from google.adk.tools.openapi_tool import OpenAPIToolset
from google.adk.tools.openapi_tool.auth.auth_helpers import token_to_scheme_credential
import httpx

def fetch_url(url: str) -> str:
    """Fetches the content of a URL."""
    with httpx.Client(follow_redirects=True) as client:
        response = client.get(url)
        response.raise_for_status()
        return response.text


openapi_spec = requests.get("https://adventure.wietsevenema.eu/openapi.json").text

auth_scheme, auth_credential = token_to_scheme_credential(
    "apikey",
    "header",
    "Authorization",
    f"ApiKey {os.environ.get('ADK_API_KEY')}",
)

adventure_game_toolset = OpenAPIToolset(
    spec_str=openapi_spec,
    auth_scheme=auth_scheme,
    auth_credential=auth_credential,
)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="An expert adventure game player.",
    instruction=(
        "You are an opportunistic and autonomous agent that helps the root_agent by taking actions that the root_agent might have overlooked even didnt done yet.\n\n"
        "Create a clear strategy to achieve the root_agent's goals, and execute it step-by-step."
        "Make the lif of the player easier by taking actions that the root_agent might have done."
        "Dont forgot to explain what you have dont with text as well, use some icons in text to make the explanation more lively."
        "Dont wait any instruction from the user, the user will just say Start in the beginning, after that you are fully autonomous."
    ),
    tools=[adventure_game_toolset, fetch_url],

)


