*** Settings ***
Library     Homepage.py  browser=chrome


*** Test Cases ***
Successfully perform a test against the home page
    # Step 1
    open browser

    # Step 2
    select category                 # selects "Government"

    # Step 3
    input zip code                  code=00001

    # Step 4, 5 and 6
    click find lawyer

    # Step 8 to 13
    select other categories for     times=5

    # Step 14
    scrolldown

    # Step 15 and 16
    loop through quotes             direction=right

    # Step 17
    loop through quotes             direction=left

    # Step 18
    assert meta tag                 meta=<meta name="keywords" content="find a lawyer, find an attorney, find lawyers, find attorneys, legal help">