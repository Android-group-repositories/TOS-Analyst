P3_background = '''


'''

# TYPE 相关prompt 7
P3_promptType1 = '''
I will enter a <text> later
If TOS requires developers to describe their actions on specific data types in the privacy policy, please output in the following format.
{#type1#,  <subject  ;  Actions  ;  object  ;  object source/target  ;  purpose  ;  condition>  ,  <need privacy policy?>}

notice:<subject  ;  Actions  ;   object  ;   object source/target  ;   purpose  ;   condition> There should be 6 elements present

To understanding elements

To understanding Purpose and condition

subject : The entity responsible for data processing(If Tos is a requirement for the content of Privacy Policy, then the subject can be Privacy Policy)
Actions : Data Operations
object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier and Object-Complement for object.
object source/target: if object is a data item, object source/target is where data come from or where data go to,If the source or destination of the data is not mentioned here, answer NULL 

Purpose: It explains the goal behind an action.It's the "why" of the action , The purpose is usually expressed by an infinitive
condition: Conditions are usually introduced by adverbs.. Usually starts with a condition, such as "if" or "unless", "except", etc.Or a conditional adverbial clause guided by 'Without'
(example:in "Customer must not process, send or store export-controlled information without obtaining required export licenses or government approvals. obtaining required export licenses or government approvals." . the Condition is "without obtaining required export licenses or government approvals")

<need privacy policy?>:If the sentence is related to providing a Privacy Policy answer<need a privacy policy>. Otherwise, answer <NULL>

If there are multiple nouns after a verb, they can be separated by a comma
If the meaning of purpose and condition is not strong, use NULL to indicate none

Because we focus on data, the object part of the following sentence has limited arrangement of data

Here are some examples:
=================================================
Input example1:
You must develop a privacy policy that clearly and accurately informs end users about the personal data you collect 
Output example1:
{#type1#,  <  a privacy policy  ;  informs end users   ;  personal data you collect    ;  NULL  ;  NULL  ; NULL>  ,  <need privacy policy?>}

Input example2:
You must develop a privacy policy informs end users how you utilize and distribute such information to third parties, including for advertising purposes.
Output example2:
{#type1#,  <  a privacy policy  ;  informs end users and partner  ;  how you utilize and distribute such information    ;  to third parties  ;  including for advertising purposes  ;  NULL>  ,  <need a privacy policy>}

Input example3:
The privacy policy must comply with and be consistent with the terms and requirements of the Agreement and the WeChat or Weixin Privacy Policy.
Output example3:
{#type1#,  <  Thea privacy policy  ;    comply with and be consistent with    ;    the terms and requirements of the Agreement and the WeChat or Weixin Privacy Policy  ;  NULL  ;  NULL  ;  NULL>  ,  <need a privacy policy>}

Input example4:
The privacy policy must specifically address the use of personal information for behaviorally targeted online advertising.
Output example4:
{#type1#,  <  Thea privacy policy  ;    address    ;    the use of personal information  ;  NULL  ;  for behaviorally targeted online advertising  ;  NULL>  ,  <need a privacy policy>}


Input example5:
The privacy policy must specifically address the use of personal information for behaviorally targeted online advertising.
Output example5:
{#type1#,  <  a privacy policy  ;    provide    ;    your Application link to the Snap Privacy Policy ;  NULL  ;  NULL  ;  easily accessible>  ,  <need a privacy policy>}


=================================================




Here are the <Text> you need to analyze:
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
object source/target: if object is a data item, object source/target is where data come from or where data go to,If the source or destination of the data is not mentioned here, answer NULL 
Purpose: It explains the goal behind an action.It's the "why" of the action , The purpose is usually expressed by an infinitive


condition: Conditions are usually introduced by adverbs.. Usually starts with a condition, such as "if" or "unless", "except", etc.Or a conditional adverbial clause guided by 'Without'
(example:in "Customer must not process, send or store export-controlled information without obtaining required export licenses or government approvals. obtaining required export licenses or government approvals." . the Condition is "without obtaining required export licenses or government approvals")

<link/url condition> : If the sentence mentions the need to provide a link, output<needed to provide a link>. If the word 'link' does not appear, output "NO link"



If no, please answer nothing

Because we focus on data, the object part of the following sentence has limited arrangement of data


Here are some examples:
=================================================
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


Input example5: 
Your privacy policy should incorporate by reference and link to the Snap Privacy Policy.

Output example5:
{#type2#,  < your privacy policy  ;  should incorporate by reference and link   ;  the Snap Privacy Polic  ;  NULL  ;  NULL  ;  NULL>  ,  <need to provide a link>  ,  <Third party is: Snap>}



Input example5:
The privacy policy should also disclose the use of third parties and cookies for attribution and serving targeted advertisements.
Output example5:
{#type1#,  <  Thea privacy policy  ;    should disclose    ;    the use of third parties and cookies  ;  NULL  ;  for attribution and serving targeted advertisements  ;  NULL>  ,  <NO link>  ,  <Third party is: NULL>}


=================================================

Here are the <Text> you need to analyze:
"""

# opt-out

P3_promptType3 = """            
Then I will enter a <text> about opt-out
If TOS requires developers to describe and opt out related terms in their privacy policy, please output in the following format.
{#type3-Q1#, <  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,  <mention condition>  ,  <guidance/link condition> }
<mention condition>: Developers need to mention content related to opt out in the privacy policy
<guidance/doc condition>: If there is a mention in<text>to prepare a link to guide opt out, output<needed link to guide how to opt out>. If not, output NULL directly.

If not, please answer nothing


Input example1:
provide a mechanism for which an End User may opt-out of receiving targeted ads Output Example , A link to guide users on optout

Output example1:
{#type3#,<  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,   <need to mention opt-out>  ,  <need link to guide how to opt-out> }


Input example2;
This privacy policy must, at a minimum, clearly describe the data sets that are collected or permitted to be collected, including a clear statement that such data may be shared with specific third parties for certain use cases and that mechanisms for opting out be clearly established.

Output example2:
{#type3#, <  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,  <need to mention opt-out>  ,  <NULL> }


<text>:
"""
