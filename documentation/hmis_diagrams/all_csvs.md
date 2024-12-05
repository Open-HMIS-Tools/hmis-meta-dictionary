```mermaid
erDiagram
    Assessment {
         S32 AssessmentID
         S32 EnrollmentID
         S32 PersonalID
         D AssessmentDate
         S250 AssessmentLocation
         I AssessmentType
         I AssessmentLevel
         I PrioritizationStatus
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    Inventory {
         S32 InventoryID
         S32 ProjectID
         S6 CoCCode
         I HouseholdType
         I Availability
         I UnitInventory
         I BedInventory
         I CHVetBedInventory
         I YouthVetBedInventory
         I VetBedInventory
         I CHYouthBedInventory
         I YouthBedInventory
         I CHBedInventory
         I OtherBedInventory
         I ESBedType
         D InventoryStartDate
         D InventoryEndDate
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    Services {
         S32 ServicesID
         S32 EnrollmentID
         S32 PersonalID
         D DateProvided
         I RecordType
         I TypeProvided
         S50 OtherTypeProvided
         S50 OtherTypeProvided
         S50 MovingOnOtherType
         I SubTypeProvided
         I SubTypeProvided
         I SubTypeProvided
         M FAAmount
         M FAAmount
         D FAStartDate
         D FAEndDate
         I ReferralOutcome
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    Organization {
         S32  OrganizationID
         S200  OrganizationName
         I  VictimServiceProvider
         S200  OrganizationCommonName
         T  DateCreated
         T  DateUpdated
         S32  UserID
         T  DateDeleted
         S32  ExportID
    }
    HMISParticipation {
         S32 HMISParticipationID
         S32 ProjectID
         I HMISParticipationType
         D HMISParticipationStatusStartDate
         D HMISParticipationStatusEndDate
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S ExportID
    }
    YouthEducationStatus {
         S32 YouthEducationStatusID
         S32 EnrollmentID
         S32 PersonalID
         D InformationDate
         I CurrentSchoolAttend
         I MostRecentEdStatus
         I CurrentEdStatus
         I DataCollectionStage
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    Funder {
         S32 FunderID
         S32 ProjectID
         I Funder
         S100 OtherFunder
         S100 GrantID
         D StartDate
         D EndDate
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    Disabilities {
         S32 DisabilitiesID
         S32 EnrollmentID
         S32 PersonalID
         D InformationDate
         I DisabilityType
         I DisabilityResponse
         I IndefiniteAndImpairs
         I TCellCountAvailable
         I TCellCount
         I TCellSource
         I ViralLoadAvailable
         I ViralLoad
         I ViralLoadSource
         I AntiRetroviral
         I DataCollectionStage
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    User {
         S32 UserID
         S50 UserFirstName
         S50 UserLastName
         S10 UserPhone
         S5 UserExtension
         S320 UserEmail
         T DateCreated
         T DateUpdated
         T DateDeleted
         S32 ExportID
    }
    HealthAndDV {
         S32 HealthAndDVID
         S32 EnrollmentID
         S32 PersonalID
         D InformationDate
         I DomesticViolenceSurvivor
         I WhenOccurred
         I CurrentlyFleeing
         I GeneralHealthStatus
         I DentalHealthStatus
         I MentalHealthStatus
         I PregnancyStatus
         D DueDate
         I DataCollectionStage
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    Exit {
         S32 ExitID
         S32 EnrollmentID
         S32 PersonalID
         D ExitDate
         I Destination
         I DestinationSubsidyType
         S50 OtherDestination
         I HousingAssessment
         I SubsidyInformation
         I SubsidyInformation
         I ProjectCompletionStatus
         I EarlyExitReason
         I ExchangeForSex
         I ExchangeForSexPastThreeMonths
         I CountOfExchangeForSex
         I AskedOrForcedToExchangeForSex
         I AskedOrForcedToExchangeForSexPastThreeMonths
         I WorkplaceViolenceThreats
         I WorkplacePromiseDifference
         I CoercedToContinueWork
         I LaborExploitPastThreeMonths
         I CounselingReceived
         I IndividualCounseling
         I FamilyCounseling
         I GroupCounseling
         I SessionCountAtExit
         I PostExitCounselingPlan
         I SessionsInPlan
         I DestinationSafeClient
         I DestinationSafeWorker
         I PosAdultConnections
         I PosPeerConnections
         I PosCommunityConnections
         D AftercareDate
         I AftercareProvided
         I EmailSocialMedia
         I Telephone
         I InPersonIndividual
         I InPersonGroup
         I CMExitReason
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    Enrollment {
         S32 EnrollmentID
         S32 PersonalID
         S32 ProjectID
         D EntryDate
         S32 HouseholdID
         I RelationshipToHoH
         S6 EnrollmentCoC
         I LivingSituation
         I RentalSubsidyType
         I LengthOfStay
         I LOSUnderThreshold
         I LOSUnderThreshold
         I PreviousStreetESSH
         D DateToStreetESSH
         I TimesHomelessPastThreeYears
         I MonthsHomelessPastThreeYears
         I DisablingCondition
         D DateOfEngagement
         D MoveInDate
         D DateOfPATHStatus
         I ClientEnrolledInPATH
         I ReasonNotEnrolled
         I PercentAMI
         I ReferralSource
         I CountOutreachReferralApproaches
         D DateOfBCPStatus
         I EligibleForRHY
         I ReasonNoServices
         I RunawayYouth
         I SexualOrientation
         S100 SexualOrientationOther
         I FormerWardChildWelfare
         I ChildWelfareYears
         I ChildWelfareMonths
         I FormerWardJuvenileJustice
         I JuvenileJusticeYears
         I JuvenileJusticeMonths
         I UnemploymentFam
         I MentalHealthDisorderFam
         I PhysicalDisabilityFam
         I AlcoholDrugUseDisorderFam
         I InsufficientIncome
         I IncarceratedParent
         S5 VAMCStation
         I TargetScreenReqd
         I TimeToHousingLoss
         I AnnualPercentAMI
         I LiteralHomelessHistory
         I ClientLeaseholder
         I HOHLeaseholder
         I SubsidyAtRisk
         I EvictionHistory
         I CriminalRecord
         I IncarceratedAdult
         I PrisonDischarge
         I SexOffender
         I DisabledHoH
         I CurrentPregnant
         I SingleParent
         I DependentUnder6
         I HH5Plus
         I CoCPrioritized
         I HPScreeningScore
         I ThresholdScore
         I TranslationNeeded
         I PreferredLanguage
         S100 PreferredLanguageDifferent
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    Event {
         S32 EventID
         S32 EnrollmentID
         S32 PersonalID
         D EventDate
         I Event
         I ProbSolDivRRResult
         I ReferralCaseManageAfter
         S250 LocationCrisisOrPHHousing
         I ReferralResult
         D ResultDate
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    ProjectCoC {
         S32 ProjectCoCID
         S32 ProjectID
         S6 CoCCode
         S6 Geocode[1]
         S100 Address1
         S100 Address2
         S50 City
         S2 State
         S5 ZIP
         I GeographyType
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    Affiliation {
         S32 AffiliationID
         S32 ProjectID
         S32 ResProjectID
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S ExportID
    }
    Project {
         S32 ProjectID
         S32 OrganizationID
         S200 ProjectName
         S200 ProjectCommonName
         D OperatingStartDate
         D OperatingEndDate
         I ContinuumProject
         I ProjectType
         I HousingType
         I RRHSubType
         I ResidentialAffiliation
         I TargetPopulation
         I HOPWAMedAssistedLivingFac
         I PITCount
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    CurrentLivingSituation {
         S32 CurrentLivingSitID
         S32 EnrollmentID
         S32 PersonalID
         D InformationDate
         I CurrentLivingSituation
         I CLSSubsidyType
         S100 VerifiedBy
         I LeaveSituation14Days
         I SubsequentResidence
         I ResourcesToObtain
         I LeaseOwn60Day
         I MovedTwoOrMore
         S250 LocationDetails
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    EmploymentEducation {
         S32 EmploymentEducationID
         S32 EnrollmentID
         S32 PersonalID
         D InformationDate
         I LastGradeCompleted
         I SchoolStatus
         I Employed
         I EmploymentType
         I NotEmployedReason
         I DataCollectionStage
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    Client {
         S32 PersonalID
         S50 FirstName
         S50 MiddleName
         S50 LastName
         S50 NameSuffix
         I NameDataQuality
         S9 SSN[1]
         I SSNDataQuality
         D DOB
         I DOBDataQuality
         I AmIndAKNative
         I Asian
         I BlackAfAmerican
         I HispanicLatinaeo
         I MidEastNAfrican
         I NativeHIPacific
         I White
         I RaceNone
         S100 AdditionalRaceEthnicity
         I Woman
         I Man
         I NonBinary
         I CulturallySpecific
         I Transgender
         I Questioning
         I DifferentIdentity
         I GenderNone
         S100 DifferentIdentityText
         I VeteranStatus
         I YearEnteredService
         I YearSeparated
         I WorldWarII
         I KoreanWar
         I VietnamWar
         I DesertStorm
         I AfghanistanOEF
         I IraqOIF
         I IraqOND
         I OtherTheater
         I MilitaryBranch
         I DischargeStatus
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    AssessmentResults {
         S32 AssessmentResultID
         S32 AssessmentID
         S32 EnrollmentID
         S32 PersonalID
         S250 AssessmentResultType
         S250 AssessmentResult
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    IncomeBenefits {
         S32 IncomeBenefitsID
         S32 EnrollmentID
         S32 PersonalID
         D InformationDate
         I IncomeFromAnySource
         M+ TotalMonthlyIncome
         I Earned
         M+ EarnedAmount
         I Unemployment
         M+ UnemploymentAmount
         I SSI
         M+ SSIAmount
         I SSDI
         M+ SSDIAmount
         I VADisabilityService
         M+ VADisabilityServiceAmount
         I VADisabilityNonService
         M+ VADisabilityNonServiceAmount
         I PrivateDisability
         M+ PrivateDisabilityAmount
         I WorkersComp
         M+ WorkersCompAmount
         I TANF
         M+ TANFAmount
         I GA
         M+ GAAmount
         I SocSecRetirement
         M+ SocSecRetirementAmount
         I Pension
         M+ PensionAmount
         I ChildSupport
         M+ ChildSupportAmount
         I Alimony
         M+ AlimonyAmount
         I OtherIncomeSource
         M+ OtherIncomeAmount
         S50 OtherIncomeSourceIdentify
         I BenefitsFromAnySource
         I SNAP
         I WIC
         I TANFChildCare
         I TANFTransportation
         I OtherTANF
         I OtherBenefitsSource
         S50 OtherBenefitsSourceIdentify
         I InsuranceFromAnySource
         I Medicaid
         I NoMedicaidReason
         I Medicare
         I NoMedicareReason
         I SCHIP
         I NoSCHIPReason
         I VHAServices
         I NoVHAReason
         I EmployerProvided
         I NoEmployerProvidedReason
         I COBRA
         I NoCOBRAReason
         I PrivatePay
         I NoPrivatePayReason
         I StateHealthIns
         I NoStateHealthInsReason
         I IndianHealthServices
         I NoIndianHealthServicesReason
         I OtherInsurance
         S50 OtherInsuranceIdentify
         I ADAP
         I NoADAPReason
         I RyanWhiteMedDent
         I NoRyanWhiteReason
         I ConnectionWithSOAR
         I DataCollectionStage
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    CEParticipation {
         S32 CEParticipationID
         S32 ProjectID
         I AccessPoint
         I PreventionAssessment
         I CrisisAssessment
         I HousingAssessment
         I DirectServices
         I ReceivesReferrals
         D CEParticipationStatusStartDate
         D CEParticipationStatusEndDate
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S ExportID
    }
    AssessmentQuestions {
         S32 AssessmentQuestionID
         S32 AssessmentID
         S32 EnrollmentID
         S32 PersonalID
         S250 AssessmentQuestionGroup
         I AssessmentQuestionOrder
         S250 AssessmentQuestion
         S500 AssessmentAnswer
         T DateCreated
         T DateUpdated
         S32 UserID
         T DateDeleted
         S32 ExportID
    }
    Export ||--|| Source : SourceID
    Export ||--|| Implementation : ImplementationID
    Organization ||--|| User : UserID
    Project ||--|| Organization : OrganizationID
    Project ||--|| User : UserID
    Funder ||--|| Project : ProjectID
    Funder ||--|| Grant : GrantID
    Funder ||--|| User : UserID
    ProjectCoC ||--|| Project : ProjectID
    ProjectCoC ||--|| User : UserID
    Inventory ||--|| Project : ProjectID
    Inventory ||--|| User : UserID
    Affiliation ||--|| Project : ProjectID
    Affiliation ||--|| ResProject : ResProjectID
    Affiliation ||--|| User : UserID
    HMISParticipation ||--|| Project : ProjectID
    HMISParticipation ||--|| User : UserID
    CEParticipation ||--|| Project : ProjectID
    CEParticipation ||--|| User : UserID
    Client ||--|| User : UserID
    Enrollment ||--|| Client : PersonalID
    Enrollment ||--|| Project : ProjectID
    Enrollment ||--|| Client : HouseholdID
    Enrollment ||--|| User : UserID
    Exit ||--|| Enrollment : EnrollmentID
    Exit ||--|| Client : PersonalID
    Exit ||--|| User : UserID
    IncomeBenefits ||--|| Enrollment : EnrollmentID
    IncomeBenefits ||--|| Client : PersonalID
    IncomeBenefits ||--|| User : UserID
    HealthAndDV ||--|| Enrollment : EnrollmentID
    HealthAndDV ||--|| Client : PersonalID
    HealthAndDV ||--|| User : UserID
    EmploymentEducation ||--|| Enrollment : EnrollmentID
    EmploymentEducation ||--|| Client : PersonalID
    EmploymentEducation ||--|| User : UserID
    Disabilities ||--|| Enrollment : EnrollmentID
    Disabilities ||--|| Client : PersonalID
    Disabilities ||--|| User : UserID
    Services ||--|| Enrollment : EnrollmentID
    Services ||--|| Client : PersonalID
    Services ||--|| User : UserID
    CurrentLivingSituation ||--|| Enrollment : EnrollmentID
    CurrentLivingSituation ||--|| Client : PersonalID
    CurrentLivingSituation ||--|| User : UserID
    Assessment ||--|| Enrollment : EnrollmentID
    Assessment ||--|| Client : PersonalID
    Assessment ||--|| User : UserID
    AssessmentQuestions ||--|| Assessment : AssessmentID
    AssessmentQuestions ||--|| Enrollment : EnrollmentID
    AssessmentQuestions ||--|| Client : PersonalID
    AssessmentQuestions ||--|| User : UserID
    AssessmentResults ||--|| Assessment : AssessmentID
    AssessmentResults ||--|| Enrollment : EnrollmentID
    AssessmentResults ||--|| Client : PersonalID
    AssessmentResults ||--|| User : UserID
    Event ||--|| Enrollment : EnrollmentID
    Event ||--|| Client : PersonalID
    Event ||--|| User : UserID
    YouthEducationStatus ||--|| Enrollment : EnrollmentID
    YouthEducationStatus ||--|| Client : PersonalID
    YouthEducationStatus ||--|| User : UserID

```