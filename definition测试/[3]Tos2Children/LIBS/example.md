type 1 
-- 只提到Service 
-- 有提及具体数据和操作
-- 是否加入 实施服务时对法律遵守

type 2 在 type1 的基础上加入第三方

---

type 3 在 type1 的基础上加入 output

type 4 其他


元组构成


{# Type1 #  ,  
1 <subject 主语 ;  Actions 操作 ;   object 对象 ;   from && go  ;   purpose  ;  condition >  ,  
<service not for  : ....>  , 

2 <Third party is: MoPub  >  ,
3 <optout is: MoPub  >}


如果有pp的意思 可以也加到 pp

Service 和 your Service 的区别

#### example 1 只有服务 比较特殊
sentry TOS
https://sentry.io/terms/
---

sentry TOS 首句存在：

These Sentry Terms of Service (“Agreement”) are entered into by and between Functional Software, Inc. d/b/a Sentry (“Sentry” or “we”) and the entity or person placing an order for or accessing the Service (“Customer” or “you”). 

If you are accessing or using the Service on behalf of your company, you represent that you are authorized to accept this Agreement on behalf of your company, and all references to “you” or “Customer” in this Agreement mean your company.

本 Sentry 服务条款（以下简称“协议”）由 Functional Software， Inc. d/b/a Sentry（以下简称“Sentry”或“我们”）与订购服务或访问服务的实体或个人（以下简称“客户”或“您”）签订。

如果您代表您的公司访问或使用服务，则您声明您被授权代表您的公司接受本协议，并且本协议中提及的所有“您”或“客户”均指您的公司。
---

meaning1
The Service is not intended for and should not be used by anyone under the age of 16. 

原文
The Service is not intended for and should not be used by anyone under the age of 16. Customer must ensure that all its Users are over 16 years old.
本服务不适用于 16 岁以下的任何人，也不应由 16 岁以下的任何人使用。**客户必须确保其所有用户均年满 16 周岁**。每个用户都必须对登录凭证保密，不得与其他任何人共享。



着重 Service 和 16
{# Type1 #  ,  < Service  ;  is not intended for and should not be used  ;   by anyone under the age of 16  ;   NULL  ;   NULL  ;  NULL>  ,  <service not for  : anyone Under 16 years old > }

#### example 2 Type2 有具体操作
meaning1
Developers are not allowed to intentionally share data of users under the age of 16 with Pollfish

着重 Service 和 16
{# Type1 #  ,  <Developers  ;  are not allowed to intentionally share  ;   data of users under the age of 16  ;   with Pollfish  ;   NULL  ;  NULL>  ,   <service not for  : Under 16 years old > ,<Third party is: MoPub  > }


#### example 3 具体数据共享，Type2 在p1做增强具体数据的收集
-- p1有问题

meaning 1:
If your services or apps are directed at children, they may be subject to COPPA regulations.

You are not allowed to share personal identifiers such as IP addresses, IDFA/IDFV, Android ID, Google Play Advertising ID, Google Play store referrer, WindowsHardware ID, Windows NetworkID, Windows Phone device ID, and UUIDs with Adjust partners or other third parties
如果您的服务或应用程序面向儿童，它们可能会受到儿童 在线隐私保护法（COPPA）的约束。您不得与Adjust合作伙伴或其他第三方共享个人标识符，例如IP地址、IDFA/IDFV、Android ID、Google Play广告ID、Google Play商店推荐人、WindowsHardware ID、Windows NetworkID、Windows Phone设备ID和UUIDs。

有具体行为了，服务那层意思不需要了
要点 ： not share 【一堆数据】with (Adjust and other third parties)

{# Type2 #  ,  < You    ;    are not allowed to share  ;  such as IP addresses, IDFA/IDFV, Android ID, Google Play Advertising ID, Google Play store referrer, WindowsHardware ID, Windows NetworkID, Windows Phone device ID, and UUIDs   ; with Adjust partners or other third parties  ;   no purpose  ;  no condition  >  ,  <Third party is: Adjust partners or other third parties  >}

#### example 4 具体数据共享，Type2 declare咋搞 可以也加到 pp
declare ？？？？
You must declare and guarantee that you will not transfer any personal information of individuals under the age of 13 to MoPub, as defined by COPPA.
{# Type2 #  ,  <You must declare and guarantee that you  ;  will not transfer  ;    any personal information of individuals under the age of 13  ;   to MoPub  ;    NULL  ;  NULL  >  ,  <Third party is: MoPub  >  ,  <service not for  : individuals under the age of 13>}

#### ---- example 5 type1 同意 + 服务 our services 去掉，不是对开发者
To use our services and be bound by COPPA, CCPA, or GDPR, you must have obtained verifiable and voluntary consent from the child's parents or guardians.
gpt来对原句only if 化
Only if you have obtained verifiable and voluntary consent from the child's parents or guardians can you use our services and be bound by COPPA, CCPA, or GDPR.

“COPPA, CCPA, or GDPR” 感觉可能被放到第4个位置
{# Type1 #  ,  <you  ;  can  ;    use our services and be bound by COPPA, CCPA, or GDPR  ;   NULL  ;    NULL  ;   must have obtained verifiable and voluntary consent from the child's parents or guardians  > , <service not for  : NULL>}


#### example 6 type1 同意 + 服务

            "description": "如果公司将Nuance许可的软件用于主要面向儿童的在线网 站、服务或产品，则不得向Nuance发送任何儿童数据。",
if the company uses software licensed by Nuance for online websites, services, or products primarily aimed at children shall it not send any child data to Nuance.
{# Type1 #  ,  <company  ;  shall not send  ;     any child data   ;   to Nuance  ;    NULL  ;   if the company uses software licensed by Nuance for online websites, services, or products primarily aimed at children > , <service not for  : NULL>}



#### example 7 type1 同意 + 服务 转个句

{# Type1 #  ,  <subject  ;  Actions  ;   object  ;     ;   purpose  ;  condition  >  ,  <Age requirement>  ,  <Other conditions>}

转义：If your applications are targeted at children under COPPA, CCPA, CPRA, or similar US privacy laws, you must obtain verifiable user or parental consent for collecting and sharing data with InMobi.

meaning 1 
开发者实施服务
+ 面向人群 children, as defined under laws such as COPPA,CCPA,CPRA 
+ 目的、内容 for the collection and sharing of Your Data with InMobi
+ 条件 you are required to obtain verifiable consent from users or parent



这个不对感觉{# Type1 #  ,  <your applications  ;  directed to  ;   children, as defined under laws such as COPPA,CCPA,CPRA  ;  NULL   ;   for the collection and sharing of Your Data with InMobi   ;  you are required to obtain verifiable consent from users or parent  >  ,  <service not for  : NULL>}

应该归到type2
{# Type2 #  ,  <your applications  ;  collect and share  ;  Your Data  ;  with InMobi   ;   NULL   ;  you are required to obtain verifiable consent from users or parent  >  ,  <service not for  : children,  defined under laws such as COPPA,CCPA,CPRA >  ,  <Third party is: InMobi  >}

#### example 8 type2 同意 + 服务 

"description": "You agree not to request or permit any Ad Partner or Attribution Partner to transmit any personal information from children under the age of 17 to Flurry.",
{# Type2 #  ,  <You agree not to request or permit any Ad Partner or Attribution Partner ;  to transmit  ;   any personal information  ;from children under the age of 17,to Flurry     ;   NULL  ;  NULL  >  ,   <service not for  : under the age of 17 >  ,  <Third party is: Flurry  >}



---

meaning 1 
开发者实施服务
+ 面向人群 children, as defined under laws such as COPPA,CCPA,CPRA 
+ 目的、内容 for the collection and sharing of Your Data with InMobi
+ 条件 you are required to obtain verifiable consent from users or parent

1 gpt 切大块 大块能不能转个模式
2 做填空题（模式改写）

meaning 1 填空题 单个大块整理点小模式 类似  14 pattern 对 object 做
开发者实施服务
+ 面向人群    {children(service for)}
+ 目的内容    {collection and sharing（action）}  {Data（object）}  {with InMobi（tag\source）}
+ 条件        {obtain  (consent) }

3 孤单的service有没有上下文

#### example 9 type3 设置opt out
推特Tos原文 该段落看起来都是在讲 “您的服务”
--- 
X for Websites widgets X for Websites 小部件

You must ensure that people are provided with clear and comprehensive information about, and consent to, the storing and accessing of cookies or other information on their devices as described in X’s cookie use, where providing such information and obtaining such consent is required by law
您必须确保向人们提供清晰、全面的信息，并同意 X 在其设备上存储和访问 Cookie 或其他信息，如 X 的 Cookie 使用中所述，其中提供此类信息并获得此类同意是法律要求的

 
Services targeted to children under 13
面向 13 岁以下儿童的服务
---


Services targeted to children under 13 must opt out of tailoring  in any Twitter embedded Post  by setting the opt-out parameter to be 'true'
{# Type3 #  ,  <Services targeted to children under 13 ; must opt out  ;   the opt-out parameter to be ‘true’ ;  ttailoring  in any Twitter embedded Post  by setting the opt-out parameter to be 'true'   ;   NULL  ;  NULL  >  ,  <service not for  : under the age of 13 >  ,  <to opt-out  : tailoring  in any Twitter embedded Post and/or embedded timelines >  ,  }


Customers should configure services to ensure that end-user data from children is not transmitted to any integration partners,


#### example 10 type3 设置opt out

{# Type1 #  ,  <Customers ;  should configure  ;   services ;  NULL   ;    to ensure that end-user data from children is not transmitted to any integration partners  ;  NULL  >  ,  <service not for  : under the age of 13 >  ,  <to opt-out  : end-user data from children is transmitted to any integration partners >  ,  }




    "requirements": [
        {
            "description": "如果您的服务或应用程序面向儿童，它们可能会受到儿童 在线隐私保护法（COPPA）的约束。您不得与Adjust合作伙伴或其他第三方共享个人标识符，例如IP地址、IDFA/IDFV、Android ID、Google Play广告ID、Google Play商店推荐人、WindowsHardware ID、Windows NetworkID、Windows Phone设备ID和UUIDs。",
            
            "type": {
                "code": "Type1",
                "summary": "遵守针对儿童的服务/应用程序的COPPA合规性" 
            }
            
太短了 没有特征  --- 即使监护人同意
"In particular, under no circumstance you shall use the Site or the Services to:
3.2.4. harm or exploit minors in any way or collect their personal information;
3.2.4. 以任何方式伤害、利用未成年人或收集其个人信息;"


### example 11 一刀切的情况不能省略

太短了 没有特征  --- 即使监护人同意
"In particular, under no circumstance you shall use the Site or the Services to:
3.2.4. harm or exploit minors in any way or collect their personal information;
3.2.4. 以任何方式伤害、利用未成年人或收集其个人信息;"
You must not use the Site or Services to harm minors or exploit them in any manner.

You must not collect personal information from minors under any circumstances (type1)

{# Type1 #  ,  <You ;   must not collect  ;   personal information ;  from minors   ; NULL  ;   under any circumstances   >  ,  <service not for  :minors>  }