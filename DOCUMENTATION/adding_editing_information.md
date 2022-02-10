# Instructions on adding and editing information displayed on the Portal

## Funding opportunities

We collect funding opportunities relevant for COVID-19, infectious diseases, and antibiotic resistance research. These are displayed on `/funding/`. The data is stored in JSON format in `data/funding.json`. Below is the format used for each entry. All required fields have to be filled out and in some cases there is a specific format. Note that for the field *topic* you should choose one or more topics corresponding of the call.

```JSON
{
  "topic": ["COVID-19", "General", "Antibiotic resistance", "Infectious diseases"],
  "funder": "funder name, required field",
  "call_title": "call title, required field",
  "call_url": "call URL, including https://, required field",
  "call_description": "call description, optional field, markdown formatting allowed",
  "applicant": "information about who can apply, optional field, markdown formatting allowed",
  "decision_date": "information about when the decision will be made, optional field",
  "funding_period": "information about the duration of funding, optional field",
  "funding_amount": "information about the amount one call apply for, optional field",
  "submission_opendate": "date in format '2006-01-02', optional field",
  "submission_deadline": "date in format '2006-01-02', required field"
}
```
