------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
CODEBOOK FOR THE 2023 SURVEY OF HOUSEHOLD ECONOMICS AND DECISIONMAKING
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
The codebook serves as the principal guide to the variables included on the public
version of the 2023 Survey of Household Economics and Decisionmaking (SHED) data
set. However, not every variable included in the survey is included in the public
use data set. For example, the data set does NOT include most variables related to
details of geography or free-text responses.

The SHED is sponsored by the Board of Governors of the Federal Reserve System. Data
for the 2023 SHED were collected by Ipsos using their online probability based
KnowledgePanel.

For a general overview of the 2023 SHED and a detailed discussion of the survey
methods, see Alicia Lloro, Ellen Merry, Jeff Larrimore, Zofsha Merchant, Fatimah
Shaalan, Anna Tranfaglia, "Economic Well-Being of U.S. Households in 2023,
Federal Reserve Board." The variables in the codebook are generally in the order
in which they were asked during the survey. For a copy of the survey questionnaire,
see the Supplemental Appendixes to the "Report on the Economic Well-Being of U.S.
Households in 2023.

Please cite the use of SHED data as: Board of Governors of the Federal Reserve
System Survey of Household Economics and Decisionmaking [dataset] (Washington:
Board of Governors, 2024), https:// doi.org/10.17016/datasets.002

------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
ANALYSIS WEIGHTS
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
Weights play a critical role in interpreting the survey data and allow the sample
population to match the U.S. population based on observable characteristics. The
public use dataset contains two sets of weights, and users should consider the
appropriate weights for their analysis.

The first set of weights  ("weight" and  "weight_pop")  should be used  when analyzing
single year cross-sections of data for all respondents. The second set of weights
("panel_weight" and "panel_weight_pop") should be used when analyzing respondents
who took both the 2022 and 2023 survey.

The sample weight, "weight," is most commonly used and is the weight used for
statistics published in the "Economic Well-Being of U.S. Households in 2023." The
population weight, "weight_pop," can be used for estimating population totals, as
it sums to the total U.S. population from March 2023 Current Population Survey
(CPS). Either weight will allow for the entire sample to reflect the observable
characteristics of the U.S. adult population.

------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
DEMOGRAPHIC PROFILE VARIABLES
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
In addition to the questions asked on the SHED, the data set includes demographic
profile variables that were collected by Ipsos prior to respondents receiving the
SHED. These demographic profile variables are typically labeled with the prefix
“pp” in the data file with some exceptions and in the variable descriptions below.
In some cases, such as the highest level of education, similar questions were asked
in these demographic profile surveys and in the SHED.  In these cases, the answers
to the SHED questions were used for the "Economic Well-Being of U.S. Households in
2023" if they were available.

------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
VARIABLE DEFINITIONS
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
CaseID 2023
CaseID
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [1,11488]

Unique values: 11,400

Units: 1

Missing .: 0/11,400

Mean: 5744.17
Std. dev.: 3318.07

Percentiles:

10%
1147.5

25%
2871.5

50%
5740.5

75%

90%
8616.5  10345.5

------------------------------------------------------------------------------------
CaseID from 2022 SHED Survey
caseid2022
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [1,11753]

Unique values: 3,870

Units: 1

Missing .: 7,530/11,400

Mean: 5696.22
Std. dev.: 3172.99

Percentiles:

10%
1261

25%
3032

50%
5772.5

75%

90%
8283  10075.5

------------------------------------------------------------------------------------
CaseID from 2021 SHED Survey
caseid2021
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [4,48180]

Unique values: 3,295

Units: 1

Missing .: 8,105/11,400

Mean: 7462.46
Std. dev.: 8437.58

Percentiles:

10%
1232

25%
2936

50%
5764

75%
8494

90%
10905

------------------------------------------------------------------------------------
CaseID from 2020 SHED Survey
caseid2020
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [6,47170]

Unique values: 2,716

Units: 1

Missing .: 8,684/11,400

Mean:  7129.1
Std. dev.: 8192.14

Percentiles:

10%
1120

25%
2884

50%
5330.5

75%
8076

90%
10688

------------------------------------------------------------------------------------
CaseID from 2019 SHED Survey
caseid2019
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [5,49970]

Unique values: 2,860

Units: 1

Missing .: 8,540/11,400

Mean: 9899.04
Std. dev.: 11273.5

Percentiles:

10%
1367

25%
3409.5

50%
6343

75%
9670

90%
33107

------------------------------------------------------------------------------------
Duration (in seconds)
duration
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [406,1045352]

Unique values: 3,558

Units: 1

Missing .: 0/11,400

Mean: 12691.8
Std. dev.:  63532

Percentiles:

10%
756

25%
935

50%
1228

75%
1824.5

90%
4777.5

------------------------------------------------------------------------------------
weight

Post-stratification weight - Main qualified
respondents scaled to sample size

------------------------------------------------------------------------------------

Type: Numeric (double)

Range: [.1662,3.8729]

Unique values: 2,639

Units: .0001
Missing .: 0/11,400

Mean:

1
Std. dev.: .465858

Percentiles:

10%
.5546

25%
.7056

50%
.9122

75%
1.1697

90%
1.5456

------------------------------------------------------------------------------------
weight_pop

Post-stratification weight - Main qualified
respondents scaled to U.S. population

------------------------------------------------------------------------------------

Type: Numeric (double)

Range: [3758.7506,87606.462]

Unique values: 2,849

Units: .0001
Missing .: 0/11,400

Mean: 22620.2
Std. dev.: 10537.8

Percentiles:

10%

25%
12544.2  15959.7

50%

90%
20635  26458.1  34961.7

75%

------------------------------------------------------------------------------------
panel_weight

Post-stratification weight - Main recontact
respondents scaled to sample size

------------------------------------------------------------------------------------

Type: Numeric (double)

Range: [.1062,3.2299]

Unique values: 2,331

Units: .0001

Missing .: 7,530/11,400

Mean:

1
Std. dev.: .416397

Percentiles:

10%
.60215

25%
.7179

50%
.90285

75%
1.2335

90%
1.5143

------------------------------------------------------------------------------------
panel_weight_pop

Post-stratification weight - Main recontact

------------------------------------------------------------------------------------

respondents scaled to U.S. population

Type: Numeric (double)

Range: [7073.7295,215218.62]

Units: .0001

Unique values: 2,562

Missing .: 7,530/11,400

Mean: 66633.2
Std. dev.:  27746

Percentiles:

10%

75%
40125.6  47838.9  60158.1  82194.2

25%

50%

90%
100902

------------------------------------------------------------------------------------
Is R a KP laptop user?
xlaptop
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: LABA

Range: [1,2]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

336
11,064

1  Yes
2  No

------------------------------------------------------------------------------------
My spouse or partner - First, do each of the
L0_a
following people currently live with you?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: L0_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

3,869
7,531

0  No
1  Yes

------------------------------------------------------------------------------------
L0_b

My child(ren) under age 18 - First, do each
of  the following people currently live with
you?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: L0_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

8,744
2,656

0  No
1  Yes

------------------------------------------------------------------------------------
My adult child(ren) age 18 or older - First,
L0_c
do each of the following people currently
live with you?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: L0_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,424
1,976

0  No
1  Yes

------------------------------------------------------------------------------------
L0_d

My parent(s) - First, do each of the
following people currently live with you?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: L0_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,159
1,241

0  No
1  Yes

------------------------------------------------------------------------------------
L0_e

Other individuals - First, do each of the
following people currently live with you?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: L0_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,968
1,432

0  No
1  Yes

------------------------------------------------------------------------------------
Are the adult children (who are age 18 or older) who live with you:
L0A
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: L0A

Range: [1,2]

Unique values: 2

Units: 1

Missing .: 9,424/11,400

Tabulation: Freq.  Numeric  Label

515

1  All currently enrolled in

1,461

9,424

school

2  One or more not currently

enrolled in school

.

------------------------------------------------------------------------------------
Your brother(s) or sister(s) - Are the people living with you:
L0B_a
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: L0B_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,968/11,400

Tabulation: Freq.  Numeric  Label

855
577
9,968

0  No
1  Yes
.

------------------------------------------------------------------------------------
Other relatives - Are the people living with you:
L0B_b
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: L0B_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,968/11,400

Tabulation: Freq.  Numeric  Label

915
517
9,968

0  No
1  Yes
.

------------------------------------------------------------------------------------
Other people not related to you - Are the people living with you:
L0B_c
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: L0B_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,968/11,400

Tabulation: Freq.  Numeric  Label

901
531
9,968

0  No
1  Yes
.

------------------------------------------------------------------------------------
L0C

How many children do you have who are under
age 18 and currently live with you?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: L0C, but 4 nonmissing values are not labeled

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 8,744/11,400

Tabulation: Freq.  Numeric  Label

1,129
957
368
126
76
8,744

1
2
3
4
5  5 or more
.

------------------------------------------------------------------------------------
How old is your (youngest) child that lives with you?
L0E
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: L0E

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 8,744/11,400

Tabulation: Freq.  Numeric  Label

569
414
896
777
8,744

1  0 to 2 years old
2  3 to 5
3  6 to 12
4  13 to 17
.

------------------------------------------------------------------------------------
Overall, which one of the following best
B2
describes how well you are managing
financially these days?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: B2

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

939
2,137
4,450
3,874

1  Finding it difficult to get by
2  Just getting by
3  Doing okay
4  Living comfortably

------------------------------------------------------------------------------------
Compared to 12 months ago, would you say that
B3

------------------------------------------------------------------------------------

you (and your family) are better off,
the same, or worse off financially?

Type: Numeric (byte)

Label: B3

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

814
2,878
5,527
1,736
445

1  Much worse off
2  Somewhat worse off
3  About the same
4  Somewhat better off
5  Much better off

------------------------------------------------------------------------------------
B6

Think of your parents when they were your
age. Would you say you (and your family)  are
better, the same, or worse off financially
than  they were?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: B6

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

930
1,968
2,508
3,285
2,709

1  Much worse off
2  Somewhat worse off
3  About the same
4  Somewhat better off
5  Much better off

------------------------------------------------------------------------------------
B7_a
------------------------------------------------------------------------------------

In your community - How would you rate economic conditions today:

Type: Numeric (byte)

Label: B7_A

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,916
4,660
4,445
379

1  Poor
2  Only fair
3  Good
4  Excellent

------------------------------------------------------------------------------------
B7_b
------------------------------------------------------------------------------------

In this country - How would you rate economic conditions today:

Type: Numeric (byte)

Label: B7_B

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

3,730
5,066
2,484
120

1  Poor
2  Only fair
3  Good
4  Excellent

------------------------------------------------------------------------------------
X11 None selected
X11_none
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: X11_NONE

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

8,067
3,333

0  No
1  Yes

------------------------------------------------------------------------------------
Currently, how many hours per week do you use paid childcare?
CG1
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: CG1

Range: [0,4]

Unique values: 5

Units: 1

Missing .: 9,521/11,400

Tabulation: Freq.  Numeric  Label

1,336
58
70
86
329
9,521

0  None
1  1 to 4 hours
2  5 to 9 hours
3  10 to 19 hours
4  20 hours or more
.

------------------------------------------------------------------------------------
CG2

How much do you pay per week for childcare (in
total for all of your children)?

------------------------------------------------------------------------------------

Type: Numeric (int)

Label: CG2, but 139 nonmissing values are not labeled

Range: [0,5000]

Unique values: 139

Units: 1

Missing .: 10,857/11,400

Examples: .
.
.
.

------------------------------------------------------------------------------------
When it comes to taking care of your children
CG3
when they are at home, which of the following
statements best describes the caretaking
responsibilities?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: CG3

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 9,776/11,400

Tabulation: Freq.  Numeric  Label

566

373

685

1  I am usually the primary

caretaker

2  My spouse/partner is usually

the primary caretaker

3  My spouse/partner and I equally

share caretaking
responsibilities

9,776

.

------------------------------------------------------------------------------------
Do you regularly provide unpaid help or take
CG4
care of an adult relative or friend who needs
assistance due to aging, disability, or
illness?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: CG4

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,496
1,904

0  No
1  Yes

------------------------------------------------------------------------------------
Your parent- Do you regularly provide unpaid
CG5_a
help or care to each of the following people
due to aging, disability, or illness?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: CG5_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,496/11,400

Tabulation: Freq.  Numeric  Label

985
919
9,496

0  No
1  Yes
.

------------------------------------------------------------------------------------
CG5_b

Your spouse's or partner's parent - Do
you regularly provide unpaid help or
care to each of the following people
due to aging, disability, or illness?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: CG5_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,148/11,400

Tabulation: Freq.  Numeric  Label

934
318
10,148

0  No
1  Yes
.

------------------------------------------------------------------------------------
Your spouse or partner- Do you regularly
CG5_c
provide unpaid help or care to each of
the  following people due to aging,
disability, or illness?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: CG5_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,148/11,400

Tabulation: Freq.  Numeric  Label

969
283
10,148

0  No
1  Yes
.

------------------------------------------------------------------------------------
CG5_d

An adult child (age 18 or older) - Do you
Regularly  provide unpaid help or care to
each  of the following people due to aging,
disability, or illness?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: CG5_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,496/11,400

Tabulation: Freq.  Numeric  Label

1,617
287
9,496

0  No
1  Yes
.

------------------------------------------------------------------------------------
CG5_e

Another relative - Do you regularly provide
unpaid help or care to each of the following
people due to aging, disability, or illness?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: CG5_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,496/11,400

Tabulation: Freq.  Numeric  Label

1,450
454
9,496

0  No
1  Yes
.

------------------------------------------------------------------------------------
CG5_f

A friend or neighbor - Do you regularly
provide  unpaid help or care to each of the
following people due to aging, disability,
or illness?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: CG5_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,496/11,400

Tabulation: Freq.  Numeric  Label

1,548
356
9,496

0  No
1  Yes
.

------------------------------------------------------------------------------------
About how often do you provide unpaid help or
CG6
care to an adult relative or friend who needs
assistance due to aging, disability, or
illness?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: CG6

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 9,496/11,400

Tabulation: Freq.  Numeric  Label
1  Daily
2  Several days per week
3  Several days per month
4  Once per month
5  Less than once per month
.

657
478
559
129
81
9,496

------------------------------------------------------------------------------------
Last month, did you do any work for either pay or profit?
D1A
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D1A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

4,813
6,587

0  No
1  Yes

------------------------------------------------------------------------------------
D4

Last month, did you have more than one job,
including part time, evening or weekend work?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D4

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 4,813/11,400

Tabulation: Freq.  Numeric  Label

5,384
1,203
4,813

0  No
1  Yes
.

------------------------------------------------------------------------------------
D48

(Thinking about all your jobs, do/Do) you
usually work 35 hours or more per week?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D48

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 4,813/11,400

Tabulation: Freq.  Numeric  Label

1,395
5,192
4,813

0  No
1  Yes
.

------------------------------------------------------------------------------------
Thinking about your main job (where you earn
D3B
the most money), do you usually work 35 hours
or more per week?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D3B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,421/11,400

Tabulation: Freq.  Numeric  Label

104

0  No

875
10,421

1  Yes
.

------------------------------------------------------------------------------------
At any time during the past month, did you want to work (more hours)?
D1E
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D1E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

8,090
3,310

0  No
1  Yes

------------------------------------------------------------------------------------
Could not find (more) work - Did each of the
D22_a
following contribute to you (not working/working
less than 35 hours per week) in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D22_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 5,192/11,400

Tabulation: Freq.  Numeric  Label

5,342
866
5,192

0  No
1  Yes
.

------------------------------------------------------------------------------------
D22_b

Full-time workweek less than 35 hours - Did
each of the following contribute to you (not
working/working  less than 35 hours per week)
in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D22_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,005/11,400

Tabulation: Freq.  Numeric  Label

1,093
302
10,005

0  No
1  Yes
.

------------------------------------------------------------------------------------
Childcare - Did each of the following contribute
D22_c
to you (not working/working less than 35 hours
per week) in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D22_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 5,192/11,400

Tabulation: Freq.  Numeric  Label

5,854
354
5,192

0  No
1  Yes
.

------------------------------------------------------------------------------------
D22_d

Caregiving for an elderly, disabled, or sick

------------------------------------------------------------------------------------

adult - Did each of the following contribute to
you (not working/working less than 35 hours per
week) in the last month?

Type: Numeric (byte)

Label: D22_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 5,192/11,400

Tabulation: Freq.  Numeric  Label

5,770
438
5,192

0  No
1  Yes
.

------------------------------------------------------------------------------------
D22_e

Other family or personal obligations - Did
each of the following contribute to you (not
working/working less than 35 hours per week)
in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D22_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 5,192/11,400

Tabulation: Freq.  Numeric  Label

5,262
946
5,192

0  No
1  Yes
.

------------------------------------------------------------------------------------
D22_f

Would lose access to unemployment benefits or
other government programs - Did each of the
following contribute to you
(not working/working less than 35 hours per
week) in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D22_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 5,192/11,400

Tabulation: Freq.  Numeric  Label

5,830
378
5,192

0  No
1  Yes
.

------------------------------------------------------------------------------------
Health limitations or disability- Did each of
D22_g
the following contribute to you
(not working/working  less than 35 hours per

week) in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D22_G

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 5,192/11,400

Tabulation: Freq.  Numeric  Label

4,673
1,535
5,192

0  No
1  Yes
.

------------------------------------------------------------------------------------
D22_h

In school or training - Did each of the
following contribute to you (not working/working
less than 35 hours per week) in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D22_H

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 5,192/11,400

Tabulation: Freq.  Numeric  Label

5,795
413
5,192

0  No
1  Yes
.

------------------------------------------------------------------------------------
D22_i

Retired - Did each of the following
contribute to you (not working/working less
than 35 hours per week) in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D22_I

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 5,192/11,400

Tabulation: Freq.  Numeric  Label

2,876
3,332
5,192

0  No
1  Yes
.

------------------------------------------------------------------------------------
[Think about your main job (the job from which
D3A
you earned the most money in the past month).
In  this job, were you working/Did you work]
for someone else, were you self-employed, or
something else?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D3A

Range: [0,2]

Unique values: 3

Units: 1

Missing .: 4,813/11,400

Tabulation: Freq.  Numeric  Label

5,624
728

235
4,813

0  Working for someone else
1  Self-employed (working for

myself)

2  Other work arrangement
.

------------------------------------------------------------------------------------
I can choose what tasks I work on - How often
D28_a
do each of these statements describe your
work situation (at your main job)?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D28_A

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 5,776/11,400

Tabulation: Freq.  Numeric  Label
1  Never
2  Rarely
3  Sometimes

704
1,042
1,929

1,447
502
5,776

4  Often
5  Always
.

------------------------------------------------------------------------------------
D28_b

I can choose how I complete tasks at work -
How often do each of these statement describe
your work situation (at your main job)?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D28_B

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 5,776/11,400

Tabulation: Freq.  Numeric  Label
1  Never
2  Rarely
3  Sometimes
4  Often
5  Always
.

402
517
1,535
2,046
1,124
5,776

------------------------------------------------------------------------------------
(Still thinking about your main job, do/Do) you
D30
normally start and end work around the same
time each day that you work, or does it vary?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D30

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 5,776/11,400

Tabulation: Freq.  Numeric  Label

4,126
629

1  Normally work the same hours
2  Schedule varies, primarily at

my request

869

3  Schedule varies, primarily

based on my employer’s needs

5,776

.

------------------------------------------------------------------------------------
(In your main job, did/Did) you agree that if
D47
you leave your employer, you will not start
or work for a competing business? This is
often called a non-compete agreement.

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D47

Range: [-2,1]

Unique values: 3

Units: 1

Missing .: 4,813/11,400

Tabulation: Freq.  Numeric  Label

730
5,097
760
4,813

-2  Don’t know

0  No
1  Yes
.

------------------------------------------------------------------------------------
D34A

Thinking about the work you did last week,
how much of it did you do by telecommuting or
working from home?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D34A

Range: [0,2]

Unique values: 3

Units: 1

Missing .: 4,813/11,400

Tabulation: Freq.  Numeric  Label

3,823
1,552
1,212
4,813

0  None
1  Some
2  All
.

------------------------------------------------------------------------------------
How likely would you be to actively look for
D36A
another job or leave your job if you had to
report in person each workday?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D36A

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 9,137/11,400

Tabulation: Freq.  Numeric  Label

693
547
575
448
9,137

1  Very likely
2  Somewhat likely
3  Not that likely
4  Not at all likely
.

------------------------------------------------------------------------------------
D36B

How likely would you be to actively look for
another job or leave your job if your employer
(kept your pay the same for a year / decreased
your pay by 1 percent / decreased your pay by
5 percent / decreased your pay by 10 percent)
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D36B

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 5,776/11,400

Tabulation: Freq.  Numeric  Label

1,875
1,524
1,437
788
5,776

1  Very likely
2  Somewhat likely
3  Not that likely
4  Not at all likely
.

------------------------------------------------------------------------------------
D44_f

(Think about any job in the past 12 months,
not just your main job). In the past 12
months, have you gotten laid off or lost a
job (including a temporary layoff)?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D44_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,793
607

0  No
1  Yes

------------------------------------------------------------------------------------
D44_a

Asked for a raise or a promotion - (Think
about any job in the past 12 months.) In the
past 12 months, have you:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D44_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 4,813/11,400

Tabulation: Freq.  Numeric  Label

5,251
1,336
4,813

0  No
1  Yes
.

------------------------------------------------------------------------------------
D44_b

Received a raise or a promotion - (Think
about any job in the past 12 months.) In the
past 12 months, have you:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D44_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 4,813/11,400

Tabulation: Freq.  Numeric  Label

2,995
3,592
4,813

0  No
1  Yes
.

------------------------------------------------------------------------------------
D44_c

Applied for a new job - (Think about any job
in the past 12 months.) In the past 12 months,
have you:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D44_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,062
2,338

0  No
1  Yes

------------------------------------------------------------------------------------
D44_d

Started a new job - (Think about any job in
the past 12 months.) In the past 12 months,
have you:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D44_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,957
1,443

0  No
1  Yes

------------------------------------------------------------------------------------
Voluntarily left a job - (Think about any job
D44_e
in the past 12 months.) In the past 12 months,

have you:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D44_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,433
967

0  No
1  Yes

------------------------------------------------------------------------------------
D37A

You indicated that you started a new job in
the past 12 months. Is your main job (where
you earn the most money) the same as it was
a  year ago?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D37A

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 10,142/11,400

Tabulation: Freq.  Numeric  Label

707

193

144

154
60
10,142

1  Different main job –  new

employer

2  Different main job –  same

employer

3  Same main job –  started a

second job

4  Was not working a year ago
5  Other
.

------------------------------------------------------------------------------------
D38_a

Pay or benefits - Are each of the following
better, the same, or worse at the main job
you have now than the one you had a year
ago?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D38_A

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 10,500/11,400

Tabulation: Freq.  Numeric  Label

498
234
168
10,500

1  Better
2  About the same
3  Worse
.

------------------------------------------------------------------------------------
D38_b

Opportunities for advancement - Are each of
the following better, the same, or worse at
the main job you have now than the one you
had a year ago?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D38_B

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 10,500/11,400

Tabulation: Freq.  Numeric  Label

412
393
95
10,500

1  Better
2  About the same
3  Worse
.

------------------------------------------------------------------------------------
D38_c

Your interest in the work - Are each of the

------------------------------------------------------------------------------------

following better, the same, or worse at the
main job you have now than the one you had
a year ago?

Type: Numeric (byte)

Label: D38_C

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 10,500/11,400

Tabulation: Freq.  Numeric  Label

461
350
89
10,500

1  Better
2  About the same
3  Worse
.

------------------------------------------------------------------------------------
Physical demands of the job - Are each of the
D38_d
following better, the same, or worse at the
main  job you have now than the one you had
a year ago?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D38_D

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 10,500/11,400

Tabulation: Freq.  Numeric  Label

282
513
105
10,500

1  Better
2  About the same
3  Worse
.

------------------------------------------------------------------------------------
Work-life balance - Are each of the following
D38_f
better, the same, or worse at the main job
you have now than the one you had a year ago?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D38_F

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 10,500/11,400

Tabulation: Freq.  Numeric  Label

380
372
148
10,500

1  Better
2  About the same
3  Worse
.

------------------------------------------------------------------------------------
Overall, is the main job you have now better,
D39
the same, or worse than the one you had a
year ago?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D39

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 10,500/11,400

Tabulation: Freq.  Numeric  Label

594
220
86
10,500

1  Better
2  About the same
3  Worse
.

------------------------------------------------------------------------------------
D45

How long have you been working continuously

in your main job (where you earn the most money)?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D45

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 5,867/11,400

Tabulation: Freq.  Numeric  Label

243
1,937
1,190
2,163
5,867

1  Less than a year
2  1 to 4 years
3  5 to 9 years
4  10 or more years
.

------------------------------------------------------------------------------------
Last month, did your spouse or partner do any work for either pay or profit?
D5
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D5

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 3,869/11,400

Tabulation: Freq.  Numeric  Label

3,025
4,506
3,869

0  No
1  Yes
.

------------------------------------------------------------------------------------
Does your spouse or partner usually work 35 hours or more per week?
D49
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D49

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 6,894/11,400

Tabulation: Freq.  Numeric  Label

820
3,686
6,894

0  No
1  Yes
.

------------------------------------------------------------------------------------
D41_a

Could not find (more) work - Did each of the
following contribute to your spouse or partner
(not working/working less than 35 hours per week)

------------------------------------------------------------------------------------

in the last month?

Type: Numeric (byte)

Label: D41_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,555/11,400

Tabulation: Freq.  Numeric  Label

3,538
307
7,555

0  No
1  Yes
.

------------------------------------------------------------------------------------
D41_b

Full-time workweek less than 35 hours - Did
each of the following contribute to your
spouse or partner (not working/working less

------------------------------------------------------------------------------------

than 35 hours per week) in the last month?

Type: Numeric (byte)

Label: D41_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .:

10,580/11,400

Tabulation: Freq.  Numeric  Label
624
196
10,580

0  No
1  Yes
.

------------------------------------------------------------------------------------
D41_c

Childcare - Did each of the following
contribute to your spouse or partner (not
working/working less than 35 hours per week)
in  the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D41_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,555/11,400

Tabulation: Freq.  Numeric  Label

3,544
301
7,555

0  No
1  Yes
.

------------------------------------------------------------------------------------
Caregiving for an elderly, disabled, or sick
D41_d
adult - Did each of the following contribute
to your spouse or partner
(not working/working less 35 hours per week)
in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D41_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,555/11,400

Tabulation: Freq.  Numeric  Label

3,662
183
7,555

0  No
1  Yes
.

------------------------------------------------------------------------------------
D41_e

Other family or personal obligations - Did
each of the following contribute to your
spouse or partner (not working/working less
than 35 hours  per week) in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D41_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,555/11,400

Tabulation: Freq.  Numeric  Label

3,465
380
7,555

0  No
1  Yes
.

------------------------------------------------------------------------------------
Would lose access to unemployment benefits or
D41_f

------------------------------------------------------------------------------------

other government programs - Did each of the
following contribute to your spouse or partner
(not working/working less than 35 hours per
week) in the last month?

Type: Numeric (byte)

Label: D41_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,555/11,400

Tabulation: Freq.  Numeric  Label

3,717
128
7,555

0  No
1  Yes
.

------------------------------------------------------------------------------------
Health limitations or disability- Did each of
D41_g
the following contribute to your spouse or
partner (not working/working less than 35
hours per week) in  the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D41_G

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,555/11,400

Tabulation: Freq.  Numeric  Label

3,137
708
7,555

0  No
1  Yes
.

------------------------------------------------------------------------------------
D41_h

In school or training - Did each of the
Following  contribute to your spouse or
partner (not working/working less than 35
hours per week) in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D41_H

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,555/11,400

Tabulation: Freq.  Numeric  Label

3,731
114
7,555

0  No
1  Yes
.

------------------------------------------------------------------------------------
D41_i

Retired - Did each of the following
contribute to your spouse or partner (not
working/working less than 35 hours per week)
in the last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D41_I

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,555/11,400

Tabulation: Freq.  Numeric  Label

1,705
2,140
7,555

0  No
1  Yes
.

------------------------------------------------------------------------------------
GH1

This section will ask some questions about
your  home. Do you (and/or your spouse or
partner):

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: GH1

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

4,814

2,905

2,896
785

1  Own your home with a mortgage

or loan

2  Own your home free and clear
(without a mortgage or loan)

3  Pay rent
4  Neither own nor pay rent

------------------------------------------------------------------------------------
Do you have either a homeowner’s insurance or
GH12
a condo insurance policy for your primary
residence?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: GH12

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,495/11,400

Tabulation: Freq.  Numeric  Label

316
2,589
8,495

0  No
1  Yes
.

------------------------------------------------------------------------------------
R1_a

Renting is cheaper - Are each of the
following a reason why you rent your home
rather than own?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R1_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,504/11,400

Tabulation: Freq.  Numeric  Label

1,666
1,230
8,504

0  No
1  Yes
.

------------------------------------------------------------------------------------
Renting is less financially risky - Are each
R1_b
of the following a reason why you rent your
home rather than own?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R1_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,504/11,400

Tabulation: Freq.  Numeric  Label

1,598
1,298
8,504

0  No
1  Yes
.

------------------------------------------------------------------------------------
Renting is more convenient or flexible –  Are
R1_c
each of the following a reason why you rent
your home rather than own?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R1_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,504/11,400

Tabulation: Freq.  Numeric  Label

1,219
1,677
8,504

0  No
1  Yes
.

------------------------------------------------------------------------------------
R1_d

Trying to buy - Are each of the following a
reason why you rent your home rather than
own?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R1_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,504/11,400

Tabulation: Freq.  Numeric  Label

2,082
814
8,504

0  No
1  Yes
.

------------------------------------------------------------------------------------
Can't qualify for home mortgage - Are each of
R1_e
the following a reason why you rent your
home rather than own?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R1_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,504/11,400

Tabulation: Freq.  Numeric  Label

1,728
1,168
8,504

0  No
1  Yes
.

------------------------------------------------------------------------------------
R1_f

Can't afford down payment to buy - Are each
of the following a reason why you rent your
home rather  than own?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R1_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,504/11,400

Tabulation: Freq.  Numeric  Label

996
1,900
8,504

0  No
1  Yes
.

------------------------------------------------------------------------------------
R1_g

Can't afford mortgage monthly payment –  Are
each of the following a reason why you rent

------------------------------------------------------------------------------------

your home rather than own?

Type: Numeric (byte)

Label: R1_G

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,504/11,400

Tabulation: Freq.  Numeric  Label

1,504
1,392
8,504

0  No
1  Yes
.

------------------------------------------------------------------------------------
Prefer to rent - Are each of the following a
R1_h
reason why you rent your home rather than
own?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R1_H

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,504/11,400

Tabulation: Freq.  Numeric  Label

1,821
1,075
8,504

0  No
1  Yes
.

------------------------------------------------------------------------------------
When did you move into your current home?
GH2
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: GH2

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,755
844
801

1  Before 2022
2  2022
3  2023

------------------------------------------------------------------------------------
Before your most recent move, did you own your previous home?
R4
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R4

Range: [0,2]

Unique values: 3

Units: 1

Missing .: 10,599/11,400

Tabulation: Freq.  Numeric  Label

572
48
181

0  No
1  Yes, and I still own that home
2  Yes, and I no longer own that

10,599

.

home

------------------------------------------------------------------------------------
R5E

Was the main reason that you moved in the
past year because of rent increases at your
previous home or apartment?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R5E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,828/11,400

Tabulation: Freq.  Numeric  Label

414
158
10,828

0  No
1  Yes
.

------------------------------------------------------------------------------------
Evicted or received an eviction notice - Did
R5B_a
each of the following contribute to your
moving in the past year?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R5B_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,828/11,400

Tabulation: Freq.  Numeric  Label

536
36
10,828

0  No
1  Yes
.

------------------------------------------------------------------------------------
R5B_b

Landlord told you, or a person you were
staying with, to leave - Did each of the
following contribute to your moving in the
past year?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R5B_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,828/11,400

Tabulation: Freq.  Numeric  Label

511
61
10,828

0  No
1  Yes
.

------------------------------------------------------------------------------------
R5B_c

You missed a rent payment and thought you
would be evicted - Did each of the following
contribute to your moving in the past year?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R5B_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,828/11,400

Tabulation: Freq.  Numeric  Label

543
29
10,828

0  No
1  Yes
.

------------------------------------------------------------------------------------
City condemned the property and forced you to
R5B_d
leave - Did each of the following contribute
to your moving in the past year?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R5B_D

Range: [0,1]

Units: 1

Unique values: 2

Missing .: 10,828/11,400

Tabulation: Freq.  Numeric  Label

567
5
10,828

0  No
1  Yes
.

------------------------------------------------------------------------------------
R5C_a

Bank took possession of your home in
foreclosure - Did each of the following
contribute to your moving in the past year?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R5C_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 11,219/11,400

Tabulation: Freq.  Numeric  Label

175
6
11,219

0  No
1  Yes
.

------------------------------------------------------------------------------------
Received a notice from bank that they planned
R5C_b
to foreclose- Did each of the following
contribute  to your moving in the past year?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R5C_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 11,219/11,400

Tabulation: Freq.  Numeric  Label

177
4
11,219

0  No
1  Yes
.

------------------------------------------------------------------------------------
R5C_c

Missed mortgage payments and thought bank
would foreclose - Did each of the following
contribute to your moving in the past year?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R5C_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 11,219/11,400

Tabulation: Freq.  Numeric  Label

175
6
11,219

0  No
1  Yes
.

------------------------------------------------------------------------------------
City condemned the property and forced you to
R5C_d
leave - Did each of the following contribute
to your moving in the past year?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R5C_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 11,219/11,400

Tabulation: Freq.  Numeric  Label

178
3
11,219

0  No
1  Yes
.

------------------------------------------------------------------------------------
R3

Approximately how much do you (and/or your
spouse or partner) pay for rent each month?

------------------------------------------------------------------------------------

Type: Numeric (int)

Label: R3, but 607 nonmissing values are not labeled

Range: [0,8500]

Unique values: 607

Units: 1

Missing .: 8,504/11,400

Examples: 1800

.
.
.

------------------------------------------------------------------------------------
Have you been behind on your rent at any time in the past year?
R11
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: R11

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,504/11,400

Tabulation: Freq.  Numeric  Label

2,379
517
8,504

0  No
1  Yes
.

------------------------------------------------------------------------------------
Approximately how much is your total monthly
M4
mortgage  payment (i.e. the amount you send
to the bank)?

------------------------------------------------------------------------------------

Type: Numeric (int)

Label: M4, but 935 nonmissing values are not labeled

Range: [0,9999]

Unique values: 935

Units: 1

Missing .: 6,586/11,400

Examples: 1368
3400
.
.

------------------------------------------------------------------------------------
Overall quality - How satisfied are you with
GH3_a
each of the following aspects of your
neighborhood?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: GH3_A

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

393
842
1,359

4,172
4,634

1  Very dissatisfied
2  Somewhat dissatisfied
3  Neither satisfied nor

dissatisfied

4  Somewhat satisfied
5  Very satisfied

------------------------------------------------------------------------------------
Quality of your local schools - How satisfied
GH3_b
are you with each of the following aspects
of your neighborhood?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: GH3_B

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

530
980
3,663

3,325
2,902

1  Very dissatisfied
2  Somewhat dissatisfied
3  Neither satisfied nor

dissatisfied

4  Somewhat satisfied
5  Very satisfied

------------------------------------------------------------------------------------
Crime risk - How satisfied are you with each
GH3_c
of the following aspects of your
neighborhood?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: GH3_C

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

711
1,523
2,024

3,966
3,176

1  Very dissatisfied
2  Somewhat dissatisfied
3  Neither satisfied nor

dissatisfied

4  Somewhat satisfied
5  Very satisfied

------------------------------------------------------------------------------------
GH3_d

Natural disaster and severe weather risk -
How satisfied are you with each of the
following aspects of your neighborhood?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: GH3_D

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

231
798
2,843

4,010
3,518

1  Very dissatisfied
2  Somewhat dissatisfied
3  Neither satisfied nor

dissatisfied

4  Somewhat satisfied
5  Very satisfied

------------------------------------------------------------------------------------
Cost of housing - How satisfied are you with
GH3_e
each of the following aspects of your
neighborhood?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: GH3_E

Range: [1,5]

Units: 1

Unique values: 5

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,792
2,395
2,894

2,979
1,340

1  Very dissatisfied
2  Somewhat dissatisfied
3  Neither satisfied nor

dissatisfied

4  Somewhat satisfied
5  Very satisfied

------------------------------------------------------------------------------------
ND0

In the past year, have you been financially
affected natural disasters or severe weather
events like flooding, hurricanes, wildfires,
or extreme temperatures?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ND0

Range: [0,3]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,263
1,346
579
212

0  No
1  Yes, slightly
2  Yes, moderately
3  Yes, substantially

------------------------------------------------------------------------------------
Income loss or work disruption - In the past
ND1_a
year, have natural disasters or severe
weather events like flooding, hurricanes,
wildfires, or extreme temperatures
affected you in each of the following ways?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ND1_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,263/11,400

Tabulation: Freq.  Numeric  Label

1,695
442
9,263

0  No
1  Yes
.

------------------------------------------------------------------------------------
ND1_b

Property damage - In the past year, have
natural disasters or severe weather events
like flooding,  hurricanes, wildfires, or
extreme temperatures affected you in each of
the following ways?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ND1_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,263/11,400

Tabulation: Freq.  Numeric  Label

1,116
1,021
9,263

0  No
1  Yes
.

------------------------------------------------------------------------------------
Needed to evacuate temporarily - In the past
ND1_c
year, have natural disasters or severe
weather events like flooding, hurricanes,

------------------------------------------------------------------------------------

wildfires, or extreme temperatures affected
you in each of the following ways?

Type: Numeric (byte)

Label: ND1_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,263/11,400

Tabulation: Freq.  Numeric  Label

1,914
223
9,263

0  No
1  Yes
.

------------------------------------------------------------------------------------
ND1_d

Longer-term displacement from home - In the
past year, have natural disasters or severe
weather events like flooding, hurricanes,
wildfires, or extreme temperatures affected
you in each of the following ways?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ND1_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,263/11,400

Tabulation: Freq.  Numeric  Label

2,066
71
9,263

0  No
1  Yes
.

------------------------------------------------------------------------------------
ND1_e

Other (please specify) - In the past year,
have natural  disasters or severe weather
events like flooding, hurricanes, wildfires,
or extreme  temperatures affected you in each
of the following ways?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ND1_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,263/11,400

Tabulation: Freq.  Numeric  Label

1,740
397
9,263

0  No
1  Yes
.

------------------------------------------------------------------------------------
ND2

Five years from now, do you think that the
chance that you will experience a natural
disaster or severe weather event will be
higher, lower or about the same as it is now?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ND2

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,059
3,091
6,693
228

1  Much higher
2  Somewhat higher
3  About the same
4  Somewhat lower

329

5  Much lower

------------------------------------------------------------------------------------
ND4_a

Investigated other places to live - In the
past year, have you done each of the following
at least partially because of the threat of
natural disasters or severe weather events?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ND4_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,957
1,443

0  No
1  Yes

------------------------------------------------------------------------------------
ND4_b

Improved your property to reduce risk - In
the past year, have you done each of the
following at least partially because of the
threat of natural disasters or severe
weather events?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ND4_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,233
2,167

0  No
1  Yes

------------------------------------------------------------------------------------
Purchased additional insurance - In the past
ND4_c
year, have you done each of the following
at least  partially because of the threat of
natural disasters or severe weather events?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ND4_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,786
614

0  No
1  Yes

------------------------------------------------------------------------------------
BK1

Do you (and/or your spouse or partner)
currently have a checking, savings or money
market account?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BK1

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

583
10,817

0  No
1  Yes

------------------------------------------------------------------------------------

BK2_a

Purchase a money order from a place other
than a bank - In the past 12 months, did you

(and/or your spouse or partner):

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BK2_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,405
995

0  No
1  Yes

------------------------------------------------------------------------------------
BK2_b

Cash a check at a place other than a bank -
In the past 12 months, did you (and/or your
spouse or partner):

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BK2_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,662
738

0  No
1  Yes

------------------------------------------------------------------------------------
BK2_c

Take out a payday loan or payday advance -
In the past 12 months, did you (and/or your
spouse or partner):

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BK2_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

11,096
304

0  No
1  Yes

------------------------------------------------------------------------------------
BK2_d

Take out a pawn shop loan or an auto title
loan - In the past 12 months, did you (and/
or your spouse or partner):

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BK2_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

11,140
260

0  No
1  Yes

------------------------------------------------------------------------------------
BK2_e

Obtain a tax refund advance to receive your
refund faster - In the past 12 months, did
you (and/or you spouse or partner):

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BK2_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

11,261
139

0  No
1  Yes

------------------------------------------------------------------------------------
BK2_f

Pay an overdraft fee on a bank account - In
the past 12 months, did you (and/or your
spouse or partner):

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BK2_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 583/11,400

Tabulation: Freq.  Numeric  Label

9,619
1,198
583

0  No
1  Yes
.

------------------------------------------------------------------------------------
If you were to apply for a credit card today,
A6
how confident are you that your application
would be approved?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A6

Range: [-2,3]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

523
7,457
1,925
1,495

-2  Don’t know

1  Very confident
2  Somewhat confident
3  Not confident

------------------------------------------------------------------------------------
A0

In the past 12 months have you applied for
any credit (such as a credit card, higher
credit card limit, mortgage, refinance,
student loan, personal loan, or other loan)?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A0

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

7,393
4,007

0  No
1  Yes

------------------------------------------------------------------------------------
A7_a

Credit card - Have you applied for each of
the following types of credit in the past 12
month?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A7_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,393/11,400

Tabulation: Freq.  Numeric  Label

1,246
2,761
7,393

0  No
1  Yes
.

------------------------------------------------------------------------------------
Car/auto loan - Have you applied for each of
A7_b
the following types of credit in the past 12
months?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A7_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,393/11,400

Tabulation: Freq.  Numeric  Label

3,075
932
7,393

0  No
1  Yes
.

------------------------------------------------------------------------------------
A7_c

Student loan - Have you applied for each of
the following types of credit in the past 12
month?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A7_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,393/11,400

Tabulation: Freq.  Numeric  Label

3,738
269
7,393

0  No
1  Yes
.

------------------------------------------------------------------------------------
A7_d

Mortgage (purchase or refinance) - Have you
applied for each of the following types of
credit in the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A7_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,393/11,400

Tabulation: Freq.  Numeric  Label

3,591
416
7,393

0  No
1  Yes
.

------------------------------------------------------------------------------------
Home equity loan or line of credit - Have you
A7_e
applied for each of the following types of
credit in the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A7_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,393/11,400

Tabulation: Freq.  Numeric  Label

3,758

0  No

249
7,393

1  Yes
.

------------------------------------------------------------------------------------
A7_f

Other credit or loan - Have you applied for
each of the following types of credit in the
past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A7_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,393/11,400

Tabulation: Freq.  Numeric  Label

3,159
848
7,393

0  No
1  Yes
.

------------------------------------------------------------------------------------
A0B

Was there a time in the past 12 months that
you desired credit but chose not to submit
a credit application?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A0B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 4,007/11,400

Tabulation: Freq.  Numeric  Label

6,649
744
4,007

0  No
1  Yes
.

------------------------------------------------------------------------------------
A1_a

Turned down for credit - In the past 12
months, has each of the following happen to
you:
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A1_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,393/11,400

Tabulation: Freq.  Numeric  Label

3,054
953
7,393

0  No
1  Yes
.

------------------------------------------------------------------------------------
A1_b

Approved for credit, but were not given as
much credit as you applied for - In the past
12 months, has each of the following happened
to you:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A1_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,393/11,400

Tabulation: Freq.  Numeric  Label

3,358
649
7,393

0  No
1  Yes
.

------------------------------------------------------------------------------------
A1_c

Put off applying for credit because you
thought you might be turned down - In the
past 12 months, has each of the following
happened to you:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A1_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,393/11,400

Tabulation: Freq.  Numeric  Label

3,250
757
7,393

0  No
1  Yes
.

------------------------------------------------------------------------------------
A8_a

Were you turned down or offered less credit
than requested for the following types of
credit in the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A8_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,408/11,400

Tabulation: Freq.  Numeric  Label

128
864
10,408

0  No
1  Yes
.

------------------------------------------------------------------------------------
A8_b

Were you turned down or offered less credit
than requested for the following types of
credit in the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A8_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 11,103/11,400

Tabulation: Freq.  Numeric  Label

139
158
11,103

0  No
1  Yes
.

------------------------------------------------------------------------------------
A8_c

Were you turned down or offered less credit
than requested for the following types of
credit in the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A8_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 11,281/11,400

Tabulation: Freq.  Numeric  Label
79
40
11,281

0  No
1  Yes
.

------------------------------------------------------------------------------------

A8_d

Were you turned down or offered less credit
than requested for the following types of
credit in the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A8_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 11,283/11,400

Tabulation: Freq.  Numeric  Label
51
66
11,283

0  No
1  Yes
.

------------------------------------------------------------------------------------
A8_e

Were you turned down or offered less credit
than requested for the following types of
credit in the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A8_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 11,307/11,400

Tabulation: Freq.  Numeric  Label
36
57
11,307

0  No
1  Yes
.

------------------------------------------------------------------------------------
A8_f

Were you turned down or offered less credit
than requested for the following types of
credit in the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A8_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,977/11,400

Tabulation: Freq.  Numeric  Label

115
308
10,977

0  No
1  Yes
.

------------------------------------------------------------------------------------
You indicated that you desired credit in the
A2
past 12 months but did not submit a credit
application. Was this because you thought
that you might be turned down or denied
credit?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: A2

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,656/11,400

Tabulation: Freq.  Numeric  Label

305
439
10,656

0  No
1  Yes
.

------------------------------------------------------------------------------------
C2A

Do you currently have at least one credit

------------------------------------------------------------------------------------

card? Please do not include debit cards
or prepaid cards.

Type: Numeric (byte)

Label: C2A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,767
9,633

0  No
1  Yes

------------------------------------------------------------------------------------
Last month, how did you handle your credit
C3P
card bills?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: C3P

Range: [-9,2]

Unique values: 3

Units: 1

Missing .: 1,767/11,400

Tabulation: Freq.  Numeric  Label

622

8,743

268

-9  did not use any of my credit
cards so had no balances

1  paid at least the minimum

payment on all credit cards
2  did not pay or paid less than

the minimum payment on at least
one card

1,767

.

------------------------------------------------------------------------------------
C4A

In the past 12 months, how frequently have
you carried an unpaid balance on one or more
of your credit cards?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: C4A

Range: [0,3]

Unique values: 4

Units: 1

Missing .: 1,767/11,400

Tabulation: Freq.  Numeric  Label

5,204

506
1,664
2,259
1,767

0  Never carried an unpaid balance

(always pay in full)

1  Once
2  Some of the time
3  Most or all of the time
.

------------------------------------------------------------------------------------
BNPL1

In the past year, have you used a “Buy Now
Pay Later” service to buy something?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BNPL1

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,945
1,455

0  No
1  Yes

------------------------------------------------------------------------------------

BNPL3

In the past year, have you ever been late
making a payment for something you bought
using a Buy Now Pay Later service?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BNPL3

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,945/11,400

Tabulation: Freq.  Numeric  Label

1,211
244
9,945

0  No
1  Yes
.

------------------------------------------------------------------------------------
In the past year, have you been charged extra
BNPL3A
because you were late on a buy now pay
later payment?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BNPL3A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 11,156/11,400

Tabulation: Freq.  Numeric  Label
96
148
11,156

0  No
1  Yes
.

------------------------------------------------------------------------------------
BNPL4_a

Avoid interest charges - Thinking about the
most recent time you used a Buy Now Pay Later
service, were each of the following a reason
why you chose to finance the purchase in this
way?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BNPL4_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,945/11,400

Tabulation: Freq.  Numeric  Label

562
893
9,945

0  No
1  Yes
.

------------------------------------------------------------------------------------
BNPL4_b

Wanted to spread out payments - Thinking
about the most recent time you used a Pay
Later service, were each of the following a
reason why you chose to finance the purchase
in this way?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BNPL4_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,945/11,400

Tabulation: Freq.  Numeric  Label

173
1,282
9,945

0  No
1  Yes
.

------------------------------------------------------------------------------------
BNPL4_c

Wanted a fixed number of payments - Thinking
about the most recent time you used a Buy Now
Pay Later service, were each of the following
a reason why you chose to finance the purchase
in this way?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BNPL4_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,945/11,400

Tabulation: Freq.  Numeric  Label

785
670
9,945

0  No
1  Yes
.

------------------------------------------------------------------------------------
Convenience - Thinking about the most recent
BNPL4_d
time you used a Buy Now Pay Later service,
were each of the following a reason why you
chose to finance the purchase in this way?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BNPL4_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,945/11,400

Tabulation: Freq.  Numeric  Label

256
1,199
9,945

0  No
1  Yes
.

------------------------------------------------------------------------------------
BNPL4_e

Only way I could afford it - Thinking about
the most recent time you used a Buy Now Pay
Later service, were each of the following a
reason why you chose to finance the purchase
in this way?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BNPL4_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,945/11,400

Tabulation: Freq.  Numeric  Label

677
778
9,945

0  No
1  Yes
.

------------------------------------------------------------------------------------
BNPL4_f

Only accepted payment method I had - Thinking
about the most recent time you used a Buy Now
Pay Later service, were each of the following
a reason why you chose to finance the purchase
in this way?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BNPL4_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,945/11,400

Tabulation: Freq.  Numeric  Label

1,160
295
9,945

0  No
1  Yes
.

------------------------------------------------------------------------------------
BNPL4_g

Did not want to use a credit card - Thinking
about the most recent time you used a Buy Now
Pay Later service, were each of the following
a reason why you chose to finance the purchase
in this way?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: BNPL4_G

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,945/11,400

Tabulation: Freq.  Numeric  Label

663
792
9,945

0  No
1  Yes
.

------------------------------------------------------------------------------------
S16_a

Bought cryptocurrency or held as an
investment - In the past year, have you done
the following with cryptocurrency, such as
Bitcoin or Ethereum?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: S16_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,679
721

0  No
1  Yes

------------------------------------------------------------------------------------
Used cryptocurrency to buy something or make
S16_b
a payment - In the past year, have you done
the following with cryptocurrency, such as
Bitcoin or Ethereum?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: S16_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

11,272
128

0  No
1  Yes

------------------------------------------------------------------------------------
Used cryptocurrency to send money to friends
S16_c
or family - In the past year, have you done
the following with cryptocurrency, such as
Bitcoin or Ethereum?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: S16_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

11,323
77

0  No
1  Yes

------------------------------------------------------------------------------------
S18

Were any of the family or friends you sent
cryptocurrency to living outside of the
United States?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: S18

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 11,323/11,400

Tabulation: Freq.  Numeric  Label
50
27
11,323

0  No
1  Yes
.

------------------------------------------------------------------------------------
S21

What was the main reason you used
cryptocurrency to buy something, make a
payment, or send money?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: S21

Range: [1,7]

Unique values: 7

Units: 1

Missing .: 11,241/11,400

Tabulation: Freq.  Numeric  Label
24
29
19
10
9
47

1  Privacy
2  To send the money faster
3  Cheaper
4  Safer
5  Don’t trust banks
6  Person or business receiving

21
11,241

the money preferred
cryptocurrency

7  Other (please specify)
.

------------------------------------------------------------------------------------
What is the highest level of school you have
ED0
completed or the highest degree you have
received?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ED0

Range: [1,9]

Unique values: 9

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

560
2,185
2,188

555
1,085
2,721
1,324
507

1  Less than high school degree
2  High school degree or GED
3  Some college but no degree

(including currently enrolled
in college)

4  Certificate or technical degree
5  Associate degree
6  Bachelor’s degree
7  Master’s degree
8  Professional degree (e.g., MBA,

275

9  Doctoral degree

MD, JD)

------------------------------------------------------------------------------------

Are you currently enrolled as a student?
D1G
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D1G

Range: [0,2]

Unique values: 3

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,702
240
458

0  No
1  Yes, as a part-time student
2  Yes, as a full-time student

------------------------------------------------------------------------------------
ED0B

What type of program are you currently
pursuing?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ED0B

Range: [1,8]

Unique values: 8

Units: 1

Missing .: 10,702/11,400

Tabulation: Freq.  Numeric  Label
35
22
58
96
287
104
40

1  High school or GED program
2  Non-degree training program
3  Certificate or technical degree
4  Associate degree
5  Bachelor’s degree
6  Master’s degree
7  Professional degree (e.g., MBA,

56
10,702

MD, JD)

8  Doctoral degree
.

------------------------------------------------------------------------------------
ED0D

Have you ever enrolled in an educational
degree program beyond high school?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ED0D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,891/11,400

Tabulation: Freq.  Numeric  Label

2,171
338
8,891

0  No
1  Yes
.

------------------------------------------------------------------------------------
ED1

Which one of the following broad
categories best describes your current
or most recent educational program?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ED1

Range: [1,13]

Unique values: 13

Units: 1

Missing .: 2,745/11,400

Examples: 5
8
10
.

Computer / information sciences
Business / management
Law

------------------------------------------------------------------------------------

ED4

In what year did you last attend this
educational program?

------------------------------------------------------------------------------------

Type: Numeric (int)

Label: ED4, but 71 nonmissing values are not labeled

Range: [1945,2023]

Unique values: 71

Units: 1

Missing .: 8,993/11,400

Examples: 2022

.
.
.

------------------------------------------------------------------------------------
In what year did you receive your Associate
ED9
degree or above, or some college and not
enrolled?

------------------------------------------------------------------------------------

Type: Numeric (int)

Label: ED9, but 72 nonmissing values are not labeled

Range: [1950,2023]

Unique values: 72

Units: 1

Missing .: 5,488/11,400

Examples: 1992
2013
.
.

------------------------------------------------------------------------------------
ED10

Overall, how would you say the lifetime
financial benefits of your (Associate Degree/
Bachelor's Degree) compares to its costs?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ED10

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 3,059/11,400

Tabulation: Freq.  Numeric  Label

2,739

1,724

2,247
734

897
3,059

1  Financial benefits are much

larger

2  Financial benefits are somewhat

larger

3  About the same
4  Financial costs are somewhat

larger

5  Financial costs are much larger
.

------------------------------------------------------------------------------------
ED11_a

Chosen a different field of study - If you
could go back and make decisions regarding
your (Associates Degree/Bachelor's degree)
again would you have done each of these
things?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ED11_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 3,059/11,400

Tabulation: Freq.  Numeric  Label

5,390

0  No

2,951
3,059

1  Yes
.

------------------------------------------------------------------------------------
Attended a different school - If you could go
ED11_b
back and make decisions regarding your
(Associates Degree/Bachelor's Degree)

again would you have done each of these

things?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ED11_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 3,059/11,400

Tabulation: Freq.  Numeric  Label

6,349
1,992
3,059

0  No
1  Yes
.

------------------------------------------------------------------------------------
ED11_c

Not attended college or completed less
education - If you could go back and make
your decisions regarding your [Associates
Degree/Bachelor's Degree) again would you
have done each of these things?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: ED11_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 3,059/11,400

Tabulation: Freq.  Numeric  Label

7,533
808
3,059

0  No
1  Yes
.

------------------------------------------------------------------------------------
ED11_d

Completed more education- If you could go
back and make decisions regarding your
(Associates Degree/Bachelor's Degree) would

------------------------------------------------------------------------------------

you have done each of these things:

Type: Numeric (byte)

Label: ED11_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 3,059/11,400

Tabulation: Freq.  Numeric  Label

4,531
3,810
3,059

0  No
1  Yes
.

------------------------------------------------------------------------------------
Do you currently have any student loan debt from your own education?
SL1
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL1

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,939

0  No

1,461

1  Yes

------------------------------------------------------------------------------------
How much do you currently owe on student loans for your own education?
SL3
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL3

Range: [-2,11]

Unique values: 12

Units: 1

Missing .: 9,939/11,400

Examples: .
.
.
.

------------------------------------------------------------------------------------
SL4A

Are you currently required to make monthly
payments on any of your student loans from
your own education?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL4A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,939/11,400

Tabulation: Freq.  Numeric  Label

490
971
9,939

0  No
1  Yes
.

------------------------------------------------------------------------------------
SL4

Approximately how much is your current
required monthly payment on the student
loans from your own education?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL4

Range: [-2,8]

Unique values: 8

Units: 1

Missing .: 10,429/11,400

Tabulation: Freq.  Numeric  Label
52
207
256
171
92
55
102
36
10,429

-2  Don’t know
2  $1 to $99
3  $100 to $199
4  $200 to $299
5  $300 to $399
6  $400 to $499
7  $500 to $999
8  $1,000 or above
.

------------------------------------------------------------------------------------
Are you behind on payments or in collections
SL6
for one or more of the student loans from
your own education?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL6

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 9,939/11,400

Tabulation: Freq.  Numeric  Label

1,217

0  No

244
9,939

1  Yes
.

------------------------------------------------------------------------------------
Did you take out any student loans to pay for
SL7
your own education that you have since
repaid?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL7

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 1,461/11,400

Tabulation: Freq.  Numeric  Label

7,729
2,210
1,461

0  No
1  Yes
.

------------------------------------------------------------------------------------
SL8_a

Certificate or technical training - Still
thinking about your own education, did you

take out any student loans for each of the
following educational programs (including any
repaid loans for education you did not
complete)?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL8_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,729/11,400

Tabulation: Freq.  Numeric  Label

3,221
450
7,729

0  No
1  Yes
.

------------------------------------------------------------------------------------
Associate degree - Still thinking about your
SL8_b
own education, did you take out any student
loans for each of the following educational
programs (including any repaid loans for
education you did not complete)?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL8_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,729/11,400

Tabulation: Freq.  Numeric  Label

2,904
767
7,729

0  No
1  Yes
.

------------------------------------------------------------------------------------
Bachelor's degree - Still thinking about your
SL8_c
own education, did you take out any student
loans for each of the following educational
programs (including any repaid loans for
education you did not complete)?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL8_C

Range: [0,1]

Units: 1

Unique values: 2

Missing .: 7,729/11,400

Tabulation: Freq.  Numeric  Label

1,237
2,434
7,729

0  No
1  Yes
.

------------------------------------------------------------------------------------
SL8_d

Professional degree (e.g., MBA, MD, JD) -
Still thinking about your own education, did
you take out any student loans for each of
the following educational programs (including
any repaid loans for education you did not
complete)?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL8_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,729/11,400

Tabulation: Freq.  Numeric  Label

3,324
347
7,729

0  No
1  Yes
.

------------------------------------------------------------------------------------
SL8_e

Master's degree or doctoral degree - Still
thinking about your own education, did you
take out any student loans for each of the
following educational programs (including
any repaid loan for education you did not
complete)?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL8_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,729/11,400

Tabulation: Freq.  Numeric  Label

3,001
670
7,729

0  No
1  Yes
.

------------------------------------------------------------------------------------
SL10A

Does your spouse or partner currently have
any student loans used to pay for their
education?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL10A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 3,869/11,400

Tabulation: Freq.  Numeric  Label

6,736
795
3,869

0  No
1  Yes
.

------------------------------------------------------------------------------------
Do you currently have any student loans used
SL11
to pay for your child's or grandchild’s
education?

------------------------------------------------------------------------------------

Type: Numeric (int)

Label: SL11

Range: [0,999]

Unique values: 3

Units: 1

Missing .: 1,739/11,400

Tabulation: Freq.  Numeric  Label

7,479
554
1,628

1,739

0  No
1  Yes

999  Do not have children or

grandchildren

.

------------------------------------------------------------------------------------
How much do you owe on student loans for your
SL13
child or grandchild’s education?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: SL13

Range: [-2,11]

Unique values: 12

Units: 1

Missing .: 10,846/11,400

Examples: .
.
.
.

------------------------------------------------------------------------------------
Do you consider yourself to be retired?
D1I
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: D1I

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

7,615
3,785

0  No
1  Yes

------------------------------------------------------------------------------------
Do you think that your retirement savings plan is currently on track?
K0
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K0

Range: [-2,1]

Unique values: 3

Units: 1

Missing .: 3,785/11,400

Tabulation: Freq.  Numeric  Label

1,342
3,566
2,707
3,785

-2  Don’t know

0  No
1  Yes
.

------------------------------------------------------------------------------------
When did you retire?
K8B
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K8B

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 7,615/11,400

Tabulation: Freq.  Numeric  Label

252
397

1  Within the past year
2  1 or 2 years ago

494
2,642
7,615

3  3 or 4 years ago
4  5 years ago or more
.

------------------------------------------------------------------------------------
K9_a

Health problem - Were each of the following
important to your decision to retire at the
age that you did?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K9_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,615/11,400

Tabulation: Freq.  Numeric  Label

2,738
1,047
7,615

0  No
1  Yes
.

------------------------------------------------------------------------------------
Wanted to do other things or spend time with
K9_b
family - Were each of the following
important to your decision to retire at the
age that you did?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K9_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,615/11,400

Tabulation: Freq.  Numeric  Label

1,838
1,947
7,615

0  No
1  Yes
.

------------------------------------------------------------------------------------
K9_c

Didn't like the work - Were each of the
following important to your decision to
retire at the age that you did?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K9_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,615/11,400

Tabulation: Freq.  Numeric  Label

3,248
537
7,615

0  No
1  Yes
.

------------------------------------------------------------------------------------
K9_d

Care for family members - Were each of the
following important to your decision to
retire at the age that you did?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K9_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,615/11,400

Tabulation: Freq.  Numeric  Label

3,219
566

0  No
1  Yes

7,615

.

------------------------------------------------------------------------------------
Reached normal retirement age - Were each of
K9_e
the following important to your decision to
retire at the age that you did?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K9_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,615/11,400

Tabulation: Freq.  Numeric  Label

1,948
1,837
7,615

0  No
1  Yes
.

------------------------------------------------------------------------------------
K9_f

Forced to retire or lack of available work -
Were each of the following important to your
decision to retire at the age that you did?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K9_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 7,615/11,400

Tabulation: Freq.  Numeric  Label

3,398
387
7,615

0  No
1  Yes
.

------------------------------------------------------------------------------------
Retirement savings account, such as a 401(k)
K21_a
plan through an employer, IRA or Roth IRA -
Do you currently have each of the following
types of savings or assets?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K21_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

4,238
7,162

0  No
1  Yes

------------------------------------------------------------------------------------
K21_b

Pension with a defined benefit through an
employer that will pay a monthly amount in
retirement - Do you currently have each of
the following types of savings or assets?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K21_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

7,680
3,720

0  No
1  Yes

------------------------------------------------------------------------------------

K21_c

Stocks, bonds, ETFs, or mutual funds held
outside a retirement account - Do you
currently have each of the following types
of savings or assets?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K21_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

7,111
4,289

0  No
1  Yes

------------------------------------------------------------------------------------
K21_d

Savings account, money market account, or
certificate of deposit (CD) - Do you
currently have each of the following types of
savings or assets?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K21_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

4,389
7,011

0  No
1  Yes

------------------------------------------------------------------------------------
K21_e

Cash value in a life insurance policy - Do
you currently have each of the following
types of savings or assets?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K21_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

8,349
3,051

0  No
1  Yes

------------------------------------------------------------------------------------
K21_f

Business or real estate investment (other
than your primary residence) - Do you
currently have each of the following types of
savings or assets?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K21_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,052
1,348

0  No
1  Yes

------------------------------------------------------------------------------------
How comfortable are you with choosing and managing your investments?
DC4
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: DC4

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,996
3,395
3,224
2,785

1  Very comfortable
2  Mostly comfortable
3  Slightly comfortable
4  Not comfortable

------------------------------------------------------------------------------------
Borrowed money - In the past 12 months, have
K5A_a
you done each of the following with money in
your retirement accounts?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K5A_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 3,785/11,400

Tabulation: Freq.  Numeric  Label

7,110
505
3,785

0  No
1  Yes
.

------------------------------------------------------------------------------------
Cashed out (permanently withdrawn) money - In
K5A_b
the past 12 months, have you done each of the
following with money in your retirement
accounts?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K5A_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 3,785/11,400

Tabulation: Freq.  Numeric  Label

7,173
442
3,785

0  No
1  Yes
.

------------------------------------------------------------------------------------
K5A_c

Reduced your regular contributions to
accounts - In the past 12 months, have you
done each of the following with money in
your retirement accounts?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: K5A_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 3,785/11,400

Tabulation: Freq.  Numeric  Label

6,925
690
3,785

0  No
1  Yes
.

------------------------------------------------------------------------------------
I0_a

Wages, salaries, or self-employment income -
In the past 12 months, did you [and/or your
spouse or partner] receive any income from
the following sources:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I0_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

4,000
7,400

0  No
1  Yes

------------------------------------------------------------------------------------
I0_b

Interest, dividends, or rental income - In
the past 12 months, did you [and/or your
spouse or partner] receive any income from
the following sources:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I0_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

7,126
4,274

0  No
1  Yes

------------------------------------------------------------------------------------
I0_c

Social Security (including old age and DI) -
In the past 12 months, did you [and/or your
spouse or partner] receive any income from
the following sources:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I0_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

7,705
3,695

0  No
1  Yes

------------------------------------------------------------------------------------
Supplemental Security Income (SSI), TANF, or
I0_d
cash assistance from a welfare program - In
the past 12 months, did you [and/or your
spouse or partner] receive any income from
the following sources:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I0_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,825
575

0  No
1  Yes

------------------------------------------------------------------------------------
Unemployment income - In the past 12 months,
I0_e
did you [and/or your spouse or partner]
receive any income from the following
sources:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I0_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

11,140
260

0  No
1  Yes

------------------------------------------------------------------------------------
I0_f

Pension - In the past 12 months, did you
[and/or your spouse or partner] receive any
income from the following sources:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I0_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

8,855
2,545

0  No
1  Yes

------------------------------------------------------------------------------------
I40

Which category represents your [and your
spouse/partner’s] total combined income in
the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I40

Range: [1,15]

Unique values: 15

Units: 1

Missing .: 0/11,400

Examples: 6

10
12
13

$25,000 to $29,999
$50,000 to $59,999
$75,000 to $99,999
$100,000 to $149,999

------------------------------------------------------------------------------------
Earned Income Tax Credit (EITC) - In the past
I41_a
12 months, have you [and/or your spouse or
partner] received any of the following?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I41_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,532
868

0  No
1  Yes

------------------------------------------------------------------------------------
I41_b

Supplemental Nutrition Assistance Program
(SNAP or food stamps) - In the past 12

------------------------------------------------------------------------------------

months, have you [and/or your spouse or
partner] received any of the following?

Type: Numeric (byte)

Label: I41_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,148
1,252

0  No
1  Yes

------------------------------------------------------------------------------------
Women, Infants, and Children (WIC) nutrition
I41_c
program benefits - In the past 12 months,
have you [and/or your spouse or partner]
received any of the following?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I41_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

11,154
246

0  No
1  Yes

------------------------------------------------------------------------------------
I41_d

Housing assistance from government program -
In the past 12 months, have you [and/or your
spouse or partner] received any of the
following?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I41_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

11,065
335

0  No
1  Yes

------------------------------------------------------------------------------------
Free or reduced price school lunches for your
I41_e
children - In the past 12 months, have you
[and/or your spouse or partner] received any
of the following?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I41_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,744/11,400

Tabulation: Freq.  Numeric  Label

1,985
671
8,744

0  No
1  Yes
.

------------------------------------------------------------------------------------
I9

In the past 12 months, which one of the
following best describes your [and your
spouse's or partner's] income?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I9

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

8,369

2,133

1  Roughly the same amount each

month

2  Occasionally varies from month

898

3  Varies quite often from month

to month

to month

------------------------------------------------------------------------------------
I12

Because your income varies, have you [and your
spouse or partner] struggled to pay your
bills in the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I12

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 8,369/11,400

Tabulation: Freq.  Numeric  Label

1,970
1,061
8,369

0  No
1  Yes
.

------------------------------------------------------------------------------------
I20

In the past month, would you say that your
[and your spouse’s or partner’s] total
spending was:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I20

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

5,593
3,608
2,199

1  Less than your income
2  The same as your income
3  More than your income

------------------------------------------------------------------------------------
I21_a

Total monthly income - Compared to a year
ago, have each of the following [for you and
your spouse or partner] increased,
decreased or stayed about the same?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I21_A

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,373
6,152
3,875

1  Decreased
2  About the same
3  Increased

------------------------------------------------------------------------------------
I21_b

Total monthly spending - Compared to a year
ago, have each of the following [for you and
your spouse or partner] increased, decreased,
or stayed about the same?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: I21_B

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,007

1  Decreased

6,019
4,374

2  About the same
3  Increased

------------------------------------------------------------------------------------
INF4

Overall, have changes in the prices you pay
compared to last year made your financial
situation worse, better, or had little or no
effect?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: INF4

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

2,203
5,322
3,487
310
78

1  Much worse
2  Somewhat worse
3  Little or no effect
4  Somewhat better
5  Much better

------------------------------------------------------------------------------------
INF3_a

Switched to cheaper products - Did you take
any of the following actions because of
increases in prices over the past 12 months?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: INF3_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

4,192
7,208

0  No
1  Yes

------------------------------------------------------------------------------------
Used less or stopped using products - Did you
INF3_b
take any of the following actions because of
increases in prices over the past 12 months?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: INF3_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

4,378
7,022

0  No
1  Yes

------------------------------------------------------------------------------------
INF3_c

Reduced savings - Did you take any of the
following actions because of increases in
prices over the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: INF3_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

6,259
5,141

0  No
1  Yes

------------------------------------------------------------------------------------
Increased borrowing - Did you take any of the
INF3_d
following actions because of increases in
prices over the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: INF3_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,729
1,671

0  No
1  Yes

------------------------------------------------------------------------------------
INF3_e

Delayed a major purchase - Did you take any
of the following actions because of increases
in prices over the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: INF3_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

5,976
5,424

0  No
1  Yes

------------------------------------------------------------------------------------
Worked more or got another job - Did you take
INF3_f
any of the following actions because of
increases in prices over the past 12 months?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: INF3_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,539
1,861

0  No
1  Yes

------------------------------------------------------------------------------------
INF3_g

Asked for a raise - Did you take any of the
following actions because of increases in
prices over the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: INF3_G

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 10,064/11,400

Tabulation: Freq.  Numeric  Label

384
952
10,064

0  No
1  Yes
.

------------------------------------------------------------------------------------
EF1

Have you set aside emergency or rainy day
funds that would cover your expenses for 3
months in case of sickness, job loss,
economic downturn, or other emergencies?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF1

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

4,918
6,482

0  No
1  Yes

------------------------------------------------------------------------------------
EF2

If you were to lose your main source of
income (for example job or government be

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF2

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 6,482/11,400

Tabulation: Freq.  Numeric  Label

3,247
1,671
6,482

0  No
1  Yes
.

------------------------------------------------------------------------------------
EF3_a

Put it on my credit card and pay it off in
full at the next statement - Suppose that you
have an emergency expense that costs $400.
Based on your current financial situation,
how would you pay for this expense?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF3_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

7,003
4,397

0  No, did not do this
1  Put it on my credit card and

pay it off in full at the next
statement

------------------------------------------------------------------------------------
Put it on my credit card and pay it off over
EF3_b
time - Suppose that you have an emergency
expense that costs $400. Based on your
current financial situation, how would you
pay for this expense?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF3_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,629
1,771

0  No, did not do this
1  Put it on my credit card and

pay it off over time

------------------------------------------------------------------------------------
EF3_c

With the money currently in my
checking/savings account or with cash -
Suppose that you have an emergency expense
that costs $400. Based on your current

------------------------------------------------------------------------------------

financial situation, how would you pay for
this expense?

Type: Numeric (byte)

Label: EF3_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

6,193
5,207

0  No, did not do this
1  With the money currently in my
checking/savings account or
with cash

------------------------------------------------------------------------------------
EF3_d

Using money from a bank loan or line of
credit - Suppose that you have an emergency
expense that costs $400. Based on your
current financial situation, how would you
pay for this expense?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF3_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

11,112
288

0  No, did not do this
1  Using money from a bank loan or

line of credit

------------------------------------------------------------------------------------
By borrowing from a friend or family member -
EF3_e
Suppose that you have an emergency expense
that costs $400. Based on your current
financial situation, how would you pay for
this expense?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF3_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,435
965

0  No, did not do this
1  By borrowing from a friend or

family member

------------------------------------------------------------------------------------
EF3_f

Using a payday loan, deposit advance, or
overdraft - Suppose that you have an
emergency expense that costs $400. Based on
your current financial situation, how would
you pay for this expense?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF3_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

11,229
171

0  No, did not do this
1  Using a payday loan, deposit

advance, or overdraft

------------------------------------------------------------------------------------
By selling something - Suppose that you have
EF3_g
an emergency expense that costs $400. Based
on your current financial situation, how
would you pay for this expense?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF3_G

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,678
722

0  No, did not do this
1  By selling something

------------------------------------------------------------------------------------
EF3_h

I wouldn't be able to pay for the expense
right now - Suppose that you have an
emergency expense that costs $400. Based on
your current financial situation, how would
you pay for this expense?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF3_H

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,063
1,337

0  No, did not do this
1  I wouldn’t be able to pay for

the expense right now

------------------------------------------------------------------------------------
EF5C

Other than any credit card bills you may
have, did you pay all your bills in full last
month?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF5C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,566
9,834

0  No
1  Yes

------------------------------------------------------------------------------------
Rent or mortgage - How did you handle each of
EF6C_a
the following types of bills last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF6C_A

Range: [-9,1]

Unique values: 3

Units: 1

Missing .: 9,834/11,400

Tabulation: Freq.  Numeric  Label

415

262

889

-9  Does not apply (do not have

bill)

0  Made partial payment or did not

pay

1  Paid in full

9,834

.

------------------------------------------------------------------------------------
Water, gas, and electric bills - How did you
EF6C_b
handle each of the following types of bills
last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF6C_B

Range: [-9,1]

Unique values: 3

Units: 1

Missing .: 9,834/11,400

Tabulation: Freq.  Numeric  Label

292

544

730
9,834

-9  Does not apply (do not have

bill)

0  Made partial payment or did not

pay

1  Paid in full
.

------------------------------------------------------------------------------------
EF6C_c

Phone, internet, and cable bills - How did
you handle each of the following types of
bills last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF6C_C

Range: [-9,1]

Unique values: 3

Units: 1

Missing .: 9,834/11,400

Tabulation: Freq.  Numeric  Label

245

411

910
9,834

-9  Does not apply (do not have

bill)

0  Made partial payment or did not

pay

1  Paid in full
.

------------------------------------------------------------------------------------
Car payment - How did you handle each of the
EF6C_d
following types of bills last month?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF6C_D

Range: [-9,1]

Unique values: 3

Units: 1

Missing .: 9,834/11,400

Tabulation: Freq.  Numeric  Label

792

244

530
9,834

-9  Does not apply (do not have

bill)

0  Made partial payment or did not

pay

1  Paid in full
.

------------------------------------------------------------------------------------
EF7

Based on your current financial situation,
what is the largest emergency expense that
you could handle right now using only your
savings?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: EF7

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,894
1,444
1,114
1,181
5,767

1  Under $100
2  $100 to $499
3  $500 to $999
4  $1,000 to $1,999
5  $2,000 or more

------------------------------------------------------------------------------------
In the past month, which of these statements
FD3
best describes the food eaten in your
household?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: FD3

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

7,678

2,957

562
203

1  Enough of the kinds of food we

wanted to eat

2  Enough, but not always the

kinds of food we wanted to eat

3  Sometimes not enough to eat
4  Often not enough to eat

------------------------------------------------------------------------------------
FD4

Please indicate whether the next statement
was often true, sometimes true, or never
true in the past month for the children
living in your household who are under 18
years old.

"The children were not eating enough because
we just couldn't afford enough food."

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: FD4

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 8,744/11,400

Tabulation: Freq.  Numeric  Label
70
245
2,341
8,744

1  Often true
2  Sometimes true
3  Never true
.

------------------------------------------------------------------------------------
E8_a

Arrested or taken into custody by the
police - Have you ever been:

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E8_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,894
1,506

0  No
1  Yes

------------------------------------------------------------------------------------
E8_b

Convicted of a criminal offense but never

received a prison sentence - Have you ever
been
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E8_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,757
643

0  No
1  Yes

------------------------------------------------------------------------------------
Convicted of a criminal offense and received
E8_c
a prison sentence - Have you ever been

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E8_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

11,189
211

0  No
1  Yes

------------------------------------------------------------------------------------
E1_a

Prescription medicine - During the past 12
months, was there a time when you needed
each of the following, but went without
because you couldn’t afford it?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E1_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,285
1,115

0  No
1  Yes

------------------------------------------------------------------------------------
E1_b

Seeing a doctor or specialist - During the
past 12 months, was there a time when you
needed each of the following, but went
without because you couldn’t afford it?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E1_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,719
1,681

0  No
1  Yes

------------------------------------------------------------------------------------
Mental health care or counseling - During the
E1_c
past 12 months, was there a time when you
needed each of the following, but went
without because you couldn’t afford it?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E1_C

Range: [0,1]

Unique values: 2

Tabulation: Freq.  Numeric  Label

10,383
1,017

0  No
1  Yes

Units: 1

Missing .: 0/11,400

------------------------------------------------------------------------------------
Dental care - During the past 12 months, was
E1_d
there a time when you needed each of the
following, but went without because you
couldn’t afford it?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E1_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,216
2,184

0  No
1  Yes

------------------------------------------------------------------------------------
E1_e

Follow-up care - During the past 12 months,
was there a time when you needed each of the
following, but went without because you
couldn’t afford it?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E1_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,360
1,040

0  No
1  Yes

------------------------------------------------------------------------------------
E2

During the past 12 months, have you had any
unexpected major medical expenses that you
had to pay out of pocket because they were
not completely paid for by insurance?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E2

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

8,676
2,724

0  No
1  Yes

------------------------------------------------------------------------------------
E2A

Approximately how much did you pay out of
pocket for unexpected major medical expenses
in the past 12 months?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E2A

Range: [-2,5]

Unique values: 6

Units: 1

Missing .: 8,676/11,400

Tabulation: Freq.  Numeric  Label
93
510
562
606
611
342
8,676

-2  Don’t know
1  $1 to $499
2  $500 to $999
3  $1,000 to $1,999
4  $2,000 to $4,999
5  $5,000 or higher
.

------------------------------------------------------------------------------------
E2B

Do you currently have any debt from medical
care you or your family members have
received?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E2B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

9,497
1,903

0  No
1  Yes

------------------------------------------------------------------------------------
Insurance through an employer or union - Are
E4_a
you currently covered by any of the
following types of health insurance or health
coverage plans?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E4_A

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

5,153
6,247

0  No
1  Yes

------------------------------------------------------------------------------------
E4_b

Insurance purchased directly from an
insurance company - Are you currently covered
by any of the following types of health
insurance or health coverage plans?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E4_B

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,026
1,374

0  No
1  Yes

------------------------------------------------------------------------------------
E4_c

Medicare or Medicaid - Are you currently
covered by any of the following types of
health insurance or health coverage plans?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E4_C

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

6,923
4,477

0  No
1  Yes

------------------------------------------------------------------------------------
E4_d

TRICARE, VA, or other military or veteran's
health care - Are you currently covered by
any of the following types of health
insurance or health coverage plans?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E4_D

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,652
748

0  No
1  Yes

------------------------------------------------------------------------------------
E4_e

Insurance purchased through a health
insurance exchange - Are you currently
covered by any of the following types of
health insurance or health coverage plans?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E4_E

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,898
502

0  No
1  Yes

------------------------------------------------------------------------------------
E4_f

Any other health insurance - Are you
currently covered by any of the following
types of health insurance or health coverage
plans?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: E4_F

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

10,675
725

0  No
1  Yes

------------------------------------------------------------------------------------
CH2A

Thinking about your family or primary
caregivers growing up, what was the highest
level of education achieved by any parent
or guardian?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: CH2A

Range: [-2,7]

Unique values: 9

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

441

-2  Don’t know

12
1,420
3,616
1,124
656
633
1,961
1,537

-1  Refused

1  Less than High School degree
2  High school degree or GED
3  Some college but no degree
4  Certificate or technical degree
5  Associate degree
6  Bachelor’s degree
7  Graduate degree

------------------------------------------------------------------------------------
Flag - order in which D36A and D36B are asked
DOV_D36_ORDER
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: DOV_D36

Range: [1,2]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

5,706
5,694

1  D36A shown first
2  D36B shown first

------------------------------------------------------------------------------------
Flag - amount of hypothetical pay change in question D36B
DOV_D36_AMOUNT
------------------------------------------------------------------------------------

Type: String (str33)

Unique values: 4

Missing "": 0/11,400

Tabulation: Freq.  Value

2,845  "decreased your pay by 1 percent"
2,841  "decreased your pay by 10 percent"
2,857  "decreased your pay by 5 percent"
2,857  "kept your pay the same for a year"

Warning: Variable has embedded blanks.

------------------------------------------------------------------------------------
Age
ppage
------------------------------------------------------------------------------------

Type: Numeric (byte)

Range: [18,100]

Unique values: 81

Units: 1

Missing .: 0/11,400

Mean: 51.6898
Std. dev.: 17.7718

Percentiles:

10%
27

25%
37

50%
53

75%
66

90%
75

------------------------------------------------------------------------------------
Age - 7 Categories
ppagecat
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPAGECAT

Range: [1,7]

Unique values: 7

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label
1  18-24
2  25-34
3  35-44
4  45-54
5  55-64
6  65-74

698
1,758
1,863
1,660
2,195
2,058

1,168

7  75+

------------------------------------------------------------------------------------
Age - 4 Categories
ppagect4
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPAGECT4

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label
1  18-29
2  30-44
3  45-59
4  60+

1,739
2,580
2,707
4,374

------------------------------------------------------------------------------------
Education (5 Categories)
ppeduc5
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPEDUC5

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

756
2,644

3,248

2,678
2,074

1  No high school diploma or GED
2  High school graduate (high

school diploma or the
equivalent GED)

3  Some college or Associate's

degree

4  Bachelor's degree
5  Master’s degree or higher

------------------------------------------------------------------------------------
Education (4 Categories)
ppeducat
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPEDUCAT

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

756
2,644

3,248

4,752

1  No high school diploma or GED
2  High school graduate (high

school diploma or the
equivalent GED)

3  Some college or Associate's

degree

4  Bachelor's degree or higher

------------------------------------------------------------------------------------
Current Employment Status
ppemploy
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPEMPLOY

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

5,454
1,548
4,398

1  Working full-time
2  Working part-time
3  Not working

------------------------------------------------------------------------------------
Race / Ethnicity
ppethm
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPETHM

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

7,776
1,209
515
1,523
377

1  White, Non-Hispanic
2  Black, Non-Hispanic
3  Other, Non-Hispanic
4  Hispanic
5  2+ Races, Non-Hispanic

------------------------------------------------------------------------------------
Gender
ppgender
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPGENDER

Range: [1,2]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

5,695
5,705

1  Male
2  Female

------------------------------------------------------------------------------------
Household Size
pphhsize
------------------------------------------------------------------------------------

Type: Numeric (byte)

Range: [1,10]

Unique values: 10

Mean: 2.63096
Std. dev.: 1.42529

Units: 1

Missing .: 0/11,400

Percentiles:

10%
1

25%
2

50%
2

75%
3

90%
4

------------------------------------------------------------------------------------
Housing Type
pphouse4
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPHOUSE4

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

8,230

1  A one-family house detached

from any other house

994

2  One-family condo or townhouse

1,742

attached to other units
3  Building with 2 or more

apartments

434

4  Other (mobile home, boat, RV,

van, etc.)

------------------------------------------------------------------------------------
Household Income
ppinc7
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPINC7

Range: [1,7]

Unique values: 7

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

461
911
1,860
1,828
1,579
2,125
2,636

1  Less than $10,000
2  $10,000 to $24,999
3  $25,000 to $49,999
4  $50,000 to $74,999
5  $75,000 to $99,999
6  $100,000 to $149,999
7  $150,000 or more

------------------------------------------------------------------------------------
Marital Status
ppmarit5
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPMARIT5

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

6,359
540
1,279
191
3,031

1  Now married
2  Widowed
3  Divorced
4  Separated
5  Never married

------------------------------------------------------------------------------------
MSA Status
ppmsacat
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPMSACAT

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,618
9,782

0  Non-Metro
1  Metro

------------------------------------------------------------------------------------
Region 4 - Based on State of Residence
ppreg4
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPREG4

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,991
2,532
4,246
2,631

1  Northeast
2  Midwest
3  South
4  West

------------------------------------------------------------------------------------
Region 9 - Based on State of Residence
ppreg9
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPREG9

Range: [1,9]

Unique values: 9

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

523
1,468
1,742
790
2,300
665
1,281
898
1,733

1  New England
2  Mid-Atlantic
3  East-North Central
4  West-North Central
5  South Atlantic
6  East-South Central
7  West-South Central
8  Mountain
9  Pacific

------------------------------------------------------------------------------------
Ownership Status of Living Quarters
pprent
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPRENT

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

8,459

2,774
167

1  Owned or being bought by you or

someone in your household

2  Rented for cash
3  Occupied without payment of

cash rent

------------------------------------------------------------------------------------
State
ppstaten
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPSTATEN

Range: [11,95]

Unique values: 51

Units: 1

Missing .: 0/11,400

Examples: 31
51
61
85

oh
de
ky
nm

------------------------------------------------------------------------------------
Presence of Household Members - Children 0-17
ppkid017
------------------------------------------------------------------------------------

Type: Numeric (byte)

Range: [0,8]

Unique values: 9

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Value

8,385  0
1,348  1
1,050  2
394  3
138  4
54  5
18  6
10  7
3  8

------------------------------------------------------------------------------------
Presence of Household Members - Adults 18+
ppt18ov
------------------------------------------------------------------------------------

Type: Numeric (byte)

Range: [1,10]

Units: 1

Unique values: 10

Missing .: 0/11,400

Mean:  2.135
Std. dev.: .944891

Percentiles:

10%
1

25%
2

50%
2

75%
2

90%
3

------------------------------------------------------------------------------------
Q26: Occupation (detailed) in current or main job
ppcm0160
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPCM0160

Range: [-2,35]

Unique values: 29

Units: 1

Missing .: 3/11,400

Examples: -2

1
16
29

Not asked
Management
Food Preparation and Serving
Other (Please specify)

------------------------------------------------------------------------------------
IND1: Industry (tight scale) in current or main job
ind1
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: IND1

Range: [1,27]

Unique values: 24

Units: 1

Missing .: 4,423/11,400

Examples: 10
16
27

.

Finance, Banking, and Insurance
Health Care (including Elder Care, Home Health Care)
Community/Non-Profit Organizations (including
Religious  and Political Organizations)

------------------------------------------------------------------------------------
GOVEMP1: Employer type
ppcm1301
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPCM1301

Range: [-2,5]

Unique values: 7

Units: 1

Missing .: 3/11,400

Tabulation: Freq.  Numeric  Label

4,404
11
1,236
3,807
863

965
111
3

-2  Not asked
-1  Refused

1  Government
2  Private-for-profit company
3  Non-profit organization

including tax exempt and
charitable organizations

4  Self-employed
5  Working in the family business
.

------------------------------------------------------------------------------------
UNION100

UNION100: Are you a member of a labor union
or an employee association similar to a
union?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: UNION100

Range: [-2,2]

Units: 1

Unique values: 4

Missing .: 5/11,400

Tabulation: Freq.  Numeric  Label

5,359
17
793
5,226
5

-2  Not asked
-1  Refused

1  Yes
2  No
.

------------------------------------------------------------------------------------
Date member completed core adult survey
ppcmdate
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [20061206,20231011]

Units: 1

Unique values: 560

Missing .: 3/11,400

Mean: 2.0e+07
Std. dev.: 5241.74

Percentiles:

10%

90%
2.0e+07  2.0e+07  2.0e+07  2.0e+07  2.0e+07

75%

25%

50%

------------------------------------------------------------------------------------
Status
------------------------------------------------------------------------------------

Armed Forces Status

Type: Numeric (byte)

Label: STATUS

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 709/11,400

Tabulation: Freq.  Numeric  Label
30
18
14
1,034
9,595
709

1  Active Duty
2  Currently Reserves
3  Currently National Guard
4  Veteran, including reserves
5  None of the above
.

------------------------------------------------------------------------------------
Date member completed Health 1 survey
pph1date
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [20200623,20231030]

Units: 1

Unique values: 574

Missing .: 773/11,400

Mean: 2.0e+07
Std. dev.: 3597.01

Percentiles:

10%

90%
2.0e+07  2.0e+07  2.0e+07  2.0e+07  2.0e+07

25%

75%

50%

------------------------------------------------------------------------------------
Q1: In general, would you say your physical health is. . .?
pph10001
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPH10001

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 793/11,400

Tabulation: Freq.  Numeric  Label

929
3,908
4,065

1  Excellent
2  Very good
3  Good

1,422
283
793

4  Fair
5  Poor
.

------------------------------------------------------------------------------------
Date member completed Financial Services survey
ppfsdate
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [20191124,20231031]

Units: 1

Unique values: 713

Missing .: 1,547/11,400

Mean: 2.0e+07
Std. dev.: 5617.85

Percentiles:

10%

90%
2.0e+07  2.0e+07  2.0e+07  2.0e+07  2.0e+07

50%

25%

75%

------------------------------------------------------------------------------------
Q1: When it comes to decisions regarding your
ppfs0001
household's financial activities (such as
banking and investment decisions), which of
the following statements best describe your
involvement?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPFS0001

Range: [1,3]

Unique values: 3

Units: 1

Missing .: 1,560/11,400

Tabulation: Freq.  Numeric  Label

4,644
4,117

1,079

1,560

1  I make most of the decisions
2  Another household member and I

share in the decisions

3  Another household member makes

most of the decisions

.

------------------------------------------------------------------------------------
Q22: What is the approximate total amount of
ppfs0596
your household's savings and investments?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPFS0596

Range: [1,7]

Unique values: 7

Units: 1

Missing .: 1,839/11,400

Tabulation: Freq.  Numeric  Label

3,896
1,163
1,323
922
822
964
471
1,839

1  Under $50,000
2  $50,000 - $99,999
3  $100,000 - $249,999
4  $250,000 - $499,999
5  $500,000 - $999,999
6  $1,000,000 or more
7  Not sure
.

------------------------------------------------------------------------------------
Q108: Where do you think your credit score falls?
ppfs1482
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPFS1482

Range: [1,6]

Unique values: 6

Units: 1

Missing .: 1,597/11,400

Tabulation: Freq.  Numeric  Label

270
431
988
2,205
5,270
639
1,597

1  Very poor
2  Poor
3  Fair
4  Good
5  Excellent
6  Don’t know
.

------------------------------------------------------------------------------------
Date member completed Hispanic survey
pphidate
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [20200410,20231029]

Units: 1

Unique values: 281

Missing .: 9,966/11,400

Mean: 2.0e+07
Std. dev.: 5928.75

Percentiles:

10%

90%
2.0e+07  2.0e+07  2.0e+07  2.0e+07  2.0e+07

50%

25%

75%

------------------------------------------------------------------------------------
Q0: What language do you usually speak at home?
pphi0001
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPHI0001

Range: [1,6]

Unique values: 6

Units: 1

Missing .: 9,969/11,400

Tabulation: Freq.  Numeric  Label
32
131
291

1  Only Spanish
2  More Spanish than English
3  Both Spanish and English

424
548
5
9,969

equally

4  More English than Spanish
5  Only English
6  Neither Spanish nor English
.

------------------------------------------------------------------------------------
Race, Census categories
ppracem
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPRACEM

Range: [1,6]

Unique values: 6

Units: 1

Missing .: 5/11,400

Tabulation: Freq.  Numeric  Label
1  White
2  Black or African American
3  American Indian or Alaska

9,053
1,278
108

458
14

484
5

Native

4  Asian
5  Native Hawaiian/Pacific

Islander
6  2+ races
.

------------------------------------------------------------------------------------
Are you Spanish, Hispanic, or Latino?
pphispan
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPHISPAN

Range: [1,8]

Unique values: 5

Tabulation: Freq.  Numeric  Label

Units: 1

Missing .: 0/11,400

9,877
823

165
78
457

1  No, I am not
2  Yes, Mexican, Mexican-American,

Chicano

3  Yes, Puerto Rican
4  Yes, Cuban, Cuban American
8  Yes, Other

------------------------------------------------------------------------------------
Date member completed Public Affairs 1 survey
ppp1date
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [20200911,20231103]

Units: 1

Unique values: 414

Missing .: 416/11,400

Mean: 2.0e+07
Std. dev.:  3785.2

Percentiles:

10%

90%
2.0e+07  2.0e+07  2.0e+07  2.0e+07  2.0e+07

25%

75%

50%

------------------------------------------------------------------------------------
Gender identity
pppagnid
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPPAGNID

Range: [0,3]

Unique values: 4

Units: 1

Missing .: 765/11,400

Tabulation: Freq.  Numeric  Label

10,474
44
57
60
765

0  Cisgender
1  Transgender
2  Other
3  Non-Binary
.

------------------------------------------------------------------------------------
Q230: Which of the following best describes how you think of yourself?
pppa_lgb
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPPA_LGB

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 769/11,400

Tabulation: Freq.  Numeric  Label

346
9,624
466
195
769

1  Gay or lesbian
2  Straight, that is, not gay
3  Bisexual
4  Something else
.

------------------------------------------------------------------------------------
Date member completed Public Affairs 2 survey
ppp2date
------------------------------------------------------------------------------------

Type: Numeric (long)

Range: [20201002,20231106]

Units: 1

Unique values: 591

Missing .: 709/11,400

Mean: 2.0e+07
Std. dev.:  5292.9

Percentiles:

10%

90%
2.0e+07  2.0e+07  2.0e+07  2.0e+07  2.0e+07

25%

50%

75%

------------------------------------------------------------------------------------
QEG22: Are you a citizen of the United States?
ppp20197
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPP20197

Range: [1,2]

Unique values: 2

Units: 1

Missing .: 420/11,400

Tabulation: Freq.  Numeric  Label

10,764
216
420

1  Yes
2  No
.

------------------------------------------------------------------------------------
Q5: In total, how many years have you lived in the United States?
pphi0018
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPHI0018, but 75 nonmissing values are not labeled

Range: [1,81]

Unique values: 75

Units: 1

Missing .: 11,024/11,400

Examples: .
.
.
.

------------------------------------------------------------------------------------
pph12003

Q190: Are you blind or do you have serious
difficulty seeing even when wearing glasses?
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPH12003

Range: [1,4]

Unique values: 2

Units: 1

Missing .: 798/11,400

Tabulation: Freq.  Numeric  Label

235
10,367
798

1  Yes
4  No
.

------------------------------------------------------------------------------------
Q190: Are you deaf or do you have serious difficulty hearing?
pph12004
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPH12004

Range: [1,4]

Unique values: 2

Units: 1

Missing .: 809/11,400

Tabulation: Freq.  Numeric  Label

367
10,224
809

1  Yes
4  No
.

------------------------------------------------------------------------------------
Q190: Do you have serious difficulty walking or climbing stairs?
pph12005
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPH12005

Range: [1,4]

Unique values: 2

Units: 1

Missing .: 809/11,400

Tabulation: Freq.  Numeric  Label

897
9,694
809

1  Yes
4  No
.

------------------------------------------------------------------------------------
pph12006

Q190: Because of a physical, mental, or
emotional condition, do you having difficulty
running errands?

------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPH12006

Range: [1,4]

Unique values: 2

Units: 1

Missing .: 798/11,400

Tabulation: Freq.  Numeric  Label

664
9,938
798

1  Yes
4  No
.

------------------------------------------------------------------------------------
Q190: Do you having difficulty dressing or bathing?
pph12007
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: PPH12007

Range: [1,4]

Unique values: 2

Units: 1

Missing .: 796/11,400

Tabulation: Freq.  Numeric  Label

253
10,351
796

1  Yes
4  No
.

------------------------------------------------------------------------------------
(unlabeled)
field_month
------------------------------------------------------------------------------------

Type: Numeric (float)

Range: [10,11]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Value

11,245  10
155  11

------------------------------------------------------------------------------------
(unlabeled)
field_day
------------------------------------------------------------------------------------

Type: Numeric (float)

Range: [1,31]

Unique values: 17

Mean: 21.6458
Std. dev.: 3.30038

Units: 1

Missing .: 0/11,400

Percentiles:

10%
20

25%
20

50%
21

75%
23

90%
25

------------------------------------------------------------------------------------
Household Size
pphhsize5
------------------------------------------------------------------------------------

Type: Numeric (float)

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Value

2,104  1
4,642  2
1,997  3
1,525  4
1,132  5

------------------------------------------------------------------------------------
variable imputation flag
[variablename]_iflag
------------------------------------------------------------------------------------

Type: Numeric (float)

Range: [0,1]

Unique values: 2

Units: 1

Numeric  Description

0  Value not imputed

1  Value imputed

------------------------------------------------------------------------------------
Race/Ethnicity - 5 categories
race_5cat
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: race_5cat

Range: [1,5]

Unique values: 5

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label
1  White
2  Black
3  Hispanic
4  Asian
5  Other

7,776
1,209
1,523
447
445

------------------------------------------------------------------------------------
Income (I40) - 4 cat - <25,25-49,50-99,100+
inc_4cat_50k
------------------------------------------------------------------------------------

Type: Numeric (float)

Label: inc_4cat_50k

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

1,972
1,963
3,311
4,154

1  Less than $25,000
2  $25,000-$49,999
3  $50,000-$99,999
4  $100,000 or more

------------------------------------------------------------------------------------
Education - 4 categories, less than hs separate
educ_4cat
------------------------------------------------------------------------------------

Type: Numeric (byte)
Label: educ_4cat_nodip

Range: [1,4]

Unique values: 4

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

560

1  Less than a high school degree

2,185
3,828

4,827

2  High school degree or GED
3  Some college/technical or

associates degree

4  Bachelor's degree or more

------------------------------------------------------------------------------------
Would handle $400 expense with cash or equivalent
pay_casheqv
------------------------------------------------------------------------------------

Type: Numeric (float)

Label: YesNoRefused

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

3,917
7,483

0  No
1  Yes

------------------------------------------------------------------------------------
Doing okay financially
atleast_okay
------------------------------------------------------------------------------------

Type: Numeric (byte)

Label: atleast_okay

Range: [0,1]

Unique values: 2

Units: 1

Missing .: 0/11,400

Tabulation: Freq.  Numeric  Label

3,076
8,324

0  No
1  Yes

------------------------------------------------------------------------------------
(unlabeled)
control
------------------------------------------------------------------------------------

Type: String (str18)

Unique values: 3

Missing "": 4,124/11,400

Tabulation: Freq.  Value

4,124  ""

442  "Private for-profit"

1,721  "Private nonprofit"
5,113  "Public"

Warning: Variable has embedded blanks.


