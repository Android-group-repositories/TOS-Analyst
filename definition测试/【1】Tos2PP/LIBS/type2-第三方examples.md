
## 1 数据共享 share to


### 详细动作+how why

----
You will provide and adhere to a published privacy policy and describes to users of your Application what user information you and your Application access, collect, and store, and how and why you and your Application use, process, and share that information with Snap and other third parties. (TYPE2-Q2 需要描述第三方的数据处理)share to


1 You adhere to a published privacy policy and describes to users of your Application what user's information you access, collect, and store(type1)
2 Your privacy policy describes to users of your Application how and why you and your Application use, process, and share user's information with Snap and other third parties. (type2)
----



you must disclose the use of Google Analytics, and how it collects and processes data. 
{#type2#,  <you  ;  must disclose  ;   use of Google Analytics ,and how it collects and processes data  ;  NULL  ;  NULL  ;  NULL>  ,  <Third party is: Google Analytics > }


{#type2#,  <subject  ;  Actions  ;  object  ;  object source/target  ;  purpose  ;  condition>  ,  <third-party condition>}

### 为了特定 purpose 而共享

> 与第三方共享+advertising目的

Your privacy policy must describe how you and the third parties, service providers, or vendors you engage with (such as Tapjoy) use, collect, and share mobile device advertising identifiers and other personal information 
简化


Input example1:
Your privacy policy must describe how third parties (such as Tapjoy) collect , use , and share mobile device advertising identifiers and other personal information 
Input example1:
{#type2#,  <Your privacy policy  ;  must describe  ;   how third parties (such as Tapjoy) collect , use , and share mobile device advertising identifiers and other personal information  ;  NULL  ;  NULL  ;  NULL>  ,  <Third party is: Tapjoy > }


## 2 sdk数据收集 get from 

>需要描述第三方的数据处理 从第三方收集"


>1.Welcome to AdSense!

>Thanks for your interest in our search and advertising services (the "Services")!
> 替换 Service ->SDK Service
You will ensure that at all times you use the Services, the Properties have a clearly labeled and easily accessible privacy policy (TYPE4-Q1 需要提供隐私政策) that provides end users with clear and comprehensive information about cookies, device-specific information, location information and other information stored on, accessed on, or collected from end users' devices in connection with the Services 


(TYPE2-Q2 需要说明第三方的数据处理--这里的 Service 就是指SDK Service，SDK相对于APP来说就是第三方),

等价于:

Output example4:
You will ensure that the Properties have a privacy policy that provides end users with clear and comprehensive information about cookies, device-specific information, location information and other information stored on, accessed on, or collected from end users' devices in connection with the AdSense-SDK-Service 
改写

Input example2:
You have a privacy policy that provides end users with clear information about cookies, device-specific information, location information and other information stored on, accessed on, or collected from end users' devices in connection with the AdSense-SDK-Service 
Input example2:
{#type2#,  <You have a privacy policy  ;  provides end users ;   with clear information about cookies, device-specific information, location information and other information stored on, accessed on, or collected ;  from end users' devices in connection with the SDK Service ;  NULL  ;  NULL>  ,  <Third party is: AdSense-SDK-Service > }


## 3 同时有 to 和 from

todo 有来源有去向 用修饰data标注来源？(句式case3)

----
You must present your service's privacy policy and disclose at least the following information: The data you collect from users of your service, how you use and share that data to X and other third parties.

等于:(这个还有 how和why 但此处关注)

Input example3:
your service's privacy policy must disclose how you use and share  data you collected from user to Twitter and other third parties
Output example3:
{#type2#,  <your service's privacy policy  ;  must disclose  ;   collect,use and share user's data ;  from user,share to third parties ;  NULL  ;  NULL>  ,  <Third party is: Twitter  > }
----




## 4 描述第三方对数据处理 （无share and collection）
if 数据使用 + 第三方 -> type2



----
Customer will make all disclosures to RevenueCat's and Stripe's processing of personally identifiable information relating to such users, 

including, without limitation, by disclosing RevenueCat's and Stripe's processing of such information in Customer's privacy policy in a reasonable and industry-standard manner.
包括但不限于以合理和行业标准的方式在客户的隐私政策中披露RevenueCats和Stripe对此类信息的处理。

句式简化成成

Input example4:
Customer's privacy policy should disclose RevenueCat's and Stripe's processing of personally identifiable information relating to such users
Output example4:
{#type2#,  < Customer's privacy policy ;  dshould disclose  ;  RevenueCat's and Stripe's processing of personally identifiable information relating to such users  ;  NULL  ;  NULL  ;  NULL>  ,  <Third party is: RevenueCat and Stripe  > }
----


----
states that such information is disclosed to and processed by third party providers like Crashlytics
----

## 5 有 link to sdk pp(可单独提取)

Input example5:
Your privacy policy should incorporate by reference and link to the Snap Privacy Policy.
Output example5:
{#type2#,  < your privacy policy  ;  should incorporate by reference and link   ;  the Snap Privacy Polic  ;  NULL  ;  NULL  ;  NULL>}


states that such information is disclosed to and processed by third party providers like Crashlytics (TYPE2-Q2 需要描述第三方的数据收集处理) by句式

## 6 要有该 sdk 的描述
Your privacy policy must describe how you and the third parties, service providers, or vendors you engage with, such as Tapjoy, use, collect, and share mobile device advertising identifiers and other personal information, including for behaviorally targeted online advertising. 





