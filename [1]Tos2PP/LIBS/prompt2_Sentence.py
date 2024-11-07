# the SDKname is "ironsource"
# notice:The subject or object of Requirements must be the privacy policy
prompt1 = '1'
P2_Types_fmt = '''

You are a privacy policy research expert. Please read the following JSON of the terms of service related to the privacy policy and classify each description in requirements into 1-4 types.
A description can belong to multiple types. 
Classification is based only on <text> descriptions, without considering general conditions.
Classification type:


Type 1. Require developers to provide a privacy policy or statement.

Type 2. Require developers to provide content related to third parties in their privacy policy, including the keyword 'third party'

Type 3. Require developers to provide content related to opt out in their privacy policy, including the keyword 'opt out'

Type 4. Other related content that does not explicitly mention privacy policy keywords.



for Type2
I will provide a list of some of the full names of specific software development kits (SDKS). Within the text discussed in this paper, these SDK names are considered third-party entities. The researcher requests that the SDK names appearing in the text be replaced with the generic term 'third party' to ensure the consistency of the text and to protect the anonymity of the related entities.

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

The classification results are as follows


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
        "summary": "privacy policy must include Opt-Out Mechanism for Targeted Ads"
        }
    }
    ]
}


You need to classify the description and code the requirement type in the input json, as shown below

{
    "requirements": [
    {
        "description": "The Partner must ensure that any data of the End Users accessed, collected, used, or shared is in line with the aforementioned rules and regulations.",
        "type": {
          "code": "Type1",
          "summary": "Users Data Handling"
        }
    },
    {
        "description": "The Partner is required to comply with all relevant laws and regulations, especially those related to data protection and privacy.",
        "type": {
          "code": "Type4",
          "summary": "Adherence to Applicable Rules"
        }
    },
    {
        "description": "The policy should clearly inform End Users about any information related to them that will be provided to ironSource or is otherwise accessible to ironSource in connection with the Services. This should be detailed as per the IronSource Mobile Privacy Policy available on ironSource’s website.",
        "type": {
          "code": "Type2",
          "summary": "Disclosure of Information Sharing with ironSource(Third-party partners)"
        }
    },
    {
        "description": "If applicable, the privacy policy must include a conspicuous mechanism that allows End Users to opt-out of receiving targeted advertisements based on their behavior and interests",
        "type": {
          "code": "Type3",
          "summary": "privacy policy must include Opt-Out Mechanism for Targeted Ads"
        }
    }
    ]
}





'''

P2_ASk2 = '''

Now, read the following text and generate a json according to the above requirements and methods

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
