
## 1 最一般的 需要前期具备（数据收集说明、条款、服务说明等）



~~- 需要清晰地说明个人数据（粗略的）的处理 包括 收集~~
### 一般-粗略情况
Input example1:
You must develop a privacy policy that clearly and accurately informs end users about the personal data you collect 
Output example1:
{#type1#,  <  a privacy policy  ;  informs end users   ;  personal data you collect    ;  NULL  ;  NULL  ; NULL> }


 
### 一般-详细情况
Input example2:
privacy policy provide notice of  use of a tracking pixel, agent or any other visitor identification technology that collects, uses, shares and stores data about end users of your Application 
Output example2:
{#type1#,  <  privacy policy ;  provide notice of   ;  privacy policy provide notice of  use of a tracking pixel, agent or any other visitor identification technology that collects, uses, shares and stores data      ;  about end users of your Application  ; NULL  ; NULL> }



Privacy Policy must provide notice of Your use of cookies, identifiers for mobile devices (e.g., Android Advertising Identifier or Advertising Identifier for iOS) or similar technology used to collect data 


Input example2:
Such privacy policy shall also mention use of third parties service and use of cookies for the purposes of attribution and/or serving targeted Advertisements.
Output example2:
{#type1#,  <  Such privacy policy ;  shall also mention   ;  use of third parties service and use of cookies    ;  NULL  ;  for the purposes of attribution and/or serving targeted Advertisements.  ; NULL> }



## 2 purposes  advertising

Input example3:
The privacy policy must specifically address the use of personal information for behaviorally targeted online advertising.
Output example3:
{#type1#,  <  The privacy policy  ;    address    ;    the use of personal information  ;  NULL  ;  for behaviorally targeted online advertising  ;  NULL>}




The privacy policy must also include data collection and use for online advertisements aimed at user behavior.

{#type1#,  <  The privacy policy  ;     must also include   ;    data collection and use  ;  NULL  ;  for online advertisements aimed at user behavior  ;  NULL>}






## 3 how
> 收集(来) 数据 共享(去)


~~ 在 个人数据收集  基础之上 加入  ~~

~~- 目的使用的声明（ how why 看看 how way的情况gpt如何处理 然后再搞how why的处理）~~

### 如何 收集+处理 共享
Input example3:
each party shall at all times post a privacy policy on its website that describes how it collects, uses and shares information

Input example3:
each party shall post a privacy policy  that describes how it collects, uses and shares information
Output example3:
{#type1#,  <  each party shall post a privacy policy   ;    describes    ;    how it collects, uses and shares information ;  NULL  ;  NULL  ;  NULL>}

### 如何 处理 共享
"This policy must describes to Users what user information Developer collects and how Developer uses and shares that information (Type1-Q1需要说明开发者如何收集使用和共享用户信息);

 




##  与PP内容 不相关 送到 type4 去

###  Condition 

> 1 需要 pp 告知用户 "我会获取条件" 也是pp需要具备的内容 可以归到"需要PP
> 
you must provide appropriate notices to users of your application(s) about data collection and use practices related to your use of our Services and obtain their consent to the Services' data collection and use, including use to reward users for their engagement with Campaign Content (for incentivized campaign types) and use for behaviorally targeted online advertising. 

> 2 PP不相关

~~> disclose pp todo 找一下 展示隐私政策能不能作为 Condition~~
The Customer is required to obtain all legally required consents and permissions from end users for data collection and processing.
You must present your service's privacy policy to individuals before they can download, install, or sign up for your service. 

