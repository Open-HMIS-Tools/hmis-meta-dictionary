"""
Note, these may not be used.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Union, Any
from datetime import date, datetime


@dataclass
class JoinDefinition:
    left_csv_name: str
    right_csv_name: str
    left_on: str
    right_on: str


# @dataclass
# class AffiliationRecord:
#     csv: str
#     element_num: Optional[str] = field(default=None)
#     name: str = field(default="")
#     key_type: str = field(default="")
#     relationship_desc: Optional[str] = field(default=None)
#     field_to_csv_relationship: Optional[str] = field(default=None)
#     type: str = field(default="")
#     list: Optional[str] = field(default=None)
#     null: Optional[str] = field(default=None)
#     notes: Optional[str] = field(default=None)
#     validate: Optional[str] = field(default=None)


# @dataclass
# class AssessmentField:
#     csv_id: int  # Corresponds to index
#     element_num: Optional[str]  # Optional string, can be None
#     name: str  # Field name
#     key_type: str  # Type of key (e.g., pk, fk)
#     relationship_desc: Optional[str]  # Optional description of the relationship
#     field_to_csv_relationship: Optional[str]  # Optional field to CSV relationship
#     type: str  # Data type (e.g., S32, D)
#     list: Optional[str]  # Optional list field, can be None
#     null: Optional[str]  # Optional, identifies if the field can be None
#     notes: Optional[str]  # Optional notes about the field
#     validate: Optional[str]  # Optional validation rule


# @dataclass
# class AssessmentResult:
#     assessment_result_id: Optional[int] = field(metadata={"db_key": "pk"})
#     assessment_id: Optional[int] = field(metadata={"db_key": "fk"})
#     enrollment_id: Optional[int] = field(metadata={"db_key": "fk"})
#     personal_id: Optional[int] = field(metadata={"db_key": "fk"})
#     assessment_result_type: str = field(default_factory=str)
#     assessment_result: str = field(default_factory=str)
#     date_created: Optional[str] = field(default=None)
#     date_updated: Optional[str] = field(default=None)
#     user_id: Optional[int] = field(metadata={"db_key": "fk"})
#     date_deleted: Optional[str] = field(default=None)
#     export_id: Optional[int] = field(metadata={"db_key": "fk"})

#     def __post_init__(self):
#         # Validate required fields
#         if not self.assessment_result_type and self.assessment_result:
#             raise ValueError(
#                 "AssessmentResultType cannot be NULL if AssessmentResult is populated"
#             )
#         # Additional constraints can be added here if necessary


# @dataclass
# class AssessmentQuestion:
#     assessment_question_id: Optional[str] = field(
#         metadata={"key": "pk", "notes": "Unique identifier"}
#     )
#     assessment_id: Optional[str] = field(metadata={"key": "fk"})
#     enrollment_id: Optional[str] = field(metadata={"key": "fk"})
#     personal_id: Optional[str] = field(metadata={"key": "fk"})
#     assessment_question_group: Optional[str] = field(
#         default=None, metadata={"notes": "Locally determined"}
#     )
#     assessment_question_order: Optional[int] = field(
#         default=None, metadata={"notes": "Locally determined"}
#     )
#     assessment_question: Optional[str] = field(
#         metadata={
#             "nullable": False,
#             "notes": "Cannot be NULL if AssessmentQuestions.csv is populated",
#         }
#     )
#     assessment_answer: Optional[str] = field(
#         default=None, metadata={"nullable": True, "notes": "Locally determined"}
#     )
#     date_created: Optional[datetime] = field(default=None)
#     date_updated: Optional[datetime] = field(default=None)
#     user_id: Optional[str] = field(metadata={"key": "fk"})
#     date_deleted: Optional[datetime] = field(default=None, metadata={"nullable": True})
#     export_id: Optional[str] = field(
#         metadata={"key": "fk", "notes": "Must match ExportID in Export.csv"}
#     )

#     def __post_init__(self):
#         # Additional validation can be added here if needed
#         pass


# @dataclass
# class CEParticipation:
#     CEParticipationID: str
#     ProjectID: Optional[str] = None
#     AccessPoint: Optional[int] = None
#     PreventionAssessment: Optional[int] = None
#     CrisisAssessment: Optional[int] = None
#     HousingAssessment: Optional[int] = None
#     DirectServices: Optional[int] = None
#     ReceivesReferrals: Optional[int] = None
#     CEParticipationStatusStartDate: Optional[datetime] = None
#     CEParticipationStatusEndDate: Optional[datetime] = None
#     DateCreated: Optional[datetime] = None
#     DateUpdated: Optional[datetime] = None
#     UserID: Optional[str] = None
#     DateDeleted: Optional[datetime] = None
#     ExportID: Optional[str] = None

#     # Validate relationships or constraints can be implemented as methods here if needed


# @dataclass
# class ClientData:
#     csv: Union[str, None]  # or str, depending on how you want to handle "nan"
#     element_num: Union[str, None]
#     name: str
#     key_type: Union[str, None]  # could also be Optional[str]
#     relationship_desc: Union[str, None]
#     field_to_csv_relationship: Union[str, None]
#     type: str
#     list: Union[str, None]  # or str, depending on how you want to handle "nan"
#     null: Union[str, None]  # or str, depending on how you want to handle "nan"
#     notes: Union[str, None]
#     validate: Union[str, None]  # can also be a validation rule or None


# @dataclass
# class CurrentLivingSituation:
#     csv: int
#     element_num: Optional[str]  # Can be a string like '4.12.1', or None
#     name: str
#     key_type: Optional[str]  # Can be 'pk', 'fk', or None
#     relationship_desc: Optional[str]  # Typically None or nan
#     field_to_csv_relationship: Optional[str]  # Typically None or nan
#     type: str  # Data type such as 'S32', 'D', 'I', etc.
#     list: Optional[str]  # Referring to relationships, can be None
#     null: Optional[str]  # Indicates if null is allowed, usually None
#     notes: Optional[str]  # Extra notes, typically None
#     validate: Optional[str]  # Validation rules, can be None


# @dataclass
# class DisabilityRecord:
#     disabilities_id: Optional[str] = field(
#         metadata={"key": "pk", "description": "Unique identifier"}
#     )
#     enrollment_id: Optional[str] = field(metadata={"key": "fk"})
#     personal_id: Optional[str] = field(metadata={"key": "fk"})
#     information_date: Optional[str] = field(
#         metadata={"description": "Date of Information"}
#     )
#     disability_type: Optional[int] = field(
#         metadata={"description": "Type of disability"}
#     )
#     disability_response: Optional[int] = field(
#         metadata={"description": "Response related to DisabilityType"}
#     )
#     indefinite_and_impairs: Optional[int] = field(
#         metadata={"description": "Indicates indefinite impairments"}
#     )
#     t_cell_count_available: Optional[int] = field(
#         metadata={
#             "description": "Available T-Cell count",
#             "conditional": "Null unless DisabilityType = 8 AND DisabilityResponse=1",
#         }
#     )
#     t_cell_count: Optional[int] = field(
#         metadata={"description": "T-Cell count", "conditional": "Null unless W4.2 = 1"}
#     )
#     t_cell_source: Optional[int] = field(
#         metadata={
#             "description": "Source of T-Cell",
#             "conditional": "Null unless W4.A is not null",
#         }
#     )
#     viral_load_available: Optional[int] = field(
#         metadata={
#             "description": "Available viral load",
#             "conditional": "Null unless DisabilityType = 8 AND DisabilityResponse=1",
#         }
#     )
#     viral_load: Optional[int] = field(
#         metadata={"description": "Viral load", "conditional": "Null unless W4.3 = 1"}
#     )
#     viral_load_source: Optional[int] = field(
#         metadata={
#             "description": "Source of viral load",
#             "conditional": "Null unless W4.C is not null",
#         }
#     )
#     anti_retrovial: Optional[int] = field(
#         metadata={
#             "description": "Anti-retroviral",
#             "conditional": "Null unless DisabilityType = 8 AND DisabilityResponse=1",
#         }
#     )
#     data_collection_stage: Optional[int] = field(
#         metadata={"description": "Stage of data collection"}
#     )
#     date_created: Optional[str] = field(
#         metadata={"description": "Date record was created"}
#     )
#     date_updated: Optional[str] = field(
#         metadata={"description": "Date record was updated"}
#     )
#     user_id: Optional[str] = field(metadata={"key": "fk"})
#     date_deleted: Optional[str] = field(
#         metadata={"description": "Date record was deleted", "conditional": "Y"}
#     )
#     export_id: Optional[str] = field(
#         metadata={"key": "fk", "description": "Must match ExportID in Export.csv"}
#     )


# @dataclass
# class EmploymentEducation:
#     csv: str
#     element_num: Optional[str] = field(default=None)
#     name: str = field(default="")
#     key_type: str = field(default="")
#     relationship_desc: Optional[str] = field(default=None)
#     field_to_csv_relationship: Optional[str] = field(default=None)
#     type: str = field(default="")
#     list: Optional[str] = field(default=None)
#     null: Optional[str] = field(default=None)
#     notes: Optional[str] = field(default=None)
#     validate: Optional[Any] = field(default=None)


# @dataclass
# class Enrollment:
#     csv: str
#     element_num: str
#     name: str
#     key_type: str
#     relationship_desc: Optional[str]
#     field_to_csv_relationship: Optional[str]
#     type: str
#     list: Optional[str]
#     null: Optional[str]
#     notes: Optional[str]
#     validate: Optional[str]


# @dataclass
# class EventField:
#     element_num: Optional[str] = field(default=None)
#     name: str = field(default="")
#     key_type: Optional[str] = field(default=None)
#     relationship_desc: Optional[str] = field(default=None)
#     field_to_csv_relationship: Optional[str] = field(default=None)
#     type: str = field(default="")
#     list: Optional[str] = field(default=None)
#     null: Optional[str] = field(
#         default=None
#     )  # Optionally indicates if the field can be null
#     notes: Optional[str] = field(default=None)
#     validate: Optional[str] = field(default=None)


# @dataclass
# class ExitRecord:
#     element_num: Optional[str]
#     name: str
#     key_type: Optional[str]
#     relationship_desc: Optional[str]
#     field_to_csv_relationship: Optional[str]
#     data_type: (
#         str  # Changed from 'type' to 'data_type' because 'type' is a built-in function
#     )
#     is_list: Optional[
#         str
#     ]  # Assumed to be either 'Y' or 'N'; can use bool for more clarity
#     is_nullable: Optional[str]  # Same as above, can also consider bool
#     notes: Optional[str]
#     validate: Optional[str]


# @dataclass
# class ExportRecord:
#     ExportID: Optional[int]  # S32 (primary key)
#     SourceType: Optional[int]  # I (identifies source database type)
#     SourceID: Optional[str]  # S32 (foreign key, valid format if SourceType = 1)
#     SourceName: Optional[str]  # S50 (name of source organization)
#     SourceContactFirst: Optional[str]  # S50 (first name of contact)
#     SourceContactLast: Optional[str]  # S50 (last name of contact)
#     SourceContactPhone: Optional[str]  # S10 (10-digit phone number)
#     SourceContactExtension: Optional[str]  # S5 (phone extension)
#     SourceContactEmail: Optional[str]  # S320 (valid email address)
#     ExportDate: Optional[str]  # T (timestamp or valid date string)
#     ExportStartDate: Optional[str]  # D (start date)
#     ExportEndDate: Optional[str]  # D (end date)
#     SoftwareName: Optional[str]  # S50 (name of software)
#     SoftwareVersion: Optional[str]  # S50 (software version)
#     CSVVersion: Optional[str]  # S50 (CSV specification version)
#     ExportPeriodType: Optional[float]  # I (export period type)
#     ExportDirective: Optional[float]  # I (export directive)
#     HashStatus: Optional[float]  # I (hash status)
#     ImplementationID: Optional[str]  # S200 (unique vendor-generated ID)


# @dataclass
# class Funder:
#     funder_id: Optional[str]  # FunderID, primary key (pk) - S32
#     project_id: Optional[str]  # ProjectID, foreign key (fk) - S32
#     funder: Optional[str]  # Funder - I (specific version)
#     other_funder: Optional[str]  # OtherFunder - S100
#     grant_id: Optional[str]  # GrantID, foreign key (fk) - S100
#     start_date: Optional[datetime]  # StartDate - D
#     end_date: Optional[datetime]  # EndDate - D
#     date_created: Optional[datetime]  # DateCreated - T
#     date_updated: Optional[datetime]  # DateUpdated - T
#     user_id: Optional[str]  # UserID, foreign key (fk) - S32
#     date_deleted: Optional[datetime]  # DateDeleted - T
#     export_id: Optional[str]  # ExportID, foreign key (fk) - S32

#     def __post_init__(self):
#         # Input validation could go here if required
#         pass


# @dataclass
# class HealthAndDVRecord:
#     csv: str
#     element_num: Optional[str]  # Optional because it can be 'nan'
#     name: str
#     key_type: Optional[str]  # Optional because it can be 'nan'
#     relationship_desc: Optional[str]  # Optional because it can be 'nan'
#     field_to_csv_relationship: Optional[str]  # Optional because it can be 'nan'
#     type: str
#     list: Optional[str]  # Optional because it can be 'nan'
#     null: Optional[str]  # Optional because it can be 'nan'
#     notes: Optional[str]  # Optional because it can be 'nan'
#     validate: Optional[str]  # Optional because it can be 'nan'


# @dataclass
# class HMISParticipation:
#     HMISParticipationID: str  # Unique identifier (pk)
#     ProjectID: Optional[str] = field(default=None)  # Foreign key (fk)
#     HMISParticipationType: Optional[str] = field(default=None)  # Type
#     HMISParticipationStatusStartDate: Optional[date] = field(default=None)  # Date
#     HMISParticipationStatusEndDate: Optional[date] = field(default=None)  # Date
#     DateCreated: Optional[datetime] = field(default=None)  # Timestamp
#     DateUpdated: Optional[datetime] = field(default=None)  # Timestamp
#     UserID: Optional[str] = field(default=None)  # Foreign key (fk)
#     DateDeleted: Optional[date] = field(default=None)  # Date
#     ExportID: Optional[str] = field(default=None)  # Foreign key (fk)

#     def __post_init__(self):
#         # Custom validation can be added here if needed
#         pass


# @dataclass
# class IncomeBenefits:
#     income_benefits_id: Optional[str] = field(
#         metadata={"description": "Unique identifier"}
#     )
#     enrollment_id: Optional[str] = field(default=None)
#     personal_id: Optional[str] = field(default=None)
#     information_date: Optional[str] = field(
#         default=None
#     )  # Assuming this is a string, format could vary
#     income_from_any_source: Optional[float] = field(default=None)
#     total_monthly_income: Optional[float] = field(default=None)
#     earned: Optional[float] = field(default=None)
#     earned_amount: Optional[float] = field(default=None)
#     unemployment: Optional[float] = field(default=None)
#     unemployment_amount: Optional[float] = field(default=None)
#     ssi: Optional[float] = field(default=None)
#     ssi_amount: Optional[float] = field(default=None)
#     ssdi: Optional[float] = field(default=None)
#     ssdi_amount: Optional[float] = field(default=None)
#     va_disability_service: Optional[float] = field(default=None)
#     va_disability_service_amount: Optional[float] = field(default=None)
#     va_disability_non_service: Optional[float] = field(default=None)
#     va_disability_non_service_amount: Optional[float] = field(default=None)
#     private_disability: Optional[float] = field(default=None)
#     private_disability_amount: Optional[float] = field(default=None)
#     workers_comp: Optional[float] = field(default=None)
#     workers_comp_amount: Optional[float] = field(default=None)
#     tanf: Optional[float] = field(default=None)
#     tanf_amount: Optional[float] = field(default=None)
#     ga: Optional[float] = field(default=None)
#     ga_amount: Optional[float] = field(default=None)
#     soc_sec_retirement: Optional[float] = field(default=None)
#     soc_sec_retirement_amount: Optional[float] = field(default=None)
#     pension: Optional[float] = field(default=None)
#     pension_amount: Optional[float] = field(default=None)
#     child_support: Optional[float] = field(default=None)
#     child_support_amount: Optional[float] = field(default=None)
#     alimony: Optional[float] = field(default=None)
#     alimony_amount: Optional[float] = field(default=None)
#     other_income_source: Optional[float] = field(default=None)
#     other_income_amount: Optional[float] = field(default=None)
#     other_income_source_identify: Optional[str] = field(
#         default=None
#     )  # Conditional based on other fields
#     benefits_from_any_source: Optional[float] = field(default=None)
#     snap: Optional[float] = field(default=None)
#     wic: Optional[float] = field(default=None)
#     tanf_child_care: Optional[float] = field(default=None)
#     tanf_transportation: Optional[float] = field(default=None)
#     other_tanf: Optional[float] = field(default=None)
#     other_benefits_source: Optional[float] = field(default=None)
#     other_benefits_source_identify: Optional[str] = field(
#         default=None
#     )  # Conditional based on other fields
#     insurance_from_any_source: Optional[float] = field(default=None)
#     medicaid: Optional[float] = field(default=None)
#     no_medicaid_reason: Optional[float] = field(
#         default=None
#     )  # Conditional based on medicaid
#     medicare: Optional[float] = field(default=None)
#     no_medicare_reason: Optional[float] = field(
#         default=None
#     )  # Conditional based on medicare
#     schip: Optional[float] = field(default=None)
#     no_schip_reason: Optional[float] = field(default=None)  # Conditional based on schip
#     vha_services: Optional[float] = field(default=None)
#     no_vha_reason: Optional[float] = field(
#         default=None
#     )  # Conditional based on vha_services
#     employer_provided: Optional[float] = field(default=None)
#     no_employer_provided_reason: Optional[float] = field(
#         default=None
#     )  # Conditional based on employer_provided
#     cobra: Optional[float] = field(default=None)
#     no_cobra_reason: Optional[float] = field(default=None)  # Conditional based on cobra
#     private_pay: Optional[float] = field(default=None)
#     no_private_pay_reason: Optional[float] = field(
#         default=None
#     )  # Conditional based on private_pay
#     state_health_ins: Optional[float] = field(default=None)
#     no_state_health_ins_reason: Optional[float] = field(
#         default=None
#     )  # Conditional based on state_health_ins
#     indian_health_services: Optional[float] = field(default=None)
#     no_indian_health_services_reason: Optional[float] = field(
#         default=None
#     )  # Conditional based on indian_health_services
#     other_insurance: Optional[float] = field(default=None)
#     other_insurance_identify: Optional[str] = field(
#         default=None
#     )  # Conditional based on other_insurance
#     adap: Optional[float] = field(default=None)
#     no_adap_reason: Optional[float] = field(default=None)  # Conditional based on adap
#     ryan_white_med_dent: Optional[float] = field(default=None)
#     no_ryan_white_reason: Optional[float] = field(
#         default=None
#     )  # Conditional based on ryan_white_med_dent
#     connection_with_soar: Optional[float] = field(default=None)
#     data_collection_stage: Optional[float] = field(default=None)
#     date_created: Optional[str] = field(
#         default=None
#     )  # Assuming string representation of datetime
#     date_updated: Optional[str] = field(
#         default=None
#     )  # Assuming string representation of datetime
#     user_id: Optional[str] = field(default=None)
#     date_deleted: Optional[str] = field(default=None)  # Nullable
#     export_id: Optional[str] = field(default=None)


# @dataclass
# class Inventory:
#     csv: Optional[str] = None
#     element_num: Optional[Union[str, float]] = None
#     name: str = ""
#     key_type: Optional[str] = None
#     relationship_desc: Optional[str] = None
#     field_to_csv_relationship: Optional[str] = None
#     type: Optional[str] = None
#     list: Optional[str] = None
#     null: Optional[str] = None
#     notes: Optional[str] = None
#     validate: Optional[str] = None


# @dataclass
# class Organization:
#     # Unique identifier
#     organization_id: Optional[str]  # S32, pk
#     organization_name: Optional[str]  # S200
#     victim_service_provider: Optional[int]  # I
#     organization_common_name: Optional[str]  # S200, nullable
#     date_created: Optional[str]  # T
#     date_updated: Optional[str]  # T
#     user_id: Optional[str]  # S32, fk, many_to_many
#     date_deleted: Optional[str]  # T, nullable
#     export_id: Optional[str]  # S32, fk, many_to_one

#     notes: Optional[str] = None  # Additional notes field


# @dataclass
# class Project:
#     ProjectID: Optional[str] = field(default=None)  # pk
#     OrganizationID: Optional[str] = field(default=None)  # fk
#     ProjectName: Optional[str] = field(default=None)
#     ProjectCommonName: Optional[str] = field(default=None)
#     OperatingStartDate: Optional[date] = field(default=None)
#     OperatingEndDate: Optional[date] = field(default=None)
#     ContinuumProject: Optional[int] = field(default=None)
#     ProjectType: Optional[int] = field(default=None)
#     HousingType: Optional[int] = field(default=None)
#     RRHSubType: Optional[int] = field(default=None)
#     ResidentialAffiliation: Optional[int] = field(default=None)
#     TargetPopulation: Optional[int] = field(default=None)
#     HOPWAMedAssistedLivingFac: Optional[int] = field(default=None)
#     PITCount: Optional[int] = field(default=None)
#     DateCreated: Optional[date] = field(default=None)
#     DateUpdated: Optional[date] = field(default=None)
#     UserID: Optional[str] = field(default=None)  # fk
#     DateDeleted: Optional[date] = field(default=None)
#     ExportID: Optional[str] = field(default=None)  # fk

#     # Additional fields might be needed for validation, notes, and other CSV-specific attributes if required
#     notes: Optional[str] = field(
#         default=None
#     )  # To store any additional notes if necessary

#     def __post_init__(self):
#         # Here you can add any validation logic specific to your requirements
#         pass


# @dataclass
# class ProjectCoC:
#     project_co_c_id: str  # ProjectCoCID (pk)
#     project_id: Optional[str] = None  # ProjectID (fk, must match a ProjectID)
#     coc_code: Optional[str] = None  # CoCCode
#     geocode_1: Optional[str] = None  # Geocode[1]
#     address1: Optional[str] = None  # Address1
#     address2: Optional[str] = None  # Address2
#     city: Optional[str] = None  # City
#     state: Optional[str] = None  # State (limited to 2-letter USPS codes)
#     zip_code: Optional[str] = None  # ZIP (limited to 5 digits)
#     geography_type: Optional[int] = None  # GeographyType (refers to Address2)
#     date_created: Optional[datetime] = None  # DateCreated
#     date_updated: Optional[datetime] = None  # DateUpdated
#     user_id: Optional[str] = None  # UserID (fk)
#     date_deleted: Optional[datetime] = None  # DateDeleted
#     export_id: Optional[str] = None  # ExportID (fk, must match an ExportID)


# @dataclass
# class ServiceField:
#     csv: Optional[str] = field(default=None)
#     element_num: Optional[str] = field(default=None)
#     name: str = field(default_factory=str)
#     key_type: Optional[str] = field(default=None)
#     relationship_desc: Optional[str] = field(default=None)
#     field_to_csv_relationship: Optional[str] = field(default=None)
#     type: str = field(default_factory=str)
#     list: Optional[str] = field(default=None)
#     null: Optional[str] = field(default=None)
#     notes: Optional[str] = field(default=None)
#     validate: Optional[str] = field(default=None)


# @dataclass
# class User:
#     element_num: float
#     name: str
#     key_type: Optional[str]
#     relationship_desc: Optional[str]
#     field_to_csv_relationship: Optional[str]
#     type: str
#     list: Optional[str]
#     null: Optional[str]
#     notes: Optional[str]
#     validate: Optional[str]
