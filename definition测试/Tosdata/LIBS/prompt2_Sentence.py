
# the SDKname is "ironsource"
# 'you'、'developer'、'customer'、'user'
# notice:The subject or object of Requirements must be the privacy policy
prompt1 = '1'
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

# print(tos1,prompt1)

snap_tos = '''
b. You will provide and adhere to a published privacy policy for your Application that is easily accessible and conspicuously linked from the Application, incorporates by reference and links to the Snap Privacy Policy, and clearly and accurately describes to users of your Application what user information you and your Application access, collect, and store, and how and why you and your Application use, process, and share that information with Snap and other third parties. While users of your Application may provide information directly to Snap through your implementation of the Snap Developer Program, you must not provide Snap with any personal data unless otherwise agreed to in writing by you and Snap.
'''

ironsource_tos = '''
4.1Partnerwill use the Services only in a manner consistent with this Agreement and the Services Documentation, and will comply with all Applicable Rules, including data protection and privacy laws and rules applicable to any data of the End Users that is being accessed, collected, used and/or shared by Partner.Partnershall post in the Partner’s App a privacy policy that abides by all applicable rules, laws, acts and regulations and that provides legally adequate disclosure to its End Users about: (i) any information relating to End Users that will be provided or is otherwise accessible to ironSource in connection with the Services, as set forth in the IronSource Mobile Privacy Policy as available on ironSource’s website and (ii) to the extent applicable, in a conspicuous manner, a mechanism for which an End User may opt-out of receiving targeted ads based on the End User’s behavior and interests. Partne rhereby confirms that it has read and understood the IronSource Mobile Privacy Policy, and that nothing therein is contrary to Partner’s privacy policy.
'''

ironsource_tos2 ='''


text:

Partnershall post in the Partner’s App a privacy policy that abides by all applicable rules, laws, acts and regulations and that provides legally adequate disclosure to its End Users about: (i) any information relating to End Users that will be provided or is otherwise accessible to ironSource in connection with the Services, as set forth in the IronSource Mobile Privacy Policy as available on ironSource’s website and (ii) to the extent applicable, in a conspicuous manner, a mechanism for which an End User may opt-out of receiving targeted ads based on the End User’s behavior and interests. 

'''
# Partne rhereby confirms that it has read and understood the IronSource Mobile Privacy Policy, and that nothing therein is contrary to Partner’s privacy policy.   


Twitter_tos = '''
You must display your service's privacy policy to people before they are permitted to download, install, or sign up to your service. It must disclose at least the following information:

The information that you collect from people who use your service

How you use and share that information (including with X)

How people can contact you with inquiries and requests regarding their information

Your privacy policy must be consistent with all applicable laws, and be no less protective of people than X's Privacy Policy and the privacy policy of our other services and corporate affiliates. You must cease your access to the X API and the use of all X Content if you are unable to comply with your and/or X’s Privacy Policy.

'''




mixpanel_TOS = '''
4.8 Privacy Statement. Mixpanel’s tracking and use of information collected about Customer on Mixpanel Sites are governed by the Mixpanel Privacy Statement, available at https://mixpanel.com/legal/privacy-policy/. The Mixpanel Privacy Statement does not cover information Mixpanel processes on Customer’s behalf in providing the Application Services and it shall be Customer’s obligation to provide Customer’s own privacy statement or notice to its End Users as well as to provide all required disclosures to and obtain all required consents from Customer’s employees and/or agents. In addition, Mixpanel may collect registration and other information about Customer as Mixpanel’s customer through Mixpanel Sites.
'''


flurry_tos = '''
Privacy & Location Data

Privacy Policy.
You agree that you have and will abide by a privacy policy that complies with all applicable laws and industry standards and that you will comply with all applicable laws relating to the collection of information from end users of your applications.

You must clearly and conspicuously post a privacy policy within your application, in any store, and on any website where the application may be acquired (when and where it is technically possible).

That policy must: 
provide notice of your use of a tracking pixel, agent or any other visitor identification technology that collects, uses, shares and stores data, including precise location data, about end users of your applications with Flurry (whether by you, Flurry, your Ad Partners or Attribution Partners); and

contain a link to Flurry’s Privacy Policy and a statement that describes how visitors may learn more about the choices offered in connection with Flurry’s use of User Data (as applicable), including advising users who wish to opt-out that they may opt-out on a device by device basis by enabling “Limit Ad Tracking” on their device and posting an active link to:

Flurry’s Privacy Dashboard at https://www.verizonmedia.com/policies/us/en/verizonmedia/privacy/dashboard/index.html; and
https://www.verizonmedia.com/policies/us/en/verizonmedia/privacy/dashboard/index.html；和
one of the following URLs:

http://www.networkadvertising.org/managing/opt_out.asp;
https://www.networkadvertising.org/mobile-choices;
http://www.aboutads.info/choices/ (or the appropriate link for the country available on https://www.verizonmedia.com/policies/xw/en/verizonmedia/privacy/optout/ -- if you use the Services outside the United States)
http://www.aboutads.info/choices/
-------------------------------------------------------------------------------------
You agree to obtain any and all end-user consents required by applicable law before you use the Services. You agree to comply with all applicable laws, policies, and regulations relating to the collection, usage and sharing of information from users.
您同意在使用服务之前获得适用法律要求的所有最终用户同意。您同意遵守与收集、使用和共享用户信息有关的所有适用法律、政策和法规。
'''



InMobi_tos = """
Each Party agrees to comply with its obligations with respect to End User data as stated in this Contract and as applicable to it in its processing thereof under relevant privacy laws.  Each Party shall provide for a conspicuous privacy policy which is adequate in accordance with applicable privacy laws.  Each privacy policy must at a minimum set out conspicuously a description of data sets collected or permitted to be collected, use cases related to personal data/information including a clear mention that such data will be shared with certain third parties for applicable use cases.  Certain privacy laws such as CCPA, CPRA and/ or other applicable US state privacy laws also requires that You provide sufficient notice regarding rights of End Users with regard to their personal information and clearly provide for mechanisms of Opt Out (defined below) elections which You agree to comply with, if applicable to the Inventory.  Such privacy policy shall also mention use of third parties and use of cookies for the purposes of attribution and/or serving targeted Advertisements.
"""