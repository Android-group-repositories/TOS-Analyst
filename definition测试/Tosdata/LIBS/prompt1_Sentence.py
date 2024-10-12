
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


P1_input_example =  '''

i give you

"You may not collect, capture, use or store PayPal Prohibited User Information. (1) Password; (2) PIN; (3) Security questions and answers. (1) Identifiers used for tax or claiming government benefits such as social security number, tax identification number, or similar health or tax insurance number in the relevant country; (2) National identity number; (3) Passport number; (4) Driver’s license number; (5) Any other government issued identifier.: (1) Full bank account number; (2) Full credit/debit card number*; and (3) Credit card expiration date or CVV2*."

What is the complete meaning of privacy protection in this service terms? Please split the sentence into short sentences
If there are specific legal and regulatory compliance requirements and specific data item requirements, please organize the relevant descriptions and do not omit them

Must be output in original text!!!!!

you give me only points in from of json

{
    "requirements": [
    {
        "description": "You may not collect, capture, use or store PayPal Prohibited User authentication information like Password,PIN,Security questions and answers",
        "type": {
        "summary": "Prohibition on handling certain types of user credentials"
        }
    },
    {
        "description": "You may not collect, capture, use or store PayPal Prohibited User Government identity and tax information like: (1) Identifiers used for tax or claiming government benefits such as social security number, tax identification number, or similar health or tax insurance number in the relevant country; (2) National identity number; (3) Passport number; (4) Driver’s license number; (5) Any other government issued identifier.",
        "type": {
        "summary": "Prohibition on handling certain types of user credentials"
        }
    },
    {
        "description": "You may not collect, capture, use or store PayPal Prohibited User 	Financial Information like:  (1) Full bank account number; (2) Full credit/debit card number*; and (3) Credit card expiration date or CVV2*. ",
        "type": {
        "summary": "Prohibited Collection of Sensitive Financial Data"
        }
    },
    ]
}


'''
# 加入要求替换单词的意义 Please read the following Term of Service and replace the same noun in the text with the definition of the noun you just learned



