P3_background = '''
You will then extract and understand the information from the input TOS <text>, answer for different types and format the output content

'''

# TYPE 相关prompt 7
P3_promptType1 = '''
I will enter a <text> later
If TOS requires developers to describe their actions on specific data types in the privacy policy, please output in the following format.
{#type1#,  <subject  ;  Actions  ;  object  ;  Modifier  ;  purpose  ;  condition>  ,  <privacy policy condition>}

notice:<subject  ;  Actions  ;   object  ;   Modifier  ;   purpose  ;   condition> There should be 6 elements present

To understanding elements

subject : The entity responsible for data processing
Actions : Data Operations
object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier for object.
Modifier: Modifier for object
Purpose : It explains the goal behind an action.It's the "why" of the action
condition : A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'
privacy policy condition : Describe some requirements for the use of privacy policy, such as whether developers need to prepare a privacy policy

If no, just answer nothing


Input example:

You must develop and follow a privacy policy that clearly and accurately informs end users about the personal data you collect and how you utilize and distribute such information to us and other third parties, including for advertising purposes.

Output example:
{#type1#,  <  You  ;  must develop and follow  ;  a privacy policy   ;  NULL  ;  informs end users and partner about the personal data you collect and how you utilize   ; NULL>  ,  <need a privacy policy>}


<Text>:
            '''

# third party 7
P3_promptType2 = """
I will enter a third party related third party related <text> later

If TOS requires developers to describe terms related to third parties in their privacy policy, please output in the following format.
{#type2#,  <subject  ;  Actions  ;  object  ;  Data Items  ;  purpose  ;  condition>   ,  <link/url condition>}

notice:<subject  ;  Actions  ;   object  ;   Data Items  ;   purpose  ;   condition> There should not be more than 6 elements present
To understanding Purpose and condition

subject :The entity responsible for data processing
Actions : Data Operations
object  : Object that is in a passive position in data processing
Data Items: The specific units that are operated on during the data operation process
Purpose: It explains the goal behind an action.It's the "why" of the action
condition:A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'
<ink/url condition> : Developers need to provide a link in the privacy policy


If no, please answer nothing


Input example:
You must make your privacy notice or privacy policy accessible to Business Users and include a link to it in your Stripe App listing within the Stripe Apps Marketplace.

Output example:
{#type2#,  < you  ;  must  prepare  ;  your privacy notice or privacy policy  ;  in your Stripe App listing within the Stripe Apps Marketplace  ;  to make your Business Users accessible to it  ;  NULL>  ,  <include a link to privacy policy>}

Input example: 
You must present your service's privacy policy to individuals before they can download, install, or sign up for your service. 
It must disclose at least the following information: The data you collect from users of your service, how you use and share that data (including with X).

Output example:
{#type2#,  < your privacy policy  ;  must  disclose  ;  The data you collect from users of your service, how you use and share that data (including with X).  ;  NULL  ;  NULL  ;  NULL>  ,  <NULL>}



<Text>:
"""

# opt-out

P3_promptType3 = """            
Then I will enter a <text> about opt-out
If TOS requires developers to describe and opt out related terms in their privacy policy, please output in the following format.
{#type3#, <  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,  <mention condition>  ,  <guidance/link condition> }
<mention condition>: Developers need to mention content related to opt out in the privacy policy
<guidance/doc condition>: In addition to mentioning opt out, developers also need to prepare guidance to guide users through opt out

If not, please answer nothing


Input example
provide a mechanism for which an End User may opt-out of receiving targeted ads Output Example,A link to guide users on optout

Output example:
{#type3#, <  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,  <need to mention opt-out>  ,  <need link to guide how to opt-out> }


Input example
This privacy policy must, at a minimum, clearly describe the data sets that are collected or permitted to be collected, including a clear statement that such data may be shared with specific third parties for certain use cases and that mechanisms for opting out be clearly established.

Output example:
{#type3#, <  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,  <need to mention opt-out>  ,  <NULL> }


<text>:
"""
