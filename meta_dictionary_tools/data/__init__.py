ALL_CSV_NAMES = [
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
]

ALL_LSA_CSV_NAMES = [
    "Affiliation",
    "Funder",
    "HMISParticipation",
    "Inventory",
    "LSACalculated",
    "LSAExit",
    "LSAHousehold",
    "LSAPerson",
    "LSAReport",
    "Organization",
    "Project",
    "ProjectCoC",
]

FUNDER_FIELDS = [
    "FunderID",
    "ProjectID",
    "Funder",
    "OtherFunder",
    "GrantID",
    "StartDate",
    "EndDate",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

INCOMEBENEFITS_FIELDS = [
    "IncomeBenefitsID",
    "EnrollmentID",
    "PersonalID",
    "InformationDate",
    "IncomeFromAnySource",
    "TotalMonthlyIncome",
    "Earned",
    "EarnedAmount",
    "Unemployment",
    "UnemploymentAmount",
    "SSI",
    "SSIAmount",
    "SSDI",
    "SSDIAmount",
    "VADisabilityService",
    "VADisabilityServiceAmount",
    "VADisabilityNonService",
    "VADisabilityNonServiceAmount",
    "PrivateDisability",
    "PrivateDisabilityAmount",
    "WorkersComp",
    "WorkersCompAmount",
    "TANF",
    "TANFAmount",
    "GA",
    "GAAmount",
    "SocSecRetirement",
    "SocSecRetirementAmount",
    "Pension",
    "PensionAmount",
    "ChildSupport",
    "ChildSupportAmount",
    "Alimony",
    "AlimonyAmount",
    "OtherIncomeSource",
    "OtherIncomeAmount",
    "OtherIncomeSourceIdentify",
    "BenefitsFromAnySource",
    "SNAP",
    "WIC",
    "TANFChildCare",
    "TANFTransportation",
    "OtherTANF",
    "OtherBenefitsSource",
    "OtherBenefitsSourceIdentify",
    "InsuranceFromAnySource",
    "Medicaid",
    "NoMedicaidReason",
    "Medicare",
    "NoMedicareReason",
    "SCHIP",
    "NoSCHIPReason",
    "VHAServices",
    "NoVHAReason",
    "EmployerProvided",
    "NoEmployerProvidedReason",
    "COBRA",
    "NoCOBRAReason",
    "PrivatePay",
    "NoPrivatePayReason",
    "StateHealthIns",
    "NoStateHealthInsReason",
    "IndianHealthServices",
    "NoIndianHealthServicesReason",
    "OtherInsurance",
    "OtherInsuranceIdentify",
    "ADAP",
    "NoADAPReason",
    "RyanWhiteMedDent",
    "NoRyanWhiteReason",
    "ConnectionWithSOAR",
    "DataCollectionStage",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

HEALTHANDDV_FIELDS = [
    "HealthAndDVID",
    "EnrollmentID",
    "PersonalID",
    "InformationDate",
    "DomesticViolenceSurvivor",
    "WhenOccurred",
    "CurrentlyFleeing",
    "GeneralHealthStatus",
    "DentalHealthStatus",
    "MentalHealthStatus",
    "PregnancyStatus",
    "DueDate",
    "DataCollectionStage",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

CEPARTICIPATION_FIELDS = [
    "CEParticipationID",
    "ProjectID",
    "AccessPoint",
    "PreventionAssessment",
    "CrisisAssessment",
    "HousingAssessment",
    "DirectServices",
    "ReceivesReferrals",
    "CEParticipationStatusStartDate",
    "CEParticipationStatusEndDate",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

ASSESSMENTRESULTS_FIELDS = [
    "AssessmentResultID",
    "AssessmentID",
    "EnrollmentID",
    "PersonalID",
    "AssessmentResultType",
    "AssessmentResult",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

ENROLLMENT_FIELDS = [
    "EnrollmentID",
    "PersonalID",
    "ProjectID",
    "EntryDate",
    "HouseholdID",
    "RelationshipToHoH",
    "EnrollmentCoC",
    "LivingSituation",
    "RentalSubsidyType",
    "LengthOfStay",
    "LOSUnderThreshold",
    "LOSUnderThreshold",
    "PreviousStreetESSH",
    "DateToStreetESSH",
    "TimesHomelessPastThreeYears",
    "MonthsHomelessPastThreeYears",
    "DisablingCondition",
    "DateOfEngagement",
    "MoveInDate",
    "DateOfPATHStatus",
    "ClientEnrolledInPATH",
    "ReasonNotEnrolled",
    "PercentAMI",
    "ReferralSource",
    "CountOutreachReferralApproaches",
    "DateOfBCPStatus",
    "EligibleForRHY",
    "ReasonNoServices",
    "RunawayYouth",
    "SexualOrientation",
    "SexualOrientationOther",
    "FormerWardChildWelfare",
    "ChildWelfareYears",
    "ChildWelfareMonths",
    "FormerWardJuvenileJustice",
    "JuvenileJusticeYears",
    "JuvenileJusticeMonths",
    "UnemploymentFam",
    "MentalHealthDisorderFam",
    "PhysicalDisabilityFam",
    "AlcoholDrugUseDisorderFam",
    "InsufficientIncome",
    "IncarceratedParent",
    "VAMCStation",
    "TargetScreenReqd",
    "TimeToHousingLoss",
    "AnnualPercentAMI",
    "LiteralHomelessHistory",
    "ClientLeaseholder",
    "HOHLeaseholder",
    "SubsidyAtRisk",
    "EvictionHistory",
    "CriminalRecord",
    "IncarceratedAdult",
    "PrisonDischarge",
    "SexOffender",
    "DisabledHoH",
    "CurrentPregnant",
    "SingleParent",
    "DependentUnder6",
    "HH5Plus",
    "CoCPrioritized",
    "HPScreeningScore",
    "ThresholdScore",
    "TranslationNeeded",
    "PreferredLanguage",
    "PreferredLanguageDifferent",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

EXIT_FIELDS = [
    "ExitID",
    "EnrollmentID",
    "PersonalID",
    "ExitDate",
    "Destination",
    "DestinationSubsidyType",
    "OtherDestination",
    "HousingAssessment",
    "SubsidyInformation",
    "SubsidyInformation",
    "ProjectCompletionStatus",
    "EarlyExitReason",
    "ExchangeForSex",
    "ExchangeForSexPastThreeMonths",
    "CountOfExchangeForSex",
    "AskedOrForcedToExchangeForSex",
    "AskedOrForcedToExchangeForSexPastThreeMonths",
    "WorkplaceViolenceThreats",
    "WorkplacePromiseDifference",
    "CoercedToContinueWork",
    "LaborExploitPastThreeMonths",
    "CounselingReceived",
    "IndividualCounseling",
    "FamilyCounseling",
    "GroupCounseling",
    "SessionCountAtExit",
    "PostExitCounselingPlan",
    "SessionsInPlan",
    "DestinationSafeClient",
    "DestinationSafeWorker",
    "PosAdultConnections",
    "PosPeerConnections",
    "PosCommunityConnections",
    "AftercareDate",
    "AftercareProvided",
    "EmailSocialMedia",
    "Telephone",
    "InPersonIndividual",
    "InPersonGroup",
    "CMExitReason",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

ASSESSMENT_FIELDS = [
    "AssessmentID",
    "EnrollmentID",
    "PersonalID",
    "AssessmentDate",
    "AssessmentLocation",
    "AssessmentType",
    "AssessmentLevel",
    "PrioritizationStatus",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

EXPORT_FIELDS = [
    "ExportID",
    "SourceType",
    "SourceID",
    "SourceName",
    "SourceContactFirst",
    "SourceContactLast",
    "SourceContactPhone",
    "SourceContactExtension",
    "SourceContactEmail",
    "ExportDate",
    "ExportStartDate",
    "ExportEndDate",
    "SoftwareName",
    "SoftwareVersion",
    "CSVVersion",
    "ExportPeriodType",
    "ExportDirective",
    "HashStatus",
    "ImplementationID",
]

YOUTHEDUCATIONSTATUS_FIELDS = [
    "YouthEducationStatusID",
    "EnrollmentID",
    "PersonalID",
    "InformationDate",
    "CurrentSchoolAttend",
    "MostRecentEdStatus",
    "CurrentEdStatus",
    "DataCollectionStage",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

PROJECTCOC_FIELDS = [
    "ProjectCoCID",
    "ProjectID",
    "CoCCode",
    "Geocode[1]",
    "Address1",
    "Address2",
    "City",
    "State",
    "ZIP",
    "GeographyType",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

EMPLOYMENTEDUCATION_FIELDS = [
    "EmploymentEducationID",
    "EnrollmentID",
    "PersonalID",
    "InformationDate",
    "LastGradeCompleted",
    "SchoolStatus",
    "Employed",
    "EmploymentType",
    "NotEmployedReason",
    "DataCollectionStage",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

USER_FIELDS = [
    "UserID",
    "UserFirstName",
    "UserLastName",
    "UserPhone",
    "UserExtension",
    "UserEmail",
    "DateCreated",
    "DateUpdated",
    "DateDeleted",
    "ExportID",
]

HMISPARTICIPATION_FIELDS = [
    "HMISParticipationID",
    "ProjectID",
    "HMISParticipationType",
    "HMISParticipationStatusStartDate",
    "HMISParticipationStatusEndDate",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

ORGANIZATION_FIELDS = [
    "OrganizationID ",
    "OrganizationName ",
    "VictimServiceProvider ",
    "OrganizationCommonName ",
    "DateCreated ",
    "DateUpdated ",
    "UserID ",
    "DateDeleted ",
    "ExportID ",
]

SERVICES_FIELDS = [
    "ServicesID",
    "EnrollmentID",
    "PersonalID",
    "DateProvided",
    "RecordType",
    "TypeProvided",
    "OtherTypeProvided",
    "OtherTypeProvided",
    "MovingOnOtherType",
    "SubTypeProvided",
    "SubTypeProvided",
    "SubTypeProvided",
    "FAAmount",
    "FAAmount",
    "FAStartDate",
    "FAEndDate",
    "ReferralOutcome",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

INVENTORY_FIELDS = [
    "InventoryID",
    "ProjectID",
    "CoCCode",
    "HouseholdType",
    "Availability",
    "UnitInventory",
    "BedInventory",
    "CHVetBedInventory",
    "YouthVetBedInventory",
    "VetBedInventory",
    "CHYouthBedInventory",
    "YouthBedInventory",
    "CHBedInventory",
    "OtherBedInventory",
    "ESBedType",
    "InventoryStartDate",
    "InventoryEndDate",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

EVENT_FIELDS = [
    "EventID",
    "EnrollmentID",
    "PersonalID",
    "EventDate",
    "Event",
    "ProbSolDivRRResult",
    "ReferralCaseManageAfter",
    "LocationCrisisOrPHHousing",
    "ReferralResult",
    "ResultDate",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

ASSESSMENTQUESTIONS_FIELDS = [
    "AssessmentQuestionID",
    "AssessmentID",
    "EnrollmentID",
    "PersonalID",
    "AssessmentQuestionGroup",
    "AssessmentQuestionOrder",
    "AssessmentQuestion",
    "AssessmentAnswer",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

AFFILIATION_FIELDS = [
    "AffiliationID",
    "ProjectID",
    "ResProjectID",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

CURRENTLIVINGSITUATION_FIELDS = [
    "CurrentLivingSitID",
    "EnrollmentID",
    "PersonalID",
    "InformationDate",
    "CurrentLivingSituation",
    "CLSSubsidyType",
    "VerifiedBy",
    "LeaveSituation14Days",
    "SubsequentResidence",
    "ResourcesToObtain",
    "LeaseOwn60Day",
    "MovedTwoOrMore",
    "LocationDetails",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

CLIENT_FIELDS = [
    "PersonalID",
    "FirstName",
    "MiddleName",
    "LastName",
    "NameSuffix",
    "NameDataQuality",
    "SSN[1]",
    "SSNDataQuality",
    "DOB",
    "DOBDataQuality",
    "AmIndAKNative",
    "Asian",
    "BlackAfAmerican",
    "HispanicLatinaeo",
    "MidEastNAfrican",
    "NativeHIPacific",
    "White",
    "RaceNone",
    "AdditionalRaceEthnicity",
    "Woman",
    "Man",
    "NonBinary",
    "CulturallySpecific",
    "Transgender",
    "Questioning",
    "DifferentIdentity",
    "GenderNone",
    "DifferentIdentityText",
    "VeteranStatus",
    "YearEnteredService",
    "YearSeparated",
    "WorldWarII",
    "KoreanWar",
    "VietnamWar",
    "DesertStorm",
    "AfghanistanOEF",
    "IraqOIF",
    "IraqOND",
    "OtherTheater",
    "MilitaryBranch",
    "DischargeStatus",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

PROJECT_FIELDS = [
    "ProjectID",
    "OrganizationID",
    "ProjectName",
    "ProjectCommonName",
    "OperatingStartDate",
    "OperatingEndDate",
    "ContinuumProject",
    "ProjectType",
    "HousingType",
    "RRHSubType",
    "ResidentialAffiliation",
    "TargetPopulation",
    "HOPWAMedAssistedLivingFac",
    "PITCount",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

DISABILITIES_FIELDS = [
    "DisabilitiesID",
    "EnrollmentID",
    "PersonalID",
    "InformationDate",
    "DisabilityType",
    "DisabilityResponse",
    "IndefiniteAndImpairs",
    "TCellCountAvailable",
    "TCellCount",
    "TCellSource",
    "ViralLoadAvailable",
    "ViralLoad",
    "ViralLoadSource",
    "AntiRetroviral",
    "DataCollectionStage",
    "DateCreated",
    "DateUpdated",
    "UserID",
    "DateDeleted",
    "ExportID",
]

FIELD_LOOKUP = {
    "Funder": FUNDER_FIELDS,
    "IncomeBenefits": INCOMEBENEFITS_FIELDS,
    "HealthAndDV": HEALTHANDDV_FIELDS,
    "CEParticipation": CEPARTICIPATION_FIELDS,
    "AssessmentResults": ASSESSMENTRESULTS_FIELDS,
    "Enrollment": ENROLLMENT_FIELDS,
    "Exit": EXIT_FIELDS,
    "Assessment": ASSESSMENT_FIELDS,
    "Export": EXPORT_FIELDS,
    "YouthEducationStatus": YOUTHEDUCATIONSTATUS_FIELDS,
    "ProjectCoC": PROJECTCOC_FIELDS,
    "EmploymentEducation": EMPLOYMENTEDUCATION_FIELDS,
    "User": USER_FIELDS,
    "HMISParticipation": HMISPARTICIPATION_FIELDS,
    "Organization": ORGANIZATION_FIELDS,
    "Services": SERVICES_FIELDS,
    "Inventory": INVENTORY_FIELDS,
    "Event": EVENT_FIELDS,
    "AssessmentQuestions": ASSESSMENTQUESTIONS_FIELDS,
    "Affiliation": AFFILIATION_FIELDS,
    "CurrentLivingSituation": CURRENTLIVINGSITUATION_FIELDS,
    "Client": CLIENT_FIELDS,
    "Project": PROJECT_FIELDS,
    "Disabilities": DISABILITIES_FIELDS,
}
