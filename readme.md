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


## Introduce of experts
1.**Xin Chen**: He presided over one National Natural Science Foundation project and one Provincial Natural Science Foundation project. Published over 40 papers, including IEEE/ACM Transactions (TSE, TR, TOIT), EMSE, SANER, ISSRE, IST, FCS, ASOC Computer Research and Development, and other well-known domestic and international journals and conferences.
2.**Jie Chen**: In 2016, she obtained a doctorate degree in computing software and theory from the Software Research Institute of the Chinese Academy of Sciences. Her main research interests including: software engineering and big data analysis, involving data mining in the open source community, code quality analysis, etc.
3. **Bin Hu**: Participated in a project funded by the National Natural Science Foundation of China. Published two high-level international conference papers as the first author
4. **Sixuan Wang**: He has served as the chief architect and technical consultant for multiple leading enterprises' digital transformation projects, covering various industries. He has years of experience in combining academic research with practical enterprise engineering,and has rich experience in school enterprise cooperation, student training, and the integration of government, industry, academia, and research.
5. **Dongjin Yu**: He has published more than 100 academic papers in SCI indexed journals, first-class journals, and international important academic conferences, edited 5 monographs, and edited one textbook for the "Twelfth Five Year Plan" for outstanding engineers.

# Introduce of Experiments
This is the main code of ASRMG, among them, reconstruct_main.Py is for refactoring purposes, and evaluate_main.Py is for analysis purposes. RQ1 to RQ4 in this article **ASRMG** are based on the analyzed data.
## HOW TO USE
Before running **reconstruct_main.py**, it is necessary to modify the configuration file. Please change the path in config to the path where your own files are stored which is shown as the picture below.


   <img width="216" alt="image" src="https://github.com/user-attachments/assets/e88bd7bd-2918-4aa4-9979-44a210bc7a8d">
   
   
   <img width="416" alt="image" src="https://github.com/user-attachments/assets/263253ad-e3cb-43f0-b6fc-4711c0542583">


After running **reconstruct_main.py**, you just need to run **evaluate_main.py** to evaluate the result of **reconstruct_main.py**. The expected output result is shown in the following figure
    
    
   <img width="416" alt="image" src="https://github.com/user-attachments/assets/17bb4e02-58da-4cdf-b2c0-077517d2f396">
