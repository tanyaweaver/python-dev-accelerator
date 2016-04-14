#  Web Application Security

Web app security is a lot like writing tests for code in that it's not necessary but it's a damn good idea. It's not quite as drastic as "untested code is broken code", but it's not far off. Here's my modification to that statement: "an unsecured app is an app waiting to be exploited". It doesn't add direct quantifiable value to your app, but it does protect it from malicous exploitation. Think about the time investment in web application security similarly to having health insurance or retirement savings. Do you need them to live? Absolutely not. However, when some sudden illness hits you or when you get old, you're going to be paying for it in spades.

Security refers to more than just protecting your app from the outside. Remember to protect the app from itself, as well as its own hardware. This includes backing up code and data regularly to several, secure sources to combat disk failure, as well as keeping code updated with any dependency upgrades.

The [2015 WhiteHat Website Security Statistics Report](https://info.whitehatsec.com/Website-Stats-Report-2015.html) noted the following:

| Industry | Always Vulnerable* | Rarely Vulnerable** |
| -------- | ----------------- | ----------------- |
| Public Administration | 64% | 14% |
| Transportation / Warehousing | 55% | 16% |
| Accommodations / Food Services | 55% | 18% |
| Other Services | 53% | 18% |
| Manufacturing | 51% | 26% |
| Health Care / Social Assistance | 50% | 18% |
| Utilities | 36% | 34% |
| Finance / Insurance | 35% | 25% |
| Information | 35% | 28% |
| Professional / Scientific / Technical Services | 30% | 20% |
| Retail Trade | 29% | 20% |
| Arts / Entertainment/Recreation | 27% | 39% |
| Education Services | 27% | 40% |

\* Always vulnerable means a site is vulnerable on every single day of the year

\** Rarely vulnerable means a site is vulnerable less than 30 days of the year

## Top Web App Vulnerabilities

### 1. Injection

Occurs when a user sends data through a query or input field that causes the execution of unintended database commands. These can be used to drop tables, retrieve sensitive information, alter table data, etc. If your site takes raw user input straight to the database, it's vulnerable.

![bobby droptables](http://imgs.xkcd.com/comics/exploits_of_a_mom.png)

More examples of SQL Injection: [https://en.wikipedia.org/wiki/SQL_injection#Examples](https://en.wikipedia.org/wiki/SQL_injection#Examples) 

Preventative measures outlined here: [http://bobby-tables.com/](http://bobby-tables.com/)

### 2. Broken Authentication and Session Management

Your system vulnerable when sessions aren't handled properly, or your authentication system is weak/broken. An attacker assumes the identity of a user and can potentially wreak havoc on your system. Even solid authentication mechanisms can be undermined by flawed credential management, e.g. password change, "remember my password" requests, account updates, etc. 

If session tokens are not properly protected, an attacker can hijack an active session and assume the identity of a user. Unless all authentication credentials and session identifiers are protected with SSL (Secure Sockets Layer) at all times and protected against disclosure from other flaws, such as cross-site scripting, an attacker can hijack a user’s session and assume their identity.

How to know when you're vulnerable: [http://fishbowl.pastiche.org/archives/docs/PasswordRecovery.pdf](http://fishbowl.pastiche.org/archives/docs/PasswordRecovery.pdf)

### 3. Cross-Site Scripting (XSS)

A type of injection attack, XSS involves using a vulnerable site to gain access to secure portions of another one by inserting client-side script (e.g. Javascript or HTML) into webpages viewed by other users. XSS attacks can be temporary, but in some cases can persist in the system, repeatedly attacking users that access it.

XSS accounted for ~84% of all security vulnerabilities documented by Symantec as of 2007. 

Examples: [https://en.wikipedia.org/wiki/Cross-site_scripting#Exploit_examples](https://en.wikipedia.org/wiki/Cross-site_scripting#Exploit_examples)

### 4. Insecure Direct Object References

Occurs when a reference to an internal implementation object, e.g. file, directory, or DB key, is exposed to the user without validation. It can allow access to contents that a given user doesn't have permissions for, some of which can be sensitive information.

More on Insecure Direct Object References [https://www.owasp.org/index.php/Top_10_2013-A4-Insecure_Direct_Object_References](https://www.owasp.org/index.php/Top_10_2013-A4-Insecure_Direct_Object_References)


## Resources

- [OWASP](https://www.owasp.org/index.php/Top_10_2013-Top_10)
- [SANS](https://www.sans.org/top25-software-errors/)
- [Microsoft](https://msdn.microsoft.com/en-us/library/zdh19h94.aspx)

Note Django handles much of this already when used correctly, **however not every site is Django-based, and not all Django sites are used correctly.** You need to be aware of what you may be walking into, and what you should be looking for, regardless of the system.
