
            
P3_promptType1="""
I will enter a<text>later
Please read<text>and answer a few questions
Does<text>describe the requirements related to children's data processing?
Please output whether the use of the service is allowed, the use of children's data, and the age that children need to reach to use the relevant functions

{# Type1 #  ,  <subject  ;  Actions  ;   object  ;   Modifier  ;   purpose  >  ,  <Age requirement>  ,  <Other conditions>}

notice : <subject  ;  Actions  ;   object  ;  Modifier  ;   purpose > There should not be more than 5 elements present

To understanding elements

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




And organize these elements into a question, asking whether the privacy policy is compliant by describing the situation, 
which can include specific values of the child's age to achieve accurate questioning. Please output in the following format:
{"question"："……"}

Input example1:
The customer must verify that all users of the SDK Service are above the age of 16, adhering to the age restriction policy of the Service.
Output example1:
{# Type1 #  ,  <customer  ;  must verify  ;   all users of the SDK Service  ;   above the age of 16  ;   adhering to the age restriction policy of the Service  >  ,  <over 16>  ,  <NULL>}


Input example2:
The Service is intended for use by individuals who are at least 16 years old, and the customer is responsible for ensuring that no one under the age of 16 uses the Service.
Output example2:
{# Type1 #  ,  <customer  ;  ensuring  ;   NULL  ;   no one under the age of 16 uses the Service  ;   NULL  >  ,  <at least 16 years old>  ,  <NULL>}



<Text>:
"""     

P3_promptType2="""
I will enter a<text>later
Please read<text>and answer a few questions
Does<text>describe the requirements related to children's data processing?
Please output whether the use of the service is allowed, the use of children's data, and the age that children need to reach to use the relevant functions

{# Type2 #  ,  <subject  ;  Actions  ;  object  ;  Modifier  ;  purpose  >  ,  <Consent conditions>  ,  <Other conditions>}

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


And organize these elements into a question, asking whether the privacy policy is compliant by describing the situation, 
which can include specific values of the child's age to achieve accurate questioning. Please output in the following format:
{"question"："……"}

Input example:
(iii) ensure it has or obtains all necessary rights, lawful basis, and, where required by law, consents (including parental consent in the case of any End User Data related to Children) to: 
(a) collect and use the End User Data; 
(b) enable the processing of End User Data by AppsFlyer as per the terms of the Agreement; 

Output example:
{# Type2 #  ,  <NULL  ;  obtains  ;   NULL  ;   all consents  ;   to  collect and use the End User Data  >  ,  <ensure it has or obtains all necessary consents (including parental consent in the case of any End User Data related to Children)>  ,  <NULL>}

<Text>:
"""     
P3_promptType3 = """
I will input <text> later
The <text> may contain content shared by a third party
Please read <text> and generate a tuple as output:

{# Type3 #  ,  <subject  ;  Actions  ;  object  ;  Modifier  ;  purpose  >  ,  <Share  ,  Specific Data  ,  to Object>  ,  <Other conditions>}


notice : <subject  ;  Actions  ;   object  ;  Modifier  ;  purpose > There should not be more than 5 elements present
To understanding Purpose and condition

subject : The entity responsible for data processing
Actions : Data Operations
object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier for object.
Modifier: Modifier for object
Purpose: It explains the goal behind an action.It's the "why" of the action
condition: A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'

And organize these elements into a question, asking whether the privacy policy is compliant by describing the situation, 
which can include specific values of the child's age to achieve accurate questioning. Please output in the following format:

Input example:
Customer shall configure the Services to ensure that End User Data from Children is not transmitted to any Integrated Partner except where both the Integrated Partner's service is specifically tailored to support and process End User Data from Children and the Integrated Partner permits Customer to transmit such End User Data related to Children to such Integrated Partner.

Output example:
{# Type3 #  ,  <  Customer  ;   shall configure the Services to ensure not transmit  ;  End User Data  ;  Data  ;  to any Integrated Partner>  ,  <Third party is: Integrated Partner>  ,  < Customer transmit  ,  End User Data  ,  to any Integrated Partner>  ,  <except where both the Integrated Partner's service is specifically tailored to support and process End User Data from Children and the Integrated Partner permits Customer to transmit such End User Data related to Children to such Integrated Partner.>}

<Text>:
"""

P3_promptType4 = """
I will input <text> later
The <text> that will be opt-out in the text
Please read <text> and generate a tuple as output:

{# Type4 #  ,  <subject  ;  Actions  ;  object  ;  Items  ;  purpose  >  ,  <opt-out conditions>  ,   <Other conditions>}
notice : <subject  ;  Actions  ;   object  ;  Modifier  ;  purpose > There should not be more than 5 elements present
To understanding Purpose and condition

subject : The entity responsible for data processing
Actions : Data Operations
object  : The object in a sentence receives the action of the verb and is essential for completing the meaning of the transitive verb, need include Modifier for object.
Modifier: Modifier for object
Purpose: It explains the goal behind an action.It's the "why" of the action
condition: A condition is what must happen before something else can. usually includes conditional conjunctions such as' if 'or' less'


And organize these elements into a question, asking whether the privacy policy is compliant by describing the situation, 
which can include specific values of the child's age to achieve accurate questioning. Please output in the following format:

Input example:
Developers must provide an opportunity for parents to opt-out before sending any contact information to OneSignal.

Output example:
{# Type4 #  ,  <Developers  ;  not sending  ;  NULL  ;  any contact information  ;  to OneSignal  >  ,  <except provide an opportunity for parents to opt-out>  ,   <NULL>}

<Text>:
"""