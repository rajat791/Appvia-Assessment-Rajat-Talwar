# Write-up: Rajat Talwar

> Fill in each section below. Bullet points are fine. Clarity beats length.
> If you're invited to the Assessment Day you'll talk an engineer through this
> document, so write it as something you'd be happy to present.

## Part 1
- I installed node.js correctly thhrough the node.js website
- I ran npm install 
- the terminal outputted
```bash
Rajats-MacBook-Air:app sirpigson$ npm install

up to date, audited 70 packages in 619ms

15 packages are looking for funding
  run `npm fund` for details

1 high severity vulnerability

To address all issues, run:
  npm audit fix --force

Run `npm audit` for details
```
## Thought process / errors
I moved the errors to the table for the write up

- I did not know funding meant package developers looking for donantions (I found by looking on google)
- After running npm fund, I ran npm audit
- npm audit showed me that one package had a version mismatch, and the audit gave me a fix
- after this i ran the app through npm start
- i got an error stating that the index.js file could not be found
- through vs code, i just looked up index.js at the top and saw no file with that name existed
- this meant that the application could not start up as there was no file called index.js
- i then looked through the other js files, and found that server.js (last line) was listening to port 3000
- i checked through package.json, and renamed the index.js to server.js which resolved the issue

- next issue was that the module morgan was not found
- similarly i looked through server.js again, and saw that it was a depedendency
- i then looked through pacakge.json and found that the the morgan package was not there so i installed it throuhg npm install morgan

- after this i ran npm start
- the taskboard ran at port 3000 but after going to that port on chrome, the app did not load and i got an error
- i tried again to run it and i had the same error
- i though of writing a GET request to check the status as said on the README file "GET /health returns {"status":"ok"}."
- I went to server.js file, and saw that the PORT variable was 300 instead of 3000. Once i added that extra 0, the website loaded.
- after closing the app through terminal, my changes did not save.
- these are errors I found with 5 minutes of just testing functionality



- played around with the application and found a few errors with behaviour
- Delete button works 
- Done button does not work and gives a 404 error
- assuming done button puts a strikethrough an item
- adding a new item works (gives a 304)
- cannot delete last item (list cannot be empty basically)
- found another one, you can add empty items to the list.
- char limit?, this doesn't break the app, but increases the width of the screen and looks messy.
- i fixed the delete and done buttons
- need to fix the empty to dos 


## 1. What was broken

List each fault you found and fixed. For each one: where it was, what the
symptom was, what the root cause was, and what you changed.

| # | Where (file) | Symptom | Root cause | My fix |
|---|--------------|---------|------------|--------|
| 1 | package.json | npm start gave an error stating that the index.js file could not be found | no file called index.js existed, server.js (last line) was listening to port 3000 instead | renamed index.js to server.js which resolved the issue |
| 2 | server.js | module morgan was not found | morgan was a dependency in server.js but was not in package.json / not installed | ran npm install morgan |
| 3 | server.js | taskboard ran at port 3000 but going to that port on chrome, the app did not load and gave an error | PORT variable was 300 instead of 3000 | added the extra 0 so PORT was 3000, website loaded |
| 4 | package.json | npm audit showed one package had a version mismatch | dependency version mismatch flagged by npm audit | ran the fix given by npm audit |
| 5 | (route file) | Done button does not work and gives a 404 error | assuming done button puts a strikethrough an item, route not working | fixed the done button |
| 6 | (route file) | Delete button works but cannot delete last item (list cannot be empty basically) | list cannot be empty | fixed the delete button |

## 2. Security concerns

Which of the issues above (or anything else you spotted) were security
problems? Why do they matter, and what could someone actually do with them?
- npm audit i noticed when i did npm install. There was a high dependency vulnerability which could let someone inject malicious code or crash the app. The audit gave me a fix which I ran in the terminal
- Input for the website. Inputs were not validates meaning someone could potentially inject malicious code into that input field. 
- The PORT and admin_code were hard coded into the app. Should use environment variables.
- Theres no authentication meaning someone could edit someone elses TO:DO list. Meaning in prod, anyone on the network could tamper with someone elses list.

## 3. How to run my submission

- App: `cd app && npm install && npm start` (plus anything extra I've added:)
- Log tool: `./analyse.sh <LEVEL> <path-to-log-file>` (written in [language])
- Anything else an engineer needs to know to run or test my work:
- Give the `analyse.sh` file permissions through `chmod +x analyse.sh`


## 4. My top three production improvements

Exactly three, in priority order, with your reasoning for both the choice and
the order.

1. Input Validation and output sanitisation. - it is a security flaw as users' data can be leaked and it is a correctness bug aswell. 
2. Move config out of code and into enviornment variables - again it ensures safe deployment.
3. Adding automated tests - automated tests could catch bugs that a human may not be able to spot. 

## 5. Optional extensions (if attempted)

Which did you pick, why, how far did you get, and what would you finish with
more time?

## 6. How I used AI tools

Which tools (if any), what you used them for, where they helped, and where
they were wrong or you overrode them. Honesty here is a positive signal.
- I used claude to help make the analyse.sh file as I was slightly unsure on how to. It also explained to me how the syntax for sh files works.
- I used w3 schools to just check python and js syntax as sometimes i forget.
- used youtube for music!

## 7. Reflections

- The hardest part of this exercise was:
- One thing I learned doing it: 
- If I had another day, I would:
