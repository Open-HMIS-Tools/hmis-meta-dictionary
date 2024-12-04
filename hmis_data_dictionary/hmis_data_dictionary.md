# FY 2024 HMIS Data Dictionary

![](_page_0_Picture_1.jpeg)

U.S. Department of Housing and Urban Development

> VERSION 1.6 RELEASED: MAY 2023 UPDATED: JUNE 2024

# Contents

| SUMMARY OF CHANGES . |
| --- |
| FY 2024 Revision History |
| FY2024 HMIS Data Standards . |
| Data Element Structure . |
| PROJECT DESCRIPTOR DATA ELEMENTS |
| 2.01 Organization Information. |
| 2.02 Project Information |
| 2.03 Continuum of Care Information |
| 2.06 Funding Sources . |
| 2.07 Bed and Unit Inventory Information |
| 2.08 HMIS Participation Status |
| 2.09 Coordinated Entry Participation Status. |
| UNIVERSAL DATA ELEMENTS. |
| 3.01 Name |
| 3.02 Social Security Number |
| 3.03 Date of Birth |
| 3.04 Race and Ethnicity |
| 3.06 Gender |
| 3.07 Veteran Status |
| 3.08 Disabling Condition . |
| 3.10 Project Start Date………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………… 27 |
| 3.11 Project Exit Date |
| 3.12 Destination . |
| 3.15 Relationship to Head of Household . |
| 3.16 Enrollment CoC |
| 3.20 Housing Move-In Date |
| 3.917 Prior Living Situation . |
| 3.917A Prior Living Situation |
| 3.917B Prior Living Situation |
| PROGRAM SPECIFIC DATA ELEMENTS |
| COMMON PROGRAM SPECIFIC DATA ELEMENTS. |
| 4.02 Income and Sources |
| 4.03 Non-Cash Benefits |
| 4.04 Health Insurance |
| 4.05 Physical Disability . |
| 4.06 Developmental Disability. |
| 4.07 Chronic Health Condition |
| 4.08 HIV/AIDS… |

| 4.09 Mental Health Disorder |
| --- |
| 4.10 Substance Use Disorder |
| 4.11 Domestic Violence . |
| 4.12 Current Living Situation |
| 4.13 Date of Engagement |
| 4.14 Bed-Night Date |
| 4.19 Coordinated Entry Assessment. |
| 4.20 Coordinated Entry Event . |
| FEDERAL PARTNER PROGRAM SPECIFIC DATA ELEMENTS |
| HUD-CoC Only Required Elements |
| C2 Moving On Assistance Provided . |
| C3 Youth Education Status |
| C4 Translation Assistance Needed . |
| HUD-HOPWA Only Required Elements |
| W1 Services Provided – HOPWA … |
| W2 Financial Assistance – HOPWA |
| W3 Medical Assistance |
| W4 T-Cell (CD4) and Viral Load . |
| W5 Housing Assessment at Exit… |
| W6 Prescribed Anti-Retroviral |
| HHS-PATH Only Required Elements |
| P1 Services Provided – PATH Funded … |
| P2 Referrals Provided – PATH … |
| P3 PATH Status . |
| P4 Connection with SOAR…………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………… 67 |
| HHS-RHY Only Required Elements . |
| R1 Referral Source |
| R2 RHY - BCP Status |
| R3 Sexual Orientation |
| R4 Last Grade Completed |
| R5 School Status ………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………… 72 |
| R6 Employment Status |
| R7 General Health Status |
| R8 Dental Health Status. |
| R9 Mental Health Status |
| R10 Pregnancy Status . |
| R11 Formerly a Ward of Child Welfare/Foster Care Agency |
| R12 Formerly a Ward of Juvenile Justice System |

| R13 Family Critical Issues |
| --- |
| R14 RHY Service Connections |
| R15 Commercial Sexual Exploitation/Sex Trafficking |
| R16 Labor Exploitation/Trafficking |
| R17 Project Completion Status. |
| R18 Counseling . |
| R19 Safe and Appropriate Exit |
| R20 Aftercare Plans |
| VA Required Elements |
| V1 Veteran's Information . |
| V2 Services Provided – SVF |
| V3 Financial Assistance – SSVF… |
| V4 Percent of AMI (SSVF Eligibility) |
| V6 VAMC Station Number………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………… 91 |
| V7 HP Targeting Criteria |
| V8 HUD-VASH Voucher Tracking |
| V9 HUD-VASH Exit Information. |
| METADATA ELEMENTS |
| 5.01 Date Created. |
| 5.02 Date Updated. |
| 5.03 Data Collection Stage . |
| 5.04 Information Date… |
| 5.05 Project Identifier… |
| 5.06 Enrollment Identifier . |
| 5.07 User Identifier . |
| 5.08 Personal Identifier . |
| 5.09 Household Identifier… |
| 5.10 Implementation Identifier . |
| REQUIRED COLLECTION POINTS AND METADATA ELEMENTS TABLE SUMMARY . |
| Required Collection Points |
| Data Elements with Multiple Collection Points |
| Data Elements with a Single Collection Point . |
| Base Metadata… |
| Project Identifier, Personal ID, and Household ID |
| Appendix A – Living Situation Information |
| Living Situation Option List . |
| Subsidy Types – Dependent Field, relies on Living Situation = 435 |

## SUMMARY OF CHANGES

#### FY 2024 Revision History

| Date | Versi | Element | Revisions |
| --- | --- | --- | --- |
|  | on |  |  |
| May 2023 | 1.0 | 2.02 Project | Remove "Emergency Shelter Tracking Method" |
|  |  | Information | Rename "Emergency Shelter – Night-by-Night" to existing emergency shelter |
|  |  |  | response option 1 |
|  |  |  | Add Response 0 – "Emergency Shelter - Entry Exit" response option Add Rapid |
|  |  |  | Re-housing subtype field |
|  |  |  | Add "RRH: Services Only" subtype to affiliation field |
|  |  |  | Remove HMIS Participating Project field from this element, create new |
|  |  |  | element for HMIS Participation Status |
|  |  |  | Change "domestic violence victim" to "survivor of domestic violence" in |
|  |  |  | target population |
|  |  | 2.06 Funding | Remove "49: HUD: CoC – Joint Component RRH/PSH" Remove "12: Rural |
|  |  | Sources | Housing Stability Assistance Program" Add "53: HUD – ESG RUSH" |
|  |  |  | Add "54: HUD: Unsheltered Special NOFO" Add "55: HUD: Rural Special |
|  |  |  | NOFO" |
|  |  | 2.07 Bed and | Change Project Type Applicability for RRH to only PH-Rapid Re-housing (RRH: |
|  |  | Unit | Housing with or without services) subtype |
|  |  | Inventory |  |
|  |  | Information |  |
|  |  | 2.08 HMIS | New Element for tracking HMIS participation – removing HMIS participation |
|  |  | Participation | field from project information PDDE |
|  |  | Status | Added comparable database participating |
|  |  | NEW |  |
|  |  | 2.09 | Add PDDE to identify projects acting as "access points" and projects that |
|  |  | Coordinated | accept referrals from CE |
|  |  | Entry |  |
|  |  | Participation |  |
|  |  | Status |  |
|  |  | NEW |  |
|  |  | 3.04 Race | Combine 3.04 Race and 3.05 Ethnicity into single element 3.04 Race and |
|  |  | and Ethnicity | Ethnicity Add response option for "Middle Eastern or North African" and add |
|  |  |  | "Hispanic/Latina/e/o" |
|  |  |  | Add text box to add detail |
|  |  | 3.05 | Combine with 3.04 Race element |
|  |  | Ethnicity |  |
|  |  | RETIRE |  |
|  |  | 3.06 Gender | Change Female to "Woman (Girl if child)" Change Male to "Man (Boy if child)" |
|  |  |  | Change "Gender other than…" to "Non-Binary" Add "Culturally Specific |
|  |  |  | Identity (e.g., Two-Spirit) |
|  |  |  | Add "Different Identity" and text box to add detail |

| 3.12 | Remove "or RHY Funded" from Field 101 in Appendix A |
| --- | --- |
| Destination | Separate Temporary and Permanent Situations into separate headers Re- |
|  | organize response options under headers |
|  | Re-number responses by adding a standard # to the beginning of each response |
|  | number based on category (i.e., 1xx for homeless situations, 2xx for |
|  | institutional situations, etc.) |
|  | Add dependency for permanent subsidized options |
| 3.16 | Change element name to "Enrollment CoC" |
| Enrollment | Change data collection stage to project start (only) |
| CoC | Update data collection instruction to tell users to record CoC code of project |
|  | funded to assist participant |
| 3.917A Prior | Add dependency for permanent subsidized options |
| Living |  |
| Situation |  |
| 3.917B Prior | Add dependency for permanent subsidized options |
| Living |  |
| Situation |  |
| 4.04 Health | Change Field 6 Response to say "Veteran's Health Administration (VHA)" |
| Insurance |  |
| 4.12 Current | Add dependency for permanent subsidized options |
| Living |  |
| Situation |  |
| 4.19 | Streamline and combine with 4.20 CE Event element into NEW element 4.21 |
| Coordinated | Coordinated Entry Activity |
| Entry |  |
| Assessment |  |
| RETIRE |  |
| 4.20 | Streamline and combine with 4.19 CE Assessment element into NEW element |
| Coordinated | 4.21 Coordinated Entry Activity |
| Entry Event |  |
| RETIRE |  |
| 4.21 | New element for tracking screening, assessments, and other CE activity in |
| Coordinated | single element |
| Entry Activity |  |
| NEW |  |
| C1 Wellbeing | Retired element; data no longer collected |
| RETIRE |  |
| C4 | New element added to assist CoCs with identifying if clients need translation |
| Translation | assistance and if so, what language |
| Assistance |  |
| Needed |  |
| NEW |  |
| W1 Services | Remove "disorder" from Substance Use services/treatment response |
| Provided – |  |
| HOPWA |  |
| W3 Medical | Renamed W3.2 to "Receiving AIDS Drug Assistance Program (ADAP)" and |
| Assistance | removed W3.A "If No for 'Receiving Public HIV/AIDS Medical Assistance' |
|  | Reason" |
| W5 Housing | Update response 7 to say "Jail/prison" and response 10 to say "Deceased" |
| Assessment |  |

| at Exit |  |
| --- | --- |
| R3 Sexual | Add HUD: CoC - PH: Permanent Supportive Housing to Funder: Program |
| Orientation | Component |
|  | required to collect |
| R14 RHY | Response label change – change "mother" to "client (person who gave birth)" |
| Service | in response 12 |
| Connections |  |
| R17 Project | Change response labels from "Youth" to "Client" |
| Completion |  |
| Status |  |
| R18 | Rephrase Field 1 label "Client received counseling" instead of "Counseling |
| Counseling | received |
|  | by client" |
| U1 Worst Housing | Retired element; data no longer collected |
| Situation |  |
| RETIRE |  |
| V1 Veteran's | Add "Space Force" response option |
| Information |  |
| V2 Services | Change response 7 to "Shallow Subsidy" |
| Provided – |  |
| ટટ્ટાન |  |
| V3 Financial | Change Field 1 to "Start Date of Financial Assistance" |
| Assistance - | Change response 15 to "Shallow Subsidy Financial Assistance" Add "Landlord |
| ટટ્ટાન | Incentive" |
|  | Add "Tenant Incentive" |
|  | Add new Field - "End Date of Financial Assistance" |
| V4 Percent | Change response in Field 1 as follows: 30% or less 31% to 50% |
| of AMI (SSVF | 51% to 80% |
| Eligibility) | 81% or greater |
| V5 Last | Retired element; data no longer collected |
| Permanent |  |
| Address |  |
| RETIRE |  |
| V7 HP | Change dependency C to "Past experience of homelessness ... " Change |
| Targeting | dependency D to "Head of Household is not a current leaseholder/renter of |
| Criteria | unit" |
|  | Change dependency E to "Head of household (HOH) never been a |
|  | leaseholder/renter of unit" |
|  | Change dependency N to "Single parent/guardian household with minor |
|  | child(ren)" |
| 5.10 | Add metadata element 5.10 Implementation Identifier that assigns a unique |
| Implementat | value to each HMIS implementation to support export management and |
| ion Identifier | client deduplication |
| NEW |  |
| All | Change "Client Refused" to "Client prefers not to answer" |
| Appendix A - | Update Living Situation Option list |
| Living |  |
| Situation |  |

|  |  | Information |  |
| --- | --- | --- | --- |
|  |  | NEW | Add list of languages to be used in C4 Translation Assistance Needed. The list |
|  |  |  | has over 300 options and will live as a standalone document on the HUD |
|  |  |  | Exchange. |
| June 2023 | 1.1 | 3.12 | Add character limit to dependency B when specifying "Other" living situations |
|  |  | Destination |  |
|  |  | C4 | Add clarifying guidance on the recommended number of language response |
|  |  | Translation | categories provided to an HMIS end user |
|  |  | Assistance |  |
|  |  | Needed |  |
|  |  | NEW |  |
| July 2023 | 1.2 | Base | Removed "Update/Occurrence" collection point for DE 3.16 Client Location |
|  |  | Metadata |  |
|  |  | 4.19 | Re-introduce 4.19 Coordinated Entry Assessment for FY2024 Data Standards |
|  |  | Coordinated |  |
|  |  | Entry |  |
|  |  | Assessment 4.20 | Re-introduce 4.20 Coordinated Entry Event for FY2024 Data Standards |
|  |  | Coordinated |  |
|  |  | Entry Event |  |
|  |  | 4.21 | Data element will not be implemented for FY2024 Data Standards |
|  |  | Coordinated |  |
|  |  | Entry Activity |  |
|  |  | RETIRE |  |
|  |  | 2.09 | Updated to serve as a data element separate from 4.21 Coordinated Entry Activity Removed any reference to 4.21 Coordinated Entry Activity |
|  |  | Coordinated |  |
|  |  | Entry | Added additional logic to 4.20.C Location of Crisis Housing or Permanent |
|  |  | Participation | Housing Referral [Project name/HMIS ID] |
|  |  | Status |  |
|  |  | C4 | Renamed C4.A "Preferred Language(s)" to "Preferred Language" because this |
|  |  | Translation | is a single-select field |
|  |  | Assistance |  |
|  |  | Needed |  |
| August | 1.3 | 4.20 | Removed "Referral to Emergency Housing Voucher" as a referral event |
| 2023 |  | Coordinated |  |
|  |  | Entry Event |  |
|  |  | C4 | Added "HUD: HOPWA – Collection required for all components" to Funder: |
|  |  | Translation | Program Component |
|  |  | Assistance |  |
|  |  | Needed |  |
| November | 1.4 | 4.11 | Removed "Victim/Survivor" from Dependent B (dependent to Field 2) data |
| 2023 |  | Domestic | element name |
|  |  | Violence |  |
|  |  | 4.12 Current | Updated Funder: Program-Component for HUD: Unsheltered Special NOFO |
|  |  | Living | and HUD: Rural Special NOFO funding sources |
|  |  | Situation | Updated language for Project Type Applicability Project Type 14 |
|  |  | C3 Youth | Removed 7: Other under Project Type Applicability |
|  |  | Education |  |

|  |  | Status |  |
| --- | --- | --- | --- |
|  |  | R7 General | Clarified in main Revision History table that R7 is no longer required for HUD: |
|  |  | Health Status | CoC – Permanent Supportive Housing |
| December | 1.5 | Data | Corrected the 4.20 data element name from "Coordinated Entry Activity" to |
| 2023 |  | Elements by | "Coordinated Entry Event" |
|  |  | Collection |  |
|  |  | Stage Table |  |
| February | 1.5 | R6 | Added Project Type 6: Services Only as eligible project component |
| 2024 |  | Employment |  |
|  |  | Status |  |
| June 2024 | 1.6 | 4.20 | Corrected "dependent to Field 2 & responses 10-15 and 17-18" to |
|  |  | Coordinated | "dependent to Field 2 responses 10-15 or 18″ in dependency logic for |
|  |  | Entry Event | Dependent D to account for removal of response 17 in Field 2 |
|  |  | 2.02 Project | Added clarity for which Project Type to use for projects funded by HUD: Pay |
|  |  | Information | for Success that do not provide permanent housing |
|  |  | 3.20 Housing | Added requirement to collect Housing Move-In Date for all Pay for Success |
|  |  | Move-In | project components |
|  |  | Date |  |
|  |  | 3.917B Prior | Clarified dependencies for "Homeless Situations" |
|  |  | Living |  |
|  |  | Situation |  |

## FY2024 HMIS Data Standards

This document is intended to support HMIS and comparable database vendors, HMIS Leads/Administrators, and HMIS end users in understanding the data element table structures for the FY2024 HMIS Data Standards. Each table defines how data elements should be structured and programmed in HMIS software. The HMIS Data Standards Manual, a partner document to this one, provides details about how the data elements are defined and provides guidance on how to ensure accuracy when collecting data from people experiencing homelessness.

## Data Element Structure

Every data element required by HUD and the federal partners to be stored within an HMIS is specified in this document. The following format is used to describe each data element:

| Header | Instruction |
| --- | --- |
| Element Name | The name of the element. |
| Field # & Response(s) | The field name and any response options associated with the field. |
|  | Most elements contain responses of "Client doesn't know" and "Client prefers not |
|  | to answer." "Data not collected" is a response option in this HMIS Data Dictionary. |
|  | It is not a response option necessary in every system or in every element. The |
|  | element is required for use by any HMIS that requires a response to an element |
|  | before allowing the user to move forward in the system. Adding the "data not |
|  | collected" response option enables a user who did not collect or simply does not |
|  | have the information to enter a response that does not present a false answer. An |
|  | HMIS that requires entry of any element for the system to progress must |
|  | implement the "Data not collected" response for all elements that require a |
|  | response. |
|  | System Note: "Data not collected" will equate to missing data or null values as |
|  | appropriate for transfer and reporting purposes. |
| Dependent to Field # & | Dependent fields and dependent response options identify the Field and Response |
| Response # | option to which they are dependent. |
|  | The dependencies outlined in the Data Dictionary are expected to be visible to |
|  | users on-screen. The methods vendors may elect to make dependencies |
|  | visible/invisible, colored for completion/shaded out, etc. are up to each |
|  | software developer. |
| Element Type | The type of data element (project descriptor, universal, program-specific, or |
|  | metadata) which indicates the level at which data are collected, whether they |
|  | apply to all funding sources, and their relationship to other data. |
|  | Project Descriptor Data Elements (PDDEs) are the required elements that define |
|  | the individual projects within an HMIS. They are initially entered at the setup of |
|  | each project within an HMIS. They must be updated by the HMIS Administrator on |
|  | a regular basis as information within the elements are subject to change and are |
|  | critical for report generation. |
|  | Universal Data Elements (UDEs) are client level data elements required for |
|  | collection by all applicable projects participating in HMIS, regardless of funding |
|  | source. |
|  | Program-Specific Data Elements (PSDEs) are client level elements required by a |
|  | specific federal program or program component. |
|  | Common Program-Specific Data Elements (Common PSDEs) are the first subset of |

|  | the program-specific data elements that are required for collection by most of the |
| --- | --- |
|  | federal partners. When combined with the UDEs, these elements comprise the |
|  | building blocks for much of the reporting generated by an HMIS. |
|  | Federal Partner Program-Specific Data Elements (Federal Partner PSDEs) are the |
|  | second subset of the program-specific data elements. These elements are listed |
|  | under the federal partner program which maintains the element. There are |
|  | elements maintained by one partner and shared with one other. When combined |
|  | with UDEs and Common PSDEs, these elements comprise specific project level |
|  | reporting generated by an HMIS. |
|  | Metadata Elements are system generated data about data elements documenting |
|  | required metadata collection for all of the above element types. |
| Funder: Program-Component | ldentifies the federal department, the program, and the program component |
|  | which requires the collection of the element. If a program component is not listed, |
|  | it does not require collection of the element. |
|  | An HMIS must have the ability to enable and restrict visibility of elements for each |
|  | project based on the reporting requirements of the federal partner program |
|  | funding the project. An HMIS may do this in whatever manner the software |
|  | provider chooses (hard coding, customization via system administrators, etc.). |
|  | HMIS vendors should note that no federal partner expects that any project would |
|  | have all elements visible to the user. The strong preference among the federal |
|  | partners is that only the elements required for the programs that fund a specific |
|  | project are visible to the users at that project. |
| Project Type Applicability | Project type(s) refers to element 2.02 Project Information and identifies the HMIS |
|  | project type required to collect and report the data element. |
| Data Collected About | Identifies the universe of client(s) for whom an element response is required (e.g., |
|  | All Clients, Head of Household, Adults, etc.). Data may be collected about a wide |
|  | group (e.g., all household members) but may be further limited in data |
|  | reporting specifications. |
| Collection Point | The point(s) at which the data must be able to be collected in an HMIS. For data |
|  | elements with multiple collection points (e.g., "Project Start", "Occurrence Point", |
|  | "Project Exit"), each record must be stored with the appropriate Data Collection |
|  | Stage (as listed in metadata element 5.03 Data Collection Stage). Data elements |
|  | with only a single collection point need not be stored with any particular Data |
|  | Collection Stage since their data collection point is inherent in their requirements. |
|  | Record Creation – Indicates the element is required to be collected when the |
|  | client record is created. Elements collected at Record Creation should have one |
|  | and only one value for each client in an HMIS. Data are collected and entered into |
|  | an HMIS, and responses must be reviewed for accuracy at each project start and |
|  | edited as necessary to make corrections or to improve data quality. This includes |
|  | elements such as 3.01 Name and 3.07 Veteran Status. |
|  | Project Start (stored with Data Collection Stage of "Project Start" for elements |
|  | with multiple collection points) – Indicates the element is required to be collected |
|  | at every project start, such as 3.917 Prior Living Situation. Some elements |
|  | collected at project start have associated Information Dates; these elements must |
|  | have an Information Date that matches the client's 3.10 Project Start Date. |
|  | Information must be accurate as of the 3.10 Project Start Date. When a data |
|  | element with multiple collection points, such as 4.02 Income and Sources, is |
|  | collected at project start, it must be stored with a Data Collection Stage of 'Project |
|  | Start'. There should be one and only one record with a Data Collection Stage of |

'Project Start' for each relevant data element for any given project start. Data may be edited by users associated with the project to correct errors or omissions; such edits will not change the Data Collection Stage associated with the record. Occurrence Point/Update – Indicates the element may be collected and entered at any point during a project stay to track changes over time or document the occurrence of events (e.g., a service is provided). These types of records must be able to be entered at any point during the project stay. Some data elements are collected once per project stay, such as 3.20 Housing Move-In Date. For others, such as 4.14 Bed-Night Dates, the system must be able to support an unlimited number of records per project stay, each with a distinct Information Date. The Information Date should reflect the date on which the information is collected and/or the date for which the information is relevant for reporting purposes. Information must be accurate as of the Information Date, regardless of the 5.01 Date Created. Data may be edited by users associated with the project to correct errors or omissions; such edits will change neither the Data Collection Stage nor the Information Date unless it is explicitly altered by the user.

Annual Assessment (stored with Data Collection Stage of "Annual Assessment") – Data elements required for collection at annual assessment, such as 4.02 Income and Sources, must be entered with an Information Date of no more than 30 days before or after the anniversary of the Head of Household's Project Start Date, regardless of the date of the most recent 'update' or any other 'annual assessment'. Information must be accurate as of the Information Date. The data collection stage may not be inferred from the Information Date, although the field must have an Information Date recorded with it. To be considered reportable to HUD as an annual assessment, data must be stored with a Data Collection Stage of 'Annual Assessment'. The Annual Assessment must include updating both the Head of Household's record and any other household members at the same time.

There should be one and only one record for each data element annually with a Data Collection Stage recorded as 'Annual Assessment' associated with any given client and Enrollment ID within the 60-day period surrounding the anniversary of the Head of Household's Project Start Date. Regardless of whether the responses have changed since project start or the previous annual assessment, a new record must be created for each subsequent annual assessment such that it is possible to view a history, by date, of the values for each data element. Data may be edited by users associated with the project to correct errors or omissions; such edits will change neither the Data Collection Stage nor the Information Date unless they are explicitly altered by the user.

Project Exit (stored with Data Collection Stage of "Project Exit" for elements with multiple collection points) – Indicates the element is required to be collected at every project exit. Elements collected at project exit, such as 3.12 Destination, must have an 'Information Date' that matches the client's Project Exit Date. Information must be accurate as of the 'Project Exit Date'. When a data element with multiple collection points is collected at project exit, it must be stored with a Data Collection Stage of 'Project Exit'. There should be one and only one record with a Data Collection Stage of 'Project Exit' for each relevant data element for any given project exit. Data may be edited by users associated with the project to correct errors or omissions; such edits will not change the Data Collection Stage or the Information Date.

Post Exit (stored with Data Collection Stage of "Post Exit" for elements with multiple collection points) – Indicates the element may be collected after project

|  | exit for a period of no longer than 180 days. This is uncommon but includes |
| --- | --- |
|  | elements such as R20 Aftercare Plans. |
| Relationship to Enrollment ID | Indicates cardinality of the element relative to an enrollment and client. This will |
| (an enrollment) | often indicate "one or more" even though the element is only applicable to certain |
|  | project types or funders which require the data element and is further limited to |
| Relationship to Personal ID (a | clients described in the "Data Collected About" line in the element. "One or more" |
| client) | does not inherently imply the element should be collected on every client in HMIS. |
|  | In general, elements recorded at least once per enrollment are required at project |
|  | start. Elements recorded 0 or more times per enrollment |
|  | might only be collected as needed or at exit, e.g., a referral. |
| System Logic & Other System | Logically required data collection or system structure information for HMIS |
| lssues | software development purposes and information on rationale, conditions, |
|  | constraints, etc. that may be applicable to a specific element and are important |
|  | for HMIS software development purposes. |
| XML | XML element in XML Specifications where the data standard element is located. |
| CSV | Primary file in CSV Specifications where the data standard element is located. |
| 2024 Revision Summary | Documents the initial change(s) to the element from the FY2022 Data Standard to |
|  | the FY2024 Data Standard. Corrections made throughout the year are tracked in |
|  | the Summary of Changes. |

# PROJECT DESCRIPTOR DATA ELEMENTS

## 2.01 Organization Information

| Header | Instruction |
| --- | --- |
| Element Name | Organization Information |
| Field 1 & Response | Organization ID – auto generate |
| Field 2 & Response | Organization Name |
| Field 3 & Response | Victim Service Provider |
|  | O No |
|  | 1 Yes |
| Element Type | Project Descriptor |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Organizations |
| Collection Point | Initial HMIS project setup, reviewed/updated no less than annually |
| System Logic & Other System | An Organization ID must be assigned to each project via a system generated |
| lssues | number or code. There is no specified format for this data element and can be up to |
|  | 32 characters in length. |
|  | Each organization must receive a distinct identifier that is consistently associated |
|  | with that organization. |
|  | Each organization must also be able to be associated with one or more projects. The |
|  | name of the organization must be captured in text within the HMIS. |

|  | An HMIS must allow the HMIS Administrator to activate and deactivate an |
| --- | --- |
|  | organization. |
|  | An HMIS application may permit the creation of a common name field more |
|  | familiar to users for use within the application while retaining the legal name for |
|  | use in reporting. |
| XML | <organization> |
| CSV | Organization |
| 2024 Revision Summary | Added character limit |

#### 2.02 Project Information

| Header | Instruction |
| --- | --- |
| Element Name | Project Information |
| Field 1 & Response | Project ID - auto generate |
| Field 2 & Response | Project Name |
| Field 3 & Response | Operating Start Date |
| Field 4 & Response | Operating End Date |
| Field 5 & Response | Continuum Project |
|  | 0 No |
|  | 1 Yes |
| Field 6 & Responses | Project Type |
|  | 0 Emergency Shelter - Entry Exit |
|  | 1 Emergency Shelter - Night-by-Night |
|  | 2 Transitional Housing |
|  | 3 PH - Permanent Supportive Housing (disability required for entry) |
|  | 4 Street Outreach |
|  | 5 RETIRED |
|  | б Services Only |
|  | 7 Other |
|  | 8 Safe Haven |
|  | 9 PH - Housing Only |
| 10 | PH – Housing with Services (no disability required for entry) |
| J J | Day Shelter |
| 12 | Homelessness Prevention |
| 13 | PH - Rapid Re-Housing |
| 14 | Coordinated Entry |
| Dependent A- Dependent to | [If PH - Rapid Re-Housing] |
| Field 6 & Response 13 | ldentify RRH subtype |
|  | । RRH: Services Only |
|  | 2 RRH: Housing with or without services |
| Dependent B - Dependent to | [If Services Only for "Project Type" or RRH: Services Only subtype] |
| Field 6 & Response 6 or Dependent A = 1 | Affiliated with a residential project |
|  | O No |
|  | 1 Yes |
| Dependent C - Dependent to | [If Yes for "Affiliated with a residential project"] |
| Dependent B & Response 1 | Project ID(s) of residential project(s) affiliated with SSO or RRH: Services Only project |
| Dependent D - Dependent to | Housing Type |
| Field 6 responses 0, 1, 2, 3, 8, |  |
| 9, 10, 13 (If 13, Dependent A = |  |
| 2) |  |

| Site-based - single site | 1 | Site-based – clustered/multiple sites | 2 |
| --- | --- | --- | --- |
| Tenant-based – scattered site | 3 | Field 7 & Responses | Target Population |
| DV: Survivors of Domestic Violence | । | 3 | HIV: Persons with HIV/AIDS |
| 4 | NA: Not applicable | Field 8 & Response | HOPWA-funded Medically Assisted Living Facility |
| 0 | No | । | Yes |
| 2 | NA – non-HOPWA Funded Project | Element Type | Project Descriptor |
| Funder: Program-Component | All Programs – All Components | Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Projects | Collection Point | Initial HMIS project setup, reviewed/updated no less than annually |
| System Logic & Other System | Projects funded with 2.06 Funding Source HUD: Pay for Success (35) and do not | Issues |  |
| provide permanent housing should use Project Type (Field 6) Other (7). |  |  |  |
| A Project ID must be assigned to each project via a system generated number or | code. Each project must receive an identifier that is unique within the HMIS and |  |  |
| consistently associated with that project. There is no specified format for this data | element and can be up to 32 characters in length. |  |  |
| Each project must be associated with one and only one organization (2.01 | Organization Information); separate projects operated by the same agency must |  |  |
| be associated with the same Organization ID. The name of the project must be | captured in text within the HMIS. |  |  |
| An HMIS may permit the creation of a common name element more familiar to users | for use within the application while retaining the legal name for use in reporting. |  |  |
| System stores collected project type and retains for historical purposes. Allow edits | if changes or corrections for data entry error. |  |  |
| A project can only have one project type assigned. |  |  |  |
| A project must be able to identify multiple affiliated residential projects if "yes" to | Dependent A. |  |  |
| Utilization of the Emergency Shelter Night-by-Night project type (2.02 Project | Information - Project Type = 1) does not mean that an HMIS must identify a client in |  |  |
| a specific bed. If an HMIS supports a custom module that identifies clients in a bed, | that module may continue to be used. |  |  |
| However, use of that module does not necessarily equate with the night- by-night | project type. |  |  |
| At the point a project closes, and an 'Operating End Date' is recorded in Field 4, all | clients must be exited on or before the 'Operating End Date'. This may be achieved |  |  |
| through a bulk update or auto exit (if such functionality exists), or manually. It is | strongly encouraged that at a minimum, an alert or notification is provided to |  |  |
| indicate active clients remain in the project once an 'Operating End Date' is | populated. |  |  |
| XML | <project> | CSV | Project and Affiliation |
| 2024 Revision Summary | Added "Emergency Shelter – Entry Exit" project type 0. Removed "Emergency |  |  |

| Shelter Tracking Method" and "HMIS Participating Project," added "Rapid Re- |
| --- |
| housing Subtype." Wording changes in system logic. |
| Added clarification of Project Type to use for projects funded by HUD: Pay for |
| Success that do not provide permanent housing. |

## 2.03 Continuum of Care Information

| Header | Instruction |
| --- | --- |
| Element Name | Continuum of Care Information |
| Field 1 & Response | Continuum Code [HUD-assigned CoC codes for the project location (text – 6 |
|  | characters)] |
| Field 2 & Response | Geocode (6 digits) |
| Field 3 & Responses | Project street address 1 (text) |
| Field 4 & Responses | Project street address 2 (text) |
| Field 5 & Responses | Project city (text) |
| Field 6 & Responses | Project state (2 letters) |
| Field 7 & Responses | Project ZIP code (5 digits) |
| Field 8 & Response | Geography Type [From look up table provided by HUD – code the following |
|  | geography types based on ZIP code] |
| 1 | Urban |
| 2 | Suburban |
| 3 | Rural |
| Element Type | Project Descriptor |
| Funder: Program-Component | All Programs - All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Continuum Projects |
| Collection Point | Initial HMIS project setup, reviewed/updated no less than annually |
| System Logic & Other System | There is a many-to-one relationship between this data element and 2.02 Project |
| Issues | Information; there may be multiple current records of this data element at any |
|  | given time. Add, edit, or remove associations with CoCs as needed to reflect |
|  | changes. There must be a one-to-one relationship to 2.02 Project Information if the |
|  | project only serves one CoC (most common). |
|  | Projects may be funded to provide housing and/or services to clients residing in |
|  | only one CoC (e.g., CoC: Transitional Housing), or they may be funded for housing |
|  | and/or services across multiple CoCs (e.g., VA: SSVF). It must be possible to |
|  | associate a project with the CoC code for every geographic area in which the |
|  | project operates and for which it will be entering data into an HMIS. |
|  | Systems operating in a single continuum may set their CoC code as a default value |
|  | for this field. |
|  | For data quality purposes, the CoC codes in this data element should be used to |
|  | populate an option list of CoC codes for 3.16 Enrollment CoC when one is required. |
|  | HUD will release an updated crosswalk of ZIP codes with a geography type for each |
|  | ZIP code biennially. This must be incorporated as a table into HMIS applications and |
|  | used to auto-populate the geography type field. |
| XML | <projectCoC> |
| CSV | ProjectCoC |

Wording changes in system logic to account for a single CoC code being associated with each enrollment rather than multiple CoC codes

#### 2.06 Funding Sources

| Header | Instruction |
| --- | --- |
| Element Name | Funding Sources |
| Field 1 & Responses | Federal Partner Program and Components |
| 1 | HUD: CoC – Homelessness Prevention (High Performing Comm. Only) |
| 2 | HUD: CoC – Permanent Supportive Housing |
| 3 | HUD: CoC - Rapid Re-Housing |
| 4 | HUD: CoC - Supportive Services Only |
| 5 | HUD: CoC – Transitional Housing |
| б | HUD: CoC - Safe Haven |
| 7 | HUD: CoC - Single Room Occupancy (SRO) |
| 43 | HUD: CoC - Youth Homeless Demonstration Program (YHDP) |
| 44 | HUD: CoC - Joint Component TH/RRH |
| 8 | HUD: ESG – Emergency Shelter (operating and/or essential services) |
| 9 | HUD: ESG – Homelessness Prevention |
| 10 | HUD: ESG - Rapid Re-Housing |
| J J | HUD: ESG - Street Outreach |
| 47 | HUD: ESG-CV |
| ટેં | HUD: ESG-RUSH |
| ਟੇਰ | HUD: Unsheltered Special NOFO |
| ટર | HUD: Rural Special NOFO |
| રૂટ | HUD: Pay for Success |
| 13 | HUD: HOPWA – Hotel/Motel Vouchers |
| 14 | HUD: HOPWA – Housing Information |
| ਹ ਦ | HUD: HOPWA – Permanent Housing (facility based or TBRA) |
| 16 | HUD: HOPWA – Permanent Housing Placement |
| 17 | HUD: HOPWA – Short-Term Rent, Mortgage, Utility assistance |
| J8 | HUD: HOPWA – Short-Term Supportive Facility |
| ਰ | HUD: HOPWA - Transitional Housing (facility based or TBRA) |
| 48 | HUD: HOPWA-CV |
| 36 | HUD: Public and Indian Housing (PIH) Programs |
| 20 | HUD: HUD/VASH |
| 52 | HUD: PIH (Emergency Housing Voucher) |
| 50 | HUD: HOME |
| ਟ ਹ | HUD: HOME (ARP) |
| 21 | HHS: PATH - Street Outreach & Supportive Services Only |
| 22 | HHS: RHY – Basic Center Program (prevention and shelter) |
| 23 | HHS: RHY – Maternity Group Home for Pregnant and Parenting Youth |
| 24 | HHS: RHY – Transitional Living Program |
| 25 | HHS: RHY - Street Outreach Project |
| 26 | HHS: RHY – Demonstration Project |
| 27 | VA: CRS Contract Residential Services |
| 37 | VA: Grant Per Diem – Bridge Housing |
| 38 | VA: Grant Per Diem – Low Demand |

| ਤਰੇ | VA: Grant Per Diem – Hospital to Housing |
| --- | --- |
| 40 | VA: Grant Per Diem – Clinical Treatment |
| 41 | VA: Grant Per Diem - Service Intensive Transitional Housing |
| 42 | VA: Grant Per Diem – Transition in Place |
| 45 | VA: Grant Per Diem - Case Management/Housing Retention |
| 30 | VA: Community Contract Safe Haven Program |
| 33 | VA: Supportive Services for Veteran Families |
| 34 | N/A |
| 46 | Local or Other Funding Source (Please Specify) |
| Dependent A - Dependent to Field 1 Response 46 | If other, specify [text] |
| Field 2 & Response | Grant Identifier |
| Field 3 & Response | Grant Start Date ([date field]) |
| Field 4 & Response | Grant End Date ((date field)) |
| Element Type | Project Descriptor |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Projects |
| Collection Point | Initial HMIS project setup, reviewed/updated no less than annually |
| System Logic & Other System Issues | This is a transactional data element; a single project may have multiple current and |
|  | historical records. Allow corrections for data entry error. |
|  | An HMIS must allow projects with multiple funder sources and multiple grants (with potentially different grant terms) from the same funding source to record and |
|  | store all funding sources for the project. |
|  | Dependent A has a 100-character limit when exporting in the HMIS CSV. |
| XML | <Funder> |
| CSV | Funder |
| 2024 Revision Summary | Removed "49: HUD: CoC – Joint Component RRH/PSH" and "12: HUD: Rural |
|  | Housing Stability Assistance Program." Added "53: HUD: ESG-RUSH", "54: HUD: |
|  | Unsheltered Special NOFO", and "55: HUD: Rural Special NOFO." |

#### 2.07 Bed and Unit Inventory Information

| Header | Instruction |
| --- | --- |
| Element Name | Bed and Unit Inventory Information |
| Field 1 & Response | Inventory start date ([date field]) |
| Field 2 & Response | Inventory end date ([date field]) |
| Field 3 & Response | Continuum Code |
| Field 4 & Responses | Household type |
|  | 1 Households without children |
|  | ന Households with at least one adult and one child |
|  | ব Households with only children |
| Field 5 & Responses | [If 2.02 Project Type = 'Emergency Shelter – Entry Exit' or 'Emergency Shelter – |
|  | Night-by-Night'] Bed Type |
|  | 1 Facility-based beds |
|  | 2 Voucher beds |
|  | 3 Other beds |
| Field 6 & Responses | [If 2.02 Project Type 'Emergency Shelter - Entry Exit' or 'Emergency Shelter - Night- |
|  | by-Night'] Availability |

| 1 | Year-round |
| --- | --- |
| 2 | Seasonal |
| 3 | Overflow |
| Field 7 & Response | Beds dedicated to chronically homeless veterans ([integer]) |
| Field 8 & Response | Beds dedicated to youth-veterans ([integer]) |
| Field 9 & Response | Beds dedicated to any other veteran ([integer]) |
| Field 10 & Response | Beds dedicated to chronically homeless youth ([integer]) |
| Field 11 & Response | Beds dedicated to any other youth ([integer]) |
| Field 12 & Response | Beds dedicated to any other CH ((integer) |
| Field 13 & Response | Non-dedicated beds ([integer]) |
| Field 14 & Response | Total bed inventory ([integer]) |
| Field 15 & Response | Total unit inventory ([integer]) |
| Element Type | Project Descriptor |
| Funder: Program-Component | All Programs - All Components |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 1: Emergency Shelter – Night-by-Night |
|  | 2: Transitional Housing |
|  | 3: PH - Permanent Supportive Housing |
|  | 8: Safe Haven |
|  | 9: PH - Housing Only |
|  | 10: PH - Housing with Services |
|  | 13: PH – Rapid Re-Housing (subtype 2: RRH: Housing with or without services) |
| Data Collected About | All Residential Projects, except for PH - Rapid Re-Housing subtype 1: RRH: Services |
|  | Only |
| Collection Point | Initial HMIS project setup reviewed at least annually and updated as needed to |
|  | reflect changes. |
| System Logic & Other System | A project may have multiple current and historical records of inventory. |
| lssues |  |
|  | For any inventory record, it must be possible to identify the CoC with which the |
|  | inventory is associated. If an HMIS produces CoC-level reporting on 2.07 Bed and |
|  | Unit Information (LSA and/or HIC) for more than one continuum, records of |
|  | inventory must be separate and associated with the CoC where the inventory is |
|  | located. |
|  | For projects that operate in a single continuum, there is a many-to-one |
|  | relationship between this data element and 2.02 Project Information, although at |
|  | any given time, only one record for this data element will be current. For projects |
|  | that operate in multiple CoCs, there is a similar many-to-one relationship with 2.03 |
|  | Continuum of Care Information. |
|  | Data entry errors should be corrected; a new record should be created to |
|  | document a change in information. A new record is only required if a change has |
|  | occurred. |
|  | Not all fields are required for all projects. |
|  | These fields must be transactional, meaning they must be able to record multiple |
|  | values over time. |
|  | Bed inventory fields are expected to be mutually exclusive categories and must |
|  | accurately sum to the Total Bed Inventory. |
| XML | <Inventory> |
| CSV | Inventory |
| 2024 Revision Summary | Project type applicability updated to account for new ES – NbN project type and |
|  | new RRH – Services Only project subtype |

#### 2.08 HMIS Participation Status

| Header | Instruction |
| --- | --- |
| Element Name | HMIS Participation Status |
| Field 1 & Response | HMIS Participation Status |
| 0 | Not Participating |
| ਹ | HMIS Participating |
| 2 | Comparable Database Participating |
| Field 2 | Participation Status Start Date ([date field]) |
| Field 3 | Participation Status End Date ([date field]) |
| Element Type | Project Descriptor |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All Project Types |
| Data Collected About | All Projects |
| Collection Point | Initial project setup reviewed at least annually and updated as needed to reflect |
|  | changes. |
| System Logic & Other System lssues | These fields must be transactional, meaning they must be able to record multiple |
|  | values over time. |
|  | HMIS Participation Status date ranges are expected to be mutually exclusive and |
|  | shall not overlap. |
|  | At any given time, all projects with a blank 'Operating End Date' should have an HMIS |
|  | Participation Status record with a blank Participation End Date. |
| XML | <HMISParticipation> |
| CSV | HMISParticipation |
| 2024 Revision Summary | New element |

### 2.09 Coordinated Entry Participation Status

| Header | Instruction |
| --- | --- |
| Element Name | Coordinated Entry Participation Status |
| Field 1 & Response | Project is a Coordinated Entry Access Point |
| O | No |
| 1 | Yes |
| Dependent A - Dependent to | Provided by CE Project |
| Field 1 Response 1 |  |
| 1 | Homelessness Prevention Assessment, Screening, and/or Referral |
| 2 | Shelter Assessment, Screening, and/or Referral |
| 3 | Housing Assessment, Screening, and/or Referral |
| 4 | Direct Services (search and/or placement support) |
| Field 2 & Response | Project Receives CE Referrals |
| O | No |
| 1 | Yes |
| Field 3 | CE Participation Status Start Date ([date field]) |
| Field 4 | CE Participation Status Start Date ([date field]) |
| Element Type | Project Descriptor |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Projects |
| Collection Point | Initial HMIS project setup, reviewed/updated no less than annually. |
| System Logic & Other System | These fields must be transactional, meaning they must be able to record multiple |
| ssues |  |

|  | values over time. |
| --- | --- |
|  | CE Participation Status date ranges are expected to be mutually exclusive and shall |
|  | not overlap. |
|  | At any given time, all projects with a blank 'Operating End Date' should have a CE |
|  | Participation Status record with a blank CE Participation Status End Date. |
|  | Field 1 – applicable to any project which conducts screenings, assessments, and/or |
|  | referrals to other projects OR provides some direct service related to diversion, |
|  | rapid resolution, or navigation. |
|  | Responses in Dependent A are multi-select. |
|  | Field 2 – This field is used in conjunction with project type to filter the list of |
|  | projects populating field 4.20.C. |
| XML | <CEParticipation> |
| CSV | CEParticipation |
| 2024 Revision Summary | New element |

# UNIVERSAL DATA ELEMENTS

#### 3.01 Name

| Header | Instruction |
| --- | --- |
| Element Name | Name |
| Field 1 & Response | First ([text]) |
| Field 2 & Response | Middle ((text)) |
| Field 3 & Response | Last ([text]) |
| Field 4 & Response | Suffix ([text]) |
| Field 5 & Responses | Name Data Quality |
| 1 | Full name reported |
| 2 | Partial, street name, or code name reported |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Universal |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Clients |
| Collection Point | Record Creation |
| Relationship to Enrollment ID | N/A |
| (an enrollment) |  |
| Relationship to Personal ID (a | One name per client |
| client) |  |
| System Logic & Other System | Associated HMIS end users must be able to edit data to correct errors or reflect |
| Issues | changes in client responses. |
|  | Systems may elect to utilize an extra field(s) for alias or for notes on name changes. |

|  | Fields 1, 2, 3, and 4 have a 50-character limit when exporting in the HMIS CSV. |
| --- | --- |
| XML | <Client><...> |
| CSV | Client |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to answer" |

## 3.02 Social Security Number

| Header | Instruction |
| --- | --- |
| Element Name | Social Security Number |
| Field 1 & Response | Social Security Number |
| Field 2 & Responses | SSN Data Quality |
|  | 1 Full SSN reported |
|  | 2 Approximate or partial SSN reported |
|  | 8 Client doesn't know |
|  | 9 Client prefers not to answer |
|  | ਰੇਰੇ Data not collected |
| Element Type | Universal |
| Funder: Program-Component | All Programs - All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Clients |
| Collection Point | Record Creation |
| Relationship to Enrollment ID | N/A |
| (an enrollment) |  |
| Relationship to Personal ID (a | One Social Security Number per client |
| client) |  |
| System Logic & Other System | System stores collected nine-digit SSN in one field and the appropriate SSN data |
| lssues | quality in another. |
|  | Associated HMIS end users must be able to edit data to correct errors or reflect |
|  | changes in client responses. |
|  | An HMIS may include hyphens or other punctuation within the SSN to improve |
|  | readability, but the SSN must be exportable as a single alphanumeric field |
|  | containing a maximum of nine characters and no punctuation. |
|  | HMIS software and HMIS Administrators may designate special non-numeric |
|  | characters (e.g., the letter x) to indicate missing digits and otherwise devise |
|  | methodologies to allow entry and effective matching of partial SSNs (if the system |
|  | permits). Because missing digits may appear in any one of the nine placeholders, it |
|  | is critical for the system to have a mechanism to indicate which digits were missing |
|  | when entering partial SSNs; an alphabetic character must be interpreted as a |
|  | placeholder. |
|  | HMIS software may reject clearly invalid SSNs at the point of entry. Relevant Social |
|  | Security Administration rules for a valid SSN are found in the HMIS Reporting |
|  | Glossary. |
| XML | <Client><...> |
| CSV | Client |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer" |

| Header | Instruction |
| --- | --- |
| Element Name | Date of Birth |
| Field 1 & Response | Date of Birth |
| Field 2 & Responses | DOB Data Quality |
| 1 | Full DOB reported |
| 2 | Approximate or partial DOB reported |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Universal |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Clients |
| Collection Point | Record Creation |
| Relationship to Enrollment ID | N/A |
| (an enrollment) |  |
| Relationship to Personal ID (a | One Date of Birth per client |
| client) |  |
| System Logic & Other System | System stores collected Date of Birth in one field and the appropriate DOB data |
| Issues | quality type in another. |
|  | Associated HMIS end users must be able to edit data to correct errors or reflect |
|  | changes in client responses. |
|  | "Client doesn't know", "Client prefers not to answer", and "Data not collected" are |
|  | explanations for missing DOB data. These three responses are only valid in |
|  | conjunction with a null DOB. |
|  | One date format field for birth dates should be created in the HMIS software. Date |
|  | of Birth must be exportable in the [date field] format. |
| XML | <Client><...> |
| CSV | Client |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer" |

#### 3.04 Race and Ethnicity

| Header |  | Instruction |
| --- | --- | --- |
| Element Name |  | Race and Ethnicity |
| Field 1 & Responses |  | Race and Ethnicity (as many as are applicable) |
|  | T | American Indian, Alaska Native, or Indigenous |
|  | 2 | Asian or Asian American |
|  | 3 | Black, African American, or African |
|  | ଚ | Hispanic/Latina/e/o |
|  | 7 | Middle Eastern or North African |
|  | ব | Native Hawaiian or Pacific Islander |
|  | ഗ | White |
|  | 8 | Client doesn't know |
|  | ਰੇ | Client prefers not to answer |

|  | ਰੇਰੇ | Data not collected |
| --- | --- | --- |
| Field 2 & Response |  | Additional Race and Ethnicity Detail |
|  |  | ([Text]) |
| Element Type |  | Universal |
| Funder: Program-Component |  | All Programs - All Components |
| Project Type Applicability |  | All HMIS Project Types |
| Data Collected About |  | All Clients |
| Collection Point |  | Record Creation |
| Relationship to Enrollment ID |  | N/A |
| (an enrollment) |  |  |
| Relationship to Personal ID (a |  | One Race per client (multiple responses selected for a client are considered one |
| client) |  | element/field in total) |
| System Logic & Other System |  | Associated HMIS end users must be able to edit data to correct errors or reflect |
| Issues |  | changes in client responses. |
|  |  | An HMIS must accommodate the recording of up to seven race and ethnicity |
|  |  | response categories per client. |
|  |  | Field 2 has a 100-character limit when exporting in the HMIS CSV. |
|  |  | This is a multi-select field with logic limitations, as follows: "Client doesn't know", |
|  |  | "Client prefers not to answer", and "Data not collected" are not races or an |
|  |  | ethnicity; they are explanations for missing race and ethnicity data. None of these |
|  |  | three responses are valid in conjunction with any other response. |
| XML |  | <Client><Race> |
| CSV |  | Client |
| 2024 Revision Summary |  | Clarified logic expectations and added "Hispanic/Latina/e/o" information from the |
|  |  | deprecated Ethnicity element as well as the "Middle Eastern or North African" |
|  |  | response option. New field collecting "Additional Race and Ethnicity Detail." |
|  |  | Changed "Client refused" to "Client prefers not to answer." |

#### 3.06 Gender

| Header | Instruction |
| --- | --- |
| Element Name | Gender |
| Field 1 & Responses | Gender (as many as are applicable) |
| O | Woman (Girl, if child) |
| ਹ | Man (Boy, if child) |
| 2 | Culturally Specific Identity (e.g., Two-Spirit) |
| 5 | Transgender |
| 4 | Non-Binary |
| ଚ | Questioning |
| 3 | Different Identity |
| 8 | Client doesn't know |
| ਰੇ | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent A - Dependent to | If Different Identity, Please Specify |
| Field 1 Response 3 | ([Text]) |
| Element Type | Universal |
| Funder: Program-Component | All Programs – All Components |

| Project Type Applicability | All HMIS Project Types |
| --- | --- |
| Data Collected About | All Clients |
| Collection Point | Record Creation |
| Relationship to Enrollment ID | N/A |
| (an enrollment) |  |
| Relationship to Personal ID (a | One Gender per client (multiple responses selected for a client are considered one |
| client) | element/field in total) |
| System Logic & Other System | Associated HMIS end users must be able to edit data to correct errors or reflect |
| Issues | changes in client responses. |
|  | Dependent A has a 100-character limit when exporting in the HMIS CSV. |
|  | This is a multi-select field with logic limitations, as follows: |
|  | An HMIS must accommodate the recording of up to seven gender response |
|  | categories per client, except "Client doesn't know", "Client prefers not to answer", |
|  | and "Data not collected." These are not gender responses; they are explanations |
|  | for missing gender data. None of these three responses are valid in conjunction |
|  | with any other response. |
|  | Field 1, response option 6, "Questioning", is not compatible with or equivalent to |
|  | response option 8, "Client doesn't know." "Questioning" articulates the client may |
|  | be at a point of exploration around their identity, including multiple expressions, |
|  | which permits the client to more accurately self-report their identity. |
| XML | <Client><Gender> |
| CSV | Client |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer," "Female" to "Woman (girl if child)," and "Male" to "Man (boy if child)." |
|  | Split "A gender other than singularly male or female (e.g. non-binary, genderfluid, |
|  | agender, culturally specific gender)" into "Culturally Specific Identity (e.g., Two- |
|  | Spirit)," "Non-Binary," and "Different Identity." |

## 3.07 Veteran Status

| Header | Instruction |
| --- | --- |
| Element Name | Veteran Status |
| Field 1 & Responses | Veteran Status |
| 0 | No |
| 1 | Yes |
| 8 | Client doesn't know |
| ਰੇ | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Universal |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Adults |
| Collection Point | Record Creation |
| Relationship to Enrollment ID | N/A |
| (an enrollment) |  |
| Relationship to Personal ID (a | One Veteran status per client |
| client) |  |

| System Logic & Other System | Associated HMIS end users must be able to edit data to correct errors or reflect |
| --- | --- |
| lssues | changes in client responses or status, or to enter a response for a client who has |
|  | turned 18. |
|  | HMIS end users are not required to ask clients under 18 about veteran status; this |
|  | does not mean that systems are required to hide or exclude this data element |
|  | from data entry forms. |
|  | HMIS end users may enter "No" for any client under 18. Systems may be |
|  | programmed to automatically create a response for clients who turn 18 while |
|  | enrolled; the auto-generated response should be "No." |
| XML | <Client><VeteranStatus> |
| CSV | Client |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer" |

## 3.08 Disabling Condition

| Header |  | Instruction |
| --- | --- | --- |
| Element Name |  | Disabling Condition |
| Field 1 & Responses |  | Disabling Condition |
|  | 0 No |  |
|  | 1 Yes |  |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ | Data not collected |
| Element Type |  | Universal |
| Funder: Program-Component |  | All Programs – All Components |
| Project Type Applicability |  | All HMIS Project Types |
| Data Collected About |  | All Clients |
| Collection Point |  | Project start (Edit as necessary to reflect new information) |
| Relationship to Enrollment ID |  | No more than one Disabling Condition per Enrollment |
| (an enrollment) |  |  |
| Relationship to Personal ID (a |  | One or more Disabling Condition per Client |
| client) |  |  |
| System Logic & Other System |  | An HMIS end user must be able to set the value of this data element to "Yes" |
| Issues |  | independent of any other data element. |
|  |  | Disabling Condition may either be entered by the HMIS end user independently of |
|  |  | any other special need field, or data in this field may be inferred by the responses |
|  |  | to "ability to live independently" for 4.05 Physical Disability, 4.07 Chronic Health |
|  |  | Condition, 4.09 Mental Health Disorder, or 4.10 Substance Use Disorder or an |
|  |  | answer of "Yes" to 4.06 Developmental Disability or 4.08 HIV/AIDS. |
|  |  | If the system auto-populates the Disabling Condition element, an HMIS end user |
|  |  | must be able to override a system-generated "No" with "Yes." Further, if Disabling |
|  |  | Condition is auto-populated with "Yes" based solely on a qualifying record for data |
|  |  | elements 4.05-4.10 (i.e., the user-entered response to Disabling Condition was |
|  |  | something other than "Yes" but was changed to "Yes" by the system due to an |
|  |  | answer in the special needs fields (4.05-4.10)) and the special needs record is later |
|  |  | deleted or edited such that it doesn't meet the criteria for a disabling condition, |
|  |  | the auto-populated "Yes" response must revert to the HMIS end user's original |

|  | response. |
| --- | --- |
|  | Regardless of the response to this data element, if a client's data indicates a |
|  | response for data elements 4.05 Physical Disability, 4.07 Chronic Health Condition, |
|  | 4.09 Mental Health Disorder, and/or 4.10 Substance Use Disorder that meets the |
|  | criteria for a disabling condition (Dependent Field A = "Yes"), OR 4.06 |
|  | Developmental Disability or 4.08 HIV/AIDS = "Yes", reporting should always count |
|  | the client as having a disabling condition. |
| XML | <Enrollment><DisablingCondition> |
| CSV | Enrollment |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer" |

## 3.10 Project Start Date

| Header | Instruction |
| --- | --- |
| Element Name | Project Start Date |
| Field 1 & Response | Project Start Date ([date field]) |
| Element Type | Universal |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Clients |
| Collection Point | Project Start |
| Relationship to Enrollment ID | No more than one Project Start Date per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Project Start Date per Client |
| client) |  |
| System Logic & Other System | The 'project start date' must be exportable in the [date field] format. |
| lssues |  |
| XML | <Enrollment><EntryDate> |
| CSV | Enrollment |
| 2024 Revision Summary | None |

### 3.11 Project Exit Date

| Header | Instruction |
| --- | --- |
| Element Name | Project Exit Date |
| Field 1 & Response | Project Exit Date ([date field]) |
| Element Type | Universal |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Clients |
| Collection Point | Project Exit |
| Relationship to Enrollment ID | Zero or one Project Exit Date per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | Zero or more Project Exit Date per Client |
| client) |  |
| System Logic & Other System lssues | The 'project exit date' must be exportable in the [date field] format. |
|  | Auto-exit functionality is not a required feature of HMIS software. However, if it is |
|  | a feature offered, it must meet certain requirements: |

|  | The CoC must be involved in the determination of "extended length of time" that |
| --- | --- |
|  | has elapsed to prompt auto-exit functionality and must establish a standard to |
|  | "automatically exit" a client after a given length of absence (e.g., 90 days from last |
|  | bed night). |
|  | For residential projects, the client's 3.11 Project Exit Date would be recorded as the |
|  | last day the client appeared at the residential project (in the case of Emergency |
|  | Shelter – Night-by-Night (Project Type = 1) projects, the day after the last 4.14 Bed |
|  | Night Date) and the 3.12 Destination would be marked as "No exit interview |
|  | completed." |
|  | For non-residential projects, the 3.11 Project Exit Date must represent the last day |
|  | a contact was made, or a service was provided, and the 3.12 Destination would be |
|  | marked as "No exit interview completed." |
| XML | <Exit><ExitDate> |
| CSV | Exit |
| 2024 Revision Summary | Wording change in system logic to account for Emergency Shelter – Night-by- Night |
|  | project type |

#### 3.12 Destination

| Header | Instruction |
| --- | --- |
| Element Name | Destination |
| Field 1 & Responses | See Appendix A – Living Situation Option List |
| Dependent A - Dependent to | Rental Subsidy Type – See Appendix A |
| Field 1 Response 435 |  |
| Dependent B - Dependent to | If Other for "Type of Residence" – text box for "Specify Where" |
| Field 1 & Response 17 |  |
| Element Type | Universal |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Clients |
| Collection Point | Project Exit |
| Relationship to Enrollment ID | Zero or one Destination per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID | Zero or more Destination per Client |
| (a client) |  |
| System Logic & Other System lssues | Dependent B has a 50-character limit when exporting in the HMIS CSV. |
|  | Display exit destinations using the same screen order as indicated in Appendix A - |
|  | Living Situation Information. This is optional but suggested for consideration. |
| XML | <Exit><...> |
| CSV | Exit |
| 2024 Revision Summary | Moved subsidized permanent destinations into Dependent A following Field 1, |
|  | response 435 ("Rental by client, with ongoing housing subsidy") |

#### 3.15 Relationship to Head of Household

| Header | Instruction |
| --- | --- |
| Element Name | Relationship to Head of Household |
| Field 1 & Responses | Relationship to Head of Household |

|  | 1 | Self (Head of Household) |
| --- | --- | --- |
|  | 2 | Head of Household's child |
|  | 3 | Head of Household's spouse or partner |
|  | 4 | Head of Household's other relation member (other relation to Head of Household) |
|  | 5 | Other: non-relation member |
| Element Type |  | Universal |
| Funder: Program-Component |  | All Programs – All Components |
| Project Type Applicability |  | All HMIS Project Types |
| Data Collected About |  | All Clients |
| Collection Point |  | Project Start |
| Relationship to Enrollment ID |  | No more than One Relationship to Head of Household per Enrollment |
| (an enrollment) |  |  |
| Relationship to Personal ID (a |  | One or more Relationship to Head of Household per Client |
| client) |  |  |
| System Logic & Other System |  | There must be exactly one Head of Household for each household (3.15 |
| lssues |  | Relationship to Head of Household = 1). |
|  |  | It is expected that both the Head of Household and the household member(s) are |
|  |  | always in HMIS together in the same household for any project in which they |
|  |  | enrolled together. |
|  |  | The system must allow for the Head of Household to leave the household and have |
|  |  | the household maintain the same 5.09 Household Identifier while assigning a new |
|  |  | Head of Household. If the Head of Household leaves the project while other |
|  |  | household members remain, another member of the household currently |
|  |  | participating in the project must be designated as the Head of Household |
|  |  | (retroactively to the beginning of the household's entire enrollment). This may |
|  |  | require additional data entry on this household member as some fields are specific |
|  |  | to the Head of Household and may not have been collected at project start. For |
|  |  | more information, please see 5.09 Household Identifier. |
|  |  | The system must allow for non-Heads of Household to enter or exit the |
|  |  | household without having to complete a full program exit and new project start of |
|  |  | the entire household. |
| XML |  | <Enrollment><RelationshipToHoH> |
| CSV |  | Enrollment |
| 2024 Revision Summary |  | Wording change in system logic. |

### 3.16 Enrollment CoC

| Header | Instruction |
| --- | --- |
| Element Name | Enrollment CoC |
| Field 1 & Response | HUD assigned CoC code for the client's location at project start |
| Element Type | Universal |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | Head of Household |
| Collection Point | Project Start |
| Relationship to Enrollment ID | One Enrollment CoC per Enrollment |
| (an enrollment) |  |

| Relationship to Personal ID (a | One or more Enrollment CoC per Client |
| --- | --- |
| client) |  |
| System Logic & Other System | All project stays must be associated with a single Continuum of Care code. |
| lssues |  |
|  | This data element must be user-entered for all projects with more than one |
|  | Continuum of Care code identified in Project Descriptor Data Element 2.03 |
|  | Continuum of Care Information. It may be auto-populated for projects that operate |
|  | in a single CoC. |
|  | To allow projects operating in multiple continuums to enter data into a single |
|  | 'host' HMIS and provide data to each of the continuums in which they are serving |
|  | clients, a continuum must be identified at each project start. The Continuum of |
|  | Care code will be used in continuum reporting in the host HMIS to exclude |
|  | irrelevant data; it will also be used as a parameter for data export to provide |
|  | relevant data to other continuums. |
|  | If this field is collected for household members other than the Head of Household, |
|  | their Enrollment CoC data must reflect the CoC the Head of Household is located in |
|  | as of project start. |
|  | Systems may set up defaults to the continuum code of an HMIS implementation |
|  | but must be able to accept any other continuum code identified in data element |
|  | 2.03 Continuum of Care Information for the project. |
|  | For data quality purposes, the CoC codes in this data element should be limited to |
|  | the same CoC codes used for element 2.03 Continuum of Care Information. |
| XML | <Enrollment> |
| CSV | Enrollment |
| 2024 Revision Summary | This element now has a 1:1 relationship with enrollments and is collected at project |
|  | start only. |

## 3.20 Housing Move-In Date

| Header | Instruction |
| --- | --- |
| Element Name | Housing Move-In Date |
| Field 1 & Response | Housing Move-in Date ([date field]) |
| Element Type | Universal |
| Funder: Program-Component | All Programs – All Permanent Housing Components |
|  | Pay for Success – All component types |
| Project Type Applicability | 3: PH – Permanent Supportive Housing |
|  | 7: Other (Pay for Success ONLY) |
|  | 9: PH - Housing Only |
|  | 10: PH - Housing with Services (no disability required for entry) |
|  | 13: PH – Rapid Re-Housing |
| Data Collected About | Head of Household |
| Collection Point | Occurrence Point: At move-in – must be entered if/when a household moves into |
|  | any type of permanent housing, regardless of funding source or whether the |
|  | project is providing the rental assistance to differentiate between clients who are |
|  | housed and those who are experiencing homelessness at different points during |
|  | their enrollment. |
| Relationship to Enrollment ID | No more than one Housing Move-In Date per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Housing Move-In Date per Client |
| client) |  |

| System Logic & Other System | Housing Move-In Date must be a date occurring either on or between the 'project |
| --- | --- |
| lssues | start date' and 'project exit date'. |
|  | There can be no more than one Housing Move-in Date per enrollment. Once a |
|  | Housing Move-in Date has been recorded for an enrollment, it should not be |
|  | removed from the client's record, even if they subsequently lose that housing |
|  | situation. HMIS end users must be able to edit data only to correct errors. |
|  | HMIS software must NOT auto-populate Housing Move-In Date from one |
|  | enrollment record (5.06 Enrollment Identifier) to another. |
| XML | <MoveInDate> |
| CSV | Enrollment |
| 2024 Revision Summary | Added all Pay for Success project components as applicable for this data element, |
|  | including projects that do not provide permanent housing and are set up as Other (7) |
|  | project types. |

## 3.917 Prior Living Situation

The former universal data elements 3.9 Residence Prior to Proiect Start and 3.17 Length of Time on the Streets, in an Emergency Shelter or in a Safe Haven were combined into one element 3.917 Living Situation in 2014 v5. The element was split into two sub-elements which use only the fields and responses necessary for the population being asked the question. 3.917A is to be used for all persons entering a Street Outreach, Emergency Shelter (both entry exit and night- by-night), or Safe Haven project and 3.917B is to be used for persons entering all other HMIS project types. The internal HMIS field numbers for the fields and dependents of the sub-elements MUST be the same for like responses. With this separation and clarification, the definition of chronic homelessness as identified in the final rule in the Federal Register published December 5, 2015 can be fully reported through an HMIS.

| 3.917A Prior Living Situation |
| --- |
| For persons entering HMIS Project Type: Street Outreach, Emergency Shelter, & Safe Haven |

| Header | Instruction |
| --- | --- |
| Element Name | Prior Living Situation (A) |
| Field 1 & Responses | Type of Residence [See Appendix A – Living Situation Option List] |
| Dependent A – Dependent to |  |
| Field 1 Response 435 | Rental Subsidy Type [See Appendix A] |
| Field 2 & Responses | Length of stay in prior living situation |
|  | 10 One night or less |
|  | 11 Two to six nights |
|  | 2 One week or more, but less than one month |
|  | ന One month or more, but less than 90 days |
|  | ব 90 days or more, but less than one year |
|  | ട One year or longer |
|  | 8 Client doesn't know |
|  | ਰੇ Client prefers not to answer |
|  | ਰੇਰੇ Data not collected |
| Field 3 & Responses | Approximate date this episode of homelessness started: ([date field]) |

| Field 4 & Responses | Regardless of where they stayed last night, number of times the client has been on |
| --- | --- |
|  | the streets, in ES, or SH in the past three years including today |
| 1 | One Time |
| 2 | Two times |
| 3 | Three times |
| 4 | Four or more times |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Field 5 & Responses | Total number of months homeless on the street, in ES, or SH in the past three years |
| 101 | One month (this time is the first month) |
| 102-112 | ([integers 2-12]) |
| 113 | More than 12 months |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Universal |
| Funder: Program- Component | All Programs – All Components which are typed as Street Outreach, Emergency |
|  | Shelter – Entry Exit, Safe Haven, or Emergency Shelter – Night-by-Night. |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 1: Emergency Shelter - Night-by-Night |
|  | 4: Street Outreach |
|  | 8: Safe Haven |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start |
| Relationship to | No more than one Living Situation per Enrollment |
| Enrollment ID (an enrollment) |  |
| Relationship to Personal ID | One or more Living Situation per Client |
| (a client) |  |
| System Logic & Other System | This element, 3.917A is required for all projects which are typed in an HMIS as |
| Issues |  |
|  | Emergency Shelter (either entry exit or night-by-night type), Street Outreach, and |
|  | Safe Haven. No substitution in language or form may be made in this element. |
|  | This element requires no dependencies, and all fields are to be visible and |
|  | entered by the HMIS end user. |
|  | HMIS end users must be able to edit data to correct errors or to enter a response |
|  | for a client who has turned 18. Responses to this data element must always reflect |
|  | living situation and circumstances as of the Project Start Date and not at the time |
|  | of collection. |
|  | The internal field numbers for each of the fields and dependents contained within |
|  | this element MUST be the same as the field numbers used for 3.917B. |
| XML | <Enrollment><...> |
| CSV | Enrollment |
| 2024 Revision Summary | Wording change in system logic. Updated project type applicability to include |
|  | Emergency Shelter - Night-by-Night. Changed "Client refused' to "Client prefers |
|  | not to answer." Moved subsidized permanent residences into Dependent A |
|  | following Field 1, response 435 ("Rental by client, with ongoing housing subsidy") |

## 3.917B Prior Living Situation

## For persons entering: Transitional Housing, any type of Permanent Housing, Services Only, Day Shelter, Homelessness Prevention, or Coordinated Entry Project

| Header | Instruction |
| --- | --- |
| Element Name | Prior Living Situation (B) |
| Field 1 & Responses | Type of Residence [See Appendix A – Living Situation Option List] |
| Dependency Logic | [If response to Field 1: "Type of Residence" is a Homeless Situation (values 100- |
|  | 199), display Fields 3, 4, and 5] |
| Dependent A- Dependent to | Rental Subsidy Type [See Appendix A] |
| Field 1 Response 435 |  |
| Field 2 & Responses | Length of stay in the prior living situation |
| 10 | One night or less |
| ਹ ਹ | Two to six nights |
| 2 | One week or more, but less than one month |
| 3 | One month or more, but less than 90 days |
| 4 | 90 days or more, but less than one year |
| 5 | One year or longer |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| DEPENDENCIES | FOR INSTITUTIONAL SITUATIONS |
| Field 2A – for Institutional | Did you stay less than 90 days? |
| Situations |  |
| 0 | No |
| 1 | Yes |
| Dependency Logic | [If No - no other response options required] |
|  | [If Yes – use Field #2 response options 10, 11, 2, 3 and go to Field 2C] |
| DEPENDENCIES | FOR TEMPORARY, PERMANENT, AND OTHER SITUATIONS |
| Field 2B - for Housing Situations | Did you stay less than 7 nights? |
| 0 | No |
| 1 | Yes |
| Dependency Logic | [If No - no other response options required] |
|  | [If Yes – use Field #2 response options 10, 11, and go to Field 2C] |
| DEPENDENCY FOR YES TO 2A |  |
| OR 2B |  |
| Field 2C – For yes to 2a or 2b | On the night before did you stay on the streets, ES, or SH |
| 0 | No |
| 1 | Yes |
| Dependency Logic | [If No - no other response options required] |
|  | [If Yes – go to Field 3, followed by Field 4, and then Field 5] |
| ELEMENTS FOR CHRONIC |  |
| HOMELESSNESS |  |
| Field 3 & Responses | Approximate date this episode of homelessness started: ([date field]] |
| Field 4 & Response | Regardless of where they stayed last night, number of times the client has been on |
|  | the streets, in ES, or SH in the past three years including today |
| 1 | One Time |
| 2 | Two times |
| 3 | Three times |
| 4 | Four or more times |
| 8 | Client doesn't know |

|  | Client prefers not to answer 9 |
| --- | --- |
|  | Data not collected ਰੇਰੇ |
| Field 5 & Responses | Total number of months homeless on the street, in ES, or SH in the past three years |
| 101 | One month (this time is the first month) |
| 102-112 | ([integers 2-12]) |
| 113 | More than 12 months |
|  | Client doesn't know 8 |
|  | Client prefers not to answer 9 |
|  | Data not collected ਰੇਰੇ |
| Element Type | Universal |
| Funder: Program-Component | All Programs - All Components |
| Project Type Applicability | 2: Transitional Housing |
|  | 3: PH - Permanent Supportive Housing (disability required for entry) |
|  | 6: Services Only |
|  | 7: Other |
|  | 9: PH - Housing Only |
|  | 10: PH – Housing with Services (no disability required for entry) |
|  | 11: Day Shelter |
|  | 12: Homelessness Prevention |
|  | 13: PH - Rapid Re-Housing |
|  | 14: Coordinated Entrv |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start |
| Relationship to Enrollment ID | No more than one Living Situation per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Living Situation per Client |
| client) |  |
| System Logic & Other System | This element, 3.917B, is required for all project types in an HMIS other than |
| lssues | Emergency Shelter (either entry exit or night-by-night type), Street Outreach, and |
|  | Safe Haven. No substitution in language or form may be made in this element. |
|  | HMIS end users must be able to edit data to correct errors or to enter a response |
|  | for a client who has turned 18. Responses to this data element must always reflect |
|  | living situation and circumstances as of the Project Start Date and not at the time |
|  | of collection. |
|  | An HMIS must be able to create dependencies for this element. Data for the fields |
|  | of this data element should be logically consistent. It is strongly recommended that |
|  | an HMIS is programmed to enforce these rules or to notify users when inconsistent |
|  | data has been entered. |
|  | If there is a "yes" response, then the next response elements must be available for |
|  | data entry. If there is any other response, then the next response element must |
|  | either be hidden or darkened or in some other way identified as not to be |
|  | completed. |
|  | The internal field numbers for each of the fields and dependents contained within |
|  | this element MUST be the same as the field numbers used for 3.917A. |
| XML | <Enrollment><...> |
| CSV | Enrollment |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Moved subsidized permanent residences into Dependent A following |
|  | Field 1, |
|  | response 435 ("Rental by client, with ongoing housing subsidy") |

## PROGRAM SPECIFIC DATA ELEMENTS

#### COMMON PROGRAM SPECIFIC DATA ELEMENTS

#### 4.02 Income and Sources

| Header | Instruction |
| --- | --- |
| Element Name | Income and Sources |
| Field 1 & Response | Information Date (date information was collected) ([date field]) |
| Field 2 & Responses | Income from Any Source |
|  | 0 No |
|  | 1 Yes |
|  | 8 Client doesn't know |
|  | 9 Client prefers not to answer |
|  | ਰੇਰੇ Data not collected |
|  | [If yes for "Income from any source"] |
|  | Indicate all sources and dollar amounts for the source that apply |
| Field 3 & Responses | Earned income (i.e., employment income) |
|  | 0 No |
|  | Yes । |
| Dependent A - Dependent to | Monthly Amount ([currency/decimal]) |
| Field 3 & Response 1 |  |
| Field 4 & Responses | Unemployment Insurance |
|  | No 0 |
|  | । Yes |
| Dependent B - Dependent to | Monthly Amount ([currency/decimal]) |
| Field 4 & Response 1 |  |
| Field 5 & Responses | Supplemental Security Income (SSI) |
|  | 0 No |
|  | Yes 1 |
| Dependent C - Dependent to | Monthly Amount ([currency/decimal]) |
| Field 5 & Response 1 |  |
| Field 6 & Responses | Social Security Disability Insurance (SSDI) |
|  | No 0 |
|  | । Yes |
| Dependent D - Dependent to | Monthly Amount ([currency/decimal]) |
| Field 6 & Response 1 |  |
| Field 7 & Responses | VA Service-Connected Disability Compensation |
|  | No 0 |
|  | T Yes |
| Dependent E-Dependent to | Monthly Amount ([currency/decimal]) |
| Field 7 & Response 1 |  |
| Field 8 & Responses | VA Non-Service-Connected Disability Pension |
|  | 0 No |
|  | Yes T |
| Dependent F - Dependent to | Monthly Amount ([currency/decimal]) |
| Field 8 & Response 1 |  |
| Field 9 & Responses | Private disability insurance |

| No | 0 | Yes | 1 |  |
| --- | --- | --- | --- | --- |
| Monthly Amount ([currency/decimal]) | Dependent G - Dependent to | Field 9 & Response 1 |  |  |
| Field 10 & Responses | Worker's Compensation | No | 0 |  |
| 1 | Yes | Monthly Amount ([currency/decimal]) | Dependent H - Dependent to |  |
| Field 10 & Response 1 | Temporary Assistance for Needy Families (TANF) [or use local name] | Field 11 & Responses |  |  |
| No | 0 | Yes | T |  |
| Monthly Amount ([currency/decimal]) | Dependent I – Dependent to | Field 11 & Response 1 |  |  |
| General Assistance (GA) [or use local name] | Field 12 & Responses | No | 0 |  |
| 1 | Yes | Monthly Amount ([currency/decimal]) | Dependent J - Dependent to |  |
| Field 12 & Response 1 | Retirement Income from Social Security | Field 13 & Responses |  |  |
| 0 | No | 1 | Yes |  |
| Monthly Amount ([currency/decimal]) | Dependent K - Dependent to | Field 13 & Response 1 |  |  |
| Pension or retirement income from a former job | Field 14 & Responses | No | O |  |
| Yes | T | Monthly Amount ([currency/decimal]) | Dependent L - Dependent to |  |
| Field 14 & Response 1 | Child support | Field 15 & Responses |  |  |
| O | No | Yes | 1 |  |
| Monthly Amount ([currency/decimal]) | Dependent M - Dependent to | Field 15 & Response 1 |  |  |
| Alimony and other spousal support | Field 16 & Responses | 0 | No |  |
| T | Yes | Monthly Amount ([currency/decimal]) | Dependent N - Dependent to |  |
| Field 16 & Response 1 | Field 17 & Responses | Other source |  |  |
| No | O | Yes | T |  |
| Monthly Amount ([currency/decimal]) | Dependent O - Dependent to | Field 17 & Response 1 |  |  |
| [If Yes for "Other Source"] | Dependent P - Dependent to | Text box for Specify Source | Field 17 & Response 1 |  |
| Total Monthly Income [ | Field 18 & Response | .00/ | Program Specific | Element Type |
| HUD: CoC – Collection required for all components except SSO Coordinated Entry | Funder: Program-Component | HUD: ESG – Collection required for all components except ES-NbN |  |  |

|  |  | HUD: ESG RUSH – Collection required for all components except Emergency Shelter |
| --- | --- | --- |
|  |  | or Street Outreach |
|  |  | HUD: HOPWA – Collection required for all components |
|  |  | HUD: Unsheltered Special NOFO – Collection required for all components except |
|  |  | SSO Coordinated Entry |
|  |  | HUD: Rural Special NOFO – Collection required for all components except SSO |
|  |  | Coordinated Entry |
|  |  | HUD: HUD-VASH – Collection required for HUD VASH Collaborative Case |
|  |  | Management |
|  |  | HUD: PFS - Collection required for all permanent housing projects |
|  |  | HHS: PATH – Collection required for all components |
|  |  | HHS: RHY – Collection only required for MGH, TLP, and Demo |
|  |  | VA: SSVF – Collection required for RRH and Homelessness Prevention |
|  |  | VA: GPD – Collection required for all components |
|  |  | VA: Community Contract Safe Haven |
|  |  | VA: CRS Contract Residential Services |
| Project Type Applicability |  | All HMIS Project Types |
| Data Collected About |  | Head of Households and Adults |
| Collection Point |  | Project Start, Update, Annual Assessment, and Project Exit |
| Relationship to Enrollment ID |  | One or more Income and Sources per Enrollment |
| (an enrollment) |  |  |
| Relationship to Personal ID (a |  | One or more Income and Sources per Client |
| client) |  |  |
| System Logic & Other System |  | The system must record the appropriate data collection stage for each record of |
| lssues |  | this data element. |
|  |  | Systems must allow users to create 'update' records to document changes |
|  |  | between required collection points. Allow corrections for data entry errors at all |
|  | stages. |  |
|  |  | Dependent P has a 50-character limit when exporting in the HMIS CSV. |
|  |  | Data for the fields of this data element should be logically consistent. It is expected |
|  |  | identified, then a 'Monthly amount' must be entered. If a 'Monthly amount' is |
|  |  | entered for any source, then a 'Total monthly income' amount is required. |
|  |  | If there is a "no" response to Field 2 'Income from any source' then the HMIS must |
|  |  | automatically record all sources as "no" and leave dollar amounts null or $0.00. |
|  |  | To reduce data collection and reporting burden: |
|  |  | ● Systems are encouraged to auto-calculate total monthly income to avoid |
|  |  | mathematical errors and reduce data collection (generate a $0.00 for total |
|  |  | monthly income if 'Income from any source' = "no"). |
|  |  | ● lf a client reports receiving income, an HMIS may be designed such that |
|  |  | projects only need to directly enter "yes" for the income source the client |
|  |  | receives and have the HMIS automatically generate a "no" response for the |
|  |  | other income sources. |
|  |  | ● An HMIS may facilitate data accuracy by automatically changing a "no" in |
|  |  | 'income from any source' to a "yes" if source(s) and dollar amount(s) are |
|  |  | indicated. |
|  |  | that an HMIS is programmed to enforce these rules or to notify users when |
|  |  | inconsistent data has been entered. If there is a "yes" response to 'Income from |
|  |  | any source' then at least one source of income must be identified. If a source is |

|  | Updates are required for persons aging into adulthood. An HMIS end user must be |
| --- | --- |
|  | able to create or edit the Income and Sources record at project start as well as |
|  | enter an update as of the participant's 18th birthday. |
| XML | <IncomeAndSources> |
| CSV | IncomeBenefits |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Removed "HUD: RHSAP – Collection required for all components" from |
|  | Funder: Program-Component section. |

#### 4.03 Non-Cash Benefits

| Header |  | Instruction |
| --- | --- | --- |
| Element Name |  | Non-Cash Benefits |
| Field 1 & Response |  | Information Date (date information was collected) ([date field]) |
| Field 2 & Responses |  | Non-Cash Benefits from Any Source |
|  | 0 | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ | Data not collected |
|  |  | [If yes for Non-cash benefits from any source"] |
|  |  | Indicate all sources that apply |
| Field 3 & Responses |  | Supplemental Nutrition Assistance Program (SNAP) (Previously known as Food |
|  |  | Stamps) |
|  | 0 | No |
|  | 1 | Yes |
| Field 4 & Responses |  | Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) |
|  | 0 | No |
|  | 1 | Yes |
| Field 5 & Responses |  | TANF Child Care services [or use local name] |
|  | 0 | No |
|  | 1 | Yes |
| Field 6 & Responses |  | TANF transportation services [or use local name] |
|  | 0 | No |
|  | 1 | Yes |
| Field 7 & Responses |  | Other TANF-funded services |
|  | 0 | No |
|  | 1 | Yes |
| Field 8 & Responses |  | Other source |
|  | 0 | No |
|  | 1 | Yes |
| Dependent A- Dependent to |  | [If Yes for "Other Source"] |
| Field 8 & Response 1 |  | Text box for Specify Source |
| Element Type |  | Program Specific |
| Funder: Program-Component |  | HUD: CoC – Collection required for all components except SSO Coordinated Entry |
|  |  | HUD: ESG – Collection required for all components except ES-NbN |
|  |  | HUD: ESG RUSH – Collection required for all components except Emergency Shelter |
|  |  | or Street Outreach |
|  |  | HUD: HOPWA – Collection required for all components |
|  |  | HUD: Unsheltered Special NOFO – Collection required for all components except |

|  | SSO Coordinated Entry |
| --- | --- |
|  | HUD: Rural Special NOFO – Collection required for all components except SSO |
|  | Coordinated Entry |
|  | HUD: HUD-VASH – Collection required for HUD VASH Collaborative Case |
|  | Management |
|  | HUD: PFS – Collection required for all permanent housing projects |
|  | HHS: PATH – Collection required for all components |
|  | HHS: RHY – Collection only required for BCP (HP and ES), MGH, TLP, and Demo |
|  | VA: SSVF – Collection required for RRH and Homelessness Prevention |
|  | VA: GPD – Collection required for all components |
|  | VA: Community Contract Safe Haven |
|  | VA: CRS Contract Residential Services |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | Head of Households and Adults |
| Collection Point | Project Start, Update, Annual Assessment, and Project Exit |
| Relationship to Enrollment ID | One or more Non-Cash Benefits per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Non-Cash Benefits per Client |
| client) |  |
| System Logic & Other System | The system must record the appropriate data collection stage for each record of |
| lssues | this data element. Systems must allow HMIS end users to create 'update' records |
|  | to document changes between required collection points. Allow corrections for |
|  | data entry errors at all stages. |
|  | Dependent A has a 50-character limit when exporting in the HMIS CSV. |
|  | Data for the fields of this data element should be logically consistent. It is expected |
|  | that the HMIS is programmed to enforce these rules or to notify users when |
|  | inconsistent data has been entered. If there is a "Yes" response to 'Non-Cash |
|  | Benefits from Any Source' then at least one source of non-cash benefit must be |
|  | identified. If there is a "No" response to "'Non-Cash Benefit from Any Source' then |
|  | the HMIS must automatically record all sources as "No." |
|  | To reduce data collection and reporting burden: |
|  | ● If a client reports receiving non-cash benefits, an HMIS may be designed |
|  | such that projects only need to directly enter "Yes" for the benefit source |
|  | the client receives and have the HMIS automatically generate a "No" |
|  | response for the other benefit sources. |
|  | ● An HMIS may facilitate data accuracy by automatically changing a "No" in |
|  | 'Non- Cash Benefits from Any Source' to a "Yes" if source(s) are indicated. |
|  | Updates are required for persons aging into adulthood. A user must be able to create |
|  | or edit the Non-Cash Benefits record at Project Start as well as enter an update as of |
|  | the participant's 18th birthday. |
|  | Non-cash benefits may be entered into more detailed categories as long as these |
|  | categories can be aggregated into the above-stated non-cash benefits. |
| XML | <NonCashBenefits> |
| CSV | IncomeBenefits |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Removed "HUD: RHSAP – Collection required for all components" from |
|  | Funder: Program-Component section. |

#### 4.04 Health Insurance

| Header | Instruction |
| --- | --- |
| Element Name | Health Insurance |
| Field 1 & Response | Information Date (date information was collected) ([date field]) |
| Field 2 & Responses | Covered by Health Insurance |
|  | 0 No |
|  | 1 Yes |
|  | 8 Client doesn't know |
|  | 9 Client prefers not to answer |
|  | ਰੇਰੇ Data not collected |
|  | [If yes for "Covered by Health Insurance"] |
|  | Indicate all sources that apply |
| Field 3 & Responses | MEDICAID |
|  | 0 No |
|  | 1 Yes |
| Field 4 & Responses | MEDICARE |
|  | 0 No |
|  | 1 Yes |
| Field 5 & Response | State Children's Health Insurance Program [or use local name] |
|  | 0 No |
|  | 1 Yes |
| Field 6 & Responses | Veteran's Health Administration (VHA) |
|  | No 0 |
|  | 1 Yes |
|  | Employer-Provided Health Insurance |
| Field 7 & Responses |  |
|  | 0 No |
|  | 1 Yes |
| Field 8 & Responses | Health Insurance obtained through COBRA |
|  | 0 No |
|  | Yes 1 |
| Field 9 & Responses | Private Pay Health Insurance |
|  | 0 No |
|  | 1 Yes |
| Field 10 & Responses | State Health Insurance for Adults [or use local name] |
|  | 0 No |
|  | 1 Yes |
| Field 11 & Responses | Indian Health Services Program |
|  | 0 No |
|  | Yes 1 |
| Field 12 & Responses | Other |
|  | 0 No |
|  | T Yes |
| (if yes to other-Specify source) | (text) |
| Dependent A - Dependent to | If "No" for each of the health insurance sources, Reason |
| Fields 3-11 & Response 0 |  |
| HOPWA FIELD ONLY |  |

| Applied; decision pending | 1 | Applied; client not eligible | 2 |
| --- | --- | --- | --- |
| 3 | Client did not apply | Insurance type N/A for this client | 4 |
| Client doesn't know | 8 | 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected | Program Specific | Element Type |
| Funder: Program-Component | HUD: CoC – Collection required for all components except SSO Coordinated Entry | HUD: ESG – Collection required for all components except ES-NbN |  |
| HUD: ESG RUSH – Collection required for all components except Emergency Shelter | or Street Outreach |  |  |
| HUD: HOPWA – Collection required for all components | HUD: Unsheltered Special NOFO – Collection required for all components except |  |  |
| SSO Coordinated Entry | HUD: Rural Special NOFO – Collection required for all components except SSO |  |  |
| Coordinated Entry | HUD: HUD-VASH – Collection required for HUD VASH Collaborative Case |  |  |
| Management | HUD: PFS – Collection required for all permanent housing projects |  |  |
| HHS: PATH – Collection required for all components | HHS: RHY – Collection required for all components |  |  |
| VA: SSVF – Collection required for RRH and Homelessness Prevention | VA: GPD – Collection required for all components |  |  |
| VA: Community Contract Safe Haven | VA: CRS Contract Residential Services |  |  |
| Project Type Applicability | All HMIS Project Types | Data Collected About | All Clients |
| Collection Point | Project Start, Update, Annual Assessment, and Project Exit | Relationship to Enrollment ID | One or more Health Insurance per Enrollment |
| (an enrollment) | Relationship to Personal ID (a | One or more Health Insurance per Client |  |
| client) | System Logic & Other System |  |  |
| The system must record the appropriate collection stage for each record of this | lssues | data element. Systems must allow HMIS end users to create 'update' records to |  |
| document changes between required collection points. Allow corrections for data | entry errors at all stages. |  |  |
| Dependent 4.04.12A has a 50-character limit when exporting in the HMIS CSV. |  |  |  |
| Data for the fields of this data element should be logically consistent. It is expected | that an HMIS is programmed to enforce these rules or to notify users when |  |  |
| inconsistent data has been entered. If there is a "yes" response to 'Covered by | health insurance' then at least one source of health insurance must be identified. If |  |  |
| there is a "no" response to 'Covered by health insurance' then the HMIS must | automatically record all sources as "no." |  |  |
| To reduce data collection and reporting burden: |  |  |  |
| If a client reports 'Covered by health insurance' as "yes", an HMIS may be | ● | designed such that projects only need to directly enter "yes" for the health |  |
| insurance the client is covered by and have the HMIS automatically | generate a "no" response for the other health insurance sources. |  |  |

|  | • An HMIS may facilitate data accuracy by automatically changing a "no" in |
| --- | --- |
|  | 'Covered by health insurance' to a "yes" if source(s) are indicated. |
| XML | <HealthInsurance> |
| CSV | IncomeBenefits |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Removed "HUD: RHSAP – Collection required for all components" |
|  | from Funder: Program-Component section. Renamed Field 6. |

#### 4.05 Physical Disability

| Header | Instruction |  |
| --- | --- | --- |
| Element Name |  | Physical Disability |
| Field 1 & Response |  | Information Date (date information was collected) ([date field]) |
| Field 2 & Responses |  | Physical Disability |
|  | 0 No |  |
|  | 1 Yes |  |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ | Data not collected |
| Dependent A - Dependent to |  | [If Yes for "Physical Disability"] |
| Field 2 & Response 1 |  | Expected to be of long–continued and indefinite duration and substantially impairs |
|  |  | ability to live independently |
|  | 0 No |  |
|  | 1 Yes |  |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ | Data not collected |
| Element Type |  | Program Specific |
| Funder: Program-Component |  | HUD: CoC – Collection required for all components except SSO Coordinated Entry |
|  |  | HUD: ESG – Collection required for all components |
|  |  | HUD: ESG RUSH – Collection required for all components except Emergency Shelter |
|  |  | or Street Outreach |
|  |  | HUD: HOPWA – Collection required for all components |
|  |  | HUD: Unsheltered Special NOFO – Collection required for all components except |
|  |  | SSO Coordinated Entry |
|  |  | HUD: Rural Special NOFO – Collection required for all components except SSO |
|  |  | Coordinated Entry |
|  |  | HUD: HUD-VASH – Collection required for HUD VASH Collaborative Case |
|  |  | Management |
|  |  | HUD: PFS – Collection required for all permanent housing projects |
|  |  | HHS: PATH - Collection required for all components |
|  |  | HHS: RHY – Collection required for all components |
|  |  | VA: GPD – Collection required for all components |
|  |  | VA: Community Contract Safe Haven |
|  |  | VA: CRS Contract Residential Services |
| Project Type Applicability |  | All HMIS Project Types |
| Data Collected About |  | All Clients |
| Collection Point |  | Project Start, Update, and Project Exit |
| Relationship to Enrollment ID |  | One or more Physical Disability per Enrollment |
| (an enrollment) |  |  |

| Relationship to Personal ID (a | One or more Physical Disability per Client |
| --- | --- |
| client) |  |
| System Logic & Other System | The system must record the appropriate data collection stage for each record of |
| Issues | this data element. Systems must allow HMIS end users to create 'update' records |
|  | to document changes between required collection points. Systems must also allow |
|  | corrections for data entry errors at all stages. |
|  | HMIS may choose to only display dependent questions if the HMIS end user selects |
|  | the appropriate response. |
| XML | <Disabilities> |
| CSV | Disabilities |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Removed "HUD: RHSAP – Collection required for all components" from |
|  | Funder: Program-Component section. |

## 4.06 Developmental Disability

| Header | Instruction |
| --- | --- |
| Element Name | Developmental Disability |
| Field 1 & Response | Information Date (date information was collected) ([date field]) |
| Field 2 & Responses | Developmental Disability |
| 0 | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: CoC – Collection required for all components except SSO Coordinated Entry |
|  | HUD: ESG – Collection required for all components |
|  | HUD: ESG RUSH – Collection required for all components except Emergency Shelter |
|  | or Street Outreach |
|  | HUD: HOPWA – Collection required for all components |
|  | HUD: Unsheltered Special NOFO – Collection required for all components except |
|  | SSO Coordinated Entry |
|  | HUD: Rural Special NOFO – Collection required for all components except SSO |
|  | Coordinated Entry |
|  | HUD: HUD-VASH – Collection required for HUD VASH Collaborative Case |
|  | Management |
|  | HUD: PFS - Collection required for all permanent housing projects |
|  | HHS: PATH – Collection required for all components |
|  | HHS: RHY – Collection required for all components |
|  | VA: GPD – Collection required for all components |
|  | VA: Community Contract Safe Haven |
|  | VA: CRS Contract Residential Services |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Clients |
| Collection Point | Project Start, Update, and Project Exit |
| Relationship to Enrollment ID | One or more Developmental Disability per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Developmental Disability per Client |
| client) |  |

| System Logic & Other System | The system must record the appropriate data collection stage for each record of |
| --- | --- |
| lssues | this data element. Systems must allow HMIS end users to create 'update' records |
|  | to document changes between required collection points. Systems must also allow |
|  | corrections for data entry errors at all stages. |
|  | HMIS may choose to only display dependent questions if the HMIS end user selects |
|  | the appropriate response. |
| XML | <Disabilities> |
| CSV | Disabilities |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Removed "HUD: RHSAP – Collection required for all |
|  | components" from Funder: Program-Component section. |

## 4.07 Chronic Health Condition

| Header | Instruction |
| --- | --- |
| Element Name | Chronic Health Condition |
| Field 1 & Response | Information Date (date information was collected) ([date field]) |
| Field 2 & Responses | Chronic Health Condition |
| O | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent A - Dependent to | [If Yes for "Chronic Health Condition"] |
| Field 2 & Response 1 | Expected to be of long-continued and indefinite duration and substantially |
|  | impairs ability to live independently |
| 0 | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: CoC – Collection required for all components except SSO Coordinated Entry |
|  | HUD: ESG – Collection required for all components |
|  | HUD: ESG RUSH – Collection required for all components except Emergency Shelter |
|  | or Street Outreach |
|  | HUD: HOPWA – Collection required for all components |
|  | HUD: Unsheltered Special NOFO – Collection required for all components except |
|  | SSO Coordinated Entry |
|  | HUD: Rural Special NOFO – Collection required for all components except SSO |
|  | Coordinated Entry |
|  | HUD: HUD-VASH – Collection required for HUD VASH Collaborative Case |
|  | Management |
|  | HUD: PFS - Collection required for all permanent housing projects |
|  | HHS: PATH – Collection required for all components |
|  | HHS: RHY – Collection required for all components |
|  | VA: GPD – Collection required for all components |
|  | VA: Community Contract Safe Haven |
|  | VA: CRS Contract Residential Services |
| Project Type Applicability | All HMIS Project Types |

| Data Collected About | All Clients |
| --- | --- |
| Collection Point | Project Start, Update, and Project Exit |
| Relationship to Enrollment ID | One or more Chronic Health Condition per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Chronic Health Condition per Client |
| client) |  |
| System Logic & Other System | The system must record the appropriate collection stage for each element. |
| lssues | Systems must allow HMIS end users to create 'update' records to document |
|  | changes between required collection points. Systems must also allow corrections |
|  | for data entry errors at all stages. |
|  | An HMIS may choose to only display dependent questions if the HMIS end user |
|  | selects the appropriate response. |
| XML | <Disabilities> |
| CSV | Disabilities |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Removed "HUD: RHSAP – Collection required for all |
|  | components" from Funder: Program-Component section. |

## 4.08 HIV/AIDS

| Header | Instruction |
| --- | --- |
| Element Name | HIV/AIDS |
| Field 1 & Response | Information Date (date information was collected) ([date field]) |
| Field 2 & Response | HIV/AIDS |
| O | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: CoC – Collection required for all components except SSO Coordinated Entry |
|  | HUD: ESG – Collection required for all components |
|  | HUD: ESG RUSH – Collection required for all components except Emergency Shelter |
|  | or Street Outreach |
|  | HUD: HOPWA – Collection required for all components |
|  | HUD: Unsheltered Special NOFO – Collection required for all components except |
|  | SSO Coordinated Entry |
|  | HUD: Rural Special NOFO – Collection required for all components except SSO |
|  | Coordinated Entry |
|  | HUD: HUD-VASH – Collection required for HUD VASH Collaborative Case |
|  | Management |
|  | HUD: PFS - Collection required for all permanent housing projects |
|  | VA: GPD – Collection required for all components |
|  | VA: Community Contract Safe Haven |
|  | VA: CRS Contract Residential Services |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Clients |
| Collection Point | Project Start, Update, and Project Exit |
| Relationship to Enrollment ID | One or more HIV/AIDS per Enrollment |
| (an enrollment) |  |

| Relationship to Personal ID (a | One or more HIV/AIDS per Client |
| --- | --- |
| client) |  |
| System Logic & Other System lssues | The system must record the appropriate data collection stage for each record of |
|  | this data element. Systems must allow HMIS end users to create 'update' records |
|  | to document changes between required collection points. Systems must also allow |
|  | corrections for data entry errors at all stages. |
| XML | <Disabilities> |
| CSV | Disabilities |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Removed "HUD: RHSAP – Collection required for all components" from |
|  | Funder: Program-Component section. |

#### 4.09 Mental Health Disorder

| Header | Instruction | Element Name | Mental Health Disorder |
| --- | --- | --- | --- |
| Information Date (date information was collected) ([date field]) | Field 1 & Response | Field 2 & Response | Mental Health Disorder |
| 0 | No | 1 | Yes |
| 8 | Client doesn't know | 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected | [If Yes for "Mental Health Disorder"] | Dependent A - Dependent to |
| Expected to be of long-continued and indefinite duration and substantially impairs | Field 2 & Response 1 | ability to live independently |  |
| 0 | No | Yes | 1 |
| Client doesn't know | 8 | 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected | Element Type | Program Specific |
| Funder: Program-Component | HUD: CoC – Collection required for all components except SSO Coordinated Entry | HUD: ESG – Collection required for all components |  |
| HUD: ESG RUSH – Collection required for all components except Emergency Shelter | or Street Outreach |  |  |
| HUD: HOPWA – Collection required for all components | HUD: Unsheltered Special NOFO – Collection required for all components except |  |  |
| SSO Coordinated Entry | HUD: Rural Special NOFO – Collection required for all components except SSO |  |  |
| Coordinated Entry | HUD: HUD-VASH – Collection required for HUD VASH Collaborative Case |  |  |
| Management | HUD: PFS – Collection required for all permanent housing projects |  |  |
| HHS: PATH - Collection required for all components | HHS: RHY – Collection required for all components |  |  |
| VA: GPD – Collection required for all components | VA: Community Contract Safe Haven |  |  |
| VA: CRS Contract Residential Services | Project Type Applicability | All HMIS Project Types |  |
| Data Collected About | All Clients |  |  |

| Collection Point | Project Start, Update, and Project Exit |
| --- | --- |
| Relationship to Enrollment ID | One or more Mental Health Disorder per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Mental Health Disorder per Client |
| client) |  |
| System Logic & Other System | The system must record the appropriate data collection stage for each record of |
| lssues | this data element. Systems must allow HMIS end users to create 'update' records |
|  | to document changes between required collection points. Systems must also allow |
|  | corrections for data entry errors at all stages. |
|  | HMIS may choose to only display dependent questions if the HMIS end user selects |
|  | the appropriate response. |
| XML | <Disabilities> |
| CSV | Disabilities |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Removed "HUD: RHSAP – Collection required for all components" from |
|  | Funder: Program-Component section. |

## 4.10 Substance Use Disorder

| Header | Instruction | Element Name | Substance Use Disorder |
| --- | --- | --- | --- |
| Field 1 & Response | Information Date (date information was collected) ([date field]) | Field 2 & Responses | Substance Use Disorder |
| O | No | Alcohol use disorder | 1 |
| 2 | Drug use disorder | 3 | Both alcohol and drug use disorders |
| 8 | Client doesn't know | 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected | Dependent A - Dependent to | [If Alcohol use disorder, Drug use disorder, or Both alcohol and drug use disorders |
| Field 2 & Response(s) 1 -3 | for "Substance Use Disorder"] | Expected to be of long-continued and indefinite duration and substantially |  |
| impairs ability to live independently | 0 | No |  |
| Yes | 1 | Client doesn't know | 8 |
| 9 | Client prefers not to answer | Data not collected | ਰੇਰੇ |
| Element Type | Program Specific | Funder: Program-Component | HUD: CoC – Collection required for all components except SSO Coordinated Entry |
| HUD: ESG – Collection required for all components | HUD: ESG RUSH - Collection required for all components except Emergency Shelter |  |  |
| or Street Outreach | HUD: HOPWA – Collection required for all components |  |  |
| HUD: Unsheltered Special NOFO – Collection required for all components except | SSO Coordinated Entry |  |  |
| HUD: Rural Special NOFO – Collection required for all components except SSO | Coordinated Entry |  |  |
| HUD: HUD-VASH – Collection required for HUD VASH Collaborative Case |  |  |  |

|  | Management |
| --- | --- |
|  | HUD: PFS – Collection required for all permanent housing projects |
|  | HHS: PATH – Collection required for all components |
|  | HHS: RHY – Collection required for all components |
|  | VA: GPD – Collection required for all components |
|  | VA: Community Contract Safe Haven |
|  | VA: CRS Contract Residential Services |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Clients |
| Collection Point | Project Start, Update, and Project Exit |
| Relationship to Enrollment ID | One or more Substance Use Disorder per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Substance Use Disorder per Client |
| client) |  |
| System Logic & Other System | The system must record the appropriate collection stage for each element. |
| Issues | Systems must allow HMIS end users to create 'update' records to document |
|  | changes between required collection points. Systems must also allow corrections |
|  | for data entry errors at all stages. |
|  | HMIS may choose to only display dependent questions if the HMIS end user selects |
|  | the appropriate response. |
| XML | <Disabilities> |
| CSV | Disabilities |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Removed "HUD: RHSAP – Collection required for all components" from |
|  | Funder: Program-Component section. |

4.11 Domestic Violence

| Header |  | Instruction |
| --- | --- | --- |
| Element Name |  | Domestic Violence |
| Field 1 & Response |  | Information Date (date information was collected) ([date field]) |
| Field 2 & Responses |  | Survivor of Domestic Violence |
|  | 0 | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Dependent A - Dependent to |  | If Yes for "Survivor of Domestic Violence" |
| Field 2 & Response 1 |  | When experience occurred |
|  | 1 | Within the past three months |
|  | 2 | Three to six months ago (excluding six months exactly) |
|  | 3 | Six months to one year ago (excluding one year exactly) |
|  | 4 | One year ago, or more |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Dependent B – Dependent to |  | If Yes for "Survivor of Domestic Violence " |
| Field 2 & Response 1 |  | Are you currently fleeing? |
|  | 0 | No |
|  | 1 | Yes |

| 8 | Client doesn't know |
| --- | --- |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: CoC – Collection required for all components except SSO Coordinated Entry |
|  | HUD: ESG – Collection required for all components |
|  | HUD: ESG RUSH – Collection required for all components except Emergency Shelter |
|  | or Street Outreach |
|  | HUD: HOPWA – Collection required for all components |
|  | HUD: Unsheltered Special NOFO – Collection required for all components except |
|  | SSO Coordinated Entry |
|  | HUD: Rural Special NOFO – Collection required for all components except SSO |
|  | Coordinated Entry |
|  | HUD: HUD-VASH – Collection required for HUD VASH Collaborative Case |
|  | Management |
|  | HUD: PFS – Collection required for all permanent housing projects |
|  | HHS: PATH – Collection required for all components |
|  | VA: SSVF – Collection required for RRH and Homelessness Prevention |
|  | VA: GPD – Collection required for all components |
|  | VA: Community Contract Safe Haven VA: CRS Contract Residential Services |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start, Update |
| Relationship to Enrollment ID | One or more Domestic Violence per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Domestic Violence per Client |
| client) |  |
| System Logic & Other System | The system must record the appropriate collection stage for each element. |
| Issues |  |
|  | Systems must also allow for 'update' information if a change occurs mid-year. |
|  | Allow corrections for data entry errors at all stages. |
|  | HMIS may choose to only display dependent questions if the HMIS end user selects |
|  | the appropriate response. |
| XML | <DomesticViolence> |
| CSV | HealthAndDV |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer" and replaced "victim" language with "survivor" language. Removed "HUD: |
|  | RHSAP – Collection required for all components" from Funder: Program- |
|  | Component section. |

#### 4.12 Current Living Situation

| Header | Instruction |
| --- | --- |
| Element Name | Current Living Situation |
| Field 1 & Response | Information Date (date of contact) ([date field]) |
| Field 2 & Responses | Current Living Situation /See Appendix A - Living Situation Information |
| Dependent A - Dependent to | Rental Subsidy Type [See Appendix A] |
| Field 2 Response 435 |  |
| Field 3 & Response |  |
| (Coordinated Entry Projects | Living situation verified by [list of Continuum projects] |
| ONLY) |  |
| Dependent B - Dependent to |  |

| Field 2 Responses all non- homeless situation responses |  |  |
| --- | --- | --- |
|  |  | Is client going to have to leave their current living situation within 14 days? |
| (17, 37, and all responses |  |  |
| between 200 and 499 inclusive) | 0 | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Dependent C - Dependent to |  | Has a subsequent residence been identified? |
| Dependent B response: 1 |  |  |
|  | 0 | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Dependent D - Dependent to |  | Does individual or family have resources or support networks to obtain other |
| Dependent B response: 1 |  | permanent housing? |
|  | 0 | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Dependent E - Dependent to |  | Has the client had a lease or ownership interest in a permanent housing unit in the |
| Dependent B response: 1 |  | last 60 days? |
|  | 0 | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Dependent F - Dependent to |  | Has the client moved 2 or more times in the last 60 days? |
| Dependent B response: 1 |  |  |
|  | 0 | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Field 4 & Response |  | Location details ([text box]) |
| Element Type |  | Program Specific |
| Funder: Program-Component |  | HUD: CoC – Collection required for SSO - Street Outreach, SSO - Coordinated Entry, |
|  |  | and any YHDP funded project type serving clients who meet Category 2 or 3 of the |
|  |  | homeless definition |
|  |  | HUD: ESG – Collection only required for Street Outreach, and NbN shelter |
|  |  | HUD: ESG RUSH – Collection required for Street Outreach, Coordinated Entry, and |
|  |  | ES - NPN |
|  |  | HUD: Unsheltered Special NOFO – Collection required for SSO – Street Outreach, |
|  |  | SSO - Coordinated Entry |
|  |  | HUD: Rural Special NOFO - Collection required for SSO - Street Outreach, SSO - |
|  |  | Coordinated Entry |

|  | HHS: PATH – Collection required for all components |
| --- | --- |
|  | HHS: RHY – Collection only required for Street Outreach |
| Project Type Applicability | 1: Emergency Shelter – Night-by-Night |
|  | 4: Street Outreach |
|  | 6: Services Only |
|  | 14: Coordinated Entry (or other depending on CoC design of Coordinated Entry |
|  | system) |
| Data Collected About | Head of Household and Adults |
| Collection Point | Occurrence Point (At the Time of Contact) |
| Relationship to Enrollment ID | 0 or more Current Living Situation per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | 1 or more Current Living Situation per Client |
| client) |  |
| System Logic & Other System | The data in this element are transactional data; each time there is a contact, a |
| Issues | record of the contact must be recorded including the date and the client's current |
|  | living situation. |
|  | Data Collection requirements for PATH-funded components are limited to the |
|  | following field 2 Living Situation Options: |
|  | (116) Place not meant for habitation (e.g., a vehicle, an abandoned building, |
|  | bus/train/subway station/airport or anywhere outside) |
|  | (101) Emergency shelter, including hotel or motel paid for with emergency shelter |
|  | voucher, or Host Home shelter |
|  | (118) Safe Haven |
|  | (17) Other |
|  | (37) Worker unable to determine |
|  | Field 3 should be populated by the list of CoC Project names in 2.02.2 Project |
|  | Information Project Name, if 2.02.5 Continuum Project indicates that the project is |
|  | a continuum project. |
|  | Dependent A and its dependencies can be used to calculate imminent and at- risk |
|  | of homelessness housing statuses based on HUD's definition of homelessness. |
|  | Field 4 has a 250-character limit when exporting in the HMIS CSV. |
|  | One Current Living Situation is required as an update for each contact made along |
|  | with the response to Field 2, which may change over the project stay. |
| XML | <CurrentLivingSituation> |
| CSV | CurrentLivingSituation |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Moved subsidized permanent residences into Dependent A following |
|  | Field 1, response 435 ("Rental by client, with ongoing housing subsidy") |

#### 4.13 Date of Engagement

| Header | Instruction |
| --- | --- |
| Element Name | Date of Engagement |
| Field 1 & Response | Date of Engagement ([date field]) |
| Element Type | Program Specific |

| Funder: Program-Component | HUD: CoC – Collection only required for Street Outreach |
| --- | --- |
|  | HUD: ESG – Collection only required for Street Outreach and ES – NbN |
|  | HUD: Unsheltered Special NOFO – Collection required for Street Outreach |
|  | HUD: Rural Special NOFO – Collection required for Street Outreach |
|  | HHS: PATH – Collection required for all components |
|  | HHS: RHY – Collection only required for Street Outreach |
| Project Type Applicability | 1: Emergency Shelter – Night-by-Night |
|  | 4: Street Outreach |
|  | 6: Services Only |
| Data Collected About | Head of Household and Adults |
| Collection Point | Occurrence Point (At the Point of Engagement) |
| Relationship to Enrollment ID | No more than one Date of Engagement per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Dates of Engagement per Client |
| client) |  |
| System Logic & Other System | Only one Date of Engagement is allowed between the Project Start Date and |
| Issues | Project Exit Date. |
|  | If a client returns to the project at a later date, the previous Date of Engagement |
|  | does not apply to the new project enrollment. A new Date of Engagement is |
|  | recorded based on the situation during the new project enrollment. |
|  | It is possible that a case may be closed without the client becoming engaged and |
|  | thus, Date of Engagement would be null in that enrollment record. |
| XML | <DateOfEngagement> |
| CSV | Enrollment |
| 2024 Revision Summary | Wording change in system logic. Updated Project Type Applicability to |
|  | accommodate addition of Emergency Shelter – Night-by-Night project type |

## 4.14 Bed-Night Date

| Header | Instruction |
| --- | --- |
| Element Name | Bed-Night Date |
| Field 1 & Response | Bed-Night Date ((date field) |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: ESG – Collection required for ES – NbN |
|  | HUD: ESG RUSH – Collection required for ES - NbN |
| Project Type Applicability | 1: Emergency Shelter – Night-by-Night |
|  | (Applicability extends to all NbN type emergency shelters that participate in HMIS, |
|  | regardless of funding source) |
| Data Collected About | All Clients |
| Collection Point | Occurrence Point (As Provided) |
| Relationship to Enrollment ID | Zero or more Bed-Night Date per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID | Zero or more Bed-Night Date per Client |
| (a client) |  |
| System Logic & Other System |  |
| ssues | Collect once for each bed night utilized. |
|  | A Bed-Night Date indicates that the client has utilized a bed in a night-by-night |
|  | emergency shelter on that date. The system must be able to store an unlimited |
|  | number of bed night dates for any 5.06 Enrollment Identifier associated with a |
|  | night-by-night emergency shelter. Entry exit emergency shelters do not use bed |
|  | nights to track client stays. |

|  | There must be a record of a bed night on the project start date into the shelter; |
| --- | --- |
|  | any additional bed night dates must be after the Project Start Date and before the |
|  | Project Exit Date. |
|  | The Bed-Night Date must be exportable in the [date field] format. |
| XML | <ServiceFAReferral> |
| CSV | Services |
| 2024 Revision Summary | Wording change in system logic. Updated Project Type Applicability to |
|  | accommodate addition of Emergency Shelter – Night-by-Night project type. |

#### 4.19 Coordinated Entry Assessment

| Header | Instruction |
| --- | --- |
| Element Name | Coordinated Entry Assessment |
| Field 1 & Response | Date of assessment [date] |
| Field 2 & Response | Assessment location [drop down] |
| Field 3 & Responses | Assessment Type |
|  | 1 Phone |
|  | 2 Virtual |
|  | 3 In person |
| Field 4 & Responses | Assessment Level |
|  | 1 Crisis Needs Assessment |
|  | 2 Housing Needs Assessment |
| Field 5 & Responses | Assessment questions - Local determination - as defined by the community |
| 1...n | Questions |
| Dependent A - Dependent to | Assessment answers - Local determination - responses to questions defined by |
| Field 5 responses | community |
| 1...n | Answer for each question in Field 5 |
| Field 6 & Responses | Assessment Result Type – Local determination - as defined by the community |
| 1...n | Result Type |
| Dependent B - Dependent to | Assessment Result |
| Field 6 |  |
| 1...n | Result for each result type in Field 6 |
| Field 7 & Responses | Prioritization Status |
|  | 1 Placed on prioritization list |
|  | 2 Not placed on prioritization list |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: CoC – Collection required for all components providing Coordinated Entry |
|  | HUD: ESG – Collection required for all components providing Coordinated Entry |
| Project Type Applicability | 14: Coordinated Entry (or other depending on CoC design of Coordinated Entry |
|  | system) |
| Data Collected About | Head of Household |
| Collection Point | At occurrence |
| Relationship to Enrollment ID | One or more Coordinated Entry Assessment per enrollment |
| (an enrollment) |  |
| Relationship to Personal ID | One or more Coordinated Entry Assessment per client |
| (a client) |  |
| System Logic & Other System | Field 2 – It is recommended that a system administrator managed list is used for |
| Issues | this field. If such functionality doesn't exist in the HMIS, a text box must be |
|  | provided. |

|  | Fields 5 & 6 and Dependents A and B are representative of whatever assessment a |
| --- | --- |
|  | community uses. There is no specified structure or format for an assessment, and |
|  | an HMIS might have more than one type of assessment (crisis needs or housing |
|  | needs or multiples of each). The system must be able to treat a single assessment |
|  | recorded for a client as one unit of data including the fields listed here as well as |
|  | the community- defined fields. |
|  | Field 5 and Dependent A are a list of key-value (question and response) pairs for |
|  | every question in the assessment, e.g. "Where did you sleep last night" / "On the |
|  | streets". |
|  | Similarly, Field 6 and Dependent B are a list of key-value (result type and result) |
|  | pairs used to contain any number of possible results, scores, or calculations on the |
|  | assessment. For example, one assessment might have three results: "Housing |
|  | stability score" / "10″; "Total score" / "81″; "Recommended placement" / "RRH". |
|  | Fields 1-4 and field 7 will be required for reporting purposes. Fields 5 & 6 are |
|  | included as placeholders for communities who currently do, or want to in the |
|  | future, collect CE Assessment questions, answers, and results in HMIS. These fields |
|  | also serve as a common frame of reference when transferring data via HMIS CSV or |
|  | XML. |
|  | Data must be able to be added in multiple stages to complete a client record for a |
|  | single assessment. |
| XML | <assessment>, <assessmentQuestions>, <assessmentResults> |
| CSV | Assessment, AssessmentQuestions, AssessmentResults |
| 2024 Revision Summary | None |

4.20 Coordinated Entry Event

| Header | Instruction |
| --- | --- |
| Element Name | Coordinated Entry Event |
| Field 1 & Response | Date of event [date] |
| Field 2 & Response | Event |
| Header: | Access Events |
| 1 | Referral to Prevention Assistance project |
| 2 | Problem Solving/Diversion/Rapid Resolution intervention or service |
| 3 | Referral to scheduled Coordinated Entry Crisis Needs Assessment |
| 4 | Referral to scheduled Coordinated Entry Housing Needs Assessment |
| Header: | Referral Events |
| 5 | Referral to post-placement/follow-up case management |
| б | Referral to Street Outreach project or services |
| 7 | Referral to Housing Navigation project or services |
| 8 | Referral to Non-continuum services: Ineligible for continuum services |
| 9 | Referral to Non-continuum services: No availability in continuum services |
| 10 | Referral to Emergency Shelter bed opening |
| ਹ ਹ | Referral to Transitional Housing bed/unit opening |
| 12 | Referral to Joint TH-RRH project/unit/resource opening |
| 13 | Referral to RRH project resource opening |
| 14 | Referral to PSH project resource opening |
| રા | Referral to Other PH project/unit/resource opening |
| 16 | Referral to emergency assistance/flex fund/furniture assistance |

|  | 18 | Referral to a Housing Stability Voucher |
| --- | --- | --- |
| Dependent A - Dependent to |  | Problem Solving/Diversion/Rapid Resolution intervention or service result - Client |
| Field 2 & Response 2 |  | housed/re-housed in a safe alternative |
|  | 0 | No |
|  | T | Yes |
| Dependent B - Dependent to |  | Referral to post-placement/follow-up case management result - Enrolled in |
| Field 2 & Response 5 |  | Attercare |
|  |  | project |
|  | O | No |
|  | T | Yes |
| Dependent C- Dependent to |  | Location of Crisis Housing or Permanent Housing Referral [Project name and/or |
| Field 2 & Responses 10-15 |  | Project ID] |
| Dependent D- dependent to |  | Referral Result |
| Field 2 responses 10-15 or 18 |  |  |
|  | 1 | Successful referral: client accepted |
|  | 2 | Unsuccessful referral: client rejected |
|  | ന | Unsuccessful referral: provider rejected |
| Dependent E - Dependent to |  | Date of result [date] |
| Dependent D |  |  |
| Element Type |  | Program Specific |
| Funder: Program-Component |  | HUD: CoC – Collection required for all components providing Coordinated Entry |
|  |  | HUD: ESG – Collection required for all components providing Coordinated Entry |
| Project Type Applicability |  | 14: Coordinated Entry (or other depending on CoC design of Coordinated Entry |
|  |  | system) |
| Data Collected About |  | Head of Household |
| Collection Point |  | At occurrence |
| Relationship to Enrollment ID |  | One or more Coordinated Entry Event per Enrollment |
| (an enrollment) |  |  |
| Relationship to Personal ID |  | One or more Coordinated Entry Event per Client |
| (a client) |  |  |
| System Logic & Other System |  | Because the collection point for this data element is "at occurrence," fields must be |
| Issues |  | updateable over time as events take place and information becomes available (e.g. |
|  |  | Dependent A). |
|  |  | The list of options for Dependent C should display a list of Project Names to the |
|  |  | HMIS end user and save the selected Project ID to the database for reporting. The |
|  |  | list should consist of those projects where 2.09.2 Project Receives CE Referrals = |
|  |  | "Yes" as of the "Date of event" (field 1) and the projects' PDDEs align with the |
|  |  | referral type as follows: |
|  |  | When Field 2 is "Referral to Emergency Shelter bed opening," Dependent C should |
|  |  | show Emergency Shelter - Entry Exit (0), Emergency Shelter - Night-by- Night (1), |
|  |  | and Safe Haven (8) projects |
|  |  | When Field 2 is "Referral to Transitional Housing bed/unit opening," Dependent C |
|  |  | should show Transitional Housing (2) projects |
|  |  | When Field 2 is "Referral to Joint TH-RRH project/unit/resource opening," |
|  |  | Dependent C should show Transitional Housing and PH – Rapid Re-Housing |
|  |  | projects that have an associated funding source record where Funder Program and |
|  |  | Components is either HUD: CoC – Joint Component TH/RRH (44), HUD: |
|  |  | Unsheltered Special NOFO (54), or HUD: Rural Special NOFO (55) and the Grant End |
|  |  | Date is either null or in the future |

|  | When Field 2 is "Referral to RRH project resource opening," Dependent C should |
| --- | --- |
|  | show PH – Rapid Re-Housing (13) projects |
|  | When Field 2 is "Referral to PSH project resource opening," Dependent C should |
|  | show PH - Permanent Supportive Housing (disability required for entry) (3) |
|  | projects |
|  | When Field 2 is "Referral to Other PH project/unit/resource opening," Dependent C |
|  | should show PH – Housing Only (9) and PH – Housing with Services (no disability |
|  | required for entry) (10) projects |
|  | System must allow for multiple records per project stay to record each instance |
|  | and must record the date the event occurred (may be more than 1 event per date). |
| XML | <event> |
| CSV | Event |
| 2024 Revision Summary | Updated system logic to include FY2024 data element 2.09 CE Participation Status to |
|  | populate Field 2, Dependent C. |

# FEDERAL PARTNER PROGRAM SPECIFIC DATA ELEMENTS

These elements are listed under the federal partner program which maintains the element. There are elements maintained by one partner and shared with one other. When combined with UDEs and Common PSDEs, these elements form the basis of data collection requirements for specific project level reporting generated by an HMIS.

HUD-CoC Only Required Elements

| C2 Moving On Assistance Provided |
| --- |

| Header | Instruction |
| --- | --- |
| Element Name | Moving On Assistance Provided |
| Field 1 & Responses | Date of Moving On Assistance ([date field]) |
| Field 2 & Responses | Moving On Assistance |
| 1 | Subsidized housing application assistance |
| 2 | Financial assistance for Moving On (e.g., security deposit, moving expenses) |
| 3 | Non-financial assistance for Moving On (e.g., housing navigation, transition |
|  | support) |
| 4 | Housing referral/placement |
| 5 | Other (please specify) |
| Dependent A to Field 2 | Other (please specify) [text] |
| Response 5 |  |
| Element Type | Program Specific |
| Funder: Program- Component | HUD: CoC – Collection required for Permanent Supportive Housing |
|  | HUD: Unsheltered Special NOFO – Collection required for Permanent Supportive |
|  | Housing |
|  | HUD: Rural Special NOFO – Collection required for Permanent Supportive Housing |
| Project Type Applicability | 3: PH - Permanent Supportive Housing (disability required for entry) |
| Data Collected About | Head of Household |
| Collection Point | Occurrence Point (as provided) |
| Relationship to Enrollment ID | Zero or more Moving-On Assistance Provided per Enrollment |

| (an enrollment) |  |
| --- | --- |
| Relationship to Personal ID (a | Zero or more Moving-On Assistance Provided per Client |
| client) |  |
| System Logic & Other System lssues | Dependent A has a 50-character limit when exporting in the HMIS CSV. |
|  | Systems must allow for update information if a change occurs mid-year and allow |
|  | corrections for data entry errors at all stages. |
| Other System Issues | None |
| XML | <ServiceFAReferral> |
| CSV | Services |
| 2024 Revision Summary | None |

#### C3 Youth Education Status

| Header | Instruction | Element Name | Youth Education Status |
| --- | --- | --- | --- |
| Field 1 & Response | Information Date (date information was collected) ([date field]) | Field 2 & Responses | Current school enrollment and attendance |
| 0 | Not currently enrolled in any school or educational course | 1 | Currently enrolled but NOT attending regularly (when school or the course is in |
| session) | 2 | Currently enrolled and attending regularly (when school or the course is in session) |  |
| 8 | Client doesn't know | 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected | Dependent A - dependent to | Most Recent Educational Status |
| Field 2 & Response 0 | 0 | K12: Graduated from high school |  |
| 1 | K12: Obtained GED | 2 | K12: Dropped out |
| 3 | K12: Suspended | 4 | K12: Expelled |
| 5 | Higher education: Pursuing a credential but not currently attending | б | Higher education: Dropped out |
| 7 | Higher education: Obtained a credential/degree | 8 | Client doesn't know |
| 9 | Client prefers not to answer | ਰੇਰੇ | Data not collected |
| Dependent B - dependent to | Current Educational Status | Field 2 Response 1 OR |  |
| Response 2 | 0 | Pursuing a high school diploma or GED |  |
| 1 | Pursuing Associate's Degree | 2 | Pursuing Bachelor's Degree |
| 3 | Pursuing Graduate Degree | 4 | Pursuing other post-secondary credential |
| 8 | Client doesn't know | 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected | Element Type | Program Specific |

| Funder: Program- Component | HUD: CoC - Youth Homeless Demonstration Program (YHDP) |
| --- | --- |
| Project Type Applicability | 2: Transitional Housing |
|  | 3: PH - Permanent Supportive Housing (disability required for entry) |
|  | 6: Services Only |
|  | 13: PH – Rapid Re-Housing |
| Data Collected About | Head of Household |
| Collection Point | Project Start, Project Exit |
| Relationship to Enrollment ID | One or two Youth Education Status per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID | One or more Youth Education Status per Client |
| (a client) |  |
| System Logic & Other System lssues | The system must record the appropriate collection stage for each element. |
|  | Systems must allow corrections for data entry errors at all stages. |
| XML | <YouthEducationStatus> |
| CSV | YouthEducationStatus |
| 2024 Revision Summary | Changed "Client refused' to "Client prefers not to answer" |

#### C4 Translation Assistance Needed

| Header | Instruction |
| --- | --- |
| Element Name | Translation Assistance Needed |
| Field 1 & Response | Translation Assistance Needed |
| 0 | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent A - Dependent to | Preferred Language |
| Field 1 response 1 |  |
|  | [Twenty languages or a similar number that is reasonable and appropriate within |
| (1-20 options, | the given HMIS implementation, selected by the HMIS Lead in partnership with the |
| ranging from 100 to 426) | CoC, from the HMIS C4 Translation Assistance Needed Supplement] |
| 21 | Different Preferred Language |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent B - Dependent to | If Different Preferred Language, please specify |
| Dependent A response 21 | ([Text]) |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: CoC – Collection required for all components |
|  | HUD: ESG – Collection required for all components |
|  | HUD: ESG RUSH - Collection required for all components except Emergency Shelter |
|  | and Street Outreach |
|  | HUD: Unsheltered Special NOFO – Collection required for all components |
|  | HUD: Rural Special NOFO – Collection required for all components |
|  | HUD: HOPWA – Collection required for all components |
| Project Type Applicability | All Project Types |
| Data Collected About | Head of Household |
| Collection Point | Project Start |
| Relationship to Enrollment ID | One Translation Assistance Needed per Enrollment |
| (an enrollment) |  |

| Relationship to Personal ID (a | One or more Translation Assistance Needed per Client |
| --- | --- |
| client) |  |
| System Logic & Other System | The HMIS C4 Translation Assistance Needed Supplement on the HUD Exchange |
| lssues | contains the complete list of languages that should be available within HMIS. In |
|  | each implementation (including a single HMIS implementation with multiple CoCs), |
|  | HMIS Administrators must be able to select 20 languages or a similar number that |
|  | is reasonable and appropriate within the given HMIS implementation, from the list |
|  | provided in the HMIS C4 Translation Assistance Needed Supplement; these |
|  | selected languages in turn must populate the list of options presented to HMIS end |
|  | users at project start. If reasonable and appropriate, a picklist of more than 20 |
|  | response options may be displayed to an HMIS end user. |
|  | Dependent B has a 100-character limit when exporting in the HMIS CSV. |
| XML | <Enrollment> |
| CSV | Enrollment |
| 2024 Revision Summary | New Element |

## HUD-HOPWA Only Required Elements

#### W1 Services Provided - HOPWA

| Header | Instruction |
| --- | --- |
| Element Name | Services Provided - HOPWA |
| Field 1 & Response | Date of Service ([date field]) |
| Field 2 & Responses | Type of Service |
| 1 | Adult day care and personal assistance |
| 2 | Case management |
| 3 | Child care |
| 4 | Criminal justice/legal services |
| 5 | Education |
| б | Employment and training services |
| 7 | Food/meals/nutritional services |
| 8 | Health/medical care |
| 9 | Life skills training |
| 10 | Mental health care/counseling |
| JI | Outreach and/or engagement |
| 12 | Substance use services/treatment |
| 13 | Transportation |
| 14 | Other HOPWA funded service |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: HOPWA – Collection required for all components |
| Project Type Applicability | 0: Emergency Shelter - Entry Exit |
|  | 2: Transitional Housing |
|  | 3: PH - Permanent Supportive Housing (disability required for entry) |
|  | 6: Services Only |
|  | 12: Homelessness Prevention |
| Data Collected About | All clients receiving services |
| Collection Point | Occurrence Point (As Provided) |
| Relationship to Enrollment ID | Zero or more Services Provided – HOPWA per Enrollment |

| (an enrollment) |  |
| --- | --- |
| Relationship to Personal ID (a | Zero or more Services Provided – HOPWA per Client |
| client) |  |
| System Logic & Other System | Data are time sensitive and may change over the project stay. System must allow |
| lssues | for multiple records per project stay to record each instance and must record the |
|  | date the service was provided. |
|  | The data in this element are transactional data; each time the service is delivered, |
|  | a record of the date of service and the service element must be maintained. |
|  | If the service benefits the entire household, it may be recorded solely for the Head |
|  | of Household. |
| XML | <ServiceFAReferral> |
| CSV | Services |
| 2024 Revision Summary | Removed "disorder" from "Substance use disorder services/treatment" option. |
|  | Updated Project Type Applicability to accommodate addition of Emergency Shelter |
|  | – Entry Exit project type |

## W2 Financial Assistance – HOPWA

| Header | Instruction |
| --- | --- |
| Element Name | Financial Assistance – HOPWA |
| Field 1 & Response | Date of Financial Assistance ([date field]) |
| Field 2 & Responses | Financial Assistance Type |
| 1 | Rental assistance [collect for PHP and STRMU and PH-TBRA] |
| 2 | Security deposits [collect for PHP] |
| 3 | Utility deposits [collect for PHP] |
| 4 | Utility payments [collect for PHP and STRMU] |
| 7 | Mortgage assistance [collect for STRMU] |
| Field 3 & Response | Financial Assistance Amount (/currency/decimal)) |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: HOPWA – Collection required for PHP and STRMU only as indicated above |
| Project Type Applicability | 6: Services Only |
|  | 12: Homelessness Prevention |
| Data Collected About | Head of Household |
| Collection Point | Occurrence Point (As Provided) |
| Relationship to Enrollment ID | Zero or more Financial Assistance – HOPWA per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | Zero or more Financial Assistance - HOPWA per Client |
| client) |  |
| System Logic & Other System | Data are time sensitive and may change over the project stay. System must allow |
| lssues | for multiple records per project stay to record each instance and must record the |
|  | date the financial assistance was provided. |
|  | The data in this element are transactional data; each time there is financial |
|  | assistance provided, a record of the assistance must be recorded including the date |
|  | and financial assistance information. |
|  | Records of financial assistance should be attached to the Head of Household. |
| XML | <ServiceFAReferral> |
| CSV | Services |
| 2024 Revision Summary | None |

| ILA IIIFAIRAI I MAIAMIIAA |  |  |  |
| --- | --- | --- | --- |
| Header | Instruction | Element Name | Medical Assistance |
| Field 1 & Response | Information Date (date information was collected) ([date field]) | Receiving AIDS Drug Assistance Program (ADAP) | Field 2 & Responses |
| 0 | No | 1 | Yes |
| 8 | Client doesn't know | 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected | If No for "Receiving AIDS Drug Assistance Program (ADAP)" | Dependent B - Dependent to |
| Reason | Field 3 & Response 0 | Applied; decision pending | 1 |
| 2 | Applied; client not eligible | Client did not apply | 3 |
| Insurance type N/A for this client | 4 | 8 | Client doesn't know |
| 9 | Client prefers not to answer | ਰੇਰੇ | Data not collected |
| Field 4 & Responses | Receiving Ryan White-funded Medical or Dental Assistance | No | 0 |
| 1 | Yes | 8 | Client doesn't know |
| 9 | Client prefers not to answer | ਰੇਰੇ | Data not collected |
| If No for "Receiving Ryan White-funded Medical or Dental Assistance" | Dependent C - Dependent to | Reason | Field 4 & Response 0 |
| Applied; decision pending | ਹ | 2 | Applied; client not eligible |
| 3 | Client did not apply | Insurance type N/A for this client | 4 |
| Client doesn't know | 8 | 9 | Client prefers not to answer |
| Data not collected | ਰੇਰੇ | Program Specific | Element Type |
| HUD: HOPWA – Collection required for all components | Funder: Program- Component | 0: Emergency Shelter – Entry Exit | Project Type Applicability |
| 2: Transitional Housing | 3: PH - Permanent Supportive Housing (disability required for entry) |  |  |
| 6: Services Only | 12: Homelessness Prevention |  |  |
| Data Collected About | All Household Members with HIV/AIDS | Project Start, Update, Project Exit | Collection Point |
| Relationship to Enrollment ID | One or more Medical Assistance per Enrollment | (an enrollment) |  |
| Relationship to Personal ID (a | One or more Medical Assistance per Client | client) |  |
| System Logic & Other System | The system must record the appropriate collection stage for each element. |  |  |

| lssues | Systems must also allow for update information if a change occurs mid-year. |
| --- | --- |
|  | Allow corrections for data entry errors at all stages. |
| XML | <MedicalAssistance> |
| CSV | IncomeBenefits |
| 2024 Revision Summary | Changed "Client refused' to "Client prefers not to answer." Updated Project Type |
|  | Applicability to accommodate addition of Emergency Shelter – Entry Exit project |
|  | type. Removed "Receiving Public HIV/AIDS Medical Assistance" and its dependent, |
|  | "If No for 'Receiving Public HIV/AIDS Medical Assistance,' Reason" |

## W4 T-Cell (CD4) and Viral Load

| Header | Instruction |
| --- | --- |
| Element Name | T-Cell (CD4) and Viral Load |
| Field 1 & Response | Information Date (date information was collected) ([date field]) |
| Field 2 & Responses | T-Cell (CD4) Count Available |
| 0 | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent A - Dependent to | If a yes to "T-Cell (CD4) Count Available" then |
| Field 2 & Response 1 | T-Cell Count (integer between 0 - 1500) |
| Dependent B - Dependent to | If a number is entered in the T-Cell (CD4) count, then |
| Field 2 & Response 1 | How was the information obtained |
| 1 | Medical Report |
| 2 | Client report |
| 3 | Other |
| Field 3 & Responses | Viral Load Information Available |
| 0 | Not Available |
| 1 | Available |
| 2 | Undetectable |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent C - Dependent to | If "Viral Load Information Available" then |
| Field 3 & Response 1 | Count ([integer between 0 – 999999] |
| Dependent D - Dependent to | If a number is entered in the Viral Load count, then |
| Field 3 & Response 1 | How was the information obtained |
| 1 | Medical Report |
| 2 | Client report |
| 3 | Other |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: HOPWA – Collection required for all components |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 3: PH – Permanent Supportive Housing (disability required for entry) |
|  | 6: Services Only |
|  | 12: Homelessness Prevention |
| Data Collected About | All Household Members with HIV/AIDS |
| Collection Point | Project Start, Update, Annual Assessment, Project Exit |
| Relationship to Enrollment ID | One or more T-Cell (CD4) and Viral Load per Enrollment |
| (an enrollment) |  |

| Relationship to Personal ID (a | One or more T-Cell (CD4) and Viral Load per Client |
| --- | --- |
| client) |  |
| System Logic & Other System lssues | The system must record the appropriate collection stage for each element. |
|  | Systems must also allow for updated information if a change occurs mid-year. |
|  | Allow corrections for data entry errors at all stages. |
|  | It is recommended that an HMIS only display this question as dependent to 4.08 |
|  | HIV/AIDS where the response is "yes." |
|  | If possible, the system should limit the numeric range of the 'viral load information |
|  | available' – response option 1 "available" to 21 to 999,999 as a response of 20 or |
|  | less is associated with an "undetectable viral load." |
| XML | <Disabilities> |
| CSV | Disabilities |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Updated Project Type Applicability to accommodate addition of |
|  | Emergency Shelter – Entry Exit project type |

#### W5 Housing Assessment at Exit

| Header | Instruction |
| --- | --- |
| Element Name | Housing Assessment at Exit |
| Field 1 & Responses | Housing Assessment at Exit |
| 1 | Able to maintain the housing they had at project entry |
| 2 | Moved to new housing unit |
| 3 | Moved in with family/friends on a temporary basis |
| 4 | Moved in with family/friends on a permanent basis |
| 5 | Moved to a transitional or temporary housing facility or program |
| б | Client became homeless - moving to a shelter or place unfit for human habitation |
| 7 | Jail/prison |
| 10 | Deceased |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent A - Dependent to | If Able to maintain the housing they had at project entry for "Housing Assessment |
| Field 1 & Response 1 | at Exit" |
|  | Subsidy information |
| 1 | Without a subsidy |
| 2 | With the subsidy they had at project entry |
| 3 | With an on-going subsidy acquired since project entry |
| 4 | Only with financial assistance other than a subsidy |
| Dependent B - Dependent to | If Moved to new housing unit for "Housing Assessment at Exit" |
| Field 1 & Response 2 | Subsidy information |
| 1 | With on-going subsidy |
| 2 | Without an on-going subsidy |
| Element Type | Program Specific |
| Funder: Program- Component | HUD: CoC – Collection required only for Homelessness Prevention component |
|  | HUD: ESG – Collection required only for Homelessness Prevention component |
|  | HUD: ESG-RUSH – Collection required for Homelessness Prevention component |
|  | HUD: HOPWA – Collection required for all components |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |

|  | 2: Transitional Housing |
| --- | --- |
|  | 3: PH - Permanent Supportive Housing (disability required for entry) |
|  | 6: Services Only |
|  | 12: Homelessness Prevention |
| Data Collected About | All Clients |
| Collection Point | Project Exit |
| Relationship to Enrollment ID (an enrollment) | Zero or one Housing Assessment at Exit per Enrollment |
| Relationship to Personal ID (a | Zero or more Housing Assessment at Exit per Client |
| client) |  |
| System Logic & Other System | System stores collected information as 'project exit' information and retains for |
| lssues | historical purposes. |
| Other System Issues | None |
| XML | <ExitHousingAssessment> |
| CSV | Exit |
| 2024 Revision Summary | Changed "Client refused' to "Client prefers not to answer," "Client went to |
|  | jail/prison" to "Jail/prison," and "Client died" to "Deceased." Updated Funder: |
|  | Program-Component field. Updated Project Type Applicability to accommodate |
|  | addition of Emergency Shelter – Entry Exit project type |

## W6 Prescribed Anti-Retroviral

| Header | Instruction | Element Name | Prescribed Anti-Retroviral |
| --- | --- | --- | --- |
| Information Date (date information was collected) ([date field]) | Field 1 & Response | Field 2 & Responses | Has the participant been prescribed anti-retroviral drugs? |
| O | No | 1 | Yes |
| 8 | Client doesn't know | 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected | Program Specific | Element Type |
| Funder: Program- Component | HUD: HOPWA – collection required for all components | 0: Emergency Shelter – Entry Exit | Project Type Applicability |
| 2: Transitional Housing | 3: PH - Permanent Supportive Housing (disability required for entry) |  |  |
| 6: Services Only | 12: Homeless Prevention |  |  |
| Data Collected About | All Household Members with HIV/AIDS | Collection Point | Project Start, Update, Project Exit |
| Relationship to Enrollment ID | One or more Prescribed Anti-Retroviral per Enrollment | (an enrollment) |  |
| Relationship to Personal ID (a | One or more Prescribed Anti-Retroviral per Client | client) |  |
| System Logic & Other System | The system must record the appropriate collection stage for each element. | lssues |  |
| Systems must allow for update information if a change occurs mid-year and allow | corrections for data entry errors at all stages. |  |  |
| It is recommended that an HMIS only display this question as dependent to 4.08 |  |  |  |

|  | HIV/AIDS where the response is "yes." |
| --- | --- |
| XML | <Disabilities> |
| CSV | Disabilities |
| 2024 Revision Summary | Wording change in system logic. Changed "Client refused' to "Client prefers not to |
|  | answer." Updated Project Type Applicability to accommodate addition of |
|  | Emergency Shelter – Entry Exit project type |

#### HHS-PATH Only Required Elements

## P1 Services Provided - PATH Funded

| Header | Instruction |
| --- | --- |
| Element Name | Services Provided – PATH Funded |
| Field 1 & Response | Date of Service ([date field]) |
| Field 2 & Responses | Type of PATH FUNDED Service Provided |
| 1 | Re-engagement |
| 2 | Screening |
| 14 | Clinical assessment |
| 3 | Habilitation/rehabilitation |
| 4 | Community Mental Health |
| 5 | Substance use treatment |
| б | Case management |
| 7 | Residential supportive services |
| 8 | Housing minor renovation |
| 9 | Housing moving assistance |
| 10 | Housing eligibility determination |
| 11 | Security deposits |
| 12 | One-time rent for eviction prevention |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: PATH – Collection required for all components |
| Project Type Applicability | 4: Street Outreach |
|  | 6: Services Only |
| Data Collected About | Head of Household and Adults |
| Collection Point | Occurrence Point (As Provided) |
| Relationship to Enrollment ID | Zero or more Services Provided-PATH Funded per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | Zero or more Services Provided-PATH Funded per Client |
| client) |  |
| System Logic & Other System | Data are time sensitive and may change over the project stay. System must allow |
| Issues | for multiple records per project stay to record each instance and must record the |
|  | date the service was provided. |
|  | If a service benefits the entire household, it must be recorded for the Head of |
|  | Household. |
|  | PATH only records services that are PATH funded. If providers want to collect other |
|  | services, then a separate element must be created to distinguish PATH funded |
|  | services from non-PATH funded services. |

|  | PATH reports will only include services for persons who received services and are |
| --- | --- |
|  | enrolled. |
| XML | <ServiceFAReferral> |
| CSV | Services |
| 2024 Revision Summary | Wording change in system logic. |

#### P2 Referrals Provided – PATH

| Header | Instruction |
| --- | --- |
| Element Name | Referrals Provided PATH |
| Field 1 & Response | Date of Referral ([date field]) |
| Field 2 & Responses | Type of Referral |
|  | Community Mental Health 1 |
|  | 2 Substance Use Treatment |
|  | 3 Primary Health/ Dental Care |
|  | 4 Job Training |
|  | 5 Educational Services |
|  | б Housing Services |
|  | J J Temporary Housing |
|  | 7 Permanent Housing |
|  | 8 Income Assistance |
|  | 9 Employment Assistance |
|  | 10 Medical Insurance |
| Dependent A - Dependent to | If any "Type of Referral" made |
| Field 2 & Responses 1-10 | Select Outcome for each |
|  | 1 Attained |
|  | 2 Not attained |
|  | 3 Unknown |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: PATH – Collection required for all components |
| Project Type Applicability | 4: Street Outreach |
|  | 6: Services Only |
| Data Collected About | Head of Household and Adults |
| Collection Point | Occurrence Point (As Provided) |
| Relationship to Enrollment ID | Zero or more Referrals Provided – PATH per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | Zero or more Referrals Provided – PATH per Client |
| client) |  |
| System Logic & Other System | Data are time sensitive and may change over the project stay. System must allow |
| lssues | multiple records per project stay to record each instance and must record the date |
|  | the referral was provided. |
|  | Multiple types of the same referral may be made over the course of project |
|  | enrollment. Each referral should have an outcome response. |
|  | Referral outcome is being shown as a dependent response. However, the |
|  | responses of attained, not attained, or unknown may have better ways of |
|  | presentation for data collection than as dependent fields as the response may not |
|  | be known simultaneous with identification of the referral. Vendors may elect |
|  | means other than a dependent field to improve data quality. The referral outcome |

|  | information is required for reporting. |
| --- | --- |
|  | PATH reports will only include referrals for persons who received referrals and are |
|  | enrolled. |
| XML | <ServiceFAReferral> |
| CSV | Services |
| 2024 Revision Summary | Wording change in system logic. |

#### P3 PATH Status

| Header | Instruction |
| --- | --- |
| Element Name | PATH Status |
| Field 1 & Response | Date of Status Determination ([date field]) |
| Field 2 & Responses | Client Became Enrolled in PATH |
| 0 | No |
| 1 | Yes |
| Dependent A - Dependent to | If No for "Client Became Enrolled in PATH" |
| Field 2 & Response 0 | Reason not enrolled |
| 1 | Client was found ineligible for PATH |
| 2 | Client was not enrolled for other reason(s) |
| 3 | Unable to locate client |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: PATH - Collection required for all components |
| Project Type Applicability | 4: Street Outreach |
|  | 6: Services Only |
| Data Collected About | Head of Household and Adults |
| Collection Point | Occurrence Point (At Determination; collect once, at or before exit, when the |
|  | status is determined) |
| Relationship to Enrollment ID | No more than one PATH Status per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more PATH Status per Client |
| client) |  |
| System Logic & Other System | Only one PATH status date and response is allowed for each project stay. If a client |
| lssues | exits and returns to the project later, the previously entered enrollment data does |
|  | not apply and a new response must be entered based on the new project start and |
|  | project exit service period. |
|  | If an HMIS supports requiring elements, then this element and its dependent |
|  | response should be required for PATH at project exit and the client should not be |
|  | able to be exited without a response to this element. This element is critical to |
|  | PATH reporting. |
| XML | <PATHStatus> |
| CSV | Enrollment |
| 2024 Revision Summary | None |

#### P4 Connection with SOAR

| Header | Instruction |
| --- | --- |
| Element Name | Connection with SOAR |
| Field 1 & Responses | Connection with SOAR |

|  | 0 | No |
| --- | --- | --- |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ | Data not collected |
| Element Type |  | Program Specific |
| Funder: Program-Component |  | HHS: PATH - Collection required for all components |
|  |  | VA: SSVF – Collection required for RRH and Homelessness Prevention |
| Project Type Applicability |  | 4: Street Outreach |
|  |  | 6: Services Only |
|  |  | 12: Homelessness Prevention |
|  |  | 13: PH - Rapid Re-Housing |
| Data Collected About |  | Head of Household and Adults |
| Collection Point |  | Project Start, Update, Annual Assessment, and Exit |
| Relationship to Enrollment ID |  | One or more Connection with SOAR per Enrollment |
| (an enrollment) |  |  |
| Relationship to Personal ID (a |  | One or more Connection with SOAR per Client |
| client) |  |  |
| System Logic & Other System |  | The system must record the appropriate collection stage for each element. |
| lssues |  | Systems must also allow for update information if a change occurs mid-year and |
|  |  | allow corrections for data entry errors at all stages. |
|  |  | If the SOAR program is locally available, CoCs may find this element helpful to their |
|  |  | CoCs for implementation in programs other than PATH. |
| XML |  | <ConnectionWithSOAR> |
| CSV |  | IncomeBenefits |
| 2024 Revision Summary |  | Changed "Client refused' to "Client prefers not to answer." Updated Funder: |
|  |  | Program-Component response "VA: SSVF - all components" to only "VA: SSVF - |
|  |  | Collection required for RRH and Homelessness Prevention" |

#### HHS-RHY Only Required Elements

R1 Referral Source

| Header |  | Instruction |
| --- | --- | --- |
| Element Name |  | Referral Source |
| Field 1 & Responses |  | Referral Source |
|  | 1 | Self-Referral |
|  | 2 | Individual: Parent/Guardian/Relative/Friend/Foster Parent/Other Individual |
|  | 7 | Outreach Project |
|  | 11 | Temporary Shelter |
|  | 18 | Residential Project |
|  | 28 | Hotline |
|  | 30 | Child Welfare/CPS |
|  | 34 | Juvenile Justice |
|  | રે રે | Law Enforcement/ Police |
|  | 37 | Mental Hospital |
|  | 38 | School |

| ਤੇਰੇ | Other Organization |
| --- | --- |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent A - Dependent to | If Outreach Project: FYSB for "Referral Source" is selected |
| Field 1 & Response 7 | Number of times approached by outreach prior to entering the project |
|  | ([Box for integer response]) |
| Element Type | Program Specific |
| Funder: Program- Component | HHS: RHY – Collection required for all components except for Street Outreach |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 12: Homelessness Prevention |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start |
| Relationship to Enrollment ID | No more than one Referral Source per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Referral Source per Client |
| client) |  |
| System Logic & Other System | System stores collected information as 'project start' information and retains for |
| lssues | historical purpose. |
| XML | <EntryRHY> |
| CSV | Enrollment |
| 2024 Revision Summary | Changed "Client refused' to "Client prefers not to answer." Updated Project Type |
|  | Applicability to accommodate addition of Emergency Shelter – Entry Exit project |
|  | type |

#### R2 RHY - BCP Status

| Header | Instruction |
| --- | --- |
| Element Name | RHY – BCP Status |
| Field 1 & Response | Date of Status Determination ([date field]) |
| Field 2 & Responses | Youth Eligible for RHY Services |
| 0 | No |
| T | Yes |
| Dependent A - Dependent to | If No for "Youth Eligible for RHY Services" |
| Field 2 & Response 0 | Reason why services are not funded by BCP grant |
| 1 | Out of age range |
| 2 | Ward of the State – Immediate Reunification |
| 3 | Ward of the Criminal Justice System – Immediate Reunification |
| 4 | Other |
| Dependent B - Dependent to | If Yes for "Youth Eligible for RHY Services" |
| Field 2 & Response 1 | Runaway youth |
| 0 | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Program Specific |
| Funder: Program- Component | HHS: RHY - Collection required for BCP only |

| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
| --- | --- |
|  | 12: Homelessness Prevention |
| Data Collected About | All Clients |
| Collection Point | Project Start |
| Relationship to Enrollment ID | No more than one RHY-BCP Status per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more RHY-BCP Status per Client |
| client) |  |
| System Logic & Other System | Only one RHY status date and only one response for 'FYSB Youth' is allowed for |
| lssues | each project stay. If a client returns to the project at a later date, the previous data |
|  | does not apply and must be entered based on the new project start and project |
|  | exit date service period. Youth who identify as "No" to 'FYSB Youth' are also not |
|  | experiencing homelessness under the HUD definition of homelessness. Data on |
|  | these youth who are identified as "No" to 'FYSB Youth' does transmit in the RHY |
|  | CSV export for the national data transfers but are filtered out in analysis. |
|  | If the system supports required elements, then this element should be required for |
|  | RHY: BCP-ES funded projects and the client should not be able to exit the project |
|  | without a response to this element. |
| XML | <RHYBCPStatus> |
| CSV | Enrollment |
| 2024 Revision Summary | Wording change in system logic. Updated Project Type Applicability to |
|  | accommodate addition of Emergency Shelter – Entry Exit project type. Changed |
|  | "Client refused' to "Client prefers not to answer" |

#### R3 Sexual Orientation

| Header | Instruction |
| --- | --- |
| Element Name | Sexual Orientation |
| Field 1 & Responses | Sexual Orientation |
|  | Heterosexual 1 |
|  | 2 Gav |
|  | 3 Lesbian |
|  | 4 Bisexual |
|  | 5 Questioning/Unsure |
|  | б Other |
|  | 8 Client doesn't know |
|  | 9 Client prefers not to answer |
|  | ਰੇਰੇ Data not collected |
| Dependent A - Dependent to | If other, please describe ([text]) |
| Response 6 |  |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: RHY – Collection required for all components |
|  | HUD: CoC – Youth Homeless Demonstration Program (YHDP) – collection required |
|  | for all components |
|  | HUD: CoC – Permanent Supportive Housing |
|  | HUD: Unsheltered Special NOFO – Collection required for Permanent Supportive |
|  | Housing |
|  | HUD: Rural Special NOFO – Collection required for Permanent Supportive Housing |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |

|  | 2: Transitional Housing |
| --- | --- |
|  | 3: PH - Permanent Supportive Housing (disability required for entry) |
|  | 4: Street Outreach |
|  | 9: PH - Housing Only |
|  | 10: PH – Housing with Services (no disability required for entry) |
|  | 12: Homelessness Prevention |
|  | 13: PH – Rapid Re-Housing |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start |
| Relationship to Enrollment ID | No more than one Sexual Orientation per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Sexual Orientation per Client |
| client) |  |
| System Logic & Other System | System stores collected information as 'project start' information and retains for |
| lssues | historical purpose. |
|  | Dependent A has a 100-character limit when exporting in the HMIS CSV. |
| XML | <EntryRHY> |
| CSV | Enrollment |
| 2024 Revision Summary | Updated Project Type Applicability to accommodate addition of Emergency Shelter |
|  | – Entry Exit project type and added "HUD: CoC –Permanent Supportive Housing." |
|  | Changed "Client refused' to "Client prefers not to answer" |

#### R4 Last Grade Completed

| Header | Instruction |
| --- | --- |
| Element Name | Last Grade Completed |
| Field 1 & Responses | Last Grade Completed |
| T | Less than Grade 5 |
| 2 | Grades 5-6 |
| 3 | Grades 7-8 |
| 4 | Grades 9-11 |
| 5 | Grade 12/High school diploma |
| б | School program does not have grade levels |
| 7 GED |  |
| 10 | Some college |
| ਹ ਹ | Associate's degree |
| 12 | Bachelor's degree |
| 13 | Graduate degree |
| 14 | Vocational certification |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: HUD-VASH – Collection required for HUD/VASH- Continuum |
|  | HHS: RHY – Collection required for all components except for Street Outreach |
|  | VA: SSVF – Collection required for RRH and Homelessness Prevention |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 3: PH - Permanent Supportive Housing (disability required for entry) |

|  | 12: Homelessness Prevention |
| --- | --- |
|  | 13: PH – Rapid Re-Housing |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start, Project Exit |
| Relationship to Enrollment ID | One or more Last Grade Completed per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Last Grade Completed per Client |
| client) |  |
| System Logic & Other System | System stores collected information as 'project start' or 'project exit' information |
| lssues | and retains for historical purpose. |
| XML | <Education><LastGradeCompleted> |
| CSV | EmploymentEducation |
| 2024 Revision Summary | Updated Project Type Applicability to accommodate addition of Emergency Shelter |
|  | – Entry Exit project type. Changed "Client refused' to "Client prefers not to answer" |

#### R5 School Status

| Header | Instruction |
| --- | --- |
| Element Name | School Status |
| Field 1 & Responses | School Status |
|  | 1 Attending school regularly |
|  | 2 Attending school irregularly |
|  | 3 Graduated from high school |
|  | 4 Obtained GED |
|  | 5 Dropped out |
|  | б Suspended |
|  | 7 Expelled |
|  | 8 Client doesn't know |
|  | 9 Client prefers not to answer |
|  | ਰੇਰੇ Data not collected |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: RHY – Collection required for all components except for Street Outreach |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 12: Homelessness Prevention |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start, Project Exit |
| Relationship to Enrollment ID | One or more School Status per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more School Status per Client |
| client) |  |
| System Logic & Other System | System stores collected information as 'project start' or 'project exit' information |
| Issues | and retains for historical purpose. |
| XML | <SchoolStatus><LastGradeCompleted> |
| CSV | EmploymentEducation |
| 2024 Revision Summary | Updated Project Type Applicability to accommodate addition of Emergency Shelter |
|  | – Entry Exit project type. Changed "Client refused' to "Client prefers not to answer" |

| Header | Instruction |
| --- | --- |
| Element Name | Employment Status |
| Field 1 & Response | Information Date (date information was collected) ([date field]) |
| Field 2 & Responses | Emploved |
| 0 | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent A - Dependent to | If Yes for "Employed" |
| Field 2 & Response 1 | Type of Employment |
| 1 | Full-time |
| 2 | Part-time |
| 3 | Seasonal / sporadic (including day labor) |
| Dependent B - Dependent to | If No for "Employed" |
| Field 2 & Response 0 | Why Not Employed |
| 1 | Looking for work |
| 2 | Unable to work |
| 3 | Not looking for work |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: HUD-VASH - Collection required for HUD/VASH-Continuum |
|  | HHS: RHY – Collection required for all components except for Street Outreach |
|  | VA: SSVF – Collection required for RRH and Homelessness Prevention |
|  | VA: GPD - collection required for all components |
| Project Type Applicability | 0: Emergency Shelter - Entry Exit |
|  | 2: Transitional Housing |
|  | 3: PH - Permanent Supportive Housing (disability required for entry) |
|  | 6: Services Only |
|  | 8: Safe Haven |
|  | 9: PH - Housing Only |
|  | 12: Homelessness Prevention |
|  | 13: PH - Rapid Re-Housing |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start, Project Exit |
| Relationship to Enrollment ID | One or more Employment Status per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Employment Status per Client |
| client) |  |
| System Logic & Other System Issues | The system must record the appropriate collection stage for each element. System |
|  | stores collected information as 'project start' or 'project exit' information and |
|  | retains for historical purpose. |
| XML | <Employment> |
| CSV | EmploymentEducation |
| 2024 Revision Summary | Updated Project Type Applicability to accommodate addition of Emergency Shelter |
|  | – Entry Exit project type. Changed "Client refused' to "Client prefers not to answer" |

#### R7 General Health Status

| Header | Instruction |
| --- | --- |
| Element Name | General Health Status |
| Field 1 & Responses | General Health Status |
| 1 | Excellent |
| 2 | Very good |
| 3 | Good |
| 4 | Fair |
| 5 | Poor |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: HUD-VASH – Collection required for HUD/VASH-Continuum |
|  | HHS: RHY – Collection required for all components except for Street Outreach |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 3: PH - Permanent Supportive Housing (disability required for entry) |
|  | 12: Homelessness Prevention |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start, Project Exit |
| Relationship to Enrollment ID | One or more General Health Status per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more General Health Status per Client |
| client) |  |
| System Logic & Other System | System stores collected information as 'project start' or 'project exit' information |
| Issues | and retains for historical purpose. |
| XML | <HealthStatus> |
| CSV | HealthAndDV |
| 2024 Revision Summary | Changed "Client refused' to "Client prefers not to answer" and removed "HUD: |
|  | CoC – Permanent Supportive Housing" from the Funder: Program-Component list |

#### R8 Dental Health Status

| Header | Instruction |
| --- | --- |
| Element Name | Dental Health Status |
| Field 1 & Responses | Dental Health Status |
| 1 | Excellent |
| 2 | Very good |
| ന | Good |
| ব | Fair |
| ട | Poor |
| 8 | Client doesn't know |
| ਰੇ | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: RHY – Collection required for all components except for Street Outreach |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |

|  | 12: Homelessness Prevention |
| --- | --- |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start, Project Exit |
| Relationship to Enrollment ID | One or more Dental Health Status per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID | One or more Dental Health Status per Client |
| (a client) |  |
| System Logic & Other System lssues | System stores collected information as 'project start' or 'project exit' information |
|  | and retains for historical purpose. |
| XML | <HealthStatus> |
| CSV | HealthAndDV |
| 2024 Revision Summary | Updated Proiect Type Applicability to accommodate addition of Emergencv |
|  | Shelter – Entry Exit project type. Changed "Client refused' to "Client prefers not to |
|  | answer" |

#### R9 Mental Health Status

| Header | Instruction |
| --- | --- |
| Element Name | Mental Health Status |
| Field 1 & Responses | Mental Health Status |
| 1 | Excellent |
| 2 | Very good |
| 3 | Good |
| 4 | Fair |
| 5 | Poor |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: RHY - Collection required for all components except for Street Outreach |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 12: Homelessness Prevention |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start, Project Exit |
| Relationship to Enrollment ID | One or more Mental Health Status per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Mental Health Status per Client |
| client) |  |
| System Logic & Other System | System stores collected information as 'project start' or 'project exit' information |
| Issues | and retains for historical purpose. |
| XML | <HealthStatus> |
| CSV | HealthAndDV |
| 2024 Revision Summary | Changed "Client refused' to "Client prefers not to answer." Updated Project Type |
|  | Applicability to accommodate addition of Emergency Shelter – Entry Exit project |
|  | type. |

#### R10 Pregnancy Status

| Header | Instruction |
| --- | --- |
| Element Name | Pregnancy Status |

| Field 1 & Responses | Pregnancy Status |
| --- | --- |
| O | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent A - Dependent to | If Yes for "Pregnancy Status" |
| Field 2 & Response 1 | Due Date ([date field]) |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: RHY – Collection required for all components |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 4: Street Outreach |
|  | 12: Homelessness Prevention |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start, Update |
| Relationship to Enrollment | One or more Pregnancy Status per Enrollment |
| ID (an enrollment) |  |
| Relationship to Personal ID | One or more Pregnancy Status per Client |
| (a client) |  |
| System Logic & Other System | Data are time sensitive and may change over the project stay. System must allow |
| Issues | for updated information collection as change occurs, must record the date the |
|  | information was collected with a data collection stage of 'project update', and |
|  | retain all updates for historical purpose. |
|  | There may be multiple records of this data element per project stay; each time |
|  | there is pregnancy, a record of the pregnancy must be recorded. |
| XML | <HealthStatus> |
| CSV | HealthAndDV |
| 2024 Revision Summary | Wording change in system logic. Updated Project Type Applicability to |
|  | accommodate addition of Emergency Shelter – Entry Exit project type. |
|  | Changed "Client refused' to "Client prefers not to answer" |

## R11 Formerly a Ward of Child Welfare/Foster Care Agency

| Header | Instruction |
| --- | --- |
| Element Name | Formerly a Ward of Child Welfare/Foster Care Agency |
| Field 1 & Responses | Formerly a Ward of Child Welfare or Foster Care Agency |
|  | 0 No |
|  | T Yes |
|  | 8 Client doesn't know |
|  | ਰੇ Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent A - Dependent to | If Yes for "Formerly a Ward of Child Welfare or Foster Care Agency" |
| Field 1 & Response 1 | Number of Years |
|  | T Less than one year |
|  | 2 1 to 2 years |
|  | 3 3 to 5 or more years |
| Dependent B - Dependent to | lf Less than one year for "Number of Years" |
| Dependent A & Response 1 | Number of Months ((integers 1-11) |
| Element Type | Program Specific |

| Funder: Program-Component | HHS: RHY – Collection required for all components except for Street Outreach |
| --- | --- |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 12: Homelessness Prevention |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start |
| Relationship to Enrollment ID | No more than one Formerly a Ward of Child Welfare or Foster Care Agency per |
| (an enrollment) | Enrollment |
| Relationship to Personal ID | One or more Formerly a Ward of Child Welfare or Foster Care Agency per Client |
| (a client) |  |
| System Logic & Other System | System stores collected information as 'project start' information and retains for |
| lssues | historical purpose. |
|  | HMIS may choose to only display dependent questions if the HMIS end user selects |
|  | the appropriate response. |
| XML | <EntryRHY> |
| CSV | Enrollment |
| 2024 Revision Summary | Updated Project Type Applicability to accommodate addition of Emergency Shelter |
|  | – Entry Exit project type. Changed "Client refused' to "Client prefers not to answer" |

## R12 Formerly a Ward of Juvenile Justice System

| Header | Instruction |
| --- | --- |
| Element Name | Formerly a Ward of Juvenile Justice System |
| Field 1 & Responses | Formerly a Ward of Juvenile Justice System |
|  | 0 No |
|  | 1 Yes |
|  | 8 Client doesn't know |
|  | 9 Client prefers not to answer |
|  | ਰੇਰੇ Data not collected |
| Dependent A - Dependent to | If Yes for "Formerly a Ward of Juvenile Justice System" |
| Field 1 & Response 1 | Number of Years |
|  | Less than one year T |
|  | 1 to 2 years 2 |
|  | 3 to 5 or more years 3 |
| Dependent B - Dependent to | lf Less than one year for "Number of Years" |
| Dependent A & Response 1 | Number of Months (1-11) |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: RHY – Collection required for all components except for Street Outreach |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 12: Homelessness Prevention |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start |
| Relationship to Enrollment ID | No more than one Formerly a Ward of Juvenile Justice System per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Formerly a Ward of Juvenile Justice System per Client |
| client) |  |
| System Logic & Other System | System stores collected information as 'project start' information and retains for |
| Issues | historical purpose. |
|  | HMIS may choose to only display dependent questions if the HMIS end user selects |

|  | the appropriate response. |
| --- | --- |
| XML | <EntryRHY> |
| CSV | Enrollment |
| 2024 Revision Summary | Updated Project Type Applicability to accommodate addition of Emergency Shelter – Entry Exit project type. Changed "Client refused' to "Client prefers not to answer" |

#### R13 Family Critical Issues

| Header | Instruction |
| --- | --- |
| Element Name | Family Critical Issues |
| Field 9 & Responses | Unemployment - Family member |
|  | 0 No |
|  | ਹ Yes |
| Field 11 & Responses | Mental Health Disorder – Family member |
|  | 0 No |
|  | 1 Yes |
| Field 15 & Responses | Physical Disability – Family member |
|  | 0 No |
|  | 1 Yes |
| Field 21 & Responses | Alcohol or Substance Use Disorder - Family member |
|  | 0 No |
|  | ਹ Yes |
| Field 22 & Responses | Insufficient Income to support youth - Family member |
|  | O No |
|  | 1 Yes |
| Field 24 & Responses | Incarcerated Parent of Youth |
|  | O No |
|  | 1 Yes |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: RHY – Collection required for all components except for Street Outreach |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 12: Homelessness Prevention |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Start |
| Relationship to Enrollment ID | No more than one Family Issues per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Family Issues per Client |
| client) |  |
| System Logic & Other System | System stores collected information as 'project start' information and retains for |
| Issues | historical purpose. |
| Other System Issues | None |
| XML | <EntryRHY> |
| CSV | Enrollment |
| 2024 Revision Summary | Updated Project Type Applicability to accommodate addition of Emergency Shelter |
|  | - Entry Exit project type |

| Instruction | Header | ВСР-Р | BCb-ES | TLP&MGH | DEMO | Element Name | RHY Service Connections | SOP |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Field 1 & Response | Date of Service ([date field]) | X | × | × | × | Type of RHY Service | × | × | × | × | Field 2 & Responses |
| 2 | X | × | Community service/service learning | (CST) |  |  |  |  |  |  |  |
| × | × | × | X | 7 | Criminal justice /legal services | 5 | × | × | X | × | Education |
| × | б | X | Employment and/or training services | × | X | × | × | 14 | Health/medical care |  |  |
| × | 26 | Home-based Services | X | X | × | × | Life skills training | 8 |  |  |  |
| Parenting education for youth with | × | × | 10 | × | X | children |  |  |  |  |  |
| Post-natal newborn care (wellness | × | X | 27 | exams; immunizations) |  |  |  |  |  |  |  |
| Post-natal care for client (person who | X | × | 12 | gave birth) |  |  |  |  |  |  |  |
| Pre-natal care | × | × | 13 | STD Testing | × | × | 28 |  |  |  |  |
| Street-based Services | 29 | × | Substance use disorder treatment | × | 17 | × | × | × |  |  |  |
| Substance Use disorder | 18 | × | × | × | × | Ed/Prevention Services |  |  |  |  |  |
| HHS: RHY – Collection required for components – as outlined above | Funder: Program -Component | 0: Emergency Shelter – Entry Exit | Project Type Applicability |  |  |  |  |  |  |  |  |
| 2: Transitional Housing | 6: Services Only |  |  |  |  |  |  |  |  |  |  |
| 12: Homelessness Prevention | Head of Household and Adults | Data Collected About |  |  |  |  |  |  |  |  |  |
| Occurrence Point (At First Service) | Collection Point | Relationship to Enrollment ID | Zero or more RHY Service Connections per Enrollment |  |  |  |  |  |  |  |  |
| (an enrollment) | Relationship to Personal ID | Zero or more RHY Service Connections per Client |  |  |  |  |  |  |  |  |  |
| (a client) | System Logic & Other System |  |  |  |  |  |  |  |  |  |  |
| Data are time sensitive and may change over the project stay. The system must | lssues | allow for multiple records per project stay to record each instance and must record |  |  |  |  |  |  |  |  |  |
| the date the new information was collected. |  |  |  |  |  |  |  |  |  |  |  |
| If the service benefits the entire household, it may be recorded solely for the Head | of Household. |  |  |  |  |  |  |  |  |  |  |
| XML | <ServiceFAReferral> | CSV | Services |  |  |  |  |  |  |  |  |
| 2024 Revision Summary | Updated Project Type Applicability to accommodate addition of Emergency Shelter | - Entry Exit project type |  |  |  |  |  |  |  |  |  |

#### R15 Commercial Sexual Exploitation/Sex Trafficking

| Header | Instruction |  |
| --- | --- | --- |
| Element Name |  | Commercial Sexual Exploitation/Sex Trafficking |
| Field 1 & Responses |  | Ever received anything in exchange for sex (e.g., money, food, drugs, shelter) |
|  | O No |  |
|  | 1 Yes |  |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Dependent A - Dependent to |  | If Yes for "Ever received anything in exchange for sex" |
| Field 1 & Response 1 |  | In the last three months |
|  | No 0 |  |
|  | 1 Yes |  |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Dependent B - Dependent to |  | If Yes for "Ever received anything in exchange for sex" |
| Field 1 & Response 1 |  | How many times |
|  | 1 1-3 |  |
|  | 2 4-7 |  |
|  | 3 | 8-J1 |
|  | 4 | 12 or more |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Dependent C - Dependent to |  | If Yes for "Ever received anything in exchange for sex" |
| Field 1 & Response 1 |  | Ever made/persuaded/forced to have sex in exchange for something |
|  | O No |  |
|  | 1 Yes |  |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Dependent D - Dependent to |  | If Yes for "Ever made/persuaded/forced to have sex in exchange for something?" |
| Dependent C & Response 1 |  | In the last three months? |
|  | 0 No |  |
|  | 1 Yes |  |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
| ਰੇਰੇ |  | Data not collected |
| Element Type |  | Program Specific |
| Funder: Program-Component |  | HHS: RHY – Collection required for all components |
| Project Type Applicability |  | 0: Emergency Shelter – Entry Exit |
|  |  | 2: Transitional Housing |
|  |  | 4: Street Outreach |
|  |  | 12: Homelessness Prevention |
| Data Collected About |  | Head of Household and Adults |
| Collection Point |  | Project Exit |
| Relationship to Enrollment ID |  | Zero or 1 Commercial Sexual Exploitation per Enrollment |
| (an enrollment) |  |  |
| Relationship to Personal ID |  | Zero or more Commercial Sexual Exploitation per Client |

| (a client) |  |
| --- | --- |
| System Logic Other System Issues | System stores collected information as 'project exit' information and retains for |
|  | historical purposes. HMIS may choose to only display dependent questions if the |
|  | HMIS end user selects the appropriate response. If mouse over/hover functionality |
|  | is available in the system for explanations/definitions, RHY requests the |
|  | information to read as follows: |
|  | Field 1: "Have you ever received anything in exchange for having sexual relations |
|  | with another person, such as money, food, drugs, or shelter?" |
|  | Dependent B: "How many times have you received something in exchange for |
|  | having sexual relations with another person, such as money, food, drugs, or |
|  | shelter?" |
|  | Dependent C: "Did someone ever make you or persuade you to have sex with |
|  | anyone else in exchange for something such as money, food, drugs, or shelter?" |
| XML | <ExitRHY> |
| CSV | Exit |
| 2024 Revision Summary | Wording change in system logic. Updated Project Type Applicability to |
|  | accommodate addition of Emergency Shelter – Entry Exit project type. Changed |
|  | "Client refused' to "Client prefers not to answer" |

#### R16 Labor Exploitation/Trafficking

| Header | Instruction |
| --- | --- |
| Element Name | Labor Exploitation/Trafficking |
| Field 1 & Responses | Ever afraid to quit/leave work due to threats of violence to yourself, family, or |
|  | friends |
| 0 | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Field 2 & Responses | Ever promised work where work or payment was different than you expected |
| 0 | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent A - Dependent to | If Yes for either "Workplace violence threats" OR "Workplace promise difference" – |
| Field 1 & 2 Response 1 | Felt forced, coerced, pressured, or tricked into continuing the job |
| 0 | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |
| ਰੇਰੇ | Data not collected |
| Dependent B - Dependent to | lf Yes for either "Workplace violence threats" OR "Workplace promise actual |
| Field 1 & 2 Response 1 | difference" – In the last 3 months |
| 0 | No |
| 1 | Yes |
| 8 | Client doesn't know |
| 9 | Client prefers not to answer |

| ਰੇਰੇ | Data not collected |
| --- | --- |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: RHY – Collection required for all components |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 4: Street Outreach |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Exit |
| Relationship to Enrollment ID | Zero or one Labor Exploitation per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | Zero or more Labor Exploitation per Client |
| client) |  |
| System Logic & Other System | System stores collected information as 'project exit' information and retains for |
| lssues |  |
|  | historical purposes. HMIS may choose to only display dependent questions if the |
|  | HMIS end user selects the appropriate response. If mouse over/hover functionality |
|  | is available in the system for explanations/definitions, RHY requests the |
|  | information to read as follows: |
|  | Field 1: "Have you ever been afraid to leave or quit a work situation due to fears of |
|  | violence or other threats of harm to yourself, family or friends?" |
|  | Field 2: "Have you ever been promised work where the work or payment ended up |
|  | being different from what you expected?" |
|  | Dependent A: "Did you feel forced, coerced, pressured or tricked into continuing |
|  | this job?" |
| XML | <ExitRHY> |
| CSV | Exit |
| 2024 Revision Summary | Wording change in system logic. Updated Project Type Applicability to |
|  | accommodate addition of Emergency Shelter – Entry Exit project type. Changed |
|  | "Client refused' to "Client prefers not to answer" |

#### R17 Project Completion Status

| Header | Instruction |
| --- | --- |
| Element Name | Project Completion Status |
| Field 1 & Responses | Project Completion Status |
|  | 1 Completed project |
|  | 2 Client voluntarily left early |
|  | ന Client was expelled or otherwise involuntarily discharged from project |
| Dependent A - Dependent to Field 1 & Response 3 | If Client was expelled or otherwise involuntarily discharged from project for "Project Completion Status" |
|  | Select the major reason |
|  | 1 Criminal activity/destruction of property/violence |
|  | Non-compliance with project rules 2 |
|  | Non-payment of rent/occupancy charge 3 |
|  | Reached maximum time allowed by project 4 |
|  | Project terminated 5 |
|  | Unknown/disappeared ଚ |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: RHY – Collection required for all components except for Street Outreach and |
|  | BCP-Prevention |

| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
| --- | --- |
|  | 2: Transitional Housing |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Exit |
| Relationship to Enrollment ID | Zero or one Project Completion Status per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | Zero or more Project Completion Status per Client |
| client) |  |
| System Logic & Other System | System stores collected information as 'project exit' information and retains for |
| Issues | historical purposes. |
| XML | <ExitRHY><ProjectCompletionStatus> |
| CSV | Exit |
| 2024 Revision Summary | Updated Project Type Applicability to accommodate addition of Emergency Shelter – Entry Exit project type. Changed "Youth" in Field 1 responses to "Client" Wording |
|  | change in system logic. |

## R18 Counseling

| Header | Instruction |
| --- | --- |
| Element Name | Counseling |
| Field 1 & Responses | Client received counseling |
| O | No |
| T | Yes |
| Dependent A - Dependent to | If Yes Identify the type(s) of counseling received |
| Field 1 & Response 1 |  |
| 1 | Individual |
| 2 | Family |
| 3 | Group - including peer counseling |
| Dependent B - Dependent to | If yes, Identify the number of sessions received by exit |
| Field 1 & Response 1 |  |
| 1 | ([integers 1-48+]) |
| Field 2 & Response | Total number of sessions planned in client's treatment or service plan |
| 1 | ([integers 1-48+]) |
| Field 3 & Responses | A plan is in place to start or continue counseling after exit |
| 0 | No |
| 1 | Yes |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: RHY – Collection required for all components except for Street Outreach |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 12: Homelessness Prevention |
| Data Collected About | Head of Household and Adults |
| Collection Point | Project Exit |
| Relationship to Enrollment ID | Zero or one Counseling per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | Zero or more Counseling per Client |
| client) |  |
| System Logic & Other System lssues | System stores collected information as 'project exit' information and retains for |
|  | historical purposes. |
| XML | <ExitRHY> |

| CSV | EXIT |
| --- | --- |
| 2024 Revision Summary | Changed response from "Counseling received by client" to "Client received |
|  | counseling." Updated Project Type Applicability to accommodate addition of |
|  | Emergency Shelter – Entry Exit project type |

#### R19 Safe and Appropriate Exit

| Header | Instruction | Safe and Appropriate Exit | Element Name |
| --- | --- | --- | --- |
| Field 1 & Responses | Exit destination safe – as determined by the client | 0 | No |
| Yes | 1 | 8 | Client doesn't know |
| 9 | Client prefers not to answer | ਰੇਰੇ | Data not collected |
| Field 2 & Responses | Exit destination safe - as determined by the project/caseworker | 0 | No |
| 1 | Yes | 2 | Worker does not know |
| Field 3 & Response | Client has permanent positive adult connections outside of project | 0 | No |
| 1 | Yes | 2 | Worker does not know |
| Field 4 & Response | Client has permanent positive peer connections outside of project | 0 | No |
| 1 | Yes | 2 | Worker does not know |
| Field 5 & Response | Client has permanent positive community connections outside of project | 0 | No |
| 1 | Yes | 2 | Worker does not know |
| Element Type | Program Specific | Funder: Program-Component | HHS: RHY – Collection required for all components except for Street Outreach and |
| Homelessness Prevention | 0: Emergency Shelter – Entry Exit | Project Type Applicability |  |
| 2: Transitional Housing | Head of Household and Adults | Data Collected About |  |
| Project Exit | Collection Point | Zero or 1 Safe and Appropriate Exit per Enrollment | Relationship to Enrollment ID |
| (an enrollment) | Zero or more Safe and Appropriate Exit per Client | Relationship to Personal ID (a |  |
| client) | System Logic & Other System |  |  |
| System stores collected information as 'project exit' information and retains for | Issues | historical purposes. |  |
| <ExitRHY> | XML | Exit | CSV |
| Updated Project Type Applicability to accommodate addition of Emergency Shelter | 2024 Revision Summary | – Entry Exit project type. Changed "Client refused' to "Client prefers not to |  |
| answer" |  |  |  |

## R20 Aftercare Plans

| Header | Instruction |
| --- | --- |
| Element Name | Aftercare Plans |
| Field 1 & Response | Information Date (date information was collected) ([date field]) |
| Field 2 & Responses | Aftercare was provided |
| 0 | No |
| 1 | Yes |
| 9 | Client prefers not to answer |
| Dependent A- Dependent to | If yes – Identify the primary way it was provided |
| Field 2 |  |
| 1 | Via email/social media |
| 2 | Via telephone |
| 3 | In person: one-on-one |
| 4 | In person: group |
| Element Type | Program Specific |
| Funder: Program-Component | HHS: RHY – Collection required for all components except for Street Outreach |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 12: Homelessness Prevention |
| Data Collected About | Head of Household and Adults |
| Collection Point | Post Exit |
| Relationship to Enrollment ID | Zero or one Aftercare Plans per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | Zero or more Aftercare Plans per Client |
| client) |  |
| System Logic & Other System | Information may be entered post exit for a period of up to 180 days after which |
| Issues | point no data should be entered. Any data entered prior to the date of exit or after |
|  | the 180th day will not be considered in reporting or exports. |
|  | Multiple "primary ways" (dependent A) must be able to be identified in one entry |
|  | or there must be the ability to have multiple instances of the element to support |
|  | data entry for a client who received aftercare via multiple methods. |
|  | New process may be required to reopen a record with an exit to record Aftercare |
|  | information. |
| XML | <ExitRHY> |
| CSV | Exit |
| 2024 Revision Summary | Updated Project Type Applicability to accommodate addition of Emergency Shelter |
|  | – Entry Exit project type. Changed "Client refused' to "Client prefers not to answer" |

## VA Required Elements

#### V1 Veteran's Information

| Header |  | Instruction |
| --- | --- | --- |
| Element Name |  | Veterans Information |
| Field 1 & Response |  | Year Entered Military Service ([year]) |
| Field 2 & Response |  | Year Separated from Military Service ([year]) |
| Field 3 & Responses |  | Theatre of Operations: World War II |
|  | 0 | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ | Data not collected |
| Field 4 & Responses |  | Theatre of Operations: Korean War |
|  | 0 | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ | Data not collected |
| Field 5 & Responses |  | Theatre of Operations: Vietnam War |
|  | O | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ | Data not collected |
| Field 6 & Responses |  | Theatre of Operations: Persian Gulf War (Operation Desert Storm) |
|  | O | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ | Data not collected |
| Field 7 & Responses |  | Theatre of Operations: Afghanistan (Operation Enduring Freedom) |
|  | 0 | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ | Data not collected |
| Field 8 & Responses |  | Theatre of Operations: Iraq (Operation Iraqi Freedom) |
|  | O | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ | Data not collected |
| Field 9 & Responses |  | Theatre of Operations: Iraq (Operation New Dawn) |
|  | 0 | No |
|  | 1 | Yes |
|  | 8 | Client doesn't know |

|  | 9 | Client prefers not to answer |
| --- | --- | --- |
|  | ਰੇਰੇ Data not collected |  |
| Field 10 & Responses |  | Theatre of Operations: Other Peace-keeping Operations or Military Interventions |
|  |  | (such as Lebanon, Panama, Somalia, Bosnia, Kosovo) |
|  | 0 No |  |
|  | 1 Yes |  |
|  | 8 Client doesn't know |  |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ Data not collected |  |
| Field 11 & Responses |  | Branch of the Military |
|  | 1 Army |  |
|  | 2 Air Force |  |
|  | 3 Navy |  |
|  | 4 Marines |  |
|  | б Coast Guard |  |
|  | 7 Space Force |  |
|  | 8 Client doesn't know |  |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ Data not collected |  |
| Field 12 & Responses | Discharge Status |  |
|  | 1 Honorable |  |
|  | 2 | General under honorable conditions |
|  | б | Under other than honorable conditions (OTH) |
|  | 4 Bad conduct |  |
|  | 5 Dishonorable |  |
|  | 7 Uncharacterized |  |
|  | 8 Client doesn't know |  |
|  | 9 | Client prefers not to answer |
|  | ਰੇਰੇ Data not collected |  |
| Element Type | Program Specific |  |
| Funder: Program-Component |  | HUD: HUD-VASH – Collection required for all components |
|  |  | VA: SSVF – Collection required for RRH and Homelessness Prevention |
|  |  | VA: GPD – Collection required for all components |
|  |  | VA: Community Contract Safe Haven |
|  |  | VA: CRS Contract Residential Services |
| Project Type Applicability |  | 0: Emergency Shelter – Entry Exit |
|  |  | 2: Transitional Housing |
|  |  | 3: PH – Permanent Supportive Housing (disability required for entry) |
|  |  | 6: Supportive Services Only |
|  | 8: Safe Haven |  |
|  | 9: PH - Housing Only |  |
|  |  | 12: Homelessness Prevention |
|  |  | 13: PH - Rapid Re-Housing |
| Data Collected About | All Veterans |  |
| Collection Point | Record Creation |  |
| Relationship to Enrollment ID | N/A |  |
| (an enrollment) |  |  |
| Relationship to Personal ID (a |  | One Veteran's Information per Client |
| client) |  |  |
| System Logic & Other System | None |  |

| ssues |  |
| --- | --- |
| XML | <ClientVeteranInfo> |
| CSV | Client |
| 2024 Revision Summary | Updated Project Type Applicability to accommodate addition of Emergency Shelter |
|  | – Entry Exit project type. Changed "Client refused' to "Client prefers not to |
|  | answer" and added "Space Force" response option |

#### V2 Services Provided - SSVF

| Header |  | Instruction |
| --- | --- | --- |
| Element Name |  | Services Provided – SSVF |
| Field 1 & Response |  | Date of Service ([date field]) |
| Field 2 & Responses |  | Type of Service |
|  | 1 | Outreach services |
|  | 2 | Case management services |
|  | 3 | Assistance obtaining VA benefits |
|  | 4 | Assistance obtaining/coordinating other public benefits |
|  | 5 | Direct provision of other public benefits |
|  | б | Other (non-TFA) supportive service approved by VA |
|  | 7 | Shallow Subsidy |
|  | 8 | Returning Home |
|  | 9 | Rapid Resolution |
| Dependent A - Dependent to |  | If "Assistance obtaining VA benefits" |
| Field 2 Response 3 |  |  |
|  | 1 | VA vocational and rehabilitation counseling |
|  | 2 | Employment and training services |
|  | 3 | Educational assistance |
|  | 4 | Health care services |
| Dependent B - Dependent to |  | If "Assistance obtaining/coordinating other public benefits" |
| Field 2 Response 4 |  |  |
|  | 1 | Health care services |
|  | 2 | Daily living services |
|  | 3 | Personal financial planning services |
|  | 4 | Transportation services |
|  | 5 | Income support services |
|  | б | Fiduciary and representative payee services |
|  | 7 | Legal services – child support |
|  | 8 | Legal services – eviction prevention |
|  | 9 | Legal services - outstanding fines and penalties |
|  | 10 | Legal services - restore/acquire driver's license |
|  | 11 | Legal services - other |
|  | 12 | Child care |
|  | 13 | Housing counseling |
| Dependent C - Dependent to |  | If "Direct provision of other public benefits" |
| Field 2 Response 5 |  |  |
|  | 1 | Personal financial planning services |
|  | 2 | Transportation services |
|  | 3 | Income support services |
|  | 4 | Fiduciary and representative payee services |
|  | 5 | Legal services – child support |

|  | б | Legal services – eviction prevention |
| --- | --- | --- |
|  | 7 | Legal services - outstanding fines and penalties |
|  | 8 | Legal services – restore/acquire driver's license |
|  | 9 | Legal services – other |
|  | 10 | Child care |
|  | J J | Housing counseling |
| Dependent D - Dependent to |  | If "Other (Non-TFA) Supportive Service approved by VA" |
| Field 2 Response 6 |  | [text box] Specify |
| Element Type |  | Program Specific |
| Funder: Program- Component |  | VA: SSVF – Collection required for RRH and Homelessness Prevention |
| Project Type Applicability |  | 12: Homelessness Prevention |
|  |  | 13: PH - Rapid Re-Housing |
| Data Collected About |  | All Clients receiving services |
| Collection Point |  | Occurrence Point (As Provided) |
| Relationship to Enrollment |  | 0 or more Services Provided - SSVF per Enrollment |
| ID (an enrollment) |  |  |
| Relationship to Personal ID |  | 1 or more Services Provided - SSVF per Client |
| (a client) |  |  |
| System Logic & Other System Issues |  | Services will be recorded as they are provided. The system must allow for a |
|  |  | theoretically unlimited number of records per project stay. |
|  |  | HMIS end users must be able to edit existing records and delete records entered in |
|  |  | error. |
|  |  | Dependent D has a 50-character limit when exporting in the HMIS CSV. |
|  |  | Services will be recorded for the Head of Household (only) unless a specific service |
|  |  | is of benefit only to a particular household member. |
| XML |  | <ServiceFAReferral> |
| CSV |  | Services |
| 2024 Revision Summary |  | Wording change in system logic. |

#### V3 Financial Assistance - SSVF

| Header |  | Instruction |
| --- | --- | --- |
| Element Name |  | Financial Assistance – SSVF |
| Field 1 & Response |  | Start Date of Financial Assistance ([date field]) |
| Field 2 & Response |  | Financial Assistance Amount ((currency/decimdl) |
| Field 3 & Responses |  | Financial Assistance Type |
|  | 1 | Rental assistance |
|  | イ | Utility fee payment assistance |
|  | 2 | Security deposit |
|  | 3 | Utility deposit |
|  | 5 | Moving costs |
|  | 8 | Transportation services: tokens/vouchers |
|  | ਰੇ | Transportation services: vehicle repair/maintenance |
|  | 10 | Child care |
|  | 12 | General housing stability assistance |
|  | 14 | Emergency housing assistance |
|  | ਹ ਦ | Shallow subsidy financial assistance |
|  | 16 | Food assistance |
|  | 17 | Landlord incentive |

| 18 | Tenant incentive |
| --- | --- |
| Field 4 & Response | End Date of Financial Assistance ([date field]) |
| Element Type | Program Specific |
| Funder-Program Component | VA: SSVF – Collection required for RRH and Homelessness Prevention |
| Project Type Applicability | 12: Homelessness Prevention |
|  | 13: PH – Rapid Re-Housing |
| Data Collected About | All Clients receiving financial assistance |
| Collection Point | Occurrence Point (As Provided) |
| Relationship to Enrollment ID | 0 or more Financial Assistance – SSVF per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID | 1 or more Financial Assistance – SSVF per Client |
| (a client) |  |
| System Logic & Other System |  |
| Issues | Financial assistance will be recorded as it is provided. The system must allow for a |
|  | theoretically unlimited number of records per project stay. HMIS end users must be |
|  | able to edit existing records and delete records entered in error. |
|  | Financial assistance will be recorded for the Head of Household (only) unless a |
|  | specific service is of distinct benefit only to a particular household member. |
| XML | <ServiceFAReferral> |
| CSV | Services |
| 2024 Revision Summary | Wording change in system logic. Renamed field 1 "Date of Financial Assistance" to |
|  | "Start Date of Financial Assistance" and added complementary field 4, "End Date |
|  | of Financial Assistance." Added "Landlord Incentive" and "Tenant Incentive." |
|  | Renamed "Extended Shallow Subsidy – Rental Assistance" to "Shallow Subsidy |
|  | Financial Assistance." |

#### V4 Percent of AMI (SSVF Eligibility)

| Header | Instruction |
| --- | --- |
| Element Name | Percent of AMI (SSVF Eligibility) |
| Field 1 & Responses | Household Income as a Percentage of AMI |
| 1 | 30% or less |
| 2 | 31% to 50% |
| 3 | 51% to 80% |
| ব | 81% or greater |
| Element Type | Program Specific |
| Funder: Program-Component | VA: SSVF – Collection required for RRH and Homelessness Prevention |
| Project Type Applicability | 12: Homelessness Prevention |
|  | 13: PH – Rapid Re-Housing |
| Data Collected About | Head of Household |
| Collection Point | Project Start |
| Relationship to Enrollment ID | No more than one Percent of AMI (SSVF Eligibility) per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more Percent of AMI (SSVF Eligibility) per Client |
| client) |  |
| System Logic & Other System ssues | System stores collected information as 'project start' information and retains for |
|  | historical purpose. |
|  | The system may not automatically calculate this field unless the VA Annual Income |
|  | worksheet is part of the HMIS and the field is calculated from that worksheet. |
|  | Calculation from Income and Sources is prohibited. |
| XML | <EntrySSVF> |

### V6 VAMC Station Number

| V V VAIVIS JIANOT NAITIVEI |  |
| --- | --- |
| Header | Instruction |
| Element Name | VAMC Station Number |
| Field 1 & Response | VAMC Station Number [drop down list of all VAMC Station codes and names] |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: HUD-VASH – Collection required for all components |
|  | VA: SSVF – Collection required for RRH and Homelessness Prevention |
|  | VA: GPD – Collection required for all components |
|  | VA: CRS Contract Residential Services |
|  | VA: Community Contract Safe Haven Program |
| Project Type Applicability | 0: Emergency Shelter – Entry Exit |
|  | 2: Transitional Housing |
|  | 3: PH - Permanent Supportive Housing (disability required for entry) |
|  | 6: Services Only |
|  | 8: Safe Haven |
|  | 9: PH - Housing Only |
|  | 12: Homelessness Prevention |
|  | 13: PH - Rapid Re-Housing |
| Data Collected About | Head of Household |
| Collection Point | Project Start |
| Relationship to Enrollment ID | No more than one VAMC Station Number per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | One or more VAMC Station Number per Client |
| client) |  |
| System Logic & Other System | Valid VAMC Station Numbers are up to 8 alphanumeric characters and should |
| Issues | correspond to the VA service location (as opposed to 3.16 Enrollment CoC). |
|  | SSVF grantees will be provided with station numbers that correspond to their |
|  | service locations. Station Numbers are provided to vendors through the Vendor |
|  | Hub. |
|  | No information date or data collection stage is required; the effective information |
|  | date is the Project Start Date and data are only collected at project start. |
| XML | <EntrySSVF> |
| CSV | Enrollment |
| 2024 Revision Summary | Wording change in system logic. Updated Project Type Applicability to |
|  | accommodate addition of Emergency Shelter – Entry Exit project type |

#### V7 HP Targeting Criteria

| Header | Instruction |
| --- | --- |
| Element Name | HP Targeting Criteria |
| Field 1 & Responses | Is Homelessness Prevention targeting screener required? |
| 0 | No |
| 1 | Yes |
| Dependency A, dependent to | Housing loss expected within ... |
| Field 1 Response 1 |  |

|  | 0 | 1-6 days |
| --- | --- | --- |
|  | 1 | 7-13 days |
|  | 2 | 14-21 days |
|  | 3 | More than 21 days |
| Dependency B, dependent to |  | Current household income |
| Field 1 Response 1 |  |  |
|  | 0 | $0 (i.e., not employed, not receiving cash benefits, no other current income) |
|  | 1 | 1-14% of Area Median Income (AMI) for household size |
|  | 2 | 15-30% of AMI for household size |
|  | 3 | More than 30% of AMI for household size |
| Dependency C, dependent |  | Past experience of Homelessness (street/shelter/transitional housing) (any adult) |
| to Field 1 Response 1 |  |  |
|  | 0 | Most recent episode occurred within the last year |
|  | 1 | Most recent episode occurred more than one year ago |
|  | 2 | None |
| Dependency D, dependent to Field 1 Response 1 |  | Head of Household is not a current leaseholder/renter of unit |
|  | 0 | No |
|  | 1 | Yes |
| Dependency E, dependent to |  | Head of Household has never been a leaseholder/renter of unit |
| Field 1 Response 1 |  |  |
|  | 0 | No |
|  | 1 | Yes |
| Dependency F, dependent |  | Currently at risk of losing a tenant-based housing subsidy or housing in a subsidized |
| to Field 1 Response 1 |  | building or unit (household) |
|  | 0 | No |
|  | T | Yes |
| Dependency G, dependent to |  | Rental Evictions within the past 7 years (any adult) |
| Field 1 Response 1 |  |  |
|  | 0 | No prior rental evictions |
|  | 1 | 1 prior rental eviction |
|  | 2 | 2 or more prior rental evictions |
| Dependency H, dependent to |  | Criminal record for arson, drug dealing or manufacture, or felony offense against |
| Field 1 Response 1 |  | persons or property (any adult) |
|  | 0 | No |
|  | T | Yes |
| Dependency I, dependent to |  | Incarcerated as adult (any adult in household) |
| Field 1 Response 1 |  |  |
|  | 0 | Not incarcerated |
|  | T | Incarcerated once |
|  | 2 | Incarcerated two or more times |
| Dependency J, dependent to |  | Discharged from jail or prison within last six months after incarceration of 90 days |
| Field 1 Response 1 |  | or more (adults) |
|  | 0 | No |
|  | T | Yes |
| Dependency K, dependent to |  | Registered sex offender (any household members) |
| Field 1 Response 1 |  |  |
|  | O | No |
|  | T | Yes |
| Dependency L |  | Head of Household with disabling condition (physical health, mental health, |
| Field 1 Response 1 |  | substance use) that directly affects ability to secure/maintain housing |
|  | 0 | No |
|  | । | Yes |

| Dependency M, dependent to | Currently pregnant (any household member) | Field 1 Response 1 |  |
| --- | --- | --- | --- |
| 0 | No | ਹ | Yes |
| Dependency N, dependent | Single parent/guardian household with minor child(ren) | to Field 1 Response 1 |  |
| 0 | No | ਹ | Yes |
| Dependency O, dependent to | Household includes one or more young children (age six or under), or a child who | Field 1 Response 1 | requires significant care |
| 0 | No | ਹ | Youngest child is under 1 year old |
| 2 | Youngest child is 1 to 6 years old and/or one or more children (any age) require | significant care. |  |
| Dependency P, dependent to | Household size of 5 or more requiring at least 3 bedrooms (due to age/gender mix) | Field 1 Response 1 |  |
| 0 | No | ਹ | Yes |
| Dependency Q, dependent to | Household includes one or more members of an overrepresented population in the | Field 1 Response 1 | homelessness system when compared to the general population. |
| 0 | No | ਹ | Yes |
| Dependency R, dependent | HP applicant total points ([integer]) | to Field 1 Response 1 |  |
| Dependency S, dependent to | Grantee targeting threshold score ([integer]) | Field 1 Response 1 |  |
| Element Type | Program Specific | Funder: Program- Component | VA: SSVF - Collection required for Homelessness Prevention |
| 12: Homelessness Prevention | Project Type Applicability | Data Collected About | Head of Household |
| Collection Point | Project Start | Relationship to Enrollment ID | No more than one SSVF HP Targeting Criteria per Enrollment |
| (an enrollment) | One or more SSVF HP Targeting Criteria per Client | Relationship to Personal ID |  |
| (a client) | System Logic & Other System |  |  |
| Records must be editable for users to correct data entry errors. | Issues |  |  |
| There are redundancies between this data element and other data collection, | including 3.08 Disabling Condition, 4.02 Income and Sources, V1 Veteran's |  |  |
| Information, V4 Percent of AMI (SSVF Eligibility), and data related to household | composition. Consistency in responses for this data element and others will be |  |  |
| used in evaluation of SSVF data quality. | XML | <EntrySSVF> |  |
| Enrollment | CSV | Added "renter of unit" language to "leaseholder" in field names | 2024 Revision Summary |

V8 HUD-VASH Voucher Tracking

| Header | Instruction |
| --- | --- |
| Element Name | HUD-VASH Voucher Tracking |
| Field 1 & Response | Information date ([date field]) |
| Field 2 & Responses | Voucher change |
|  | Referral package forwarded to PHA |

|  | 2 | Voucher denied by PHA |
| --- | --- | --- |
|  | 3 | Voucher issued by PHA |
|  | 4 | Voucher revoked or expired |
|  | 5 | Voucher in use - veteran moved into housing |
|  | б | Voucher was ported locally |
|  | 7 | Voucher was administratively absorbed by new PHA |
|  | 8 | Voucher was converted to Housing Choice Voucher |
|  | 9 | Veteran exited - voucher was returned |
|  | 10 | Veteran exited - family maintained the voucher |
|  | JI | Veteran exited - prior to ever receiving a voucher |
|  | 12 | Other |
| Dependent A - Dependent to |  | If Other- |
| Field 2 & Response 12 |  | [text box] Specify |
| Element Type |  | Program Specific |
| Funder: Program-Component |  | HUD: HUD-VASH – Collection required for HUD/VASH Collaborative Case |
|  |  | Management |
| Project Type Applicability |  | 3: PH - Permanent Supportive Housing (disability required for entry) |
| Data Collected About |  | Head of Household/Veteran |
| Collection Point |  | Occurrence Point (as provided) |
| Relationship to Enrollment ID |  | Zero or more HUD-VASH Voucher Tracking per Enrollment |
| (an enrollment) |  |  |
| Relationship to Personal ID (a |  | Zero or more HUD-VASH Voucher Tracking per Client |
| client) |  |  |
| System Logic & Other System lssues |  | There may be only one response per Information Date. |
|  |  | The system must record the appropriate collection stage for each element. |
|  |  | Systems must also allow for update information if a change occurs mid-year. Allow |
|  |  | corrections for data entry errors at all stages. |
| XML |  | <ServiceFAReferral> |
| CSV |  | Services |
| 2024 Revision Summary |  | Updated Funder: Program-Component |

#### V9 HUD-VASH Exit Information

| Header |  | Instruction |
| --- | --- | --- |
| Element Name |  | HUD-VASH Exit Information |
| Field 1 & Responses |  | Case Management Exit Reason |
|  | 1 | Accomplished goals and/or obtained services and no longer needs CM |
|  | 2 | Transferred to another HUD-VASH program site |
|  | 3 | Found/chose other housing |
|  | ব | Did not comply with HUD-VASH CM |
|  | ട | Eviction and/or other housing related issues |
|  | e | Unhappy with HUD-VASH housing |
|  | 7 | No longer financially eligible for HUD-VASH voucher |
|  | 8 | No longer interested in participating in this program |
|  | ਰੇ | Veteran cannot be located |
|  | 10 | Veteran too ill to participate at this time |
|  | J J | Veteran is incarcerated |
|  | 12 | Veteran is deceased |
|  | 13 | Other |

| Dependent B - Dependent to | If Other- |
| --- | --- |
| Field 1 & Response 13 | [text box] Specify |
| Element Type | Program Specific |
| Funder: Program-Component | HUD: HUD-VASH – Collection required for HUD/VASH Collaborative Case |
|  | Management |
| Project Type Applicability | 3: PH - Permanent Supportive Housing (disability required for entry) |
| Data Collected About | Head of Household/Veteran |
| Collection Point | Project Exit |
| Relationship to Enrollment ID | Zero or one HUD-VASH Exit Information per Enrollment |
| (an enrollment) |  |
| Relationship to Personal ID (a | Zero or more HUD-VASH Exit Information per Client |
| client) |  |
| System Logic & Other System | The system must record the appropriate collection stage for each element. |
| lssues |  |
| XML | <ExitVASH> |
| CSV | Exit |
| 2024 Revision Summary | Updated Funder: Program-Component |

## METADATA ELEMENTS

The term metadata is often defined as 'data about data.' Instead of capturing information about a project or a client, Metadata Elements capture information about the data itself:

- When it was collected ●
- When it was entered into HMIS
- Who entered it
- Which project is responsible for it

The Metadata Elements are intended to facilitate reporting from HMIS, to simplify the writing of programming specifications, and to provide an audit trail. These elements do not represent an attempt to standardize the way that an HMIS stores data. As long as an HMIS is able to accomplish the purposes identified for the Metadata Elements, the software is not required to use the exact metadata elements listed here. Future programming specifications for reports will reference these Metadata Elements. The Metadata Elements are:

#### 5.01 Date Created

| Header | Instruction |
| --- | --- |
| Element Name | Date Created |
| Field 1 & Response | ([date field]) |
| Element Type | Metadata |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Records |
| Collection Point | Record Creation |
| System Logic & Other System | HMIS auto-generated. An HMIS must have the ability to identify the date on which |
| lssues | a record was first created in HMIS for any data element. Data elements that are |
|  | collected together on a single form may share a single Date Created. HMIS end |
|  | users and HMIS Administrators must not have the ability to enter or to modify the |
|  | information in this Metadata Element. |
|  | An HMIS must store this metadata for all client-level data elements. It is not |
|  | necessary that this information be displayed in the user interface of the HMIS, but |
|  | it must be accessible in the programming of reports. Date Created must not change |
|  | when a data element is edited. If two client records representing the same person |
|  | are merged, the earliest Date Created must be retained for data elements for |
|  | which an HMIS stores only one value per client (e.g., name, SSN, date of birth). |
| XML | XML attribute: DateCreated |
| CSV | <*><DateCreated> (Field collected across multiple files) |
| 2024 Revision Summary | None |

#### 5.02 Date Updated

| Header | Instruction |
| --- | --- |
| Element Name | Date Updated |
| Field 1 & Response | ([date field]) |
| Element Type | Metadata |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Data Elements |
| Collection Point | Record Creation / Edit |
| System Logic & Other System | HMIS auto-generated. Created by the HMIS when a record for any data element |

| Issues | is first created and updated by the HMIS every time the record is saved by an HMIS |
| --- | --- |
|  | end user. |
|  | An HMIS must be able to determine, for all data elements, the date on which it |
|  | was last edited by an HMIS end user. Each time an HMIS end user saves data, the |
|  | HMIS must store the current date as the Date Updated with the data being saved. |
|  | Data elements that are collected together on a single form may share a single Date |
|  | Updated. HMIS end users or HMIS administrators must not have the ability to enter |
|  | or to modify the information in this metadata element. |
| XML | XML attribute: DateUpdated |
| CSV | <*><DateUpdated> (Field collected across multiple files) |
| 2024 Revision Summary | None |

#### 5.03 Data Collection Stage

| Header | Instruction |
| --- | --- |
| Element Name | Data Collection Stage |
| Field 1 & Response | Data Collection Stage |
| 1 | Project start |
| 2 | Project update |
| 5 | Project annual assessment |
| 3 | Project exit |
| б | Post exit |
| Element Type | Metadata |
| Funder: Program-Component | All Programs - All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Data Elements with multiple data collection stages |
| Collection Point | Client Data Entry of Specified Elements |
| System Logic & Other System | HMIS auto-generated or HMIS end user selected. |
| lssues | An HMIS must be able to distinguish between data collected at different points in |
|  | time or stages (e.g., at project start, project update (during a project stay), and at |
|  | project exit). |
|  | Data elements that are collected together on a single form generally share a single |
|  | Data Collection Stage. |
|  | HMIS end users should not have the ability to create more than one record per |
|  | data element at either project start or project exit (e.g., for a single project stay, a |
|  | client should have one and only one record of 4.02 Income and Sources identified |
|  | at project start). |
|  | The system must allow a user to save a dated record for a client's annual |
|  | assessment as an 'annual assessment'. |
|  | The response categories correlate to response categories defined in the XML and |
|  | CSV specifications. |
|  | An 'annual assessment' is required as noted in the collection stage for some PSDEs. |
|  | The Annual Assessment must include updating both the Head of Household's |
|  | record and any other household members at the same time. |
|  | Elements for which a collection point of 'annual assessment' is required and must |
|  | be collected at least once annually for each client. An Annual Assessment and the |

|  | Information Date must be no more than 30 days before or after the anniversary of |
| --- | --- |
|  | the Head of Household's Project Start Date; information must be accurate as of the |
|  | Information Date. The date range of the Annual Assessment is based entirely |
|  | around the Head of Household's Project Start Date, not on the date of the client's |
|  | or Head of Household's previous assessment. For all projects which require an |
|  | annual assessment, data collected as part of an annual assessment must have a |
|  | Data Collection Stage of 'annual assessment.' There should be one and only one |
|  | record for each data element with a Data Collection Stage of 'annual assessment' |
|  | within the 60-day period surrounding the anniversary of the Head of Household's |
|  | Project Start Date. Regardless of whether the responses have changed since |
|  | project start or the previous annual assessment, a new record must be created for |
|  | each annual assessment such that it is possible to view a history, by date, of the |
|  | values for each data element. |
| XML | XML attribute: DataCollectionStage |
| CSV | <*><DataCollectionStage> (Field collected across multiple files) |
| 2024 Revision Summary | None |

#### 5.04 Information Date

| Header | Instruction |
| --- | --- |
| Element Name | Information Date |
| Field 1 & Response | ([date field]) |
| Element Type | Metadata |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | As Specified in Data Element Definitions |
| Collection Point | Client Program-Specific Data Entry |
| System Logic & Other System | This Metadata Element is a hybrid in that it pertains to the client data and not |
| lssues | directly to the client, but it will be entered in HMIS by HMIS end users. |
|  | Throughout the Data Dictionary this Metadata Element has been added to the data |
|  | elements where it applies (e.g., 4.02 Income and Sources, with Response 1 |
|  | Information Date). The metadata element is included here to provide further |
|  | information for HMIS vendors and HMIS Administrators. |
|  | Data that is collected the first time the client is entered into HMIS (e.g., 3.01 Name, |
|  | 3.02 Social Security Number) do not require an Information Date. |
|  | Data that is collected only at project start or only at project exit, may be assumed |
|  | to have an Information Date that matches the Project Start Date or Project Exit |
|  | Date, respectively, or an HMIS may require that an HMIS end user specify the date. |
|  | Data elements that are collected together on a single form generally share a single |
|  | Information Date. |
|  | This Metadata Element is applicable to all elements which can change over time. |
| XML | XML attribute: InformationDate |
| CSV | <*><InformationDate> (Field collected across multiple files) |
| 2024 Revision Summary | Wording change in system logic and clarified collection point |

| Header | Instruction |
| --- | --- |
| Element Name | Project Identifier |
| Field 1 & Response | Project Identifier (2.02 Project Information) of the project that entered or edited |
|  | the data |
| Element Type | Metadata |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | Specified Data Elements |
| Collection Point | Record Creation/Edit |
| System Logic & Other System lssues | HMIS auto-generated or HMIS end user selected. If end user selected, HMIS |
|  | software must enforce uniqueness of this identifier. |
|  | Data elements that are collected together on a single form/screen generally share |
|  | a single Project Identifier. In order to report on data quality on a project's report, it |
|  | is first necessary to establish that the project in question was responsible for the |
|  | data. |
|  | This is a basic requirement that assumes a simple relationship between clients and |
|  | projects. In circumstances where one project may be responsible for entering data |
|  | that would appropriately appear on another project's required report (e.g., a |
|  | central intake point), it may be necessary to create a more sophisticated method |
|  | to establish responsibility for the data entered. |
| XML | Unique Identifier: ProjectID |
| CSV | <*><ProjectID> (Field collected across multiple files) |
| 2024 Revision Summary | Wording change in system logic and clarified collection point |

## 5.06 Enrollment Identifier

| Header | Instruction |
| --- | --- |
| Element Name | Enrollment Identifier |
| Field 1 & Response | A unique project start identifier used to associate data with a particular period of |
|  | service. |
| Element Type | Metadata |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Enrollment Level Data |
| Collection Point | Record Creation |
| System Logic & Other System | HMIS auto-generated. The data element should be created by the HMIS at the time |
| lssues | that the record of a project start is first entered into HMIS and should be stored with |
|  | any data that pertains to that particular period of service. |
|  | Data elements that are collected together on a single form/screen may share a |
|  | single Enrollment Identifier. An HMIS should be able to correlate data to a specific |
|  | project stay. |
|  | This metadata element must be stored with all elements identified in this |
|  | document as having a collection point 'Project Start'. |
| XML | Unique Identifier: EnrollmentID |
| CSV | <*><EnrollmentID> (Field collected across multiple files) |
| 2024 Revision Summary | Clarified collection point |

| Header | Instruction |
| --- | --- |
| Element Name | User Identifier |
| Field 1 & Response | A unique ID used to associate data with the user who entered and/or edited it |
| Element Type | Metadata |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Records |
| Collection Point | All Data Collection Points/Stages |
| System Logic & Other System | HMIS generated. Each HMIS end user must have a unique identifier stored in the |
| lssues | HMIS. Every time data is entered or edited in HMIS, the HMIS must keep a record |
|  | of which HMIS end user entered or edited the data based on the credentials |
|  | supplied at the time of login. |
|  | The data element should be stored with any Universal or Program-Specific Data |
|  | Element entered or edited in an HMIS. |
|  | It must be possible to determine, for all client-level data, which HMIS end user |
|  | entered it in the HMIS. Each time an HMIS end user saves data, the HMIS must |
|  | store the User Identifier of that HMIS end user with the data being saved. |
|  | Data elements that are collected together on a single form may share a single User |
|  | ldentifier. |
|  | HMIS end users must not have the ability to enter or to modify the information in |
|  | this Metadata Element. |
|  | If a data element is edited, the HMIS must retain the original value, along with the |
|  | User Identifier of the HMIS end user who entered it, in addition to storing the new |
|  | value and the User Identifier of the editing HMIS end user. |
| XML | XML attribute: UserID |
| CSV | <*><UserID> (Field collected across multiple files) |
| 2024 Revision Summary | Wording change in system logic and clarified collection point |

## 5.08 Personal Identifier

| Header | Instruction |
| --- | --- |
| Element Name | Personal Identifier |
| Field 1 & Response | Personal ID [HMIS Generated] |
| Element Type | Metadata |
| Funder: Program-Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Clients |
| Collection Point | Record Creation |
| System Logic & Other System | The purpose of this data element is to ensure that, regardless of how many client |
| lssues | records exist for a single person in an HMIS, that person is only counted once for |
|  | reporting purposes. While the expectation is that every effort will be made to |
|  | minimize duplicate client records, for those instances where duplication is |
|  | unavoidable, the Personal ID must link a given person's client records for the |
|  | purposes of deduplication within reports. |

|  | A Personal ID is an automatically generated identifier created by an HMIS |
| --- | --- |
|  | application. A Personal ID must be static and unique to a single individual within an |
|  | HMIS implementation, regardless of how many client records exist for the |
|  | individual. There is no required format for generating a Personal ID; however, the |
|  | Universal Data Elements used to create a Personal ID should not be visible in the |
|  | Personal ID. |
|  | The Personal ID must be able to be attached to the same individual when served by |
|  | multiple projects. There is a one-to-one relationship between Personal ID and3.01 |
|  | Name, 3.02 Social Security Number, 3.03 Date of Birth, 3.04 Race and Ethnicity, |
|  | 3.06 Gender, and 3.07 Veteran Status or a combination of these that provides a |
|  | high degree of confidence that multiple client records represent the same |
|  | individual. |
|  | HMIS must have functionality to allow the HMIS Administrators to de-duplicate |
|  | multiple client records with distinct Personal IDs that are identified as representing |
|  | the same individual based on identifying information. |
| XML | <Client><PersonalID> |
| CSV | Client |
| 2024 Revision Summary | Provided clarification of the purpose of Personal Identifier. Wording change in |
|  | system logic to account for updates to 3.04 Race and Ethnicity. |

## 5.09 Household Identifier

| Header | Instruction |
| --- | --- |
| Element Name | Household Identifier |
| Field 1 & Response | Household ID [HMIS Generated] |
| Element Type | Metadata |
| Funder: Program- Component | All Programs – All Components |
| Project Type Applicability | All HMIS Project Types |
| Data Collected About | All Clients |
| Collection Point | Project Start |
| System Logic & Other System | A Household ID will be assigned to each household at each project start and applies |
| lssues | for the duration of that project stay to all members of the household served. |
|  | The Household ID must be automatically generated by an HMIS application to |
|  | ensure that it is unique. The Household ID must be unique within each HMIS |
|  | implementation regardless of how many CoCs it covers. This includes data |
|  | warehouses that may be pulling in data from multiple HMIS instances, and one or |
|  | more CoCs. |
|  | The Household ID has no meaning beyond a single 'household enrollment'; it is |
|  | used in conjunction with the 2.02.1 Project ID, 3.10 Project Start Date, and 3.11 |
|  | Project Exit Date to link records for household members together and indicate that |
|  | they were served together. |
|  | The Household ID is to be unique to each household stay in a project; reuse of the |
|  | identification for the same or similar household upon readmission into the project is |
|  | unacceptable. |
|  | Persons may join a household with members who have already begun a project |
|  | start or may leave a project although other members of the household remain in |
|  | the project. A common Household ID must be assigned to each member of the |

|  | same household. Persons in a household (either adults or children) who are not |
| --- | --- |
|  | present when the household initially applies for assistance and later join the |
|  | household should be assigned the same Household ID that links them to the rest of |
|  | the persons in the household. The early departure of a household member would |
|  | have no impact on the Household ID. A household member who leaves and returns |
|  | to the same household while others in the household remain enrolled should be |
|  | reassigned the same Household ID as that member's earlier enrollment. |
| XML | <Enrollment><HouseholdID> |
| CSV | Enrollment |
| 2024 Revision Summary | Wording changes in system logic |

### 5.10 Implementation Identifier

| Header | Instruction |
| --- | --- |
| Element Name | Implementation Identifier |
| Field 1 & Response | Implementation ID [Vendor Generated] |
| Element Type | Metadata |
| Data Collected About | All HMIS Implementations |
| Collection Point | Upon creation of HMIS implementation |
| System Logic & Other System | The purpose of Implementation ID is to indicate the scope of uniqueness of the |
| lssues | primary keys within an export. Each implementation of HMIS is unique and the |
|  | Implementation ID is to identify that exported data is affiliated with a given HMIS |
|  | implementation. For example, an HMIS vendor providing HMIS software to two |
|  | distinct CoCs with two distinct HMIS implementations would have different |
|  | Implementation IDs for those different implementations. Alternatively, an HMIS |
|  | vendor providing HMIS software to two distinct CoCs sharing an HMIS |
|  | implementation would have the same Implementation ID. |
|  | A unique Implementation ID must be created per HMIS instance, but there is no |
|  | required format. |
| XML | <source> |
| CSV | Export |
| 2024 Revision Summary | New element |

## REQUIRED COLLECTION POINTS AND METADATA ELEMENTS TABLE SUMMARY

## Required Collection Points

Users must be able to enter each data element at the appropriate point in time, as identified in each individual data element definition and summarized in the table below.

Data Elements with Multiple Collection Points

- Data elements with multiple collection points must be recorded with 5.03 Data Collection Stage.
- There may be no more than one record per 5.06 Enrollment ID of any multiple-point data element with a 5.03

Data Collection Stage of 'project start' or 'project exit'.

- Users must be able to create a theoretically infinite number of records per 5.06 Enrollment ID with a data collection stage of 'update' or 'annual assessment' for multiple-point data elements.
## Data Elements with a Single Collection Point

- Data elements with a single collection point may be recorded with 5.03 Data Collection Stage, but it is not ● required.
- There may be no more than one record per 5.06 Enrollment ID of any data element collected only at project start, only at project exit, or only post-exit.
- Users must be able to create a theoretically infinite number of records per 5.06 Enrollment ID for singlepoint data elements with a plain 'X' in the 'Update/Occurrence Point' column in the table below.
- There may be no more than one record per 5.06 Enrollment ID for single-point data elements with 'X (0...1)' in the 'Update/Occurrence Point' column in the table below.

## Base Metadata

5.01 Date Created, 5.02 Date Updated, and 5.07 User Identifier are not shown in the table below; these base metadata elements are required for every data element. Data elements collected on a single form/stored as fields in one record of a table may share a single set of this base metadata as long as the data elements, as they are defined by this Dictionary, are collected at the same point.

Example 1: 5.08 Personal ID, 3.02 Social Security Number, 3.03 Date of Birth, 3.04 Race and Ethnicity, 3.06 Gender, 3.07 Veteran Status, and V1 Veteran's Information all exist at the same level/have a one-to-one relationship with one another. They may share a 5.01 Date Created, 5.02 Date Updated, and 5.07 User ID.

Example 2: 3.10 Project Start Date and 3.11 Project Exit Date both have a one-to-one relationship with 5.06 Enrollment ID but have different collection points. To evaluate timeliness of data entry, 3.10 Project Start Date and 3.11 Project Exit Date must have separate base metadata elements.

## Project Identifier, Personal ID, and Household ID

Because 3.10 Project Start Date initiates an enrollment, the creation of this data element is assumed to also create 5.06 Enrollment ID. Along with the 5.06 Enrollment ID, 3.10 Project Start Date must also be associated with 5.05 Project Identifier, 5.08 Personal ID, and 5.09 Household ID. The relationship of each of these metadata elements to 5.06 Enrollment ID is one-to-one. Every record for any enrollment-related data element (e.g., every data element requiring 5.06 Enrollment ID) is associated with a single project, client, and household through the 5.06 Enrollment ID.

|  |  |  |  |  | Collection Points |  |  | Required Metadata | Elements |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DE | Element | Record | Project | Update/ | Annual | Project | Post-Exit | Enrollment | Data |
|  |  | Creation | Start | Occurrence | Assess- | Exit |  | ID | Collection Stage |
|  |  |  |  | Point | ment |  |  |  |  |
| 3.01 | Name | × |  |  |  |  |  |  |  |
| 3.02 | Social Security Number | × |  |  |  |  |  |  |  |
| 3.03 | Date of Birth | × |  |  |  |  |  |  |  |
| 3.04 | Race and Ethnicity | × |  |  |  |  |  |  |  |
| 3.06 | Gender | × |  |  |  |  |  |  |  |
| 3.07 | Veteran Status | × |  |  |  |  |  |  |  |
| 3.08 | Disabling Condition |  | X |  |  |  |  | × |  |
| 3.10 | Project Start Date |  | × |  |  |  |  | × |  |
| 3.11 | Project Exit Date |  |  |  |  | × |  | × |  |
| 3.12 | Destination |  |  |  |  | × |  | × |  |
| 3.15 | Relationship to Head of |  | × |  |  |  |  | × |  |
|  | Household |  |  |  |  |  |  |  |  |
| 3.16 | Enrollment CoC |  | × |  |  |  |  | × | × |
| 3.20 | Housing Move-In Date |  |  | X (0 ... 1) |  |  |  | × |  |
| 3.917 | Prior Living Situation (A) and |  | × |  |  |  |  | × |  |
|  | (B) |  |  |  |  |  |  |  |  |
| 4.02 | Income and Sources |  | × | × | × | × |  | × | × |
| 4.03 | Non-Cash Benefits |  | X | × | X | × |  | × | × |
| 4.04 | Health Insurance |  | X | X | × | × |  | × | × |
| 4.05 | Physical Disability |  | X | X |  | × |  | × | × |
| 4.06 | Developmental Disability |  | X | × |  | × |  | × | × |
| 4.07 | Chronic Health Condition |  | X | X |  | × |  | × | × |
| 4.08 | HIV/AIDS |  | X | X |  | × |  | × | × |
| 4.09 | Mental Health Disorder |  | X | X |  | × |  | × | × |
| 4.10 | Substance Use Disorder |  | × | × |  | × |  | × | × |
| 4.11 | Domestic Violence |  | × | × |  |  |  | × | × |
| 4.12 | Current Living Situation |  |  | × |  |  |  | × |  |
| 4.13 | Date of Engagement |  |  | X (0 ... 1) |  |  |  | × |  |
| 4.14 | Bed-Night Date |  |  | × |  |  |  | × |  |
| 4.19 | Coordinated Entry |  |  | × |  |  |  |  |  |
|  | Assessment |  |  |  |  |  |  |  |  |
| 4.20 | Coordinated Entry Event |  |  | X |  |  |  | × |  |
| W1 | Services Provided – HOPWA |  |  | × |  |  |  | × |  |
| W2 | Financial Assistance – |  |  | × |  |  |  | × |  |
|  | HOPWA |  |  |  |  |  |  |  |  |
| W3 | Medical Assistance |  | X | X |  | × |  | × | X |
| W4 | T-Cell (CD4) and Viral Load |  | X | X | × | × |  | × | × |
| we | Housing Assessment at Exit |  |  |  |  | × |  | × |  |
| We | Prescribed Anti-Retroviral |  | X | X |  | × |  | × |  |
| C2 | Moving On |  |  | × |  |  |  | × |  |
| C3 | Youth Education Status |  | × |  |  | × |  | × | X |
| C4 | Translation Assistance |  | × |  |  |  |  | × |  |
|  | Needed |  |  |  |  |  |  |  |  |

| DE | Element | Record | Project | Update/ | Annual | Project | Post-Exit | Enrollment | Data |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Creation | Start | Occurrence Point | Assess- ment | Exit |  | ID | Collection Stage |
| bJ | Services Provided – PATH |  |  | × |  |  |  | × |  |
|  | Funded |  |  |  |  |  |  |  |  |
| ь2 | Referrals Provided – PATH |  |  | × |  |  |  | × |  |
| ь3 | PATH Status |  |  | X (0 ... 1) |  |  |  | × |  |
| P4 | Connection with SOAR |  | × | × | × | × |  | × | × |
| RT | Referral Source |  | X |  |  |  |  | × |  |
| R2 | RHY-BCP Status |  | X | X (0 ... 1) |  |  |  | × |  |
| R3 | Sexual Orientation |  | X |  |  |  |  | × |  |
| R4 | Last Grade Completed |  | × |  |  | X |  | × | X |
| R5 | School Status |  | × |  |  | × |  | × | × |
| R6 | Employment Status |  | X |  |  | × |  | × | X |
| R7 | General Health Status |  | X |  |  | × |  | × | × |
| R8 | Dental Health Status |  | X |  |  | X |  | × | × |
| R9 | Mental Health Status |  | X |  |  | × |  | × | × |
| R10 | Pregnancy Status |  | X | X |  |  |  | × | X |
| R11 | Formerly a Ward of Child |  | X |  |  |  |  | × |  |
|  | Welfare or Foster Care |  |  |  |  |  |  |  |  |
|  | Agency |  |  |  |  |  |  |  |  |
| R12 | Formerly a Ward of Juvenile |  | × |  |  |  |  | × |  |
|  | Justice System |  |  |  |  |  |  |  |  |
| R13 | Family Issues |  | × |  |  |  |  | × |  |
| R14 | RHY Service Connections |  |  | X |  |  |  | × |  |
| ૪૩૨ | Commercial Sexual |  |  |  |  | × |  | × |  |
|  | Exploitation |  |  |  |  |  |  |  |  |
| RTE | Labor Exploitation |  |  |  |  | × |  | × |  |
| R17 | Project Completion Status |  |  |  |  | × |  | × |  |
| R18 | Counseling |  |  |  |  | × |  | × |  |
| لاده | Safe and Appropriate Exit |  |  |  |  | × |  | × |  |
| R20 | Aftercare Plans |  |  |  |  |  | X | × |  |
| V1 | Veteran's Information | X |  |  |  |  |  | X |  |
| V2 | Services Provided – SSVF |  |  | X |  |  |  | × |  |
| /3 | Financial Assistance – SSVF |  |  | X |  |  |  | × |  |
| V4 | Percent of AMI (SSVF |  | X |  |  |  |  | × |  |
|  | Eligibility) |  |  |  |  |  |  |  |  |
| VE | VAMC Station Number |  | X |  |  |  |  | × |  |
| V7 | HP Targeting Criteria |  | X |  |  |  |  | X |  |
| V8 | HUD-VASH Voucher Tracking |  | X | X |  | × |  | X | X |
| Wa | HUD-VASH Exit Information |  |  |  |  | × |  | × |  |

## Appendix A - Living Situation Information

#### Living Situation Option List

| Field # |  | Prior Living | Current Living |  |
| --- | --- | --- | --- | --- |
|  | Response | Situation | Situation | Destination |
| Header | Homeless Situations (100-199) | (3.917) | (4.12) | (3.12) |
|  | Place not meant for habitation (e.g., a vehicle, an abandoned |  |  |  |
| JIE | building, bus/train/subway station/airport or anywhere outside) | X | X | X |
|  | Emergency shelter, including hotel or motel paid for with |  |  |  |
| JOJ | emergency shelter voucher, Host Home shelter | X | X | × |
| 118 | Safe Haven | X | X | × |
| Header | Institutional Situations (200-299) |  |  |  |
| 212 | Foster care home or foster care group home | X | X | X |
| 206 | Hospital or other residential non-psychiatric medical facility | X | X | × |
| 207 | Jail, prison, or juvenile detention facility | X | X | × |
| 225 | Long-term care facility or nursing home | X | × | X |
| 204 | Psychiatric hospital or other psychiatric facility | X | × | × |
| 205 | Substance abuse treatment facility or detox center | X | × | × |
| Header | Temporary Housing Situations (300-399) |  |  |  |
| 302 | Transitional housing for homeless persons (including homeless | X | X | X |
|  | youth) |  |  |  |
| 329 | Residential project or halfway house with no homeless criteria | X | X | X |
| 314 | Hotel or motel paid for without emergency shelter voucher | X | X | × |
| 332 | Host Home (non-crisis) | X | X | × |
| 312 | Staying or living with family, temporary tenure (e.g., room, |  |  | X |
|  | apartment, or house) |  |  |  |
|  | Staying or living with friends, temporary tenure (e.g., room, |  |  |  |
| 313 | apartment, or house) |  |  | X |
| 327 | Moved from one HOPWA funded project to HOPWA TH |  |  | × |
| 336 | Staying or living in a friend's room, apartment, or house | X | × |  |
| 332 | Staying or living in a family member's room, apartment, or house | X | × |  |
| Header | Permanent Housing situation (400 -499) |  |  |  |
| 422 | Staying or living with family, permanent tenure |  |  | × |
| 423 | Staying or living with friends, permanent tenure |  |  | × |
| 426 | Moved from one HOPWA funded project to HOPWA PH |  |  | X |
| 410 | Rental by client, no ongoing housing subsidy | X | X | × |
| 435 | Rental by client, with ongoing housing subsidy | × | × | X |
| 421 | Owned by client, with ongoing housing subsidy | X | X | × |
| 411 | Owned by client, no ongoing housing subsidy | X | X | X |
| Header | Other (1-99) |  |  |  |
| 30 | No exit interview completed |  |  | × |
| 17 | Other |  | X | X |
| 24 | Deceased |  |  | X |
| 37 | Worker unable to determine |  | × |  |
| 8 | Client doesn't know | X | X | X |
| 9 | Client prefers not to answer | X | X | × |
| ਰੇਰੇ | Data not collected | X | × | X |

#### Subsidy Types - Dependent Field, relies on Living Situation = 435

| Field # | Response |
| --- | --- |
| 428 | GPD TIP housing subsidy |
| 418 | VASH housing subsidy |
| 431 | RRH or equivalent subsidy |
| 433 | HCV voucher (tenant or project based) (not dedicated) |
| 434 | Public housing unit |
| 420 | Rental by client, with other ongoing housing subsidy |
| 436 | Housing Stability Voucher |
| 437 | Family Unification Program Voucher (FUP) |
| 438 | Foster Youth to Independence Initiative (FYI) |
| 438 | Permanent Supportive Housing |
| 440 | Other permanent housing dedicated for formerly homeless persons |

This material is based upon work supported, in whole or in part, by Federal award number H-20-NP-VA-001 awarded to ICF by the U.S. Department of Housing and Urban Development for NHDAP-related technical assistance. The substance and findings of the work are dedicated to the public. Neither the United States Government, nor any of its employees, makes any warranty, express

or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed, or represents that its use would not infringe privately-owned rights. Reference herein to any individuals, agencies, companies, process, services, service by trade name, trademark, manufacturer, or otherwise does not constitute or imply an endorsement, recommendation, or favoring by the author(s), contributor(s), the U.S. Government or any agency thereof. Opinions contained herein are those of the author(s) and do not necessarily reflect the official position of, or a position that is endorsed by, HUD or any Federal agency.

