from rich import print

from metadictionary_tools.herd import HERDPainter
from metadictionary_tools import ALL_CSV_NAMES

print(ALL_CSV_NAMES)

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
