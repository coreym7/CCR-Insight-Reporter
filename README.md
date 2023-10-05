# CCR-Insight-Reporter
**This script is still in progress and not yet functional**

Calculates CCR data according to MSIP 6 from various separate reports
The general report for this data has been named "starship" and will be referenced as this at different points. 

**The following is a review of a spreadsheet that performed the CCR calculations manually**
**Overview of Starship**
The spreadsheet represents a comprehensive analysis of student performance based on multiple assessments. Each student has a unique identifier (student ID), which is used to pull corresponding data from several assessment source sheets including ACT, ASVAB, Workkeys, AP, DC, IRC, AP Exam, and PLTW Exam.
In the output sheet "MSIP 5", each student's scores and grades from these different assessments are brought together. The sheet comprises a multitude of columns but starting from the "CCR 1-3 Total" and moving to the right, formulas are used to process and analyze the data.
**Key Columns for Calculations:**
1.	CCR 1-3 Total: Contains the maximum weighted value from ACT, ASVAB, and Workkeys.
2.	CCR 4 Total: Contains the maximum weighted value from Semester 1 (S1) and Semester 2 (S2) AP Grade, S1 and S2 DC Grade, AP Exam Score, IRC Exam, and PLTW Exam Score.
All the other columns between and after these two represent scores from different assessments, and their respective weights.
**Weighting and Formulas**
Each type of score or grade gets a weight assigned according to a specific range of values. Here's the rundown for each of them:
1.	ACT: Weight = 0.25 if score < 18; 0.75 if 18 ≤ score < 22; 1 if 22 ≤ score < 26; 1.25 if score ≥ 26.
2.	ASVAB: Weight = 0.25 if score < 30; 0.75 if 30 ≤ score < 63; 1 if 63 ≤ score < 88; 1.25 if score ≥ 88.
3.	Workkeys: Weight = 0.25 if score < 4; 0.75 if score = 4; 1 if score = 5; 1.25 if score ≥ 6.
4.	Semester 1 (S1) and Semester 2 (S2) AP Grade & DC Grade: Weight = 1 if grade is one of "A+", "A", "A-", "B+", "B", "B-"; 0 for any other grade.
5.	AP Exam: Weight = 1.25 if score ≥ 3; 0 otherwise.
6.	IRC Exam: Weight = 1 if exam result = "P" (Pass); 0 otherwise.
7.	PLTW Exam: Weight = 1 if score ≥ 6; 0 otherwise.
**Based on these weights:**
•	CCR 1-3 Total is the maximum of (ACT Weight, ASVAB Weight, Workkeys Weight)
•	CCR 4 Total is the maximum of (S1 AP Weight, S1 DC Weight, S2 AP Weight, S2 DC Weight, AP Exam Weight, IRC Exam Weight, PLTW Exam Weight)



**Limitations of calculating this in excel**
1.	The way Excel pulls the grades/scores from the source sheets is only pulling the first entry it finds, if multiple entries for a single student in any of these types of scores are present, it is not taking the highest. The highest score is needed for proper calculations of CCR data. Excel is not ideal to achieve this but could be done in the script/program I write to create this report. 
2. The reports done in excel seem to sometimes be limited to a single year of data, ideally CCR should be calculated using the prior 4 or even 5 years to ensure the capture of a student that may have been held back a year is included.


**The following is the setup and expectations of the script for report naming and column headings - this may need updated as work progresses with this script**
file names: (These will be saved within a folder named "dataSources" that will be located in the same location as the script will be saved)

ACT_CY.csv - ACT scores from current school year
ACT_PY1.csv - ACT scores from school year 1 years ago
ACT_PY2.csv - ACT scores from school year 2 years ago
ACT_PY3.csv - ACT scores from school year 3 years ago
ACT_PY4.csv - ACT scores from school year 4 years ago

ACT Column Headers
StudentNumber	Name	Current School	Test Date	Test Grade Level	Term ID	Test ID	Test Name	Score Name	Num Score	Pct Score	Alpha Score
composite score from "Score Name" is used? 

AP_School1_PY1.csv - School1 AP scores from school year 1 year go
AP_School1_PY2.csv - School1 AP scores from school year 2 year go
AP_School1_PY3.csv - School1 AP scores from school year 3 year go

AP_School2_PY1.csv - School2 AP scores from school year 1 year go
AP_School2_PY2.csv - School2 AP scores from school year 2 year go
AP_School2_PY3.csv - School2 AP scores from school year 3 year go

AP_School3_PY1.csv - School3 AP scores from school year 1 year go
AP_School3_PY2.csv - School3 AP scores from school year 2 year go
AP_School3_PY3.csv - School3 AP scores from school year 3 year go

AP Column headers:
AP Number / AP ID	Last Name	First Name	Middle Initial	Student Street Address 1	Student Street Address 2	Student Street Address 3	Student State	Student Zip Code	Student Province	Student International Postal Code	Student Country Code	Gender	Date of Birth	Filler	School ID	Grade Level	Filler	Ethnic Group 2015 and Prior	Filler	Best Language	Previous AI Year 1	Previous AI Code 1	Previous AI Year 2	Previous AI Code 2	Award Type 1	Award Year 1	Award Type 2	Award Year 2	Award Type 3	Award Year 3	Award Type 4	Award Year 4	Award Type 5	Award Year 5	Award Type 6	Award Year 6	AI Code	AI Institution Name	AI Street Address 1	AI Street Address 2	AI Street Address 3	AI State	AI Zip Code	AI Province	AI International Postal Code	AI Country Code	College Code	Contact Name	DI Institution Name	DI Street Address 1	DI Street Address 2	DI Street Address 3	DI State	DI Zip Code	DI Province	DI International Postal Code	DI Country Code	Admin Year 01	Exam Code 01	Exam Grade 01	Irregularity Code #1 01	Irregularity Code #2 01	Class Section Code 01	Admin Year 02	Exam Code 02	Exam Grade 02	Irregularity Code #1 02	Irregularity Code #2 02	Class Section Code 02	Admin Year 03	Exam Code 03	Exam Grade 03	Irregularity Code #1 03	Irregularity Code #2 03	Class Section Code 03	Admin Year 04	Exam Code 04	Exam Grade 04	Irregularity Code #1 04	Irregularity Code #2 04	Class Section Code 04	Admin Year 05	Exam Code 05	Exam Grade 05	Irregularity Code #1 05	Irregularity Code #2 05	Class Section Code 05	Admin Year 06	Exam Code 06	Exam Grade 06	Irregularity Code #1 06	Irregularity Code #2 06	Class Section Code 06	Admin Year 07	Exam Code 07	Exam Grade 07	Irregularity Code #1 07	Irregularity Code #2 07	Class Section Code 07	Admin Year 08	Exam Code 08	Exam Grade 08	Irregularity Code #1 08	Irregularity Code #2 08	Class Section Code 08	Admin Year 09	Exam Code 09	Exam Grade 09	Irregularity Code #1 09	Irregularity Code #2 09	Class Section Code 09	Admin Year 10	Exam Code 10	Exam Grade 10	Irregularity Code #1 10	Irregularity Code #2 10	Class Section Code 10	Admin Year 11	Exam Code 11	Exam Grade 11	Irregularity Code #1 11	Irregularity Code #2 11	Class Section Code 11	Admin Year 12	Exam Code 12	Exam Grade 12	Irregularity Code #1 12	Irregularity Code #2 12	Class Section Code 12	Admin Year 13	Exam Code 13	Exam Grade 13	Irregularity Code #1 13	Irregularity Code #2 13	Class Section Code 13	Admin Year 14	Exam Code 14	Exam Grade 14	Irregularity Code #1 14	Irregularity Code #2 14	Class Section Code 14	Admin Year 15	Exam Code 15	Exam Grade 15	Irregularity Code #1 15	Irregularity Code #2 15	Class Section Code 15	Admin Year 16	Exam Code 16	Exam Grade 16	Irregularity Code #1 16	Irregularity Code #2 16	Class Section Code 16	Admin Year 17	Exam Code 17	Exam Grade 17	Irregularity Code #1 17	Irregularity Code #2 17	Class Section Code 17	Admin Year 18	Exam Code 18	Exam Grade 18	Irregularity Code #1 18	Irregularity Code #2 18	Class Section Code 18	Admin Year 19	Exam Code 19	Exam Grade 19	Irregularity Code #1 19	Irregularity Code #2 19	Class Section Code 19	Admin Year 20	Exam Code 20	Exam Grade 20	Irregularity Code #1 20	Irregularity Code #2 20	Class Section Code 20	Admin Year 21	Exam Code 21	Exam Grade 21	Irregularity Code #1 21	Irregularity Code #2 21	Class Section Code 21	Admin Year 22	Exam Code 22	Exam Grade 22	Irregularity Code #1 22	Irregularity Code #2 22	Class Section Code 22	Admin Year 23	Exam Code 23	Exam Grade 23	Irregularity Code #1 23	Irregularity Code #2 23	Class Section Code 23	Admin Year 24	Exam Code 24	Exam Grade 24	Irregularity Code #1 24	Irregularity Code #2 24	Class Section Code 24	Admin Year 25	Exam Code 25	Exam Grade 25	Irregularity Code #1 25	Irregularity Code #2 25	Class Section Code 25	Admin Year 26	Exam Code 26	Exam Grade 26	Irregularity Code #1 26	Irregularity Code #2 26	Class Section Code 26	Admin Year 27	Exam Code 27	Exam Grade 27	Irregularity Code #1 27	Irregularity Code #2 27	Class Section Code 27	Admin Year 28	Exam Code 28	Exam Grade 28	Irregularity Code #1 28	Irregularity Code #2 28	Class Section Code 28	Admin Year 29	Exam Code 29	Exam Grade 29	Irregularity Code #1 29	Irregularity Code #2 29	Class Section Code 29	Admin Year 30	Exam Code 30	Exam Grade 30	Irregularity Code #1 30	Irregularity Code #2 30	Class Section Code 30	Date Grades Released to College	Date of Last Student Update	Date of this report	Student Identifier	Race Ethnicity Student Response 2016 and Forward	Derived Aggregate Race Ethnicity 2016 and Forward

Exam Grade Columns contain grades for each student in a single row

ASVAB_PY1.csv - ASVAB scores from school year 1 year ago
ASVAB_PY2.csv - ASVAB scores from school year 2 year ago
ASVAB_PY3.csv - ASVAB scores from school year 3 year ago
ASVAB_PY4.csv - ASVAB scores from school year 4 year ago

ASVAB column headers
StudentNumber	Name	Current School	Test Date	Test Grade Level	Term ID	Test ID	Test Name	Score Name	Num Score	Pct Score	Alpha Score
EntranceScore is score evaluated


workkeys_PY1.csv - work key scores from school year 1 year ago
workkeys_PY2.csv - work key scores from school year 2 year ago
workkeys_PY3.csv - work key scores from school year 3 year ago
workkeys_PY4.csv - work key scores from school year 4 year ago

work keys Column headers:
StudentNumber	Name	Current School	Test Date	Test Grade Level	Term ID	Test ID	Test Name	Score Name	Num Score	Pct Score	Alpha Score
Num score or alpha score for calculations?

IRC.csv - IRC scores for all students

AP/DC naming to be determined after reports are exported

Output file
Starship_<append_date>.xlsx

Column headers:
Student Number	MOSIS Number	Attending School	Reporting School	Student Name	Grade Level	CCR 1-3 Total	CCR 4 Total	ACT	ACT Weight	ASVAB	ASVAB Weight	Workkeys	WorkKeys Weight	S1 AP Grade	S1 AP Weight	S1 DC Grade	S1 DC Weight	S2 AP Grade	S2 AP Weight	S2 DC Grade	S2 DC Weight	AP Exam Score	AP Exam Weight	IRC Exam	IRC Exam Weight	PLTW Exam Score	PLTW Exam Weight

Most of these values will be pulled from the raw data files listed above, any columns that mention weight, will have added calculations later. For the S1 & S2 for both AP and DC, this gets tricky. When looking at each file, there should be two corresponding grades, from the same session or semester. What will be put in for S1 and S2 on the output file is the year (each file is a year) that had the highest average Grade between the two semesters, for each student. 

CCR 1-3 TOtal, will be another calculation done after weighted calculations are added, the same for CCR 4 Total. 

Once this intermediate output file is made, a pivot table should be created that shows # of students, sum of the CCR1-3 total, and the sum of the ccr 4 total, grouped by reporting school, and then attending school. Ideally this pivot table should have a drop down option to select what grade level is being viewed or to view all. 
