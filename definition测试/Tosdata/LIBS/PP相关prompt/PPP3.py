P3_background = '''
Then you will extract information from the input TOS <text> and output the following content
{ #type1-Q1-i# , <subject, verb, object, noun, purpose, condition>}
{"question":"......."}

The question is the ToS's requirement for privacy policy, which requires the privacy policy to describe some content to ensure compliance
'''
    
'''
You will then extract information from the input <text> and output the following
{ #type1-Q1-i# , <subject, verb, object, noun, purpose, condition>}
{"question":"......."}

The question is about the ToS's requirements for privacy policy, 
which requires the privacy policy to describe some content to ensure compliance.

'''

# TYPE 相关prompt
P3_promptType1 = '''
I will enter a <text> later
Please read <text> and answer a few questions for me
1. Does <text> describe the processing of specific data?
If yes, please output in the following format. If there are multiple groups, please output multiple groups
{ #type1-Q1-i# , <subject, verb, object, noun, purpose, condition>,}
{}
To understanding Purpose and condition
Purpose: It explains the goal behind an action.It's the "why" of the action
condition：A condition is what must happen before something else can. The privacy policy sentence has no 'if' or 'unless,'  
etc,so no condition is given."


If there are multiple nouns after a verb, they can be separated by a comma
If the meaning of purpose and condition is not strong, use N/A to indicate none


And organize these elements into a question asking whether the privacy policy meets compliance by describing this situation. Please output it in the following format:
{"question":"......."}

If no, just answer
{#type1-Q1#, <NO>}

2. Do developers need to specify what information will be processed in privacy policy?
{ #type1-Q2# , need clearly state information }

If no, just answer
{#type1-Q1#, <NO>}




Input example:
You should develop and adhere to a privacy policy that clearly and accurately describes to end users what personal data you collect and how you use and share such information with us and other third parties (including for advertising)

Output example:
{#type1-Q1-1 ,<You; Collect; End user; Personal data; N/A; N/A>}
{"question":"Does the following privacy policy text mention the collection of end user personal data?"}


{#type1-Q1-2 ,<You; Share with ; us and other third parties; Such information,personal data; N/A; N/A>}
{"question":"Does the following privacy policy text mention the sharing of personal data with tos writers and third parties?"}



<Text>:
            '''
            
            
P3_promptType2 = """
I will enter a <text> later
Please read <text> and answer a few questions for me

1. <text>Do you need to explain whether you have a cooperative relationship with a third party?

If yes, please enter the cooperative object in the following format. If there are multiple groups, please output multiple groups
It is better to specify the name of the third party

{#type2-Q1-i, , <Third party is: ....>}
Organize these elements into a question, asking whether a paragraph of text describes this situation, please output in the following format
{"question:........"}

If there is no group, please answer only
{#type2-Q1#, <No>third party mentioned>}

<subject, verb, object , noun, purpose, condition>

2. Is there a requirement to clearly explain and share data with third parties
If it involves the object of sharing, answer

{#type2-Q2# , <Share,Specific Data,to Object>}
Organize these elements into a question, asking whether a paragraph of text describes this situation, please output in the following format
{"question:........"}

If no, please answer only
{#type2-Q2#, <NO>} , no question

3. Do you want to display third-party links in the privacy policy?
If yes, please output in the following format
{#type2-Q3# , <Need to link to...>}
Organize these elements into a question, asking whether a paragraph of text describes this situation, please output in the following format
{"question:........"}

If no, please answer
{#type2-Q3#, <No> third-party links} , no question
<Text>:

Input example:
Be transparent to users about Mixpanel's collection of registration and other information through the Mixpanel website.

Output example:
{#type2-Q1#, <Third party is: Mixpanel>}
{"question":"Does the privacy policy mention Mixpanel?"}

{#type2-Q2# , <Mixpanel, collects, user, registration and other information, N/A, N/A>}
{"question":"Does the privacy policy mention Mixpanel in the context of collecting user registration and other information through the Mixpanel website?"}

{#type2-Q3# , <Need to link to Flurry privacy policy>}
{"question":"Does the following text contain a link about Mixpanel?"}

<Text>:
            """
            
            
P3_promptType3 = """            
Then I will enter a <text>
Please read <text> and answer a few questions about "opt-out"

1. Is it necessary to mention opt-out in the privacy policy
If yes, please answer in the original text
{#type3-Q1#, < need to mention opt-outt>}
Organize these elements into a question, asking whether a paragraph of text describes this situation, please output in the following format
{"question:........"}

If not, please answer
{#type3-Q1#, <No>need opt-out links or doc>}


2. In addition to mentioning opt-out, is it necessary to provide guidance on how to opt-out, which can be a link to the opt-out guidance page
For example, please answer in the original text
{#type3-Q2#, < need guidance on how to opt-out>}
Organize these elements into a question, asking whether a paragraph of text describes this situation, please output in the following format
{"question:........"}

If not, please answer
{#type3-Q1#, <No>need guidance >}

Input example
provide a mechanism for which an End User may opt-out of receiving targeted ads Output Example,A link to guide users on optout

Output example:
{#type3-Q1#  need to mention opt-outt}
{"question":"Does the following privacy policy text mention opt out"}
{#type3-Q2#  need guidance on how to opt-out}
{"question":"Does the following privacy policy text contain content to guide users to opt out"}

<text>:
            """
            
P3_promptType4="""
Then I will enter a <text>
Please read <text> and answer several questions related to "privacy policy"
1. Does <text> require developers to maintain a privacy policy?
If yes, please answer according to the following cities
{#type4-Q1#   need pp, text original words:<.....>}

If no, please answer
{#type4-Q1#, <NO> no need pp}

Input example
each party shall at all times post a privacy policy on its website that describes how it collects, uses and shares information, and that provides information about how an End User can opt out of interest-based advertising (e.g., online behavioral or mobile cross-app advertising).

Output example:
{#type4-Q1#  need pp, text original words:<.....>}

<text>:

            """            