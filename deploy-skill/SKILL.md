---
name: GRE-VOCABULARY-TEST
description: Creates GRE level vocabulary test base on the words file provided. Takes user answer and outputs the result.
---



## Instructions

1. **Read the provided words**:
   First, read the words provided in `resources/WRDS.txt`.
   Each word is listed in new line. Word and its definitions are separated by colon symbol. Some words may have more than 1 deinition, these definitions are separated
   by coma.
   
2. **SELECT 1 random word**:
   Select 1  word randomly from the words file provided.
3. ** Define the test**:
    Type of the question is multiple choice question.
    The test question will be in this form: "Please select the correct definition of Selected-Word". 
    Selected-Word is place holder for the word which agent selected in step2.
    Select 3 other words from the same file which agent read in step1. Definitions of these words and the word which agent selected in step 2 will be options for the     test.
    Print each option in new line and label them A, B, C, and D. List options in a way that the correct answer to not be one of the options everytime.
    Following is an example of the question and the options:
    """ 
       Please select correct definition of Apposite :
       A) treating serious issues with deliberately inappropriate humor.
       B) ecstasy, exhilaration.
       C) appropriate, relevant, pertinent.
       D) distracted or absentminded. 
                                      """
    

4. **Take the user's answer**:
   Take user's answer as one of the A, B, C, or D.
   User will type one letter as nswer and will push enter. Take that as user's final answer for that question do not ask for furthur approval.

5. **Check the answer**:
   Check the user's answer. Do not show the result of test for each question.
   Show the results of test when user decides to end the test.
   If user ends the test show the results in this form: 
   """
         n1 correct answers
         n2 incorrect answers
                                                 """
   Here n1 is the count of the corect answers and n2 is the number of incorrect answers.