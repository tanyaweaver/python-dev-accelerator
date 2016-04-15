# Break the Site/Fix Your Site

This is a continuation of the last Break the Site/Fix the Site assignment. The website is again from [https://github.com/nVisium/django.nV](https://github.com/nVisium/django.nV). This assignment will go through the next four of the top ten. This assignment will also have you trying to attack one of your partner's projects and expose a vulnerability if one exists.

## Tasks

### The Primary Work

- Create a github branch for this assignment called `repairman-2`
- Add your vulnerability tests to your existing `vulnerability-report.md`.
- Address the following vulnerabilities. **DO NOT JUST REGURGITATE THE GIVEN SOLUTION**:
	- A5 - Misconfig
	- A6 - Exposure
	- A7 - Access
	- A8 - CSRF
	
- For each of the above vulnerabilities report:
	- How you found and exploited the vulnerability, including the code/method you used
	- What you were able to do with the vulnerability (i.e. what was exposed?)
	- The code that fixes the vulnerability

```eval_rst
.. note:: For your vulnerability report, please see :doc:`this sample-vulnerability-report <sample-vulnerability-report>`. Use the format shown in that document.
```

### Infuriate Your Partner

- Clone one of your partner's working sites prior to week 6. Can be from this class, or any other working project.
- Create a branch for your clone called `housecall-[projectname]`
- Test for at least one vulnerability.
- Report on this test in another `vulnerability-report.md` for this project. Same method as before.
- **If no vulnerabilities are found**, write about what you *tried* to test for and how you *tried* to test for it.

## Submitting Your Work

When you've addressed the vulnerabilities and filled out your reports, push your code sets to github. You should be pushing the vulnerability reports for each project, as well as the *fixed* code. Open a pull request from your `repairman-2` branch to the `master` branch. Copy the URL of that pull request and submit it in Canvas.

For the test on your partner's project, open a pull request from your `housecall-[projectname]` branch to your clone's `master` branch. Copy the URL of that pull request into the Comments box of the same Canvas submission.