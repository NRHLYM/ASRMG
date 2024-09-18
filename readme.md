# Introduce of professor data
This is the data of five experts discussing and analyzing five microservice systems, manually labeling their odors and refactoring results for each system。

# Introduce of research2
This is the main code of ASRMG,among them, reconstruct_main.Py is for refactoring purposes, and evaluate_main.Py is for analysis purposes.
## HOW TO USE
Before running **reconstruct_main.py**, it is necessary to modify the configuration file.


   <img width="216" alt="image" src="https://github.com/user-attachments/assets/e88bd7bd-2918-4aa4-9979-44a210bc7a8d">
   
   
   <img width="416" alt="image" src="https://github.com/user-attachments/assets/263253ad-e3cb-43f0-b6fc-4711c0542583">


After running **reconstruct_main.py**,please run **evaluate_main.py** to evaluate the result.The expected output result is shown in the following figure
    
    
   <img width="416" alt="image" src="https://github.com/user-attachments/assets/17bb4e02-58da-4cdf-b2c0-077517d2f396">



# Introduce of this dataset
The repository provided 5 architectural granularity smells present in the microservices system, stored by means of Excel.
The smells were determined by our team through vote process. and was used to support the analyze of our method "**ASRMG**" to refactor microservice
architecture granularity smells.

# Structure of this dataset
Each .xlsx file consists of three columns representing **the first column** means the of the microservice, 
**the second column means** full name of the interface, 
and **the third column means** whether or not there is an architectural granularity smell. for use this dataset,
you can download these .xlxs files and read them through file operate utils(such as **pandas**) in program, and operate in the way
of operate Workbook.
