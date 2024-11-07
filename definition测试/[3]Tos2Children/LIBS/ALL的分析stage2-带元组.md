---
大多会围绕 "服务" 而非直接提到去收集之类的具体词汇

item可能可以细分
如果只有服务，那去考虑
实施服务+面向人群 +目的 +条件 就OK了

如果有详细的use collect 等，舍弃“服务”这层含义保留具体的数据操作
(具体操作)+面向人群 +目的 +条件 

---


## 1 基本 (有对使用服务的约束  也有对详细一点的数据操作的约束)

### 没有儿童的明确说明

太短了 没有特征  --- 即使监护人同意
"In particular, under no circumstance you shall use the Site or the Services to:
3.2.4. harm or exploit minors in any way or collect their personal information;
3.2.4. 以任何方式伤害、利用未成年人或收集其个人信息;"

### 年龄 + 只提到了服务

The Service is not intended for and should not be used by anyone under the age of 16. Customer must ensure that all its Users are over 16 years old
本服务不适合且不应由 16 岁以下的任何人使用。
客户必须确保其所有用户年满 16 周岁。"

#### example 1 只有服务
meaning1
The Service is not intended for and should not be used by anyone under the age of 16. 
着重 Service 和 16
{# Type1 #  ,  <Service  ;  is not intended for and should not be used  ;   by anyone under the age of 16  ;   NULL  ;   NULL  ;  NULL>  ,  <service not for  : Under 16 years old > }



---
"Child-Directed Apps. You represent and warrant that (i) no application within the Publisher Network is a website or online service directed to children, as defined under the Children’s Online Privacy Protection Act (“COPPA”), and (ii) You will not transmit any “Personal Information” (as defined under COPPA) about or relating to an individual under the age of 13 to MoPub.
患儿导向性的应用。您声明并保证(i)根据《儿童在线隐私保护法》(“COPPA”)的定义，发布者网络中的任何应用程序都不是针对儿童的网站或在线服务，并且(ii)您不会将关于13岁以下个人的或与之相关的任何“个人信息”(根据COPPA的定义)传输给MoPub。"

---

{
"requirements": [
{
"description": "Pollfish 的服务不针对 16 岁以下的儿童，并且开发者的平台也遵守此年龄限制。",

}, 目标meaning
{
"description": "开发者必须遵守美国《儿童在线隐私保护法》（COPPA），并确保在协议期限内遵守该规定。",
"type": {
"code": "Type1",
"summary": "COPPA 合规性"  -- 丢弃
}
},
{
"description": "开发者必须在其隐私政策中包含有关适用法律规定的未成年人隐私权利的信息。",
"type": {
"code": "Type1",
"summary": "隐私政策披露" 不好丢弃
}
},

"description": "开发者必须做出合理的商业努力来确定未成年人的年龄。用户并避免收集 16 岁以下儿童的信息。",

{
"description": "开发者不得故意与 Pollfish 分享 16 岁以下用户的数据。",
Developers are not allowed to intentionally share data of users under the age of 16 with Pollfish

#### example 2 有具体操作
meaning1
Developers are not allowed to intentionally share data of users under the age of 16 with Pollfish

着重 Service 和 16
{# Type1 #  ,  <Developers  ;  are not allowed to intentionally shar  ;   data of users under the age of 16  ;   with Pollfish  ;   NULL  ;  NULL>  ,  <service not for  : Under 16 years old > }


"type": {
"code": "Type3",
"summary": "数据共享限制"  这个可以 作为目标meaning
}
},
{
"description": "如果 Pollfish 检测到 16 岁以下的用户，它将阻止该用户使用其服务。",
"type": {
"code": "Type4",
"summary": "用户阻止协议"  检测不了 丢弃
}
}
]
}
"
(vii) Pollfish does not direct our Services to children under the age of 16. You represent and warrant that your Platform is not directed to children under the age of 16 either; and that you comply (and will comply throughout the Term) with the U.S. Children's Online Privacy Protection Act (""COPPA""). You will also provide relevant information in your Privacy Policy to all Users relating to the privacy rights of minors under Applicable Laws.
You will make commercially reasonable efforts to identify the age of your Users and refrain from collecting information from children under the age of 16. You will not knowingly share the data of any Users under the age of 16 with Pollfish. If Pollfish detects any User is under the age of 16, Pollfish will promptly block that User from our Services.

（vii） Pollfish 不会将我们的服务定向给 16 岁以下的儿童。您声明并保证您的平台也不针对 16 岁以下的儿童;并且您遵守（并将在整个期限内遵守）《美国儿童在线隐私保护法》（“COPPA”）。您还将在您的隐私政策中向所有用户提供与适用法律规定的未成年人隐私权相关的信息。

您将尽商业上合理的努力来识别用户的年龄，并避免收集 16 岁以下儿童的信息。您不会故意与 Pollfish 共享任何 16 岁以下用户的数据。如果 Pollfish 检测到任何用户未满 16 岁，Pollfish 将立即阻止该用户使用我们的服务。"


"The Service is not intended for and should not be used by anyone under the age of 16. Customer must ensure that all its Users are over 16 years old
本服务不适合且不应由 16 岁以下的任何人使用。客户必须确保其所有用户年满 16 周岁。"



### coppa+具体数据项
{
    "requirements": [
        {
            "description": "如果您的服务或应用程序面向儿童，它们可能会受到儿童 在线隐私保护法（COPPA）的约束。您不得与Adjust合作伙伴或其他第三方共享个人标识符，例如IP地址、IDFA/IDFV、Android ID、Google Play广告ID、Google Play商店推荐人、WindowsHardware ID、Windows NetworkID、Windows Phone设备ID和UUIDs。",
            
            "type": {
                "code": "Type1",
                "summary": "遵守针对儿童的服务/应用程序的COPPA合规性" 
            }
        },
        {


            "description": "上述标识符被视为在服务中收集的数据，不应与第三方共享。",（归类为type3）

            


            "type": {
                "code": "Type3",
                "summary": "禁止与第三方共享某些个人标识符"
            }
        },
        {
            "description": "有关COPPA如何定义面向儿童的服务以及规则要求的更多信息，请参考提供的链接。",
            "type": {
                "code": "Type4",
                "summary": "针对儿童服务的COPPA要求指南"
            }
        }
    ]
}

不得 包含即使获取同意也不能用的意思

Customers with services/apps directed to children might be subject to the US Children’s Online Privacy Protection Act (“COPPA”). If applicable, Customer is not allowed to share personal identifiers including but not limited to IP-addresses, IDFA (Identifier for Advertising) or IDFV (Identifier for Vendor), Android ID, Google Play Advertising ID and Google Play store referrer, WindowsHardware ID, Windows NetworkID, Windows Phone device ID and UUIDs (“Personal Identifiers”) with Partners of Adjust or other third parties. All the aforementioned identifiers are potentially data collected within the Services. To learn more about how COPPA defines services directed to children and the rule’s requirements, see here.

拥有针对儿童的服务/应用程序的客户可能会受到美国儿童在线隐私保护法（“COPPA”）的约束。如果适用，客户

不得共享个人标识符，包括但不限于 
IP 地址、IDFA（广告标识符）或 IDFV（供应商标识符）、Android ID、Google Play 广告 ID 和 Google Play 商店引荐来源网址、WindowsHardware ID、与 Adjust 合作伙伴或其他第三方的 Windows NetworkID、Windows Phone 设备 ID 和 UUID（“个人标识符”）

所有上述标识符都可能是在服务中收集的数据。要了解有关 COPPA 如何定义针对儿童的服务以及规则要求的更多信息，请参阅此处。

---

#### example 3 具体数据共享，Type2 在p1做增强具体数据的收集
-- p1有问题

meaning 1:
If your services or apps are directed at children, they may be subject to COPPA regulations. You are not allowed to share personal identifiers such as IP addresses, IDFA/IDFV, Android ID, Google Play Advertising ID, Google Play store referrer, WindowsHardware ID, Windows NetworkID, Windows Phone device ID, and UUIDs with Adjust partners or other third parties
如果您的服务或应用程序面向儿童，它们可能会受到儿童 在线隐私保护法（COPPA）的约束。您不得与Adjust合作伙伴或其他第三方共享个人标识符，例如IP地址、IDFA/IDFV、Android ID、Google Play广告ID、Google Play商店推荐人、WindowsHardware ID、Windows NetworkID、Windows Phone设备ID和UUIDs。

有具体行为了，服务那层意思不需要了
要点 ： not share 【一堆数据】with (Adjust and other third parties)

{# Type2 #  ,  <You  ;  Actions  ;    are not allowed to share  ;  such as IP addresses, IDFA/IDFV, Android ID, Google Play Advertising ID, Google Play store referrer, WindowsHardware ID, Windows NetworkID, Windows Phone device ID, and UUIDs   ; with Adjust partners or other third parties  ;   no purpose  ;  no condition  >  ,  <Third party is: Adjust partners or other third parties  >}

---

{
"requirements": [
{
"description": "您必须确保发布商网络内的任何应用程序均不针对 COPPA 定义的儿童。",
"type": {
"code": "Type1",
"summary": "无儿童导向服务"  实施服务类
}
},
{
"description": "您必须声明并保证您不会向 MoPub 传输任何 13 岁以下个人的个人信息，如 COPPA 所定义。",
#### example 4 具体数据共享，Type2 declare咋搞
declare ？？？？
You must declare and guarantee that you will not transfer any personal information of individuals under the age of 13 to MoPub, as defined by COPPA.
{# Type2 #  ,  <You must declare and guarantee that you  ;  will not transfer  ;    any personal information of individuals under the age of 13  ;   to MoPub  ;    NULL  ;  NULL  >  ,  <Third party is: MoPub  >  ,  <service not for  : individuals under the age of 13>}


"type": {
"code": "Type1",
"summary": "不传输 13 岁以下儿童的个人信息"  数据和使用类
}
}
]
}

"Child-Directed Apps. You represent and warrant that (i) no application within the Publisher Network is a website or online service directed to children, as defined under the Children’s Online Privacy Protection Act (“COPPA”), and (ii) You will not transmit any “Personal Information” (as defined under COPPA) about or relating to an individual under the age of 13 to MoPub.
患儿导向性的应用。您声明并保证(i)根据《儿童在线隐私保护法》(“COPPA”)的定义，发布者网络中的任何应用程序都不是针对儿童的网站或在线服务，并且(ii)您不会将关于13岁以下个人的或与之相关的任何“个人信息”(根据COPPA的定义)传输给MoPub。"

### coppa+具体数据项+同意


{
    "requirements": [
        {
            "description": "要使用我们的服务，如果受到COPPA、CCPA或GDPR的约束，您必须已经获得儿童的父母或监护人的可验证且自愿的同意。",
            "type": {
                "code": "Type1",
                "summary": "隐私法规下的父母同意要求"                
#### example 5 type1 同意 + 服务
To use our services and be bound by COPPA, CCPA, or GDPR, you must have obtained verifiable and voluntary consent from the child's parents or guardians.
gpt来对原句only if 化
Only if you have obtained verifiable and voluntary consent from the child's parents or guardians can you use our services and be bound by COPPA, CCPA, or GDPR.

“COPPA, CCPA, or GDPR” 感觉可能被放到第4个位置
{# Type1 #  ,  <you  ;  can  ;    use our services and be bound by COPPA, CCPA, or GDPR  ;   NULL  ;    NULL  ;   must have obtained verifiable and voluntary consent from the child's parents or guardians  > , <service not for  : NULL>}

            }
        },
        {
            "description": "同意必须涵盖使用、收集和共享移动设备广告标识符和其 他数据，用于我们隐私政策中描述的行为定向在线广告。",
            "type": {
                "code": "Type1",
                "summary": "父母同意的范围" ？？？这是不是应该和到目的里面  回稳定理解出涵盖的意义
            }
        }
    ]
}


"Children's Online Privacy Protection Act (""COPPA""), the California Consumer Privacy Act (""CCPA""), and the GDPR), then as a condition of using our Services, you must either have obtained the verifiable and freely given consent of the child's parent or guardian to the use, collection and sharing of mobile device advertising identifiers and other data for behaviorally targeted online advertising as described in our Privacy Policy 

《儿童在线隐私保护法》（“COPPA”）、《加利福尼亚州消费者隐私法》（”CCPA“）和《通用数据保护条例》），作为使用我们服务的条件，
您必须获得儿童父母或监护人的可验证和自由同意，才能使用、收集和共享移动设备广告标识符和其他数据，用于我们隐私政策中所述的行为定向在线广告"

### 同意之同意 条件之条件
1 有条件的同意
2 依旧只提到年龄+服务 

{
    "requirements": [
        {
            "description": "公司在处理16岁以下儿童的个人数据时，必须确保遵守GDPR、COPPA和其他数据保护法律。",
            "type": {
                "code": "Type1",
                "summary": "遵守儿童数据的数据保护法律" -- 丢弃
            }
        },
        {
            "description": "公司不得将Nuance的服务用于主要针对16岁以下儿童的在 线网站、服务或产品。",
            "type": {
                "code": "Type1",
                "summary": "禁止Nuance服务用于主要面向儿童的内容"
            }
        },
        {

#### example 6 type1 同意 + 服务

            "description": "如果公司将Nuance许可的软件用于主要面向儿童的在线网 站、服务或产品，则不得向Nuance发送任何儿童数据。",
if the company uses software licensed by Nuance for online websites, services, or products primarily aimed at children shall it not send any child data to Nuance.
{# Type1 #  ,  <company  ;  shall not send  ;     any child data   ;   to Nuance  ;    NULL  ;   if the company uses software licensed by Nuance for online websites, services, or products primarily aimed at children > , <service not for  : NULL>}

            "type": {
                "code": "Type2",
                "summary": "禁止传输面向儿童的主要使用内容的儿童数据"
            }
        },
        {
            "description": "对于16岁以下儿童可以访问的混合受众或普通受众的在线 网站、服务或产品，公司必须实施可验证的父母同意机制，并就向Nuance转移儿童数据及Nuance收集和处理此类数据提供充分的披露。",
            "type": {
                "code": "Type1",
                "summary": "混合或普通受众内容的父母同意和披露"
            }
        },
        {
            "description": "双方同意，Nuance不被视为COPPA中定义的运营商。",    
            "type": {
                "code": "Type4",
                "summary": "Nuance作为COPPA下非运营商的地位"
            }
        }
    ]
}

7.1 Child Data. Company hereby represents and warrants that;
(a) Where applicable, Company’s website, services and products comply with the GDPR, US Children's Online Privacy Protection Act of 1998, (“COPPA”) and other Data Protection Laws protecting Personal Data from children under 16 (“Child Data”) including but not limited to any rules for obtaining consent.
(b) Company shall not use Nuance’s Services in connection with an online site, service, or product that targets children under 16 as its primary audience (“Primarily Child‑Directed”). Primarily Child‑Directed is based on empirical evidence regarding audience composition, and evidence regarding the intended audience, such as subject matter, visual content, use of animated characters or child‑oriented activities and incentives, music or other audio content, age of models, presence of child celebrities or celebrities who appeal to children, language or other characteristics of the web site or online service, as well as whether advertising promoting or appearing on the web site or online service is directed to children.
(c) If Company uses Nuance licensed software for Primarily Child‑Directed online sites, services or products, then Company must not send to Nuance (in connection with maintenance, support and tools regarding the Nuance licensed software, or otherwise) any Child Data.
(d) If Company uses Services for mixed audience or general audience online sites, services or products which may be accessed by children under 16, but are not Primarily Child‑Directed, then Company’s verifiable parental consent mechanism, direct notice, and web notice, when required by Data Protection Laws, shall adequately disclose and sufficiently cover the transfer of Child Data to Nuance and Nuance's collection and Processing of Child Data consistent with this DPA.
The Parties agree that Nuance is not an operator as that term is defined in COPPA. 

(a)在适用的情况下，公司的网站、服务和产品遵守GDPR、1998年美国儿童在线隐私保护法(“COPPA”)和其他保护16岁以下儿童个人数据(“儿童数据”)的数据保护法，包括但不限于获得同意的任何规则。

(b)公司不得将Nuance的服务用于以16岁以下儿童为主要受众(“主要针对儿童”)的在线网站、服务或产品。

“主要以儿童为导向”是基于关于受众构成的经验证据，以及关于目标受众的证据，如主题、视觉内容、动画角色或面向儿童的活动和奖励的使用、音乐或其他音频内容、模特的年龄、儿童名人或对儿童有吸引力的名人的存在、网站或在线服务的语言或其他特征。以及网站或在线服务上的广告推广或出现是否针对儿童。？？？？无意义

(c)如果公司将Nuance许可的软件用于主要针对儿童的在线网站、服务或产品，则公司不得向Nuance发送任何儿童数据(与Nuance许可软件相关的维护、支持和工具或其他方面有关)。

(d)如果公司将服务用于混合受众或一般受众的在线网站、服务或产品，这些网站、服务或产品可由16岁以下的儿童访问，但主要不是针对儿童的，则公司可验证的家长同意机制、直接通知和网络通知应在数据保护法要求时充分披露并充分涵盖将儿童数据传输给Nuance以及Nuance根据本DPA收集和处理儿童数据。

meaning 1 
公司不得将Nuance的服务用于主要针对16岁以下儿童的在 线网站、服务或产品

meaning 2 
如果公司将Nuance许可的软件用于主要面向儿童的在线网 站、服务或产品，则不得向Nuance发送任何儿童数据
不得 发送 儿童数据

meaning 3 
"对于16岁以下儿童可以访问的混合受众或普通受众的在线 网站、服务或产品，公司必须实施可验证的父母同意机制，并就向 Nuance 转移儿童数据及Nuance收集和处理此类数据提供充分的披露

实施服务
+人群 16岁以下
+条件 具有同意机制、向 Nuance





### 对针对性的服务 获取统同意
If applications on Your Network or Inventory are directed to children as defined under COPPA, CCPA, CPRA and/ or such other similar US state privacy legislations, You will obtain verifiable user or   parental consent , as required under the applicable privacy and data protection law(s) for the collection and sharing of Your Data with InMobi 

and you will specifically identify to InMobi the applications/Inventory that are directed to children. InMobi may elect not to serve any behavioural advertising on Inventory targeted to children.

如果您的网络或库存上的应用程序根据COPPA、CCPA、CPRA和/或其他类似的美国州隐私立法的定义针对儿童，您将根据适用的隐私和数据保护法的要求，获得可验证的用户或家长同意，以便与 InMobi 收集和共享您的数据，

并且您将明确向InMobi指明针对儿童的应用程序/库存。InMobi可以选择不在库存上提供针对儿童的任何行为广告。
转义

#### example 7 type1 同意 + 服务 转句

{# Type1 #  ,  <subject  ;  Actions  ;   object  ;     ;   purpose  ;  condition  >  ,  <Age requirement>  ,  <Other conditions>}

转义：If your applications are targeted at children under COPPA, CCPA, CPRA, or similar US privacy laws, you must obtain verifiable user or parental consent for collecting and sharing data with InMobi.

meaning 1 
实施服务
+面向人群 children, as defined under laws such as COPPA,CCPA,CPRA 
+目的 for the collection and sharing of Your Data with InMobi
+条件 you are required to obtain verifiable consent from users or parent



这个不对感觉{# Type1 #  ,  <your applications  ;  directed to  ;   children, as defined under laws such as COPPA,CCPA,CPRA  ;  NULL   ;   for the collection and sharing of Your Data with InMobi   ;  you are required to obtain verifiable consent from users or parent  >  ,  <service not for  : NULL>}


{# Type2 #  ,  <your applications  ;  collect and share  ;  Your Data  ;  with InMobi   ;   NULL   ;  you are required to obtain verifiable consent from users or parent  >  ,  <service not for  : children,  defined under laws such as COPPA,CCPA,CPRA >  ,  <Third party is: MoPub  >}

meaning 2 其他 ，不太关心的意义，主语不是 开发者

并且您将明确向InMobi指明针对儿童的应用程序/库存。InMobi可以选择不在库存上提供针对儿童的任何行为广告。
InMobi may choose not to serve behavioral advertising on inventory that is targeted at children.






### 不同地区 年龄不同

-- 只提到有服务
{
    "requirements": [
        {
            "description": "服务旨在为一般受众设计，并非针对儿童。",
            "type": {
                "code": "Type1",
                "summary": "预期受众"  像个法子丢弃
            }
        },
        {
            "description": "我们不会故意收集13岁以下儿童的个人信息。",
            "type": {
                "code": "Type1",
                "summary": "不收集儿童个人信息"  meaning1
            }
        },
        {
            "description": "如果我们意识到未达到同意年龄的儿童提供了个人信息， 应通过DPO@unity3d.com通知我们。",
            "type": {
                "code": "Type1",
                "summary": "未经授权的数据收集报告机制" ???是不是想个法子丢弃
            }
        },
        {
            "description": "同意年龄因地区而异，例如美国为13岁，欧盟和日本为16 岁。",  这玩意有个句号而且句号后面主语不是sdk
            "type": {
                "code": "Type1",
                "summary": "同意年龄"      meaning2
            }
        }
    ]
}



"Unless expressly provided otherwise, the Services are intended for general audiences and are not intended for children. We do not knowingly collect Personal Information from children under 13. If any party becomes aware that a child under the age to provide lawfulconsentto processing in their region (e.g., 13 in the U.S., 16 in the E.U.,16 in Japan) has provided us with Personal Information in contravention of our policies, they shouldcontactus at DPO@unity3d.com.
除非另有明确规定，否则服务面向一般受众，不适合儿童。我们不会故意收集 13 岁以下儿童的个人信息。如果任何一方发现未达到其所在地区合法同意处理年龄的儿童（例如美国 13 岁、欧盟 16 岁、日本 16 岁）向我们提供了个人信息如有违反我们政策的信息，应通过 DPO@unity3d.com 与我们联系。"



## 2 第三方 

### 收集 分享
{
    "requirements": [
        {
            "description": "You agree not to use any Service for applications labeled or described as 'Kids' or 'Children'.",
            "type": {
                "code": "Type1",
                "summary": "禁止将服务用于标记或描述为“儿童”或“儿童”的应用"    
            }
        },
        {
            "description": "You agree not to use any Service in connection with applications, advertisements, or services directed towards children under the age of 17.",
            "type": {
                "code": "Type1",
                "summary": "禁止将服务用于针对17岁以下儿童的应用、广告或服务"  
            }
        },
        {
            "description": "You agree not to collect any personal information from children using the Service.",
            "type": {
                "code": "Type1",
                "summary": "禁止通过服务收集儿童的个人信息"
            }
        },
        {
            "description": "You agree not to request or permit any Ad Partner or Attribution Partner to transmit any personal information from children under the age of 17 to Flurry.",

#### example 7 type1 同意 + 服务 

{# Type1 #  ,  <You agree not to request or permit any Ad Partner or Attribution Partner ;  to transmit  ;   any personal information  ;from children under the age of 17,to Flurry     ;   NULL  ;  NULL  >  ,   <service not for  : under the age of 17 >  ,  <Third party is: Flurry  >}
            "type": {
                "code": "Type3", 
                "summary": "禁止要求或允许任何广告合作伙伴或归因合作伙伴将17岁 以下儿童的个人信息传输给Flurry"  任何广告合作伙伴或归因合作伙伴  那么也包含自己吧
            }
        },
        {
            "description": "These restrictions are in accordance with the Network Advertising Initiative 2020 Code of Conduct, Section D.II.1.",
            "type": {
                "code": "Type4",
                "summary": "遵守NAI行为准则2020关于儿童个人信息的规定" 完美的丢弃
            }
        }
    ]
}
"13 Children's Data 儿童数据
You agree that you will not use any Service in connection with any application labeled or described as a ""Kids"" or ""Children"" application, and will not use any Service 
(i) in connection with any application, advertisement or service directed towards children under the age of 17; 
(ii) to collect any personal information from children; or 
(iii) request or permit any Ad Partner or Attribution Partner to transmit any personal information from children under the age of 17 to Flurry (see Network Advertising Initiative 2020 Code of Conduct, Section D.II.1).


您同意，您不会使用与任何标记或描述为“儿童”或“儿童”应用程序相关的任何服务，并且不会使用
(i) 与针对儿童的任何应用程序、广告或服务相关的任何服务。 17 岁；
(ii) 收集儿童的任何个人信息；
(iii) 请求或允许任何广告合作伙伴或归因合作伙伴将 17 岁以下儿童的任何个人信息传输给 Flurry（请参阅《网络广告促进会 2020 年行为准则》第 D.II.1 节）。"

### send store
{
    "requirements": [
        {
            "description": "客户必须配置服务，以防止将儿童的最终用户数据传输给集成合作伙伴，除非集成合作伙伴的服务专门设计用于处理此类数据，并且他们允许传输与儿童相关的最终用户数据。",
            "type": {
                "code": "Type2",
                "summary": "向集成合作伙伴传输儿童数据"
            }
        },
        {
            "description": "集成合作伙伴必须拥有专门定制的服务，以支持和处理来自儿童的最终用户数据。",
            "type": {
                "code": "Type2",
                "summary": "处理儿童数据的服务要求"
            }
        },
        {
            "description": "集成合作伙伴必须允许传输与儿童相关的最终用户数据。",
            "type": {
                "code": "Type2",
                "summary": "传输儿童数据的许可要求"
            }
        }
    ]
}
{
    "requirements": [
        {
            "description": "Customers must set up the Services to prevent the transmission of End User Data from Children to Integrated Partners unless the Integrated Partner's service is designed to handle such data and they allow the transmission of End User Data related to Children.",
            "type": {
                "code": "Type2",
                "summary": "Transmission of Child Data to Integrated Partners"
            }
        },
        {
            "description": "Integrated Partners must have services specifically tailored to support and process End User Data from Children.",
            "type": {
                "code": "Type2",
                "summary": "Service Requirement for Handling Child Data"
            }
        },
        {
            "description": "Integrated Partners must permit the transmission of End User Data related to Children.",
            "type": {
                "code": "Type2",
                "summary": "Permission Requirement for Transmitting Child Data"
            }
        }
    ]
}

"2.1 Restrictions. Customer shall not and shall not permit or authorize any third party,including, but not limited to its Authorized Users, to: 
(ii) use the Application Services to send spam or otherwise duplicative or unsolicited messages in violation of applicable laws, or to process, send or store Prohibited Information, 

14.15 “Prohibited Information” means (iv) personally identifiable information collected from children under the age of 13 or from online services directed toward children; 

“2.1 限制。客户不得且不得允许或授权任何第三方（包括但不限于其授权用户）：
(ii) 使用应用服务发送违反适用法律的垃圾邮件或其他重复或未经请求的消息，或处理、发送或存储禁止信息，

14.15 “禁止信息”是指 (iv) 从 13 岁以下儿童或针对儿童的在线服务收集的个人身份信息；”"

### 直接禁止

"AppLovin does not knowingly collect personal information from children or serve ads to children. You may not provide AppLovin with personal information from children, use the Services to serve ads to children, or use the Services for any Property that is exclusively designed for or exclusively directed to children. 
AppLovin不會有意收集兒童的個人資訊或向兒童提供廣告。您不得向AppLovin提供儿童的个人信息，不得使用服务向儿童提供广告服务，或不得将服务用于任何专门为儿童设计或专门针对儿童的财产。"



## 3 设置 不好对比 但能提取

### optout
"
Services targeted to children under 13 must opt out of tailoring  in any Twitter embedded Post and/or embedded timelines by setting the opt-out parameter to be ‘true’ as described here
面向 13 岁以下儿童的服务必须通过将选择退出参数设置为“true”来选择退出任何嵌入式帖子和/或嵌入式时间线中定制 X"

#### example 9 type3 设置opt out
Services targeted to children under 13 must opt out of tailoring  in any Twitter embedded Post  by setting the opt-out parameter to be 'true'
{# Type3 #  ,  <Services targeted to children under 13 ; must opt out  ;   the opt-out parameter to be ‘true’ ;  ttailoring  in any Twitter embedded Post  by setting the opt-out parameter to be 'true'   ;   NULL  ;  NULL  >  ,  <service not for  : under the age of 13 >  ,  <to opt-out  : tailoring  in any Twitter embedded Post and/or embedded timelines >  ,  }

### 


"Customer shall configure the Services to ensure that End User Data from Children is not transmitted to any Integrated Partner except where both the Integrated Partner’s service is specifically tailored to support and process End User Data from Children and the Integrated Partner permits Customer to transmit such End User Data related to Children to such Integrated Partner.

Customers must configure services to prevent the transfer of children's end-user data to integration partners, unless the integration partner's services are intended to support and process such data and they allow the transfer of end-user data related to children.
客户应配置服务，以确保不会将来自儿童的最终用户数据传输给任何集成合作伙伴，

除非集成合作伙伴的服务是专门为支持和处理来自儿童的最终用户数据而定制的，且集成合作伙伴允许客户将与儿童有关的最终用户数据传输给该集成合作伙伴。" (这两段一直在讲集成伙伴，和我们的目标属实没有重合)


Customers should configure services to ensure that end-user data from children is not transmitted to any integration partners,


#### example 10 type3 设置opt out

{# Type1 #  ,  <Customers ;  should configure  ;   services ;  NULL   ;    to ensure that end-user data from children is not transmitted to any integration partners  ;  NULL  >  ,  <service not for  : under the age of 13 >  ,  <to opt-out  : end-user data from children is transmitted to any integration partners >  ,  }

