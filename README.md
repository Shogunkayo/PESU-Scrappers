# PESU Scrappers
----

## Overview:

- This repository contains python scripts to scrape publicly available information from websites related to PES University.
- The main purpose is to scrape instagram posts of various clubs and announcements made by the university, and compile them so that the chances of missing out are reduced
- The srn scrapper scrapes the registration numbers, which can be used as a method of verifying people 


## Installation:

- The following modules are used which are not built-in

1. selenium
```
pip install selenium
```

2.  webdriver_manager
```
pip install webdriver_manager
```


## How To Use:

#### 1. SRN Scrapper

```
python3 srn_scrapper.py {arguements}
```

##### Arguements - 

- Scrape a single srn and print the details
```
python3 srn_scrapper.py 1 [srn]
```

- Scrape all the srns in a particular branch and write the details to a csv file
 ```
python3 srn_scrapper.py 2 [branch_code] [year in YY format] [campus_code]
```         
   
- Scrape all the srns from a particular year and campus, and write to a csv file
```
python3 srn_scrapper.py 3 [year in YYYY format] [campus_code]
```      

   
| Campus Code | Campus    |
| ----------- | --------- |
| 1           | RR Campus |
| 2           | EC Campus | 

| Branch Code | Branch           |
| ----------- | ---------------- |
| CS          | Computer Science |
| EC          | Electronics      |
| EE          | Electrical       |
| ME          | Mechanical       |
| BT          | Biotech          |
| BB          | BBA              |
| AL          | BBA-LLB          |
| BL          | BB-LLB           |
| BA          | Architecture     |
| BD          | Design           |
| MB          | MBA              | 
