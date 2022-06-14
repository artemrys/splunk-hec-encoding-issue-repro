# splunk-hec-encoding-issue-repro

This repository shows the issue with the encoding when data is being ingested to Splunk via HEC.

There are 2 images showing 2 scenarios, when data is being ingested and being showed in Japanese and another case when data is being showed using Unicode characters.

Working example:

![Working example](/images/working.png "Working example")

Not working example:

![Not working example](/images/not_working.png "Not working example")

To run the examples youself:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests

python main_working.py
python main_not_working.py
```
