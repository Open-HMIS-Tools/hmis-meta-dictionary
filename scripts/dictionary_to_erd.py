from rich import print

from meta_dictionary_tools.erd_maker import HERDPainter

OUTPUT_DIR = "./documentation/hmis_diagrams"

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
