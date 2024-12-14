# tools.py
from typing import Any, Dict, List
from langchain_core.tools import tool, InjectedToolArg
from typing_extensions import Annotated

# Define the tool for adding GraphQL APIs
@tool
def add_graphql_api(
    url: str,
    *,
    state: Annotated[Dict[str, Any], InjectedToolArg]
) -> Dict[str, Any]:
    """Add a GraphQL API to our collection.

    This function stores and analyzes a GraphQL API.
    Args:
        url (str): The GraphQL API URL to be added.
        state (dict): The current state, injected at runtime.

    Returns:
        dict: Information about the added API.
    """
    # Initialize or retrieve the ingested_apis list from the state
    ingested_apis = state.setdefault("ingested_apis", [])

    # Construct the API info object
    api_info = {
        "url": url,
        "description": "Description of the API",  # Customize as needed
        "schema": "Schema information here"       # Customize as needed
    }

    # Add the API info to the state
    ingested_apis.append(api_info)
    print(f"Added API: {url}")

    return api_info

# Define the tool for listing GraphQL APIs
@tool
def list_graphql_apis(
    *,
    state: Annotated[Dict[str, Any], InjectedToolArg]
) -> List[Dict[str, Any]]:
    """List all ingested GraphQL APIs from the state.

    Args:
        state (dict): The current state, injected at runtime.

    Returns:
        List[dict]: A list of dictionaries containing the ingested APIs.
    """
    # Retrieve the ingested_apis list from the state
    ingested_apis = state.get("ingested_apis", [])
    print(f"Listing {len(ingested_apis)} APIs: {ingested_apis}")
    return ingested_apis

# Tools list to register both functions
TOOLS = [add_graphql_api, list_graphql_apis]
