# Anomaly Detection Learning Resources

------------

**Anomaly detection**, also known as **outlier detection**, is a fascinating and useful technique to identify outlying data objects. It has been proven critical in many fields, such as credit card fraud analytics and mechanical unit defect detection.

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
    - [2. Courses/Seminars/Videos](#2-coursesseminarsvideos)
    - [3. Toolbox & Datasets](#3-toolbox-datasets)
        - [3.1. Python](#31-python)
        - [3.2. Matlab](#32-matlab)
        - [3.3. Java](#33-java)
        - [3.4. Datasets](#34-datasets)
    - [4. Papers](#4-papers)
        - [4.1. Overview & Survey Papers](#41-overview-survey-papers)
        - [4.2. Key Algorithms](#42-key-algorithms)
        - [4.3. Graph & Network Outlier Detection](#43-graph-network-outlier-detection)
        - [4.4. Time Series Outlier Detection](#44-time-series-outlier-detection)
        - [4.5. Spatial Outliers](#45-spatial-outliers)
        - [4.6. High-dimensional & Subspace Outliers](#46-high-dimensional-subspace-outliers)
        - [4.7. Outlier Ensembles](#47-outlier-ensembles)
    - [5. Key Conferences/Workshops/Journals](#5-key-conferencesworkshopsjournals)
        - [6.1. Conferences & Workshopes](#61-conferences-workshopes)
        - [6.2. Journals](#62-journals)

<!-- /TOC -->
## 1. Books & Tutorials

### 1.1. Books
[Outlier Analysis](https://www.springer.com/gp/book/9781461463955 "Outlier Analysis") by Charu Aggarwal: Classical text book covering most of the outlier analysis techniques. A must-read for people in outlier detection. [[Preview.pdf]](http://charuaggarwal.net/outlierbook.pdf "Preview.pdf")

[Outlier Ensembles: An Introduction](https://www.springer.com/gp/book/9783319547640 "Outlier Ensembles: An Introduction") by Charu Aggarwal and Saket Sathe: Great intro book for ensemble learning in outlier anaysis.

[Data Mining: Concepts and Techniques (3rd)](https://www.elsevier.com/books/data-mining-concepts-and-techniques/han/978-0-12-381479-1 "Data Mining: Concepts and Techniques (3rd)") by Jiawei Han Micheline Kamber Jian Pei: Chapter 12 discusses outlier detection with many important points. [[Google Search]](https://www.google.ca/search?&q=data+mining+jiawei+han&oq=data+ming+jiawei "[Google Search]")

### 1.2. Tutorials
Kriegel, H.P., Kröger, P. and Zimek, A., 2010. Outlier detection techniques. *Tutorial at ACM SIGKDD*, 10. [[Download PDF]](https://imada.sdu.dk/~zimek/publications/KDD2010/kdd10-outlier-tutorial.pdf)

Chawla, S. and Chandola, V., 2011, Anomaly Detection: A Tutorial. *Tutorial at ICDM 2011*.  [[Download PDF]](http://webdocs.cs.ualberta.ca/~icdm2011/downloads/ICDM2011_anomaly_detection_tutorial.pdf)

Lazarevic, A., Banerjee, A., Chandola, V., Kumar, V. and Srivastava, J., 2008, September. Data mining for anomaly detection. In *Tutorial at ECML PKDD 2008*. [[See Video]](http://videolectures.net/ecmlpkdd08_lazarevic_dmfa/)

## 2. Courses/Seminars/Videos 

**Coursera Introduction to Anomaly Detection (by IBM)**:
https://www.coursera.org/learn/ai/lecture/ASPv0/introduction-to-anomaly-detection

**Coursera Machine Learning by Andrew Ng also partly covers the topic**:
- [Anomaly Detection vs. Supervised Learning](https://www.coursera.org/learn/machine-learning/lecture/Rkc5x/anomaly-detection-vs-supervised-learning)
- [Developing and Evaluating an Anomaly Detection System](https://www.coursera.org/learn/machine-learning/lecture/Mwrni/developing-and-evaluating-an-anomaly-detection-system)

**Udemy Outlier Detection Algorithms in Data Mining and Data Science**: https://www.udemy.com/outlier-detection-techniques/

**Stanford Data Mining for Cyber Security** also covers part of anomaly detection techniques. http://web.stanford.edu/class/cs259d/


## 3. Toolbox & Datasets

### 3.1. Python

[Scikit-learn Novelty and Outlier Detection](http://scikit-learn.org/stable/modules/outlier_detection.html). It supports some popular algorithms like LOF, Isolation Forest and One-class SVM

[Python Outlier Detection (PyOD)](https://github.com/yzhao062/Pyod): Under construction, it supports a series of outlier detection algorithms and combination frameworks. It is now released on PyPI and can be installed with "pip install pyod".

### 3.2. Matlab
[Anomaly Detection Toolbox - Beta](http://dsmi-lab-ntust.github.io/AnomalyDetectionToolbox/): A collection of popular outlier detection algorithms in Matlab.

### 3.3. Java

[ELKI: Environment for Developing KDD-Applications Supported by Index-Structures](https://elki-project.github.io/): ELKI is an open source (AGPLv3) data mining software written in Java. The focus of ELKI is research in algorithms, with an emphasis on unsupervised methods in cluster analysis and outlier detection. 

### 3.4. Datasets

**ELKI Outlier Datasets**: https://elki-project.github.io/datasets/outlier

**Outlier Detection DataSets (ODDS)**: http://odds.cs.stonybrook.edu/#table1

**Unsupervised Anomaly Detection Dataverse**: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OPQMVF

**Anomaly Detection Meta-Analysis Benchmarks**: https://ir.library.oregonstate.edu/concern/datasets/47429f155

## 4. Papers

### 4.1. Overview & Survey Papers

Chandola, V., Banerjee, A. and Kumar, V., 2009. Anomaly detection: A survey. *ACM computing surveys* , 41(3), p.15. [[Download PDF]](https://www.vs.inf.ethz.ch/edu/HS2011/CPS/papers/chandola09_anomaly-detection-survey.pdf )

Hodge, V. and Austin, J., 2004. A survey of outlier detection methodologies. *Artificial intelligence review*, 22(2), pp.85-126. [[Download PDF]](https://www-users.cs.york.ac.uk/vicky/myPapers/Hodge+Austin_OutlierDetection_AIRE381.pdf )

Campos, G.O., Zimek, A., Sander, J., Campello, R.J., Micenková, B., Schubert, E., Assent, I. and Houle, M.E., 2016. On the evaluation of unsupervised outlier detection: measures, datasets, and an empirical study. *Data Mining and Knowledge Discovery*, 30(4), pp.891-927. [[HTML]](https://link.springer.com/article/10.1007/s10618-015-0444-8"[HTML]") [[SLIDES]](https://imada.sdu.dk/~zimek/InvitedTalks/TUVienna-2016-05-18-outlier-evaluation.pdf"[SLIDES]")

Goldstein, M. and Uchida, S., 2016. A comparative evaluation of unsupervised anomaly detection algorithms for multivariate data. *PloS one*, 11(4), p.e0152173.  [[Download PDF]](http://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0152173&type=printable )

### 4.2. Key Algorithms

**k Nearst Neighbors (kNN) Outlier Detector**.
- Ramaswamy, S., Rastogi, R. and Shim, K., 2000, May. Efficient algorithms for mining outliers from large data sets. *ACM Sigmod Record*, 29(2), pp. 427-438). [[Download PDF]](https://webdocs.cs.ualberta.ca/~zaiane/pub/check/ramaswamy.pdf)
- Angiulli, F. and Pizzuti, C., 2002, August. Fast outlier detection in high dimensional spaces. In *European Conference on Principles of Data Mining and Knowledge Discovery* pp. 15-27. [[HTML]](https://link.springer.com/chapter/10.1007/3-540-45681-3_2)

**Local Outlier Factor (LOF)**. Breunig, M.M., Kriegel, H.P., Ng, R.T. and Sander, J., 2000, May. LOF: identifying density-based local outliers. *ACM Sigmod Record*, 29(2), pp. 93-104. [[Download PDF]](http://www.dbs.ifi.lmu.de/Publikationen/Papers/LOF.pdf)

### 4.3. Graph & Network Outlier Detection
Akoglu, L., Tong, H. and Koutra, D., 2015. Graph based anomaly detection and description: a survey. *Data Mining and Knowledge Discovery*, 29(3), pp.626-688. [[Download PDF]](https://arxiv.org/pdf/1404.4679.pdf)

### 4.4. Time Series Outlier Detection
Gupta, M., Gao, J., Aggarwal, C.C. and Han, J., 2014. Outlier detection for temporal data: A survey. *IEEE Transactions on Knowledge and Data Engineering*, 26(9), pp.2250-2267. [[Download PDF]](https://pdfs.semanticscholar.org/18d1/714870fb989f32b4311892e8765f00f7098f.pdf )

### 4.5. Spatial Outliers

### 4.6. High-dimensional & Subspace Outliers
Zimek, A., Schubert, E. and Kriegel, H.P., 2012. A survey on unsupervised outlier detection in high‐dimensional numerical data. *Statistical Analysis and Data Mining: The ASA Data Science Journal*, 5(5), pp.363-387. [[Downloadable Link]](https://onlinelibrary.wiley.com/doi/abs/10.1002/sam.11161)

### 4.7. Outlier Ensembles

Aggarwal, C.C., 2013. Outlier ensembles: position paper. *ACM SIGKDD Explorations Newsletter*, 14(2), pp.49-58. [[Download PDF]](https://pdfs.semanticscholar.org/841e/ce7c3812bbf799c99c84c064bbcf77916ba9.pdf )

Zimek, A., Campello, R.J. and Sander, J., 2014. Ensembles for unsupervised outlier detection: challenges and research questions a position paper. *ACM Sigkdd Explorations Newslette*r, 15(1), pp.11-22. [[Download PDF]](http://www.kdd.org/exploration_files/V15-01-02-Zimek.pdf )

## 5. Key Conferences/Workshops/Journals
### 6.1. Conferences & Workshopes
[ACM International Conference on Knowledge Discovery and Data Mining (SIGKDD)](http://www.kdd.org/conferences)
 **Note: SIGKDD is usually associated with an Outlier Detection Workshop (ODD), see [ODD 2018](https://www.andrew.cmu.edu/user/lakoglu/odd/index.html)**.

[ACM International Conference on Management of Data (SIGMOD)](https://sigmod.org/)

[The Web Conference (WWW)](https://www2018.thewebconf.org/)

[IEEE International Conference on Data Mining (ICDM)](http://icdm2018.org/)

[SIAM International Conference on Data Mining (SDM)](https://www.siam.org/meetings/sdm18/)

[IEEE International Conference on Data Engineering (ICDE)](https://icde2018.org/)

[ACM InternationalConference on Information and Knowledge Management (CIKM)](http://www.cikmconference.org/)

[ACM International Conference on Web Search and Data Mining(WSDM)](http://www.wsdm-conference.org/2018/)

[The European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML-PKDD)](http://www.ecmlpkdd2018.org/)

[The Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD)](http://prada-research.net/pakdd18/)

### 6.2. Journals 

[ACM Transactions on Knowledge Discovery from Data (TKDD)](https://tkdd.acm.org/)

[IEEE Transactions on Knowledge and Data Engineering (TKDE)](https://www.computer.org/web/tkde)

[ACM SIGKDD Explorations Newsletter](http://www.kdd.org/explorations)

[Data Mining and Knowledge Discovery](https://link.springer.com/journal/10618)

[Knowledge and Information Systems (KAIS)](https://link.springer.com/journal/10115)