
P2_Types_fmt = '''

You are an expert in privacy policy research. Please read the following terms of service related to the privacy policy, extract the requirements of ToS for developers to use the privacy policy, and generate the json according to the example I gave

Type of requirements:


Type1. Requires description of what kind of data the developer will process (may include keywords: information, data, etc.)

Type2. Third party sharing/collection: This type of description describes how user information is shared with or collected by third parties.

Type3. Other: Additional sub tags used for introductions or general text. This tag is not suitable for terms related to privacy compliance.


for the type2
I will provide a list containing the names of specific software development kits (SDKs). Within the text discussed in this paper, these SDK names are considered third-party entities. The researcher requests that the SDK names appearing in the text be replaced with the generic term 'third party' to ensure the consistency of the text and to protect the anonymity of the related entities.

list of SDK names：
============== start of list ================
Mixpanel
amplitude
firebase
flurry
onesignal
Stripe
RevenuCat
twitter
line
wechat
Facebook
tiktok
snap creative kit
Tapjoy
ironsource
unity3dads
applovin 
AdMob/AdSense
vungle
MoPub
start.io
Sentry
dropbox
ZOOM
============== start of end   ================

Only output the text in JSON that starts and ends with curly braces
The resulting json is similar to

====================================
{
    "requirements": [
      {
        "description": "Provide clear, meaningful and prominent notices regarding the collection, disclosure, use, and security of data",
        "type": {
          "summary": "Requires description of what kind of data the developer will process"
        }
      },
      {
        "description": "Obtain necessary consent or permission for data processing",
        "type": {
          "summary": "Require description of data processing operations"
        }
      },
      {
        "description": "Explain that Services Data can be processed according to the Unity Privacy Policy or ironSource Privacy Policy",
        "type": {
          "summary": "Require description of data processing operations"
        }
      },
      {
        "description": "Include a link to the Unity Privacy Policy or ironSource Privacy Policy",
        "type": {
          "summary": "Require description of the relationship between the app and third-party"
        }
      }
    ]
}
====================================

You need to classify the description and code the requirement type in the input json, as shown below
Please keep the value of the key description unchanged

====================================
{
    "requirements": [
      {
        "description": "Provide clear, meaningful and prominent notices regarding the collection, disclosure, use, and security of data",
        "type": {
          "code": "Type1",
          "summary": "Requires description of what kind of data the developer will process"
        }
      },
      {
        "description": "Obtain necessary consent or permission for data processing",
        "type": {
          "code": "Type1",
          "summary": "Require description of data processing operations"
        }
      },
      {
        "description": "Explain that Services Data can be processed according to the Unity Privacy Policy or ironSource Privacy Policy",
        "type": {
          "code": "Type1",
          "summary": "Require description of data processing operations"
        }
      },
      {
        "description": "Include a link to the Unity Privacy Policy or ironSource Privacy Policy",
        "type": {
          "code": "Type2",
          "summary": "Require description of the relationship between the app and third-party"
        }
      }
    ]
}
====================================

'''

P2_ASk2 = '''

Now, read the following text and generate a json according to the above requirements and methods

Note that only the json should be output, and no useless information should be output.
'''
