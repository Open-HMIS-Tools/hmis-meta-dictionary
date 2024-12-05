from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from rich import print

import os

from metadictionary_tools.hmis_mermaid_maker import FocusedERD
from metadictionary_tools.hmis_models import HMISField, HMISFields


class HERDPainter:
    """
    HMIS ERD Painter creates scoped diagrams.
    """

    def __init__(
        self, name: str, csvs_to_include: list[str], csvs_to_exclude: list[str]
    ) -> None:
        self.name = name
        self.csvs_to_include = csvs_to_include
        self.csvs_to_exclude = csvs_to_exclude

        self._fields = HMISFields.load()

    def write(self, output_dir: str, as_markdown: bool = True) -> None:
        name = self.name.replace(" ", "_").lower()
        filtered_fields = [
            field for field in self._fields if field.csv in self.csvs_to_include
        ]
        fk_fields = [field for field in filtered_fields if field.is_foreign_key()]

        erd_markup = FocusedERD(
            "Client Centered", fk_fields, self.csvs_to_exclude
        ).generate()

        if as_markdown:
            erd_markup = "```mermaid\n" + erd_markup + "\n```"

        output_filepath = f"{output_dir}/{name}.md"

        with open(output_filepath, "+w") as f:
            f.write(erd_markup)


client_centered_erd = HERDPainter(
    "Client Centered",
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
client_centered_erd.write("./hmis_diagrams")

# project_centered_erd = HERDPainter()
