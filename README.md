# CMPUT404Lab1

**Question 1:** What is your GitHub URL?
- Me: https://github.com/Sean-Meyers
- This repo: https://github.com/Sean-Meyers/CMPUT404Lab1

**Question 2:** What version is the requests library installed on the system?
- 2.28.1

**Question 3:** What version is the requests library installed in the virtualenv?
- 2.28.1 because the same version was installed this time.

**Question 4:** What is the difference between the virtual environment and the not virtual environment python?
- They are running completely different scripts. Well, they are the same, but they are different files. The virtualenv is its own clean slate, so the requests installation is separate from the non virtualenv version.

**Question 5:** What status code is returned for http://google.com ? What URL must you visit to get a 200 status code?
- http://google.com: 301 Moved
- To get 200: http://www.google.com/

**Question 6:** What status code is returned for http://google.com/teapot? Is it the one returned by curl -i or curl -iL? What happens when you curl http://www.google.com/teapot?
- http://google.com/teapot -i: 301 Moved Permanently
- http://google.com/teapot -iL: 301 Moved Permanently
- http://www.google.com/teapot -i: 418 I'm a Teapot
- http://www.google.com/teapot -iL: 418 I'm a Teapot

**Question 7:** What changed in the output of https://webdocs.cs.ualberta.ca/~hindle1/1.py when you used -X POST? What is this method useful for?
- A form field was added in the post version with mini field storage containing characters 'X' and 'Y'. This is useful for when we want to store some data on the server. For example, we may be writing a forum post where we give it a name, and some text.

**Question 8:** What is the raw URL to your Python script on GitHub?
- https://raw.githubusercontent.com/Sean-Meyers/CMPUT404Lab1/main/requestsVer.py