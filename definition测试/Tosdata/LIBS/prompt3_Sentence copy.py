

P3_promptType1 = '''
I will enter a <text> later
Please read <text> and answer a few questions for me

Does <text> describe the processing of specific data?
If yes, please output in the following format. If there are multiple groups, please output multiple groups

{ #type1-Q1-i#,  <subject  ;  Actions  ;  object  ;  Modifier  ;  purpose  ;  condition>}


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
{#type1-Q1-1#,<You  ;  Collect  ;  personal information, financial information, business information or any other information  ;  from Your User, a PayPal User, or any other third party on behalf of PayPal  ;  NULL  ;  NULL>}


Input example2:
10.1.4 Prohibited Activities.  You may not do any of the following:
(d) Sell,  lease, rent, transfer, assign or otherwise disclose PayPal User Information to a third party;
(f) Use the PayPal User Information to engage in marketing or other sales activities.

Output example2:
{#type1-Q1-1#,<You  ;  not Sell, lease, rent, transfer, assign or otherwise disclose  ;  PayPal User Information to a third party  ;  to a third party  ;  NULL  ;  NULL>}
{#type1-Q1-2#,<You  ;  not Use  ;  User Information  ;  NULL   ;   in marketing or other sales activitie  ;  NULL>}



Input example3:  
You must not collect, retain, or use any Business Services Data except as expressly permitted under these Snap Developer Terms. ;

Output example3:
{#type1-Q1-1#,<You  ;  must not collect, retain, or use  ;  Business Services  ;   Data   ;  NULL  ;  except as expressly permitted under these Snap Developer Terms.>}

Input example4:  
You must not solicit, collect, store, cache, proxy, or use Facebook or Instagram login credentials of other Users.

Output example4:
{#type1-Q1-1#,<You  ;  must not solicit, collect, store, cache, proxy, or use  ;  Facebook or Instagram login credentials of other Users  ;   other Users   ;  NULL  ;  NULL>}




<Text>:
'''
            
            
P3_promptType2 = """
I will input <text> later
The <text> may contain content shared by a third party
Please read <text> and generate a tuple as output:

{#type2-Q1-1,# , <subject  ;  verb  ;  object  ;  Modifier  ;  purpose  ;  condition>  ,  <Third party is: ....>}

notice : <subject  ;  Actions  ;   object  ;  Modifier  ;  purpose > There should not be more than 5 elements present
To understanding Purpose and condition

subject : The entity responsible for data processing
Actions : Data Operations
object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier for object.
Modifier: Modifiers are usually used to d involving conditions and purposes.

Purpose: It explains the goal behind an action.It's the "why" of the action , The purpose is usually expressed by an infinitive (to/for+verb prototype), such as "to finish the task"

condition: A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'


Input example1:
"You shall not make available to a third party, any token, key, password or other login credentials to the X API"

Output example1:
{#type2-Q1-1,#  <You  ;  shall not make available  ;  any token, key, password or other login credentials to the X API to a third party  ;  to a third party   ;  NULL  ;  NULL>}

Input example2:
"You will maintain the security of the X API, and will not make available to any third party, any token, key, password or other login credentials to the X API."

Output example2:
{#type2-Q1-1,#  <You  ;  will maintain  ;  the security of the X API to a third party  ;  to a third party  ;  NULL  ;   NULL>  ,  <Third party is: any third party>}
{#type2-Q1-2,#  <You  ;  will not make available  ;  any token, key, password or other login credentials to a third party  ;   to a third party   ;  NULL  ;   NULL>  ,  <Third party is: to any third party>}

<Text>:
"""





# =======================

# P3_promptType4 = """
# I will input <text> later
# The <text> that will be opt-out in the text
# Please read <text> and generate a tuple as output:

# {#Type4 #  ,  <subject  ;  Actions  ;  object  ;  Modifier  ;  purpose  >  ,  <opt-out conditions>  ,   <Other conditions>}
# notice : <subject  ;  Actions  ;   object  ;  Modifier  ;  purpose > There should not be more than 5 elements present
# To understanding Purpose and condition

# subject : The entity responsible for data processing
# Actions : Data Operations
# object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier for object.

# Modifier: Modifiers are usually used to d involving conditions and purposes.

# Purpose: It explains the goal behind an action.It's the "why" of the action , The purpose is usually expressed by an infinitive (to/for+verb prototype), such as "to finish the task"
    
# condition: A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'


# And organize these elements into a question, asking whether the privacy policy is compliant by describing the situation, 
# which can include specific values of the child's age to achieve accurate questioning. Please output in the following format:

# Input example:
# Developers must provide an opportunity for parents to opt-out before sending any contact information to OneSignal.

# Output example:
# {#Type4 #  ,  <Developers  ;  not sending  ;  NULL  ;  any contact information  ;  to OneSignal  >  ,  <except provide an opportunity for parents to opt-out>  ,   <NULL>}

# <Text>:
# """