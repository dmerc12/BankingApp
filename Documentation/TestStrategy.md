# Testing Strategy:

## API guidelines:
- API should be restful.
- API will be written in python using flask.

## Workflow Guidelines:
- Version control will be handled via the use of a GitHub repository. This repository will be used for this project specifically.

## Best coding practices:
- All variable names should be spelled out completely (i.e. customer_id).
- All case conventions should be followed per the language being used:
  - Python - snake_case.
  - JSON response - camelCase.
- Development should be behaviour driven and test driven:
  - Each module in each tier should have a separate suite of unit tests consisting of at least:
    - DAL methods: 
      - 1 positive test.
    - SAL methods:
      - 1 positive test.
      - all business logic must have a negative test.
    - API methods:
      - all must have a positive test using Postman.
      - all must have negative tests for all possible errors.
  
## Test Results:
- Unit testing results will be stored in the repo in html file using pytest-html.
- Integration testing will be done utilizing Postman.