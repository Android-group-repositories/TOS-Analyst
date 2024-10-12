P3_background = '''
You will then extract and understand the information from the input TOS <text>, answer for different types and format the output content

'''

# TYPE 相关prompt 7
P3_promptType1 = '''
I will enter a <text> later
If TOS requires developers to describe their actions on specific data types in the privacy policy, please output in the following format.
{#type1#,  <subject  ;  Actions  ;  object  ;  object source/target  ;  purpose  ;  condition>  ,  <privacy policy condition>}

notice:<subject  ;  Actions  ;   object  ;   Modifier  ;   purpose  ;   condition> There should be 6 elements present

To understanding elements

To understanding Purpose and condition

subject : The entity responsible for data processing(If Tos is a requirement for the content of Privacy Policy, then the subject can be Privacy Policy)
Actions : Data Operations
object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier and Object-Complement for object.
object source/target: if object is a data item, object source/target is where data come from or where data go to
Purpose: It explains the goal behind an action.It's the "why" of the action , The purpose is usually expressed by an infinitive
condition: Conditions are usually introduced by adverbs.. Usually starts with a condition, such as "if" or "unless", "except", etc.Or a conditional adverbial clause guided by 'Without'
(example:in "Customer must not process, send or store export-controlled information without obtaining required export licenses or government approvals. obtaining required export licenses or government approvals." . the Condition is "without obtaining required export licenses or government approvals")

If there are multiple nouns after a verb, they can be separated by a comma
If the meaning of purpose and condition is not strong, use NULL to indicate none

Because we focus on data, the object part of the following sentence has limited arrangement of data
Input example1:
You must develop a privacy policy that clearly and accurately informs end users about the personal data you collect 
Output example1:
{#type1#,  <  a privacy policy  ;  informs end users   ;  personal data you collect    ;  NULL  ;  NULL  ; NULL>  ,  <need a privacy policy>}

Input example1:
You must develop a privacy policy informs end users how you utilize and distribute such information to third parties, including for advertising purposes.
Output example1:
{#type1#,  <  a privacy policy  ;  informs end users and partner  ;  how you utilize and distribute such information    ;  to third parties  ;  including for advertising purposes  ;  NULL>  ,  <need a privacy policy>}




<Text>:
            '''

# third party 7
P3_promptType2 = """
I will enter a third party related third party related <text> later

If TOS requires developers to describe terms related to third parties in their privacy policy, please output in the following format.
{#type2#,  <subject  ;  Actions  ;  object  ;  object source/target  ;  purpose  ;  condition>  ,  <link/url condition>  ,  <Third party is: ....>}
notice: <subject  ;  Actions  ;   object  ;   object source/target  ;   purpose  ;   condition> There should not be more than 6 elements present

To understanding Purpose and condition
subject : The entity responsible for data processing(If Tos is a requirement for the content of Privacy Policy, then the subject can be Privacy Policy)
Actions : Data Operations
object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier and Object-Complement for object.
object source/target: if object is a data item, object source/target is where data come from or where data go to
Purpose: It explains the goal behind an action.It's the "why" of the action , The purpose is usually expressed by an infinitive
condition: Conditions are usually introduced by adverbs.. Usually starts with a condition, such as "if" or "unless", "except", etc.Or a conditional adverbial clause guided by 'Without'
(example:in "Customer must not process, send or store export-controlled information without obtaining required export licenses or government approvals. obtaining required export licenses or government approvals." . the Condition is "without obtaining required export licenses or government approvals")

<ink/url condition> : Developers need to provide a link in the privacy policy



If no, please answer nothing

Because we focus on data, the object part of the following sentence has limited arrangement of data
Input example1:
You must make your privacy notice or privacy policy accessible to Business Users in your Stripe App listing within the Stripe Apps Marketplace
Output example1:
{#type2#,  < you  ;  must  prepare  ;  your privacy notice or privacy policy  ;  NULL  ;  to make your Business Users accessible to it  ;  in your Stripe App listing within the Stripe Apps Marketplac>  ,  <NO link>  ,  <Third party is: NULl>}


Input example2:
You must make your privacy notice or privacy policy  include a link to it in your Stripe App listing within the Stripe Apps Marketplace.
Output example2:
{#type2#,  < your privacy policy   ;  must  include  ;  a link to it  ;  NULL  ;  NULL  ;  in your Stripe App listing within the Stripe Apps Marketplac>  ,  <need to provide a link>  ,  <Third party is: NULL>}


Input example3: 
You must present your service's privacy policy to individuals before they can download, install, or sign up for your service. 
Output example3:
{#type2#,  < your privacy policy  ;  must  disclose  ;  The data you collect from users of your service, how you use and share that data (including with X).  ;  NULL  ;  NULL  ;  NULL>  ,  <NO link>  ,  <Third party is: NULL>}


Input example4: 
You must present your service's privacy policy and disclose at least the following information: The data you collect from users of your service, how you use and share that data (including with X).

Output example4:
{#type2#,  < your privacy policy  ;  must  disclose  ;  The data you collect from users of your service, how you use and share that data (including with twitter).  ;  share that data with X  ;  NULL  ;  NULL>  ,  <NO link>  ,  <Third party is: twitter>}


Input example: 
Your privacy policy should incorporate by reference and link to the Snap Privacy Policy.

Output example5:
{#type2#,  < your privacy policy  ;  should incorporate by reference and link   ;  the Snap Privacy Polic  ;  NULL  ;  NULL  ;  NULL>  ,  <need to provide a link>  ,  <Third party is: Snap>}


<Text>:
"""

# opt-out

P3_promptType3 = """            
Then I will enter a <text> about opt-out
If TOS requires developers to describe and opt out related terms in their privacy policy, please output in the following format.
{#type3-Q1#, <  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,  <mention condition>  ,  <guidance/link condition> }
<mention condition>: Developers need to mention content related to opt out in the privacy policy
<guidance/doc condition>: In addition to mentioning opt out, developers also need to prepare guidance to guide users through opt out

If not, please answer nothing


Input example
provide a mechanism for which an End User may opt-out of receiving targeted ads Output Example,A link to guide users on optout

Output example:
{#type3#,<  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,   <need to mention opt-out>  ,  <need link to guide how to opt-out> }


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Input example
This privacy policy must, at a minimum, clearly describe the data sets that are collected or permitted to be collected, including a clear statement that such data may be shared with specific third parties for certain use cases and that mechanisms for opting out be clearly established.

Output example:
{#type3#, <  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,  <need to mention opt-out>  ,  <NULL> }


<text>:
"""
