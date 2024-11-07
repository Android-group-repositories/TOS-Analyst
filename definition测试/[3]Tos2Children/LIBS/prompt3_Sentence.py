

"""

"""
            
P3_promptType1="""
I will enter a<text>later
Please read<text>and answer a few questions
Does<text>describe the requirements related to children's data processing?
Please output whether the use of the service is allowed, the use of children's data, and the age that children need to reach to use the relevant functions

{# Type1 #  ,  <subject  ;  Actions  ;   object  ;   Modifier  ;   purpose  ;  condition >  ,  <service not for  : ....>}

notice : <subject  ;  Actions  ;   object  ;   Modifier  ;   purpose  ;  condition > There should not be more than 6 elements present

To understanding elements

subject : Entity performing the operation
Actions : Data Operations
object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier for object.
Modifier: Modifier for object
Purpose: It explains the goal behind an action.It's the "why" of the action
condition: A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'


There are 3 ways to represent <Operations on users in this age range>:
1. Clear age range like : 0-13 , 13-16 , over 16
2. children as defined by COPPA, CCPA, CPRA, or similar US state privacy laws
3. only children or Other expressions for "children"

只有服务
input example 1:
The Service is not intended for and should not be used by anyone under the age of 16. 
output example 1:
{# Type1 #  ,  <The Service  ;  is not intended for and should not be used  ;   by anyone under the age of 16  ;   NULL;   NULL  ;  NULL>  ,  <service not for  : Under 16 years old > }


同意 + 服务
input example 2:
Only if you have obtained verifiable and voluntary consent from the child's parents or guardians can you use our services and be bound by COPPA, CCPA, or GDPR.
output example 2:
{# Type1 #  ,  <you  ;  can  ;    use our services and be bound by COPPA, CCPA, or GDPR  ;   NULL  ;    NULL  ;   must have obtained verifiable and voluntary consent from the child's parents or guardians  > , <service not for  : NULL>}

同意 + 服务
input example 3:
if the company uses software licensed by Nuance for online websites, services, or products primarily aimed at children shall it not send any child data to Nuance.
output example 3:
{# Type1 #  ,  <company  ;  shall not send  ;     any child data   ;   to Nuance  ;    NULL  ;   if the company uses software licensed by Nuance for online websites, services, or products primarily aimed at children > , <service not for  : NULL>}




<Text>:
"""     

P3_promptType2="""
I will enter a<text>later
Please read<text>and answer a few questions
Does<text>describe the requirements related to children's data processing?
Please output whether the use of the service is allowed, the use of children's data, and the age that children need to reach to use the relevant functions

{# Type2 #  ,  <subject  ;  Actions  ;   object  ;   Modifier  ;   purpose  ;  condition >  ,  <service not for  : ....>  ,  <Third party is: ...... >}

notice : <subject  ;  Actions  ;   object  ;  Modifier  ;  purpose > There should not be more than 5 elements present
To understanding Purpose and condition

subject : The entity responsible for data processing
Actions : Data Operations
object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier for object.
Modifier: Modifier for object
Purpose: It explains the goal behind an action.It's the "why" of the action
condition: A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'

There are 3 ways to represent <Operations on users in this age range>:
1. Clear age range like : 0-13 , 13-16 , over 16
2. children as defined by COPPA, CCPA, CPRA, or similar US state privacy laws
3. only children or Other expressions for "children"

<Consent conditions> :If there is no consent-related condition in the text, then even if the App obtains the consent of the user's parents, it cannot collect data. At the same time, you need to fill in <  NULL  :  In this case, the consent obtained is invalid.  > in the <Consent conditions> item.

&有具体操作 第三方
input example 1:
Developers are not allowed to intentionally share data of users under the age of 16 with Pollfish
output example 1:
{# Type1 #  ,  <Developers  ;  are not allowed to intentionally shar  ;   data of users under the age of 16  ;   with Pollfish  ;   NULL  ;  NULL>  ,  <service not for  : Under 16 years old > }


&有具体行为了，服务那层意思不需要了
input example 2:
If your services or apps are directed at children, they may be subject to COPPA regulations. You are not allowed to share personal identifiers such as IP addresses, IDFA/IDFV, Android ID, Google Play Advertising ID, Google Play store referrer, WindowsHardware ID, Windows NetworkID, Windows Phone device ID, and UUIDs with Adjust partners or other third parties
output example 2:
{# Type2 #  ,  <You    ;    are not allowed to share  ;  such as IP addresses, IDFA/IDFV, Android ID, Google Play Advertising ID, Google Play store referrer, WindowsHardware ID, Windows NetworkID, Windows Phone device ID, and UUIDs   ; with Adjust partners or other third parties  ;   NULL  ;  NULL >  ,  <Third party is: Adjust partners or other third parties  >  ,  <service not for  : directed at children >}


&具体数据共享
input example 3:
You must declare and guarantee that you will not transfer any personal information of individuals under the age of 13 to MoPub, as defined by COPPA.
output example 3:
{# Type2 #  ,  <You must declare and guarantee that you  ;  will not transfer  ;    any personal information of individuals under the age of 13  ;   to MoPub  ;    NULL  ;  NULL  >  ,  <Third party is: MoPub  >  ,  <service not for  : individuals under the age of 13>}


input example 4:
If your applications are targeted at children under COPPA, CCPA, CPRA, or similar US privacy laws, you must obtain verifiable user or parental consent for collecting and sharing data with InMobi.
output example 4:
{# Type2 #  ,  <your applications  ;  collect and share  ;  Your Data  ;  with InMobi   ;   NULL   ;  you are required to obtain verifiable consent from users or parent  >  ,  <service not for  : children,  defined under laws such as COPPA,CCPA,CPRA >  ,  <Third party is: InMobi  >}



同意 + 服务 
input example 5:
You agree not to request or permit any Ad Partner or Attribution Partner to transmit any personal information from children under the age of 17 to Flurry
output example 5:
{# Type2 #  ,  <You agree not to request or permit any Ad Partner or Attribution Partner ;  to transmit  ;   any personal information  ;from children under the age of 17,to Flurry     ;   NULL  ;  NULL  >  ,   <service not for  : under the age of 17 >  ,  <Third party is: Flurry  >}



<Text>:
"""     
P3_promptType3 = """
I will input <text> later
The <text> may contain content shared by a third party
Please read <text> and generate a tuple as output:

{# Type3 #  ,  <subject  ;  Actions  ;   object  ;   Modifier  ;   purpose  ;  condition >  ,  <service not for  : ....>  ,  <to opt-out  : ...... >}


notice : <subject  ;  Actions  ;   object  ;   Modifier  ;   purpose  ;  condition > There should not be more than 5 elements present
To understanding Purpose and condition





Input example 1:
Services targeted to children under 13 must opt out of tailoring  in any Twitter embedded Post  by setting the opt-out parameter to be 'true'
output example 1:
{# Type3 #  ,  <Services targeted to children under 13 ; must opt out  ;   the opt-out parameter to be 'true' ;  ttailoring  in any Twitter embedded Post  by setting the opt-out parameter to be 'true'   ;   NULL  ;  NULL  >  ,  <service not for  : under the age of 13 >  ,  <to opt-out  : tailoring  in any Twitter embedded Post and/or embedded timelines >  ,  }




Input example 2:
Customers should configure services to ensure that end-user data from children is not transmitted to any integration partners,

output example 2:
{# Type3 #  ,  <Customers  ;  should configure  ;   services ;  NULL   ;    to ensure that end-user data from children is not transmitted to any integration partners  ;  NULL  >  ,  <service not for  : children >  ,  <to opt-out  : end-user data from children is transmitted to any integration partners >  }


<Text>:
"""

# P3_promptType4 = """
# I will input <text> later
# The <text> that will be opt-out in the text
# Please read <text> and generate a tuple as output:

# {# Type4 #  ,  <subject  ;  Actions  ;  object  ;  Items  ;  purpose  >  ,  <opt-out conditions>  ,   <Other conditions>}
# notice : <subject  ;  Actions  ;   object  ;  Modifier  ;  purpose > There should not be more than 5 elements present
# To understanding Purpose and condition

# subject : The entity responsible for data processing
# Actions : Data Operations
# object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier for object.
# Modifier: Modifier for object
# Purpose: It explains the goal behind an action.It's the "why" of the action
# condition: A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'


# And organize these elements into a question, asking whether the privacy policy is compliant by describing the situation, 
# which can include specific values of the child's age to achieve accurate questioning. Please output in the following format:

# Input example:
# Developers must provide an opportunity for parents to opt-out before sending any contact information to OneSignal.

# Output example:
# {# Type4 #  ,  <Developers  ;  not sending  ;  NULL  ;  any contact information  ;  to OneSignal  >  ,  <except provide an opportunity for parents to opt-out>  ,   <NULL>}

# <Text>:
# """