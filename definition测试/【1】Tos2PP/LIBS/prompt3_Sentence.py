P3_background = '''


'''
P3_elements_prompt = '''
notice:<subject  ;  actions  ;   object  ;   object source/target  ;   purpose  ;   condition> There should be 6 elements present

To understanding elements

To understanding Purpose and condition

subject : The entity responsible for data processing(If Tos is a requirement for the content of Privacy Policy, then the subject can be Privacy Policy)
actions : Data Operations
object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier and Object-Complement for object,If the subject is a Privacy Policy, the object may contain Tos that require the Privacy Policy to be declared (operations+data).

object source/target: if object is a data item, object source/target is where data come from or where data go to,If the source or destination of the data is not mentioned here, answer NULL .If the subject is Privacy Policy, the source/target may be "from user" or "share to" third-party, etc(Sharing and collection can appear simultaneously)

purpose  : It explains the goal behind an action.It's the "why" of the action , The purpose is usually expressed by an infinitive

condition: Conditions are usually introduced by adverbs.. Usually starts with a condition, such as "if" or "unless", "except", etc.Or a conditional adverbial clause guided by 'Without'
(example:in "Customer must not process, send or store export-controlled information without obtaining required export licenses or government approvals. obtaining required export licenses or government approvals." . the Condition is "without obtaining required export licenses or government approvals")
'''

# TYPE 相关prompt 7
P3_promptType1 = '''
I will enter a <text> later
If TOS requires developers to describe their actions on specific data types in the privacy policy, please output in the following format.
{#type1#,  <subject  ;  Actions  ;  object  ;  object source/target  ;  purpose  ;  condition> }
'''  +P3_elements_prompt + '''

If there are multiple nouns after a verb, they can be separated by a comma
If the meaning of purpose and condition is not strong, use NULL to indicate none

Because we focus on data, the object part of the following sentence has limited arrangement of data

Here are some examples:
=================================================
Input example1:
You must develop a privacy policy that clearly and accurately informs end users about the personal data you collect 
Output example1:
{#type1#,  <  a privacy policy  ;  informs end users   ;  personal data you collect    ;  NULL  ;  NULL  ; NULL> }

Input example2:
privacy policy provide notice of  use of a tracking pixel, agent or any other visitor identification technology that collects, uses, shares and stores data about end users of your Application 
Output example2:
{#type1#,  <  privacy policy ;  provide notice of   ;  privacy policy provide notice of  use of a tracking pixel, agent or any other visitor identification technology that collects, uses, shares and stores data      ;  about end users of your Application  ; NULL  ; NULL> }

Input example3:
Such privacy policy shall also mention use of third parties service and use of cookies for the purposes of attribution and/or serving targeted Advertisements.
Output example3:
{#type1#,  <  Such privacy policy ;  shall also mention   ;  use of third parties service and use of cookies    ;  NULL  ;  for the purposes of attribution and/or serving targeted Advertisements.  ; NULL> }


Input example4:
The privacy policy must specifically address the use of personal information for behaviorally targeted online advertising.
Output example4:
{#type1#,  <  The privacy policy  ;    address    ;    the use of personal information  ;  NULL  ;  for behaviorally targeted online advertising  ;  NULL>}



=================================================
'''

# third party 7
P3_promptType2 = '''
I will enter a third party related third party related <text> later

If TOS requires developers to describe terms related to third parties in their privacy policy, please output in the following format.
{#type2#,  <subject  ;  Actions  ;  object  ;  object source/target  ;  purpose  ;  condition>  ,  <third-party condition>}
'''  +P3_elements_prompt + '''
<third-party condition>: Output according to the meaning of the sentence: 
1 When it only comes to third parties : <Third party is: ....  >     
2 When it comes to third-party links : < need LINK to : ....> 
The third party may be :
    - SDK name 
    - a vague "third party"



If no, please answer nothing

Because we focus on data, the object part of the following sentence has limited arrangement of data


Here are some examples:
=================================================

Input example1:
Your privacy policy must describe how third parties (such as Tapjoy) collect , use , and share mobile device advertising identifiers and other personal information 
Input example1:
{#type2#,  <Your privacy policy  ;  must describe  ;   how third parties (such as Tapjoy) collect , use , and share mobile device advertising identifiers and other personal information  ;  NULL  ;  NULL  ;  NULL>  ,  <Third party is: Tapjoy > }

Input example2:
You have a privacy policy that provides end users with clear information about cookies, device-specific information, location information and other information stored on, accessed on, or collected from end users' devices in connection with the AdSense-SDK-Service 
Input example2:
{#type2#,  <You have a privacy policy  ;  provides end users ;   with clear information about cookies, device-specific information, location information and other information stored on, accessed on, or collected ;  from end users' devices in connection with the SDK Service ;  NULL  ;  NULL>  ,  <Third party is: AdSense-SDK-Service > }

Input example3:
your service's privacy policy must disclose how you use and share  data you collected from user to Twitter and other third parties
Output example3:
{#type2#,  <your service's privacy policy  ;  must disclose  ;   collect,use and share user's data ;  from user,share to third parties ;  NULL  ;  NULL>  ,  <Third party is: Twitter  > }


Input example4:
Customer's privacy policy should disclose RevenueCat's and Stripe's processing of personally identifiable information relating to such users
Output example4:
{#type2#,  < Customer's privacy policy ;  dshould disclose  ;  RevenueCat's and Stripe's processing of personally identifiable information relating to such users  ;  NULL  ;  NULL  ;  NULL>  ,  <Third party is: RevenueCat and Stripe  > }


Input example5:
Your privacy policy should incorporate by reference and link to the Snap Privacy Policy.
Output example5:
{#type2#,  < your privacy policy  ;  should incorporate by reference and link   ;  the Snap Privacy Polic  ;  NULL  ;  NULL  ;  NULL>}

=================================================

Here are the <Text> you need to analyze:
'''

# opt-out

P3_promptType3 = """            
Then I will enter a <text> about opt-out
If TOS requires developers to describe and opt out related terms in their privacy policy, please output in the following format.
{#type3-Q1#, <  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,  <opt-out condition>  ,  <opt-out guidance/link condition> }

<opt-out condition> : Output according to the meaning of the sentence: 
1 need to mention opt out:<mention opt out>
2 need to mention what to opt out:<mention opt out : .....>,The object of opt out may be:
    - advertising Behavior
    - data processing activities
    - etc.
3 no need to opt out:<NULL>

<guidance/doc condition>: Output according to the meaning of the sentence: 
1 <need link to guidance how to opt-out >
2 no guidance or linkmentioned : <NULL>


Input example1:
provide a mechanism for which an End User may opt-out of receiving targeted ads Output Example , A link to guide users on optout

Output example1:
{#type3#,<  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,   <mention opt-out : receiving targeted ads>  ,  <need link to guide how to opt-out> }


Input example2;
This privacy policy must, at a minimum, clearly describe the data sets that are collected or permitted to be collected, including a clear statement that such data may be shared with specific third parties for certain use cases and that mechanisms for opting out be clearly established.

Output example2:
{#type3#, <  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,  <mention opt-out : data processing >  ,  <NULL> }


增加情况 3 没有data processing DONE

Input example3:
You provide sufficient notice for mechanisms of Opt Out (defined below) elections which You agree to comply with, if applicable to the Inventory.
Output example3:
{#type3#, <  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  ;  NULL  >  ,  <mention opt out>  ,  <NULL> }


<text>:
"""
print(P3_promptType1)