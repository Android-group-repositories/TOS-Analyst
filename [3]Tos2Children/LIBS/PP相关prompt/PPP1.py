
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


P1_input_example =  '''



for example
i ask you

"4.1Partner will use the Services only in a manner consistent with this Agreement and the Services Documentation, and will comply with all Applicable Rules, including data protection and privacy laws and rules applicable to any data of the End Users that is being accessed, collected, used and/or shared by Partner.
Partnershall post in the Partner's App a privacy policy that abides by all applicable rules, laws, acts and regulations and that provides legally adequate disclosure to its End Users about: (i) any information relating to End Users that will be provided or is otherwise accessible to ironSource in connection with the Services, as set forth in the IronSource Mobile Privacy Policy as available on ironSource’s website and (ii) to the extent applicable, in a conspicuous manner, a mechanism for which an End User may opt-out of receiving targeted ads based on the End User’s behavior and interests. Partne rhereby confirms that it has read and understood the IronSource Mobile Privacy Policy, and that nothing therein is contrary to Partner’s privacy policy.
"
Regarding this TOS, as a developer, what do I need to write in myprivacy policy? 

If there are specific legal and regulatory compliance requirements and specific data item requirements, 
please sort out the relevant descriptions without omission

Must be output in original text!!!!!

you give me only points in from of json

{
    "requirements": [
    {
        "description": "The Partner must ensure that any data of the End Users accessed, collected, used, or shared is in line with the aforementioned rules and regulations.",
        "type": {
        "summary": "Data Handling"
        }
    },
    {
        "description": "The Partner is required to comply with all relevant laws and regulations, especially those related to data protection and privacy.",
        "type": {
        "summary": "Adherence to Applicable Rules"
        }
    },
    {
        "description": "The policy should clearly inform End Users about any information related to them that will be provided to ironSource or is otherwise accessible to ironSource in connection with the Services. This should be detailed as per the IronSource Mobile Privacy Policy available on ironSource’s website.",
        "type": {
        "summary": "Disclosure of Information Sharing"
        }
    },
    {
        "description": "If applicable, the privacy policy must include a conspicuous mechanism that allows End Users to opt-out of receiving targeted advertisements based on their behavior and interests",
        "type": {
        "summary": "Opt-Out Mechanism for Targeted Ads"
        }
    }
    ]
}

'''
P1_ask = """
    \n
Summarize the text and output the main points of the text. The sentence structure should be clear and easy to understand. Try to express it in the original text.
"""   