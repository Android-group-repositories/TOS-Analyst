P3_background = '''
Then you will extract information from the input TOS <text> and output the following content
{ #type1-Q1-i#, <YES>,  <subject  ;  Actions  ;  object  ;  Data Items  ;  purpose  ;  condition> }
{"question":"......."}

The subject is usually the developer who needs to comply with these Tos. Common 'subjects' include' you ',' developer ',' customer ', and' user'
The question is the ToS's requirement for privacy policy, which requires the privacy policy to describe some content to ensure compliance

'''

# { #type1-Q1-i#, <YES>, <subject  ;  verb  ;  object  ;  noun  ;  purpose  ;  condition>}

# TYPE 相关prompt
P3_promptType1 = '''
I will enter a <text> later
Please read <text> and answer a few questions for me

1. Does <text> describe the processing of specific data?
If yes, please output in the following format. If there are multiple groups, please output multiple groups

{ #type1-Q1-i#, <YES>, <subject  ;  Actions  ;  object  ;  Data Items  ;  purpose  ;  condition>}
<Operations on users in this age range>

notice：<subject  ;  Actions  ;   object  ;   Data Items  ;   purpose  ;   condition> There should not be more than 6 elements present
To understanding Purpose and condition

subject ：The entity responsible for data processing
Actions : Data Operations
object  : Object that is in a passive position in data processing
Data Items: The specific units that are operated on during the data operation process
Purpose: It explains the goal behind an action.It's the "why" of the action
condition：A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'


If there are multiple nouns after a verb, they can be separated by a comma
If the meaning of purpose and condition is not strong, use NULL to indicate none


And organize these elements into a question asking whether the privacy policy meets compliance by describing this situation. Please output it in the following format:
{"question":"......."}

If no, just answer
{#type1-Q1#, <NO>}

Input example:
You may not do any of the following: Collect personal information, financial information, business information or any other information directly from Your User, a PayPal User, or any other third party on behalf of PayPal. 

Output example:
{#type1-Q1-1#,<YES>,<You  ;  Collect  ;  from Your User, a PayPal User, or any other third party on behalf of PayPal  ;  personal information, financial information, business information or any other information  ;  NULL  ;  NULL>}
{Question: "Does the developer indicate that they will collect personal information, financial information, business information, or any other information from end-users, PayPal users, or any other third party representing PayPal? As a result, it leads to non compliant behavior"}


Input example:
10.1.4 Prohibited Activities.  You may not do any of the following:
(d) Sell,  lease, rent, transfer, assign or otherwise disclose PayPal User Information to a third party;
(f) Use the PayPal User Information to engage in marketing or other sales activities.

Output example:
{#type1-Q1-1#,<YES>,<You  ;  not Sell, lease, rent, transfer, assign or otherwise disclose  ;  to a third party  ;  PayPal User Information  ;  NULL  ;  NULL>}
{Question: "Has the developer indicated that they will sell, lease, rent, transfer, distribute, or otherwise disclose PayPal user information to third parties? Therefore, it can lead to non compliant behavior"}
{#type1-Q1-2#,<YES>,<You  ;  not Use  ;  User  ;  Information  ;   in marketing or other sales activitie  ;  NULL>}
{Question: "Has the developer indicated that they will use PayPal user information for marketing or other sales activities.? As a result, it leads to non compliant behavior"}


Input example:  if Sentence include conditional conjunctions like "if" "except" or "unless"
You must not collect, retain, or use any Business Services Data except as expressly permitted under these Snap Developer Terms. ;

Output example:
{#type1-Q1-1#,<YES>,<You  ;  must not collect, retain, or use  ;  Business Services  ;   Data   ;  NULL  ;  except as expressly permitted under these Snap Developer Terms.>}
{Question: "Has the developer indicated that they will collect, retain, or use any Business Services Data? Therefore, it can lead to non compliant behavior"}



<Text>:
            '''
            
            
P3_promptType2 = """
I will enter a <text> later
Please read <text> and answer a few questions for me

1. Does this <text> imply sharing with a third party or being collected by a third party?


If so,  Please output a 6-tuple containing a third party (or a third-party pronoun):
<subject, verb, object, noun, purpose, condition>

{#type2-Q1-i,# <YES>, <subject  ;  verb  ;  object  ;  noun  ;  purpose  ;  condition>}
And organize these elements into a question asking whether the privacy policy meets compliance by describing this situation. Please output it in the following format:
{"question":"......."}

notice：<subject  ;  Actions  ;   object  ;   Data Items  ;   purpose  ;   condition> There should not be more than 6 elements present
To understanding Purpose and condition

subject ：The entity responsible for data processing
Actions : Data Operations
object  : Object that is in a passive position in data processing
Data Items: The specific units that are operated on during the data operation process
Purpose: It explains the goal behind an action.It's the "why" of the action
condition：A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'

If no, please answer only
{#type2-Q2#, <NO>} , no question

Input example1:
"You shall not make available to a third party, any token, key, password or other login credentials to the X API"

Output example1:
{#type2-Q1-1,# <YES>, <You  ;  shall not make available  ;  to a third party  ;  any token, key, password or other login credentials to the X API  ;  NULL  ;  NULL>}
{"question":"Has the developer indicated that they will provide X API tokens, keys, passwords, or other login credentials to third parties? As a result, it leads to non compliant behavior"}



Input example2:
"You will maintain the security of the X API, and will not make available to any third party, any token, key, password or other login credentials to the X API."

Output example2:
{#type2-Q1-1,# <YES>, <You  ;  will maintain  ;  to a third party  ;  the security of the X API  ;  NULL  ;   NULL>}
{#type2-Q1-2,# <YES>, <You  ;  will not make available  ;  to a third party  ;   any token, key, password or other login credentials  ;  NULL  ;   NULL>}
{"question":"Has the developer indicated that they will provide X API tokens, keys, passwords, or other login credentials to any third party? As a result, it leads to non compliant behavior"}


<Text>:
"""



            
            
P3_promptType1 = """            
I will enter a<text>later
Please read<text>and answer a few questions
Has the condition related to the age of the child been described?
Please output the restricted operation and the age requirements for executing the operation
{# Type 1-Q1-i #,<Yes>,<Data Processing Operation>,<Age Condition>}
And organize these elements into a question, asking whether the privacy policy is compliant by describing the situation, 
which can include specific values of the child's age to achieve accurate questioning. Please output in the following format:
{“question”：“……”}

Input example:
The Service is intended for use by individuals who are at least 16 years old, and the customer is responsible for ensuring that no one under the age of 16 uses the Service.


Output example:
{# Type 1-Q1-1 #,<YES>,<no one uses the Service>,<under the age of 16>}


<Text>:
"""
            
P3_promptType2="""
I will enter a<text>later
Please read<text>and answer a few questions
Has the operation related to children's data and other conditions beyond age been described?
Please output restricted operations and age independent conditions required to perform the operation
{# Type 1-Q1-i #,<Yes>,<Data Processing Operation>,<Age Condition>,<Other Condition/Consent Condition>}
And organize these elements into a question, asking whether the privacy policy is compliant by describing the situation, 
which can include specific values of the child's age to achieve accurate questioning. Please output in the following format:
{“question”：“……”}




Input example:
"OneSignal permits developers to use the service in applications “directed to children under 13” but Licensee must meet certain obligations, including obtaining verifiable parental consent and an opportunity to opt-out prior to sending a push token, email, or other contact information to OneSignal.
"



Output example:
{# Type 1-Q1-1 #  ,  <Yes>  ,  <use the service in applications>  ,  <children under 13>  ,  <must meet certain obligations>}
{# Type 1-Q1-3 #  ,  <Yes>  ,  <to sending a push token, email, or other contact information to OneSignal>  ,  <children under 13>  ,  <obtaining verifiable parental consent>}




<Text>:
"""            