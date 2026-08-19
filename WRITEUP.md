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
| 1 |              |         |            |        |
| 2 |              |         |            |        |

## 2. Security concerns

Which of the issues above (or anything else you spotted) were security
problems? Why do they matter, and what could someone actually do with them?

## 3. How to run my submission

- App: `cd app && npm install && npm start` (plus anything extra I've added:)
- Log tool: `./analyse.sh <LEVEL> <path-to-log-file>` (written in [language])
- Anything else an engineer needs to know to run or test my work:

## 4. My top three production improvements

Exactly three, in priority order, with your reasoning for both the choice and
the order.

1.
2.
3.

## 5. Optional extensions (if attempted)

Which did you pick, why, how far did you get, and what would you finish with
more time?

## 6. How I used AI tools

Which tools (if any), what you used them for, where they helped, and where
they were wrong or you overrode them. Honesty here is a positive signal.

## 7. Reflections

- The hardest part of this exercise was:
- One thing I learned doing it:
- If I had another day, I would:
