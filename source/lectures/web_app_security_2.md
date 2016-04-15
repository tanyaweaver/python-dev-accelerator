# Web App Security: More Vulnerabilities and Best Practices 

The next 4 out of the top 10

## Top Web App Vulnerabilities

### 5. Security Misconfiguration

Is pretty much exactly as it sounds. Not necessarily the fault of the developer (i.e. YOU), but still of paramount importance. Occurs when holes are left in the security framework by sys admins, database admins, or divs.

These can occur at *any* level of the application stack: the platform level, the web server, the app server, the database, framework, or custom code. Typically these misconfigurations are found through unauthorized access to default accounts, unused webpages, unpatched flaws, unprotected files, directories, and more.

### 6. Sensitive Data Exposure

[http://kemptechnologies.com/blog/owasp-top-ten-series-sensitive-data-exposure/](http://kemptechnologies.com/blog/owasp-top-ten-series-sensitive-data-exposure/)

"Sensitive data" typically refers to confidential records, password, payment info, personal info, or user account info. Basically **any data you wouldn't want displayed to anyone aside from intended users**. Usually exposed when data is in transit and not properly encrypted, or unencrypted backups are accessed.

### 7. Missing Function Level Access Control

[http://www.tutorialspoint.com/security_testing/missing_function_level_access_control.htm](http://www.tutorialspoint.com/security_testing/missing_function_level_access_control.htm)

A user with limited (or no) access may try to directly access site functions against a server without permissions control. An attacker may try to force direct access to site functions against a server without proper permissions control.

Ex: Directly accessing `http://www.website.com/some_app/admin` instead of logging in. Admin functions should be wrapped in authorization checks, and only accessible (with everything within it being similarly protected) through a login wall.

### 8. Cross-site Request Forgery (CSRF)

The attacker (Jerkface) forces an authenticated user (User A) to send a forged HTTP request, including User A's session cookie, to a vulnerable web app. This allows Jerkface to force User A's browser to generate requests such that the vulnerable app perceives them as legitimate requests from User A.

User A may have no knowledge of their part in this scheme. They may click on something that they think is legitimate, like an image, that actually sends a request instead.

## Basic Vulnerability Protection

- Use environment variables instead of hardcoding sensitive information
- Require authorization for certain features/pages
- Back up often (app needs will vary wildly) and keep backups physically secure
- Close unused ports and turn off unused services
- Require irregular passwords
- Don't run your app as the system admin
- Keep files for your web app in a folder below the application root
- Do not allow users the option of specifying a path for any file access
- Never use unfiltered user input for public-facing applications. Consider how much cleaning needs to be done for some given input
- Never store unfiltered unfiltered input in the database
- Do not assume that HTTP request headers are safe
- Use informative but non-specific, custom error messages
- Make sure that when you're live, turn off whatever DEBUG mode your app has
- When error-handling, make sure that any caught resources are released upon failure.
- Set size limits on file uploads


## Best Practices

### Know your app

Taking an inventory of your applications is the most important step. You’d be surprised by how many rogue applications are out there. Know what they do and why you have them. If they take user input, be especially aware. If they're third-party apps, be thorough with the docs and dip into the source code. Ensure that the benefit of using the app doesn't come at the cost of a security hole (intentional or otherwise).

### Prioritize your apps

Categorize your apps as critical (external-facing with customer info), serious (external or internal containing sensitive info), or normal (less exposure). You should have plans to test them all, but a) categorization allows for smaller projects for you, and b) getting to the most sensitive first protects you where you need it most in a timely manner.

### Prioritize the vulnerabilities

Yes, the apps should be ranked. The vulnerabilities you test for should also be ranked. They all take different resources and require different practices. Some are more costly in time/effort than others, some are more devastating than others, and some are more common/edge-casey than others. 

### Build awareness internally

Educate your team, both the technical staff and the non-technical users/contributors in your company. A chain is only as strong as its weakest link, and non-savvy users are the weakest of links. They may not understand certain security practices (or even have context for them), and may actively try to circumvent security in favor of convenience. As annoying as they are, limited sessions, login pages, and "CAPTCHA"s exist for a reason.

### Create a plan

Create an Application Security Blueprint, consisting of your goals, which apps you want to secure and with what priority you want to secure them, how you're going to test them, who's involved, and (where applicable) how much it would cost. In addition to giving your team a framework for carrying out proper security measures, this sort of plan makes it easier to justify costs when the purse isn't yours to spend. Of course, keep this plan secure.


### Interim protection

No one has the illusion that you have infinite time to ferret out every last vulnerability that your app may or may not contain under ever potential attack scenario. You can get by with targeting specific vulnerabilities and removing some unnecessary (or low-priority) functionality while you develop your master security suite.

### Don't forget code in production

Code in production is just as, if not more important, as code in development. It's *currently* customer-facing, and so is already in danger of ruining their lives or ruining yours. You need to secure that and you need to test it, just as much as if not more than code you're prepping for deployment.

### Keep vigilance

Web app security isn't a box to be checked off, but a habit to be developed. Make it a practice, and make testing regular. Adhere to your plan, and update as your needs and capabilities change.

### Celebrate every victory

Any war fought will drain you if all you see is the battle. When you achieve part of your security plan, celebrate! Take breaks between hunts for bugs and appreciate the improvements you've made. Every time you close one of those security holes, you've now made your product that much more valuable to your clients (or to yourself).