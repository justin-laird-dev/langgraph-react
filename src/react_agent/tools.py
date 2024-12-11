"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

from typing import Any, Callable, List, Optional, cast

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import InjectedToolArg
from typing_extensions import Annotated

from react_agent.configuration import Configuration


# async def search(
#     query: str, *, config: Annotated[RunnableConfig, InjectedToolArg]
# ) -> Optional[list[dict[str, Any]]]:
#     """Search for general web results.

#     This function performs a search using the Tavily search engine, which is designed
#     to provide comprehensive, accurate, and trusted results. It's particularly useful
#     for answering questions about current events.
#     """
#     configuration = Configuration.from_runnable_config(config)
#     wrapped = TavilySearchResults(max_results=configuration.max_search_results)
#     result = await wrapped.ainvoke({"query": query})
#     return cast(list[dict[str, Any]], result)

async def add_graphql_api(
    url: str, *, state: Annotated[RunnableConfig, InjectedToolArg]
) -> Optional[dict[str, Any]]:
    """Add a GraphQL API to our collection.

    This function will store and analyze a GraphQL API.
    """
    print('state', state)
    print('Added API', url)

    # Construct the data structure to return
    api_info = {
        "url": url,
        "description": "Description of the API",  # You can customize this as needed
        "schema": "Schema information here"  # You can customize this as needed
    }

    return api_info

TOOLS: List[Callable[..., Any]] = [add_graphql_api]
