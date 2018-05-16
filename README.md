# Anomaly Detection Learning Resources

------------

**Anomaly detection**, also known as **outlier detection**, is a fascinating and useful technique to identify outlying data objects. It has been proven critical in many fields, such as credit card fraud analytics and mechanical unit defect identification.

In this repository, you will find many:
1. Books & Academic Papers 
2. Learning Materials, e.g, online courses and videos 
3. Outlier Datasets
4. Outlier Detection Libraries & Demo Codes
5. **Paper Downloader**: a Python 3 script to download the open access papers listed in this repository. 

**I would continue adding more items to the repository**. Please feel free to suggest some key materials by opening an issue or dropping me an email (yuezhao@cs.toronto.edu). Enjoy reading!
<!-- TOC -->

- [Anomaly Detection Learning Resources](#anomaly-detection-learning-resources)
    - [1. Books & Tutorials](#1-books-tutorials)
        - [1.1. Books](#11-books)
        - [1.2. Tutorials](#12-tutorials)
    - [2. Papers](#2-papers)
        - [2.1. Overview & Survey Paper](#21-overview-survey-paper)
        - [2.2. Graph & Network Outlier Detection](#22-graph-network-outlier-detection)
        - [2.3. Time Series Outlier Detection](#23-time-series-outlier-detection)
        - [2.4. Spatial Outliers](#24-spatial-outliers)
        - [2.5. Outlier Ensembles](#25-outlier-ensembles)
    - [3. Courses/Seminars/Videos](#3-coursesseminarsvideos)
    - [4. Ouliter Datasets](#4-ouliter-datasets)
    - [5. Outlier Detection Libraries and Demo Codes](#5-outlier-detection-libraries-and-demo-codes)
        - [5.1. Python](#51-python)
        - [5.2. Java](#52-java)

<!-- /TOC -->
## 1. Books & Tutorials

### 1.1. Books
[Outlier Analysis](https://www.springer.com/gp/book/9781461463955 "Outlier Analysis") by Charu Aggarwal: Classical text book covering most of the outlier analysis techniques. A must-read for people in outlier detection. [[Preview.pdf]](http://charuaggarwal.net/outlierbook.pdf "Preview.pdf")

[Outlier Ensembles: An Introduction](https://www.springer.com/gp/book/9783319547640 "Outlier Ensembles: An Introduction") by Charu Aggarwal and Saket Sathe: Great intro book for ensemble learning in outlier anaysis.

[Data Mining: Concepts and Techniques (3rd)](https://www.elsevier.com/books/data-mining-concepts-and-techniques/han/978-0-12-381479-1 "Data Mining: Concepts and Techniques (3rd)") by Jiawei Han Micheline Kamber Jian Pei: Chapter 12 discusses outlier detection with many important points. [[[Google Search]]](https://www.google.ca/search?&q=data+mining+jiawei+han&oq=data+ming+jiawei "[Google Search]")

### 1.2. Tutorials
Kriegel, H.P., Kröger, P. and Zimek, A., 2010. Outlier detection techniques. *Tutorial at ACM SIGKDD*, 10. [[Download PDF]](https://imada.sdu.dk/~zimek/publications/KDD2010/kdd10-outlier-tutorial.pdf)


## 2. Papers

### 2.1. Overview & Survey Paper
Chandola, V., Banerjee, A. and Kumar, V., 2009. Anomaly detection: A survey. *ACM computing surveys* , 41(3), p.15. [[Download PDF]](https://www.vs.inf.ethz.ch/edu/HS2011/CPS/papers/chandola09_anomaly-detection-survey.pdf "[Download PDF]")

Hodge, V. and Austin, J., 2004. A survey of outlier detection methodologies. *Artificial intelligence review*, 22(2), pp.85-126. [[Download PDF]](https://www-users.cs.york.ac.uk/vicky/myPapers/Hodge+Austin_OutlierDetection_AIRE381.pdf "[Download PDF]")

Campos, G.O., Zimek, A., Sander, J., Campello, R.J., Micenková, B., Schubert, E., Assent, I. and Houle, M.E., 2016. On the evaluation of unsupervised outlier detection: measures, datasets, and an empirical study.* Data Mining and Knowledge Discovery*, 30(4), pp.891-927. [[HTML]](https://link.springer.com/article/10.1007/s10618-015-0444-8"[HTML]") [[SLIDES]](https://imada.sdu.dk/~zimek/InvitedTalks/TUVienna-2016-05-18-outlier-evaluation.pdf"[SLIDES]")

Goldstein, M. and Uchida, S., 2016. A comparative evaluation of unsupervised anomaly detection algorithms for multivariate data. *PloS one*, 11(4), p.e0152173.  [[Download PDF]](http://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0152173&type=printable "[Download PDF]")

### 2.2. Graph & Network Outlier Detection

### 2.3. Time Series Outlier Detection
Gupta, M., Gao, J., Aggarwal, C.C. and Han, J., 2014. Outlier detection for temporal data: A survey. *IEEE Transactions on Knowledge and Data Engineering*, 26(9), pp.2250-2267. [[Download PDF]](https://pdfs.semanticscholar.org/18d1/714870fb989f32b4311892e8765f00f7098f.pdf "[Download PDF]")

### 2.4. Spatial Outliers
### 2.5. Outlier Ensembles

Aggarwal, C.C., 2013. Outlier ensembles: position paper. *ACM SIGKDD Explorations Newsletter*, 14(2), pp.49-58. [[Download PDF]](https://pdfs.semanticscholar.org/841e/ce7c3812bbf799c99c84c064bbcf77916ba9.pdf "[Download PDF]")

Zimek, A., Campello, R.J. and Sander, J., 2014. Ensembles for unsupervised outlier detection: challenges and research questions a position paper. *ACM Sigkdd Explorations Newslette*r, 15(1), pp.11-22. [[Download PDF]](http://www.kdd.org/exploration_files/V15-01-02-Zimek.pdf "[Download PDF]")

## 3. Courses/Seminars/Videos 
**Udemy Outlier Detection Algorithms in Data Mining and Data Science**: https://www.udemy.com/outlier-detection-techniques/

**Stanford Data Mining for Cyber Security** also covers part of anomaly detection techniques. http://web.stanford.edu/class/cs259d/
## 4. Ouliter Datasets

ELKI Outlier Datasets: https://elki-project.github.io/datasets/outlier
Outlier Detection DataSets (ODDS): http://odds.cs.stonybrook.edu/#table1

## 5. Outlier Detection Libraries and Demo Codes

### 5.1. Python

[Scikit-learn Novelty and Outlier Detection](http://scikit-learn.org/stable/modules/outlier_detection.html). It supports some popular algorithms like LOF, Isolation Forest and One-class SVM

[Python Outlier Detection (PyOD)](https://github.com/yzhao062/Pyod): Under construction, it supports a series of outlier detection algorithms and combination frameworks

### 5.2. Java

[ELKI: Environment for Developing KDD-Applications Supported by Index-Structures](https://elki-project.github.io/): ELKI is an open source (AGPLv3) data mining software written in Java. The focus of ELKI is research in algorithms, with an emphasis on unsupervised methods in cluster analysis and outlier detection. 

 
