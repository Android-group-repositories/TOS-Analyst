P3_background = '''
Then you will extract information from the input TOS <text> and output the following content
{ #type1#,   <subject  ;  Actions  ;  object  ;  Data Items  ;  purpose  ;  condition> }
{"question":"......."}

The subject is usually the developer who needs to comply with these Tos. Common 'subjects' include' you ',' developer ',' customer ', and' user'
The question is the ToS's requirement for privacy policy, which requires the privacy policy to describe some content to ensure compliance

'''


P3_promptType1 = '''
I will enter a <text> later
Please read <text> and answer a few questions for me

Does <text> describe the processing of specific data?
If yes, please output in the following format. If there are multiple groups, please output multiple groups

{ #type1#,  <subject  ;  Actions  ;  object  ;  Modifier  ;  purpose  ;  condition>}


notice : <subject  ;  Actions  ;   object  ;  Modifier  ;  purpose > There should not be more than 5 elements present
To understanding Purpose and condition

subject : The entity responsible for data processing
Actions : Data Operations

object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier and Object-Complement for object.
Modifier: Modifier for object
Purpose: It explains the goal behind an action.It's the "why" of the action
condition: A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'


If there are multiple nouns after a verb, they can be separated by a comma
If the meaning of purpose and condition is not strong, use NULL to indicate none



Input example1:
You may not do any of the following: Collect personal information, financial information, business information or any other information directly from Your User, a PayPal User, or any other third party on behalf of PayPal. 

Output example1:
{#type1#,<You  ;  Collect  ;  personal information, financial information, business information or any other information  ;  from Your User, a PayPal User, or any other third party on behalf of PayPal  ;  NULL  ;  NULL>}


Input example2:
10.1.4 Prohibited Activities.  You may not do any of the following:
(d) Sell,  lease, rent, transfer, assign or otherwise disclose PayPal User Information to a third party;
(f) Use the PayPal User Information to engage in marketing or other sales activities.

Output example2:
{#type1#,<You  ;  not Sell, lease, rent, transfer, assign or otherwise disclose  ;  PayPal User Information to a third party  ;  to a third party  ;  NULL  ;  NULL>}
{#type1#,<You  ;  not Use  ;  User Information  ;  NULL   ;   in marketing or other sales activitie  ;  NULL>}



Input example3:  
You must not collect, retain, or use any Business Services Data except as expressly permitted under these Snap Developer Terms. ;

Output example3:
{#type1#,<You  ;  must not collect, retain, or use  ;  Business Services  ;   Data   ;  NULL  ;  except as expressly permitted under these Snap Developer Terms.>}

Input example4:  
You must not solicit, collect, store, cache, proxy, or use Facebook or Instagram login credentials of other Users.

Output example4:
{#type1#,<You  ;  must not solicit, collect, store, cache, proxy, or use  ;  Facebook or Instagram login credentials of other Users  ;   other Users   ;  NULL  ;  NULL>}




<Text>:
'''
            
            
P3_promptType2 = """
I will input <text> later
The <text> may contain content shared by a third party
Please read <text> and generate a tuple as output:

{#type2,# , <subject  ;  verb  ;  object  ;  Modifier  ;  purpose  ;  condition>  ,  <Third party is: ....>}

notice : <subject  ;  Actions  ;   object  ;  Modifier  ;  purpose > There should not be more than 5 elements present
To understanding Purpose and condition

subject : The entity responsible for data processing
Actions : Data Operations
object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier for object.
Modifier: Modifier for object
Purpose: It explains the goal behind an action.It's the "why" of the action
condition: A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'


Input example1:
"You shall not make available to a third party, any token, key, password or other login credentials to the X API"

Output example1:
{#type2,#  <You  ;  shall not make available  ;  any token, key, password or other login credentials to the X API to a third party  ;  to a third party   ;  NULL  ;  NULL>}

Input example2:
"You will maintain the security of the X API, and will not make available to any third party, any token, key, password or other login credentials to the X API."

Output example2:
{#type2,#  <You  ;  will maintain  ;  the security of the X API to a third party  ;  to a third party  ;  NULL  ;   NULL>  ,  <Third party is: any third party>}
{#type2,#  <You  ;  will not make available  ;  any token, key, password or other login credentials to a third party  ;   to a third party   ;  NULL  ;   NULL>  ,  <Third party is: to any third party>}

<Text>:
"""



