# the SDKname is "ironsource"
# notice:The subject or object of Requirements must be the privacy policy
prompt1 = '1'
P2_Types_fmt = '''

You are a privacy policy research expert. Please read the following JSON of the terms of service related to the privacy policy and classify each description in requirements into 1-4 types.
A description can belong to multiple types. 
Classification is based only on <text> descriptions, without considering general conditions.
Classification type:


Type 1. Require developers to provide a privacy policy or data collection statement.

Type 2. Require developers to provide content related to third parties in their privacy policy, including the keyword 'third party'

Type 3. Require developers to provide content related to opt-out in their privacy policy, including the keyword 'opt out' or 'opt-out'

Type 4. Other related content that does not explicitly mention the keyword 'privacy policy', although mentioning data use and consent to access, is unrelated to privacy policy

for type1
If the paragraph mentions somethingthe privacy policy needs to do, it should be classified as Type 1

for Type2
I will provide a list of some of the full names of specific software development kits (SDKS). Within the text discussed in this paper, these SDK names are considered third-party entities. The researcher requests that the SDK names appearing in the text be replaced with the generic term 'third party' to ensure the consistency of the text and to protect the anonymity of the related entities.

for Type3
As long as there is an opt out, it is classified as type3

for Type4 
1 Although the sentences in quotation marks are related to data collection, they are not related to the privacy policy and are classified as type 4.
"Customer can collect, submit, and use data only if it obtains all legally required consents and permissions"
2 It has nothing to do with the Privacy Policy and I don't understand what it is talking about.
"including via a link in your Stripe App listing in the Stripe Apps Marketplace"
3 It only states that the privacy policy should be displayed, but there is no clear requirement for the content.
"Partners shall publish a privacy policy in their applications that complies with all applicable rules, laws, acts and regulations"

list of SDK names:
============== start of list ================
Mixpanel
Amplitude
Firebase
Flurry
Onesignal
Stripe
RevenuCat
Twitter/X
Line
Wechat
Facebook
Tiktok
Snap creative kit
Tapjoy
Ironsource
Unity
Applovin 
AdMob/AdSense
Vungle
MoPub
Start.io
Sentry
Dropbox
ZOOM
============== start of end   ================




Only output the text in JSON that starts and ends with curly braces
Do not include JSON in the form of markdown code blocks
```json
{
  json
}
```
Directly output JSON text
{
  json
}

The classification result example is as follow


{
    "requirements": [
    {
        "description": "You represent and warrant that with respect to any data collected by Unity, provided by you to Unity, or to which you grant Unity access under or in connection with these Terms that constitutes "personal data" or "personal information" as defined under applicable privacy and data protection laws",
        "type": {
        "summary": "Declaration of Compliance with Laws"
        }
    },
    {
        "description": "Your privacy policy must include a link to the Unity Privacy Policy, or ironSource Privacy Policy, as applicable",
        "type": {
        "summary": "privacy policy must include a link"
        }
    },
    {
        "description": "You must develop a privacy policy informs end users how you utilize and distribute such information to third parties, including for advertising purposes.",
        "type": {
        "summary": "Detailing data use and sharing with third parties in privacy policy "
        }
    },
    {
        "description": "Your privacy policy must explains how End-Users can opt out of the offerings,if applicable",
        "type": {
        "summary": "explains opt-out to End-Users in privacy policy " 
        }
    },
    {
        "description": "Your privacy policy must  provide notice of your use of a tracking pixel, agent or any other visitor identification technology that collects, uses, shares and stores data about end users of your Application",
        "type": {
        "summary": "Data Collection Technology Statement in privacy policy "
        }
    },
    {
        "description": "Customer can collect registration and other information about Customer's employees and/or agents only if providing all required disclosures and obtaining all required consents",
        "type": {
        "summary": "Users collect data according to conditions"
        }
    },
    
    ]
}


You need to classify the description and code the requirement type in the input json, the example as shown below

{
    "requirements": [
    {
        "description": "You represent and warrant that with respect to any data collected by Unity, provided by you to Unity, or to which you grant Unity access under or in connection with these Terms that constitutes "personal data" or "personal information" as defined under applicable privacy and data protection laws",
        "type": {
        "code": "Type4",
        "summary": "Declaration of Compliance with Laws"
        }
    },
    {
        "description": "Your privacy policy must include a link to the Unity Privacy Policy, or ironSource Privacy Policy, as applicable",
        "type": {
        "code": "Type3",
        "summary": "privacy policy must include a Unity link"
        }
    },
    {
        "description": "You must develop a privacy policy informs end users how you utilize and distribute such information to third parties, including for advertising purposes.",
        "type": {
        "code": "Type2",
        "summary": "Detailing data use and sharing with third parties"
        }
    },
    {
        "description": "Your privacy policy must explains how End-Users can opt out of the offerings,if applicable",
        "type": {
        "code": "Type3",
        "summary": "explains opt-out to End-Users" 
        }
    },
    {
        "description": "Your privacy policy must  provide notice of your use of a tracking pixel, agent or any other visitor identification technology that collects, uses, shares and stores data about end users of your Application",
        "type": {
        "code": "Type1",
        "summary": "Data Collection Technology Statement"
        }
    },
        {
        "description": "Customer can collect registration and other information about Customer's employees and/or agents only if providing all required disclosures and obtaining all required consents",
        "type": {
        "code": "Type4",
        "summary": "Users collect data according to conditions"
        }
    },
    
    ]
}




'''

P2_ASk2 = '''

Now, read the following text and generate a json like the above requirements and examples

Note that only the json should be output, and no useless information should be output.
'''

# ===========================================================================================
P2_prompt_add_tos = '''
Now, read the following text and generate a json according to the above requirements and methods. 


Note that only the json should be output, and no useless information should be output.

text:
'''
tos1 = '''

"you agree to provide sufficiently clear, meaningful and prominent notices to, make all required disclosures to, and obtain the necessary consent or permission from any individual to whom such data relates regarding the collection, disclosure, use and security of such data. 

In addition, you will at all times maintain, display and abide by a conspicuously placed privacy policy that makes appropriate disclosures to End-Users, including disclosures that

(ii) explain that Services Data can be processed as contemplated by these Terms and as set out in the Unity Privacy Policy, or ironSource Privacy Policy, as applicable; 

(iii) provide notice of your use of a tracking pixel, agent or any other visitor identification technology that collects, uses, shares and stores data about end users of your Application, which privacy policy shall also include a link to the Unity Privacy Policy, or ironSource Privacy Policy, as applicable"
'''
