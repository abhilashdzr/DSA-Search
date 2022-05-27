A Search Engine to hunt DSA problems from Codeforces, Codechef and Leetcode.

The app is hosted on https://desearch.herokuapp.com/ 

<h2>Note</h2> 

**1. Please do not query over heroku, the app will break** </br>
**2. The app doesn't run outside virtual environment as of now**

<h2>Installation</h2>
1 Clone the repository and change dir to the project dir </br>

`git clone https://github.com/abhilashdzr/DSA-Search.git`</br>

2 Change to project directory
  `cd ./DSA-Search `

3 Start and activate a virtual environment `python3 -m venv env` `source env/bin/activate` </br>

4 Install node `https://nodejs.org/en/download/`

5 Install dependencies
`pip install -r requirements.txt`
`npm install`

6 Run the server `npm start`</br>

7 Log in to `localhost:3000`

<h2>POINTS to NOTE when querying</h2>
1. See that the spellings of the words are correct </br>
2. In case none of the typed words are familiar to the database, it will randomly generate 10 results. </br>
3. It might be possible that the question you type in is not present in the database, so might not be retrieved. If you do not get appropriate results, then try adding a few more keywords or correct any spelling mistake, if present </br>
4. This database might show results according to question tags, but will not according to company tags (e.g. Amazon, Microsoft) </br>
5. Any query takes at most 2.5 seconds to load, so hang on for that time  </br>
