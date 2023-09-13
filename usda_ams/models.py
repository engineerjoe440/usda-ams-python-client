################################################################################
"""
United States Department of Agriculture Animal Marketing Service Python API
--------------------------------------------------------------------------------

A Python client for the USDA AMS API.

License: MIT
Author: Joe Stanley
"""
################################################################################

from pydantic import BaseModel

class USDAReport(BaseModel):
    """Generic Data for a Single USDA Report."""


class USDAReportAccessInformation(BaseModel):
    """Generic Summary for a Report."""
    slug_id: int
    slug_name: str
    report_title: str
    markets: list[str]
    offices: list[str]
    sectionNames: list[str]