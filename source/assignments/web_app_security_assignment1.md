# Break the Site/Fix the Site

In this series of assignments you will practice identifying various types of vulnerabilities in a website, and then set about fixing them to make the site more secure. The vulnerabilities you will be looking out for will come from the [Open Web App Security Project Top 10](https://www.owasp.org/index.php/Top_10_2013-Top_10). The website that you will be breaking is **made for exploitation**, and will be found [https://github.com/nVisium/django.nV](https://github.com/nVisium/django.nV). This particular assignment will go through the first four of the top ten.

## Tasks

- Fork the django.nV repository linked above, clone ***YOUR*** fork and create a virtualenv for the project
- Create a github branch for this assignment called `repairman-1`
- Create a markdown file documenting your vulnerability tests called `vulnerability-report.md`.
- Address the following vulnerabilities. **DO NOT JUST REGURGITATE THE GIVEN SOLUTION**:
	- A1 - Injection
	- A2 - Broken Auth
	- A3 - XSS
	- A4 - Insecure DOR
	
- For each of the above vulnerabilities report:
	- How you found and exploited the vulnerability, including the code/method you used
	- What you were able to do with the vulnerability (i.e. what was exposed?)
	- The code that fixes the vulnerability

```eval_rst
.. note:: For your vulnerability report, please see :doc:`this sample-vulnerability-report <sample-vulnerability-report>`. Use the format shown in that document.
```

## Submitting Your Work

Commit and push your `master` branch to github. This should *only* include the raw, broken django.nV repository.

When you've addressed the vulnerabilities and filled out your report, push your code to github. Open a pull request from your `repairman-1` branch to the `master` branch. Copy the URL of that pull request and submit it in Canvas.