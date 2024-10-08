

P2_Types_fmt = '''

You are an expert in privacy policy research. Please read the following terms of service related to the privacy policy, extract the requirements of ToS for developers to use the privacy policy, and generate the json according to the example I gave

Type of requirements:

Type1. The service terms will describe clear age restrictions for children or Tos contains instructions on whether applications, services, or content are targeted towards specific groups(e.g. 13 years old)

Type2. TOS will describe how to obtain the guardian's consent and stipulate that certain actions can only be performed with the guardian's consent.

type3. The Tos will describe the relevant constraints and requirements for the transmission of children's data to third parties (  Third-Party Partners  ,  Third-Party Service Providers  )

type4. The service terms will describe the operations and requirements related to opt-out 

type5. Types unrelated to the first 5 situations but related to child constraints

Type6. Other:Additional sub-tags for introductions or general text. Not so much about child protection

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

