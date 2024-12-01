Feature: Find car details

    Read input file to get the car reg
    Get car details from webuyanycar website
    Compare the details with output file.

    @FindCarDetails @CompareCarDetails
    Scenario Outline: Find car details based on registration
        Given Get the car registration from input file '<inputFileName>'
        And User launch the webuyanycar application
        When User retrieves car details from UI based on reg
        Then I compare with output file data 'car_output V4.txt'

        Examples:
            | inputFileName    |
            | car_input V4.txt |
