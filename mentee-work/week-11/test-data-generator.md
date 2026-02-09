# Week 11 - Exercise 2: Test Data Generator

**Your Name:** Kamen Asenov  
**Date:** 2026-01-26  

---

## Script Output

======================================================================
SAUCEDEMO CHECKOUT TEST DATA GENERATOR
======================================================================

Generated 50 random records.

RANDOM DATA (50 records)
----------------------------------------------------------------------
#     First Name                Last Name                 Zip Code  
----------------------------------------------------------------------
1     Kathryn                   Montgomery                26098     
2     Cheryl                    Kennedy                   21508     
3     Jay                       Goodman                   78216     
4     Kevin                     Lynch                     35224     
5     Chris                     Savage                    22161     
6     Justin                    Byrd                      11650     
7     Michele                   Gomez                     46852     
8     Amber                     Smith                     31804     
9     Robert                    Combs                     42847     
10    Cynthia                   Edwards                   47747     
11    Joseph                    Phillips                  79759     
12    Daniel                    Molina                    80677     
13    Jamie                     Jensen                    39014     
14    John                      Stokes                    77232     
15    Donna                     Houston                   12006     
16    Dustin                    Butler                    42724     
17    Tara                      Davila                    71942     
18    Yolanda                   Peters                    59622     
19    Edward                    Stevenson                 67001     
20    Jimmy                     Dixon                     60491     
21    Joseph                    Mitchell                  27307     
22    Michelle                  Hopkins                   25565     
23    Jordan                    Mccarthy                  45146     
24    Eddie                     Campos                    62671     
25    Abigail                   Garner                    49334     
26    Catherine                 Krueger                   09797     
27    Sara                      Craig                     57477     
28    Bridget                   Rodriguez                 34998     
29    Christopher               Russo                     55565     
30    Christopher               Jones                     05061     
31    Mary                      Martin                    85684     
32    Jack                      Perry                     59583     
33    Gina                      Chavez                    76815     
34    Christine                 Wood                      18451     
35    Valerie                   Bradley                   17588     
36    Joseph                    Gonzalez                  69246     
37    Raymond                   Huerta                    05793     
38    Heather                   Murray                    98974     
39    Emily                     Hartman                   15404     
40    Samantha                  Lee                       71881     
41    Jeffery                   King                      40092     
42    Amy                       Knight                    54395     
43    Misty                     Torres                    14124     
44    Peter                     Wallace                   87586     
45    Robert                    Zimmerman                 59262     
46    Denise                    Turner                    00816     
47    Robert                    Smith                     89983     
48    Jaclyn                    Fields                    87263     
49    Cynthia                   Cole                      14443     
50    Dustin                    Miller                    37746     

Generated 8 edge-case records.

EDGE CASES
----------------------------------------------------------------------
#     First Name                Last Name                 Zip Code  
----------------------------------------------------------------------
1     A                         B                         12345     
2     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB 99999     
3     John-Paul                 O'Brien                   12345     
4     María                     José                      90210     
5     John123                   Doe456                    12345     
6     John Paul                 Van Der Berg              12345     
7     François                  Müller                    12345     
8     北京                        东京                        12345     

✅ Test data generation complete!
Code Explanation

What does fake.first_name() do?
It generates a realistic random first name using the Faker library (different value each run unless a seed is set).

Why use a loop for _ in range(count)?
To generate the same structure of data multiple times (e.g., 50 records) without writing repetitive code manually.

What is a tuple (first_name, last_name, zip_code)?
A tuple is an ordered, immutable group of values. Here it holds exactly 3 related fields for one checkout test data record.

Real QA Use Case

Time saved:

Manual: ~1–2 hours to prepare 50 unique datasets

Python: ~5–10 seconds to generate them

Savings: ~1–2 hours

How I would use this in real testing:
I would run the script before a checkout testing session, copy a set of generated names/zip codes, and use them to execute multiple checkout tests quickly, including edge cases for validation and input handling.

Reflection

What was challenging?
Understanding how to structure the data and print it in a readable way (table formatting) and choosing useful edge cases.

What will you use this for?
Generating test data for other forms as well (login, registration, address forms) to speed up manual testing and avoid repeating the same dummy values.