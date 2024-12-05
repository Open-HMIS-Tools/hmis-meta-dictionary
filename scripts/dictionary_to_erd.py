from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from rich import print

import os

from metadictionary_tools.hmis_mermaid_maker import FocusedERD
from metadictionary_tools.hmis_models import HMISField, HMISFields


fields = HMISFields.load()


class HERDPainter:
    """
    HMIS ERD Painter creates scoped diagrams.
    """

    def __init__(self, csvs_to_include: list[str], csvs_to_exclude: list[str]) -> None:
        self.csvs_to_include = csvs_to_include
        self.csvs_to_exclude = csvs_to_exclude

    def write(self, output_path: str, as_markdown: bool = True) -> None:
        filtered_fields = [
            field for field in fields if field.csv in self.csvs_to_include
        ]
        fk_fields = [field for field in filtered_fields if field.is_foreign_key()]

        erd_markup = FocusedERD(
            "Client Centered", fk_fields, self.csvs_to_exclude
        ).generate()

        if as_markdown:
            erd_markup = "```mermaid\n" + erd_markup + "\n```"

        with open(output_path, "+w") as f:
            f.write(erd_markup)


client_centered_erd = HERDPainter(
    [
        "Client",
        "Enrollment",
        "Project",
        "Household",
        "User",
        "Organization",
        "ProjectCoC",
    ],
    ["Export"],
)

client_centered_erd.write("test_it.md")
