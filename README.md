Features : 
- The automation runs in RobotFramework for Selenium in Python programming language
- This has the capability to run your `chrome` and/or `firefox` regardless of your platform (Mac, Linux or Windows) 
- This generates a report log after the execution. The log can be seen in the root directory (`/legalmatch`)
- The report consists of 3 files : 
1. `log.html`
2. `output.xml`
3. `report.html`

Requirements : 

- Python 3.6.*
- pyenv (`brew install pyenv` for Mac)
- Chrome version 83.*
- Firefox version 77.*

Installation : 

- Clone the repository
- Run `pip install -r requirements.txt`

Running the test : 
- `cd` to `legalmatch/tests/homepage/`
- Run `robot --variable browser:chrome  ./tests/homepage/TestHomePage.robot`
- If you prefer to run it with Firefox, just change the value of `browser` variable to `firefox` as in `browser:firefox`
- The browser will open and do as what the steps in the exam requires. (please see the `TestHomePage.robot` for the reference of the keywords being run)
- After the execution, there will 3 files generated related to result of the test. To see the report, open the `log.html` from the root directory of this repository to your desired browser.

Note : 
- The 3 files are rewritten everytime you re-run the test.
 