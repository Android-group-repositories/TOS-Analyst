
P1_Background_Definition = """
Background Definition
I will give you the annotation scheme consists of ten data practice categories with its 
explanation. The annotations are to the website's Terms of Service (Tos).

The relationship between Terms of Service (Tos), developers, Privacy Policy(PP), and App is interconnected and forms the basic framework of modern digital services and products. Here are the main relationships between them:

Developer:

A developer is an individual or team that creates and maintains applications or other digital products.
They are responsible for writing code, designing interfaces, testing functions, and ensuring that the application meets user needs and market standards.

App:

An app is a software product created by developers for specific devices or platforms (such as smartphones, tablets, computers, etc.).
Apps provide services or functions to users and can be free or paid.

Terms of Service (Tos):

Terms of Service are the legal contracts that users must agree to when using an app.
It stipulates the rights and obligations between the user and the developer, including conditions of use, liability limits, service changes or termination, etc.
Users usually need to accept the Tos before using the app.

Privacy Policy:

A Privacy Policy is a document that explains how developers collect, use, protect, and share users' personal information.
It details the purpose of data collection, scope of use, data storage, and protection measures, etc.
The Privacy Policy helps to improve transparency and ensure that users understand how their personal information is handled.
"""

X_Background_Definition = """
Developers should note that 'X' is considered a third-party entity, distinct from both the developers and the service users.
"""


P1_input_example1 =  '''


===== Step 1: =====
for example I give you

"6.6. You represent and warrant that with respect to any data collected by Unity, provided by you to Unity, or to which you grant Unity access under or in connection with these Terms that constitutes “personal data” or “personal information” as defined under applicable privacy and data protection laws, you agree to provide sufficiently clear, meaningful and prominent notices to, make all required disclosures to, and obtain the necessary consent or permission from any individual to whom such data relates regarding the collection, disclosure, use and security of such data.In addition, you will at all times maintain, display and abide by a conspicuously placed privacy policy that makes appropriate disclosures to End-Users, including disclosures that (i) comply with all applicable privacy and data protection laws and regulations and/or any applicable requirements, terms, or guidelines required by your platform providers; (ii) explain that Services Data can be processed as contemplated by these Terms and as set out in the Unity Privacy Policy, or ironSource Privacy Policy, as applicable; (iii) provide notice of your use of a tracking pixel, agent or any other visitor identification technology that collects, uses, shares and stores data about end users of your Application, which privacy policy shall also include a link to the Unity Privacy Policy, or ironSource Privacy Policy, as applicable; and (iv) if applicable, explains how End-Users can opt out of the Offerings."

What is the complete meaning of privacy protection in this service terms? Please split the sentence into short sentences
If there are specific legal and regulatory compliance requirements and specific data item requirements, please organize the relevant descriptions and do not omit them

Must be output in original text!!!!!

You split the paragraph into JSON format:
{
    "requirements": [
    {
        "description": "You represent and warrant that with respect to any data collected by Unity, provided by you to Unity, or to which you grant Unity access under or in connection with these Terms that constitutes "personal data" or "personal information" as defined under applicable privacy and data protection laws",
        "type": {
        "summary": "Declaration of Compliance with Laws"
        }
    },
    {
        "description": "you agree to provide sufficiently clear, meaningful and prominent notices to, make all required disclosures to, and obtain the necessary consent or permission from any individual to whom such data relates regarding the collection, disclosure, use and security of such data. ",
        "type": {
        "summary": "Obtain necessary consent and disclosure"
        }
    },
    {
        "description": "You must maintain, display, and adhere to a privacy policy that makes suitable disclosures to End-Users ",
        "type": {
        "summary": "maintain and appropriately disclose a privacy policy to end users"
        }
    },
    {
        "description": "Your privacy policy must  provide notice of your use of a tracking pixel, agent or any other visitor identification technology that collects, uses, shares and stores data about end users of your Application",
        "type": {
        "summary": "Data Collection Technology Statement"
        }
    },
    {
        "description": "Your privacy policy must include a link to the Unity Privacy Policy, or ironSource Privacy Policy, as applicable",
        "type": {
        "summary": "privacy policy must include a link"
        }
    },
    {
        "description": "Your privacy policy must explains how End-Users can opt out of the offerings,if applicable",
        "type": {
        "summary": "explains opt-out to End-Users" 
        }
    }
    ]
}
'''

# 改写句式方案
# 目前已收集
# 1 Condition
P1_input_example2 = '''
===== Step 2: =====
Then I need you to rewrite the sentence structure of the "description"

I am more concerned about data manipulation, but I need to deal with some sentences with messy sentence structures
The rule is for the following 1 cases

--- case 1 start---
I would like you to rephrase the sentence structure with conditions such as consent to focus on data processing
Obtain+(benefits, etc.)+for/to+(data collection/service usage)
Rewrite as (Data collection)+only if+(conditions such as consent)


example1:
"The Customer is required to obtain all legally required consents and permissions from end users for data collection and processing."
For sentences that are conditional on data and collection, the structure is : Customer obtain+(conditions such as consent)+for/to+(data collection)
Rewrite as : (Data collection)+only if+(conditions such as consent)
"Data collection and processing can only take place only if the Customer has obtained all legally required consents and permissions from end users."

example2:
"The Customer is responsible for making all necessary disclosures to their users and obtaining the required consents and authorizations for RevenueCat to perform the Services."
The structure is : Customer responsible \ obtain+(conditions such as consent)+for/to+(service usage)
Rewrite as : (Service usage)+only if+(conditions such as consent)
"Customer can use RevenueCat's services only if making all necessary disclosures to their users and obtaining the required consents and authorizations"

notice:
"Legally required" is not a condition
"Privacy policy" is not a condition
--- case 1 end ---

For example, in Step 1, you get JSON:

{
    "requirements": [
    {
        "description": "You must obtain user consent for the data collection and use practices associated with our Services.",
        "type": {
        "summary": "Declaration of Compliance with Laws"
        }
    },
    {
        "description": "The privacy policy must specifically address the use of personal information for behaviorally targeted online advertising.",
        "type": {
        "summary": "Privacy policy must detail data use in ads"
        }
    },
    ]
}
The first description is "obtain+(conditions such as consent)+for/to+(data collection/service usage)
But the second description is not related to the condition
we rewrite it into
{
    "requirements": [
    {
        "description": "your data collection and use practices associated with our Services can only be implemented if user consent is obtained",
        "type": {
        "summary": "Declaration of Compliance with Laws"
        }
    },
    {
        "description": "The privacy policy must specifically address the use of personal information for behaviorally targeted online advertising.",
        "type": {
        "summary": "Privacy policy must detail data use in ads"
        }
    },
    ]
}

you give me only points in from of rewrited json
'''
P1_ask = """
    \n
Summarize the text and output the main points of the text. The sentence structure should be clear and easy to understand. Try to express it in the original text.
"""   