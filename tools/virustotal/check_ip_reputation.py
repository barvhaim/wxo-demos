"""
IP Reputation Checker using VirusTotal API.

This tool allows you to check the reputation of an IP address using VirusTotal.
You need to have a VirusTotal API key wxO connection to use this tool.
The connection should be named `vt_api_key`.
"""

import requests
from typing import Dict, Any
from urllib.parse import quote_plus
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.agent_builder.connections import (
    ConnectionType,
    ExpectedCredentials,
)


class VirusTotalIPReputation:
    """A class to handle IP reputation checks using VirusTotal API."""

    BASE_URL = "https://www.virustotal.com/api/v3"

    def __init__(self, api_key: str = None):
        """Initialize the VirusTotal client with API key.

        Args:
            api_key (str, optional): VirusTotal API key. If not provided, will be read from
                VIRUSTOTAL_API_KEY environment variable.

        Raises:
            ValueError: If no API key is provided.
        """
        self.api_key = api_key
        if not self.api_key:
            raise ValueError(
                "VirusTotal API key not provided. " "Please pass it as an argument."
            )
        self.headers = {"x-apikey": self.api_key, "Accept": "application/json"}

    def get_ip_reputation(self, ip_address: str) -> Dict[str, Any]:
        """Get reputation information for an IP address.

        Args:
            ip_address (str): The IP address to check.

        Returns:
            Dict[str, Any]: A dictionary containing:
                - success (bool): Whether the operation was successful
                - data (dict, optional): Reputation data if successful
                - error (str, optional): Error message if unsuccessful
        """
        if not self._is_valid_ip(ip_address):
            return {"success": False, "error": f"Invalid IP address: {ip_address}"}

        url = f"{self.BASE_URL}/ip_addresses/{quote_plus(ip_address)}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()

            data = response.json()
            return {"success": True, "data": self._format_response(data)}

        except requests.exceptions.RequestException as e:
            return {"success": False, "error": f"Error querying VirusTotal: {str(e)}"}

    def _format_response(self, data: Dict) -> Dict:
        """Format the VirusTotal API response into a standardized format.

        Args:
            data (dict): Raw response data from VirusTotal API.

        Returns:
            dict: Formatted response containing IP reputation information.
        """
        attributes = data.get("data", {}).get("attributes", {})

        # Get last analysis stats
        stats = attributes.get("last_analysis_stats", {})

        # Get top malicious verdicts
        malicious_verdicts = []
        last_analysis = attributes.get("last_analysis_results", {})
        for vendor, result in last_analysis.items():
            if result.get("category") == "malicious":
                malicious_verdicts.append(
                    {"vendor": vendor, "result": result.get("result")}
                )

        return {
            "ip": data.get("data", {}).get("id"),
            "asn": attributes.get("asn"),
            "as_owner": attributes.get("as_owner"),
            "country": attributes.get("country"),
            "reputation": attributes.get("reputation"),
            "harmless": stats.get("harmless", 0),
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0),
            "undetected": stats.get("undetected", 0),
            "timeout": stats.get("timeout", 0),
            "malicious_verdicts": malicious_verdicts,
        }

    @staticmethod
    def _is_valid_ip(ip_address: str) -> bool:
        """Validate if the given string is a valid IPv4 address.

        Args:
            ip_address (str): The IP address string to validate.

        Returns:
            bool: True if the input is a valid IPv4 address, False otherwise.
        """
        parts = ip_address.split(".")
        if len(parts) != 4:
            return False

        try:
            return all(0 <= int(part) <= 255 for part in parts)
        except ValueError:
            return False


@tool(
    name="CheckIpReputation",
    description="Check the reputation of an IP address using VirusTotal.",
    permission=ToolPermission.READ_ONLY,
    expected_credentials=[
        ExpectedCredentials(app_id="vt_api_key", type=ConnectionType.API_KEY_AUTH)
    ],
)
def check_ip_reputation(ip_address: str) -> Dict[str, Any]:
    """Check the reputation of an IP address using VirusTotal.

    This is the main entry point for the tool that integrates with the agent framework.

    Args:
        ip_address (str): The IP address to check the reputation for.

    Returns:
        Dict[str, Any]: A dictionary containing:
            - success (bool): Whether the operation was successful
            - data (dict, optional): Reputation data if successful
            - error (str, optional): Error message if unsuccessful
    """
    try:
        conn = connections.api_key_auth("vt_api_key")
        api_key = conn.api_key
        if not api_key:
            return {
                "success": False,
                "error": "VirusTotal API key not found. Please set `vt_api_key` wxO connection.",
            }

        vt = VirusTotalIPReputation(api_key)
        return vt.get_ip_reputation(ip_address)
    except Exception as e:
        return {
            "success": False,
            "error": f"Error initializing VirusTotal client: {str(e)}",
        }
