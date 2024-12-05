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

    def get_csv_names(self) -> list[str]:
        return list(set([field.csv for field in self._fields]))

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


OUTPUT_DIR = "./hmis_diagrams"

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
client_centered_erd.write(OUTPUT_DIR)

"""
'Funder',
'IncomeBenefits',
'HealthAndDV',
'CEParticipation',
'AssessmentResults',
'Enrollment',
'Exit',
'Assessment',
'Export',
'YouthEducationStatus',
'ProjectCoC',
'EmploymentEducation',
'User',
'HMISParticipation',
'Organization',
'Services',
'Inventory',
'Event',
'AssessmentQuestions',
'Affiliation',
'CurrentLivingSituation',
'Client',
'Project',
'Disabilities'
"""

# project_centered_erd = HERDPainter(
#     "Project Centered"
# )


all_csvs = HERDPainter(
    "All CSVs",
    [
        "Funder",
        "IncomeBenefits",
        "HealthAndDV",
        "CEParticipation",
        "AssessmentResults",
        "Enrollment",
        "Exit",
        "Assessment",
        "Export",
        "YouthEducationStatus",
        "ProjectCoC",
        "EmploymentEducation",
        "User",
        "HMISParticipation",
        "Organization",
        "Services",
        "Inventory",
        "Event",
        "AssessmentQuestions",
        "Affiliation",
        "CurrentLivingSituation",
        "Client",
        "Project",
        "Disabilities",
    ],
    ["Export"],
)

all_csvs.write(OUTPUT_DIR)
