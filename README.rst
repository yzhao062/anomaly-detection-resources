Anomaly Detection Learning Resources
====================================

.. image:: https://img.shields.io/github/stars/yzhao062/anomaly-detection-resources.svg
   :target: https://github.com/yzhao062/anomaly-detection-resources/stargazers
   :alt: GitHub stars


.. image:: https://img.shields.io/github/forks/yzhao062/anomaly-detection-resources.svg?color=blue
   :target: https://github.com/yzhao062/anomaly-detection-resources/network
   :alt: GitHub forks


.. image:: https://img.shields.io/github/license/yzhao062/anomaly-detection-resources.svg?color=blue
   :target: https://github.com/yzhao062/anomaly-detection-resources/blob/master/LICENSE
   :alt: License


.. image:: https://awesome.re/badge-flat2.svg
   :target: https://awesome.re/badge-flat2.svg
   :alt: Awesome


.. image:: https://img.shields.io/badge/ADBench-benchmark_results-pink
   :target: https://github.com/Minqi824/ADBench
   :alt: Benchmark


----

`Outlier Detection <https://en.wikipedia.org/wiki/Anomaly_detection>`_
(also known as *Anomaly Detection*) is an exciting yet challenging field,
which aims to identify outlying objects that are deviant from the general data distribution.
Outlier detection has been proven critical in many fields, such as credit card
fraud analytics, network intrusion detection, and mechanical unit defect detection.

**This repository collects**:


#. Books & Academic Papers 
#. Online Courses and Videos
#. Outlier Datasets
#. Open-source and Commercial Libraries/Toolkits
#. Key Conferences & Journals


**More items will be added to the repository**.
Please feel free to suggest other key resources by opening an issue report,
submitting a pull request, or dropping me an email @ (yzhao010@usc.edu).
Enjoy reading!

BTW, you may find my `[GitHub] <https://github.com/yzhao062>`_ and
`[outlier detection papers] <https://scholar.google.com/citations?user=zoGDYsoAAAAJ&hl=en>`_ useful,
especially `PyOD library <https://github.com/yzhao062/pyod>`_ and `ADBench benchmark <https://github.com/Minqi824/ADBench>`_.

----

Table of Contents
-----------------


* `1. Books & Tutorials & Benchmarks <#1-books--tutorials--benchmarks>`_

  * `1.1. Books <#11-books>`_
  * `1.2. Tutorials <#12-tutorials>`_
  * `1.3. Benchmarks <#13-benchmarks>`_

* `2. Courses/Seminars/Videos <#2-coursesseminarsvideos>`_
* `3. Toolbox & Datasets <#3-toolbox--datasets>`_

  * `3.1. Multivariate data outlier detection <#31-multivariate-data>`_
  * `3.2. Time series outlier detection <#32-time-series-outlier-detection>`_
  * `3.3. Graph Outlier Detection <#33-graph-outlier-detection>`_
  * `3.4. Real-time Elasticsearch <#34-real-time-elasticsearch>`_
  * `3.5. Datasets <#35-datasets>`_

* `4. Papers <#4-papers>`_

  * `4.1. Overview & Survey Papers <#41-overview--survey-papers>`_
  * `4.2. Key Algorithms <#42-key-algorithms>`_
  * `4.3. Graph & Network Outlier Detection <#43-graph--network-outlier-detection>`_
  * `4.4. Time Series Outlier Detection <#44-time-series-outlier-detection>`_
  * `4.5. Feature Selection in Outlier Detection <#45-feature-selection-in-outlier-detection>`_
  * `4.6. High-dimensional & Subspace Outliers <#46-high-dimensional--subspace-outliers>`_
  * `4.7. Outlier Ensembles <#47-outlier-ensembles>`_
  * `4.8. Outlier Detection in Evolving Data <#48-outlier-detection-in-evolving-data>`_
  * `4.9. Representation Learning in Outlier Detection <#49-representation-learning-in-outlier-detection>`_
  * `4.10. Interpretability <#410-interpretability>`_
  * `4.11. Outlier Detection with Neural Networks <#411-outlier-detection-with-neural-networks>`_
  * `4.12. Active Anomaly Detection <#412-active-anomaly-detection>`_
  * `4.13. Interactive Outlier Detection <#413-interactive-outlier-detection>`_
  * `4.14. Outlier Detection in Other fields <#414-outlier-detection-in-other-fields>`_
  * `4.15. Outlier Detection Applications <#415-outlier-detection-applications>`_
  * `4.16. Automated Outlier Detection <#416-automated-outlier-detection>`_
  * `4.17. Machine Learning Systems for Outlier Detection <#417-machine-learning-systems-for-outlier-detection>`_
  * `4.18. Fairness and Bias in Outlier Detection <#418-fairness-and-bias-in-outlier-detection>`_
  * `4.19. Isolation-based Methods <#419-isolation-based-methods>`_
  * `4.20. Emerging and Interesting Topics <#420-emerging-and-interesting-topics>`_

* `5. Key Conferences/Workshops/Journals <#5-key-conferencesworkshopsjournals>`_

  * `5.1. Conferences & Workshops <#51-conferences--workshops>`_
  * `5.2. Journals <#52-journals>`_


----


1. Books & Tutorials & Benchmarks
---------------------------------

1.1. Books
^^^^^^^^^^

`Outlier Analysis <https://link.springer.com/book/10.1007/978-3-319-47578-3>`_ 
by Charu Aggarwal: Classical text book covering most of the outlier analysis techniques. 
A **must-read** for people in the field of outlier detection. `[Preview.pdf] <http://charuaggarwal.net/outlierbook.pdf>`_

`Outlier Ensembles: An Introduction <https://www.springer.com/gp/book/9783319547640>`_ 
by Charu Aggarwal and Saket Sathe: Great intro book for ensemble learning in outlier analysis.

`Data Mining: Concepts and Techniques (3rd) <https://www.elsevier.com/books/data-mining-concepts-and-techniques/han/978-0-12-381479-1>`_ 
by Jiawei Han and Micheline Kamber and Jian Pei: Chapter 12 discusses outlier detection with many key points. `[Google Search] <https://www.google.ca/search?&q=data+mining+jiawei+han&oq=data+ming+jiawei>`_

1.2. Tutorials
^^^^^^^^^^^^^^

===================================================== ============================================  =====  ============================  ==========================================================================================================================================================================
Tutorial Title                                        Venue                                         Year   Ref                           Materials
===================================================== ============================================  =====  ============================  ==========================================================================================================================================================================
Data mining for anomaly detection                     PKDD                                          2008   [#Lazarevic2008Data]_         `[Video] <http://videolectures.net/ecmlpkdd08_lazarevic_dmfa/>`_
Outlier detection techniques                          ACM SIGKDD                                    2010   [#Kriegel2010Outlier]_        `[PDF] <https://imada.sdu.dk/~zimek/publications/KDD2010/kdd10-outlier-tutorial.pdf>`_
Anomaly Detection: A Tutorial                         ICDM                                          2011   [#Chawla2011Anomaly]_         `[PDF] <http://webdocs.cs.ualberta.ca/~icdm2011/downloads/ICDM2011_anomaly_detection_tutorial.pdf>`_
Anomaly Detection in Networks                         KDD                                           2017   [#Mendiratta2017Anomaly]_     `[Page] <https://veena-mendiratta.blog/tutorial-anomaly-detection-in-networks/>`_
Which Outlier Detector Should I use?                  ICDM                                          2018   [#Ting2018Which]_             `[PDF] <https://ieeexplore.ieee.org/document/8594824>`_
Deep Learning for Anomaly Detection                   KDD                                           2020   [#Wang2020Deep]_              `[HTML] <https://sites.google.com/view/kdd2020deepeye/home>`_, `[Video] <https://www.youtube.com/watch?v=Fn0qDbKL3UI&list=PLn0nrSd4xjja7AD3aY9Jxmr820gx59EQC&index=66>`_
Deep Learning for Anomaly Detection                   WSDM                                          2021   [#Pang2021Deep]_              `[HTML] <https://sites.google.com/site/gspangsite/wsdm21_tutorial>`_
Toward Explainable Deep Anomaly Detection             KDD                                           2021   [#Pang2021Toward]_            `[HTML] <https://sites.google.com/site/gspangsite/kdd21_tutorial>`_
Recent Advances in Anomaly Detection                  CVPR                                          2023   [#Pang2023recent]_            `[HTML] <https://sites.google.com/view/cvpr2023-tutorial-on-ad/>`_, `[Video] <https://www.youtube.com/watch?v=dXxrzWeybBo&feature=youtu.be>`_
Trustworthy Anomaly Detection                         SDM                                           2024   [#Yuan2024Trustworthy]_       `[HTML] <https://yuan.shuhan.org/talks/SDM24/>`_
===================================================== ============================================  =====  ============================  ==========================================================================================================================================================================


1.3. Benchmarks
^^^^^^^^^^^^^^^

**News**: We just released a 36-page, the most comprehensive `anomaly detection benchmark paper <https://www.andrew.cmu.edu/user/yuezhao2/papers/22-preprint-adbench.pdf>`_.
The fully `open-sourced ADBench <https://github.com/Minqi824/ADBench>`_ compares 30 anomaly detection algorithms on 55 benchmark datasets.


=============  =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Data Types     Paper Title                                                                                        Venue                         Year   Ref                           Materials
=============  =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Time-series    Revisiting Time Series Outlier Detection: Definitions and Benchmarks                               NeurIPS                       2021   [#Lai2021Revisiting]_         `[PDF] <https://openreview.net/pdf?id=r8IvOsnHchr>`_, `[Code] <https://github.com/datamllab/tods/tree/benchmark>`_
Graph          Benchmarking Node Outlier Detection on Graphs                                                      NeurIPS                       2022   [#Liu2022Benchmarking]_       `[PDF] <https://arxiv.org/abs/2206.10071>`_, `[Code] <https://github.com/pygod-team/pygod/tree/main/benchmark>`_
Graph          GADBench: Revisiting and Benchmarking Supervised Graph Anomaly Detection                           NeurIPS                       2023   [#Tang2023GADBench]_          `[PDF] <https://arxiv.org/abs/2306.12251>`_, `[Code] <https://github.com/squareRoot3/GADBench>`_
Tabular        ADBench: Anomaly Detection Benchmark                                                               NeurIPS                       2022   [#Han2022Adbench]_            `[PDF] <https://arxiv.org/abs/2206.09426>`_, `[Code] <https://github.com/Minqi824/ADBench>`_
Tabular        ADGym: Design Choices for Deep Anomaly Detection                                                   NeurIPS                       2023   [#Jiang2023adgym]_            `[PDF] <https://arxiv.org/abs/2309.15376>`_, `[Code] <https://github.com/Minqi824/ADGym>`_
=============  =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


----

2. Courses/Seminars/Videos
--------------------------

**Coursera Introduction to Anomaly Detection (by IBM)**\ :
`[See Video] <https://www.coursera.org/learn/ai/lecture/ASPv0/introduction-to-anomaly-detection>`_

**Get started with the Anomaly Detection API (by IBM)**\ :
`[See Website] <https://developer.ibm.com/learningpaths/get-started-anomaly-detection-api/>`_

**Practical Anomaly Detection by appliedAI Institute**\:
`[See Website] <https://transferlab.ai/trainings/practical-anomaly-detection/>`_, `[See Video] <https://www.youtube.com/watch?v=sEoMIDARpJ0&list=PLz6xKPm1Bnd6cDDgct3MDhNWJuPXzsmyW>`_, `[See GitHub] <https://github.com/aai-institute/tfl-training-practical-anomaly-detection>`_

**Coursera Real-Time Cyber Threat Detection and Mitigation partly covers the topic**\ :
`[See Video] <https://www.coursera.org/learn/real-time-cyber-threat-detection>`_

**Coursera Machine Learning by Andrew Ng also partly covers the topic**\ :


* `Anomaly Detection vs. Supervised Learning <https://www.coursera.org/learn/machine-learning/lecture/Rkc5x/anomaly-detection-vs-supervised-learning>`_
* `Developing and Evaluating an Anomaly Detection System <https://www.coursera.org/learn/machine-learning/lecture/Mwrni/developing-and-evaluating-an-anomaly-detection-system>`_

**Udemy Outlier Detection Algorithms in Data Mining and Data Science**\ :
`[See Video] <https://www.udemy.com/outlier-detection-techniques/>`_

**Stanford Data Mining for Cyber Security** also covers part of anomaly detection techniques\ :
`[See Video] <http://web.stanford.edu/class/cs259d/>`_

----

3. Toolbox & Datasets
---------------------

3.1. Multivariate Data
^^^^^^^^^^^^^^^^^^^^^^

[**Python**] `Python Outlier Detection (PyOD) <https://github.com/yzhao062/pyod>`_\ : PyOD is a comprehensive and scalable Python toolkit for detecting outlying objects in multivariate data. It contains more than 20 detection algorithms, including emerging deep learning models and outlier ensembles.

[**Python**, **GPU**] `TOD: Tensor-based Outlier Detection (PyTOD) <https://github.com/yzhao062/pytod>`_: A general GPU-accelerated framework for outlier detection.

[**Python**] `Python Streaming Anomaly Detection (PySAD) <https://github.com/selimfirat/pysad>`_\ : PySAD is a streaming anomaly detection framework in Python, which provides a complete set of tools for anomaly detection experiments. It currently contains more than 15 online anomaly detection algorithms and 2 different methods to integrate PyOD detectors to the streaming setting.

[**Python**] `Scikit-learn Novelty and Outlier Detection <http://scikit-learn.org/stable/modules/outlier_detection.html>`_. It supports some popular algorithms like LOF, Isolation Forest, and One-class SVM.

[**Python**] `Scalable Unsupervised Outlier Detection (SUOD) <https://github.com/yzhao062/suod>`_\ : SUOD (Scalable Unsupervised Outlier Detection) is an acceleration framework for large-scale unsupervised outlier detector training and prediction, on top of PyOD.

[**Julia**] `OutlierDetection.jl <https://github.com/OutlierDetectionJL/OutlierDetection.jl>`_\ : OutlierDetection.jl is a Julia toolkit for detecting outlying objects, also known as anomalies.

[**Java**] `ELKI: Environment for Developing KDD-Applications Supported by Index-Structures <https://elki-project.github.io/>`_\ :
ELKI is an open source (AGPLv3) data mining software written in Java. The focus of ELKI is research in algorithms, with an emphasis on unsupervised methods in cluster analysis and outlier detection. 

[**Java**] `RapidMiner Anomaly Detection Extension <https://github.com/Markus-Go/rapidminer-anomalydetection>`_\ : The Anomaly Detection Extension for RapidMiner comprises the most well know unsupervised anomaly detection algorithms, assigning individual anomaly scores to data rows of example sets. It allows you to find data, which is significantly different from the normal, without the need for the data being labeled.

[**R**] `CRAN Task View: Anomaly Detection with R <https://github.com/pridiltal/ctv-AnomalyDetection>`_\ : This CRAN task view contains a list of packages that can be used for anomaly detection with R.

[**R**] `outliers package <https://cran.r-project.org/web/packages/outliers/index.html>`_\ : A collection of some tests commonly used for identifying outliers in R.

[**Matlab**] `Anomaly Detection Toolbox - Beta <http://dsmi-lab-ntust.github.io/AnomalyDetectionToolbox/>`_\ : A collection of popular outlier detection algorithms in Matlab.


3.2. Time Series Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[**Python**] `TODS <https://github.com/datamllab/tods>`_\ : TODS is a full-stack automated machine learning system for outlier detection on multivariate time-series data.

[**Python**] `skyline <https://github.com/earthgecko/skyline>`_\ : Skyline is a near real time anomaly detection system.

[**Python**] `banpei <https://github.com/tsurubee/banpei>`_\ : Banpei is a Python package of the anomaly detection.

[**Python**] `telemanom <https://github.com/khundman/telemanom>`_\ : A framework for using LSTMs to detect anomalies in multivariate time series data.

[**Python**] `DeepADoTS <https://github.com/KDD-OpenSource/DeepADoTS>`_\ : A benchmarking pipeline for anomaly detection on time series data for multiple state-of-the-art deep learning methods.

[**Python**] `NAB: The Numenta Anomaly Benchmark <https://github.com/numenta/NAB>`_\ : NAB is a novel benchmark for evaluating algorithms for anomaly detection in streaming, real-time applications.

[**Python**] `CueObserve <https://github.com/cuebook/CueObserve>`_\ : Anomaly detection on SQL data warehouses and databases.

[**Python**] `Chaos Genius <https://github.com/chaos-genius/chaos_genius>`_\ : ML powered analytics engine for outlier/anomaly detection and root cause analysis.

[**R**] `CRAN Task View: Anomaly Detection with R <https://github.com/pridiltal/ctv-AnomalyDetection>`_\ : This CRAN task view contains a list of packages that can be used for anomaly detection with R.

[**R**] `AnomalyDetection <https://github.com/twitter/AnomalyDetection>`_\ : AnomalyDetection is an open-source R package to detect anomalies which is robust, from a statistical standpoint, in the presence of seasonality and an underlying trend.

[**R**] `anomalize <https://cran.r-project.org/web/packages/anomalize/>`_\ : The 'anomalize' package enables a "tidy" workflow for detecting anomalies in data.


3.3. Graph Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[**Python**] `Python Graph Outlier Detection (PyGOD) <https://github.com/pygod-team/pygod/>`_\ : PyGOD is a Python library for graph outlier detection (anomaly detection). It includes more than 10 latest graph-based detection algorithms


3.4. Real-time Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[**Open Distro**] `Real Time Anomaly Detection in Open Distro for Elasticsearch by Amazon <https://github.com/aws/random-cut-forest-by-aws>`_\ : A machine learning-based anomaly detection plugins for Open Distro for Elasticsearch. See `Real Time Anomaly Detection in Open Distro for Elasticsearch <https://opendistro.github.io/for-elasticsearch/blog/odfe-updates/2019/11/real-time-anomaly-detection-in-open-distro-for-elasticsearch/>`_.

[**Python**] `datastream.io <https://github.com/MentatInnovations/datastream.io>`_\ : An open-source framework for real-time anomaly detection using Python, Elasticsearch and Kibana.


3.5. Datasets
^^^^^^^^^^^^^

**ELKI Outlier Datasets**\ : https://elki-project.github.io/datasets/outlier

**Outlier Detection DataSets (ODDS)**\ : http://odds.cs.stonybrook.edu/#table1

**Unsupervised Anomaly Detection Dataverse**\ : https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OPQMVF

**Anomaly Detection Meta-Analysis Benchmarks**\ : https://ir.library.oregonstate.edu/concern/datasets/47429f155

**Skoltech Anomaly Benchmark (SKAB)**\ : https://github.com/waico/skab


----


4. Papers
---------

4.1. Overview & Survey Papers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Papers are sorted by the publication year.

======================================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                                             Venue                         Year   Ref                           Materials
======================================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
A survey of outlier detection methodologies                                                                             ARTIF INTELL REV              2004   [#Hodge2004A]_                `[PDF] <https://www-users.cs.york.ac.uk/vicky/myPapers/Hodge+Austin_OutlierDetection_AIRE381.pdf>`_
Anomaly detection: A survey                                                                                             CSUR                          2009   [#Chandola2009Anomaly]_       `[PDF] <https://www.vs.inf.ethz.ch/edu/HS2011/CPS/papers/chandola09_anomaly-detection-survey.pdf>`_
A meta-analysis of the anomaly detection problem                                                                        Preprint                      2015   [#Emmott2015A]_               `[PDF] <https://arxiv.org/pdf/1503.01158.pdf>`_
On the evaluation of unsupervised outlier detection: measures, datasets, and an empirical study                         DMKD                          2016   [#Campos2016On]_              `[HTML] <https://link.springer.com/article/10.1007/s10618-015-0444-8>`_, `[SLIDES] <https://imada.sdu.dk/~zimek/InvitedTalks/TUVienna-2016-05-18-outlier-evaluation.pdf>`_
A comparative evaluation of unsupervised anomaly detection algorithms for multivariate data                             PLOS ONE                      2016   [#Goldstein2016A]_            `[PDF] <http://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0152173&type=printable>`_
A comparative evaluation of outlier detection algorithms: Experiments and analyses                                      Pattern Recognition           2018   [#Domingues2018A]_            `[PDF] <https://www.researchgate.net/publication/320025854_A_comparative_evaluation_of_outlier_detection_algorithms_Experiments_and_analyses>`_
Research Issues in Outlier Detection                                                                                    Book Chapter                  2019   [#Suri2019Research]_          `[HTML] <https://link.springer.com/chapter/10.1007/978-3-030-05127-3_3>`_
Quantitative comparison of unsupervised anomaly detection algorithms for intrusion detection                            SAC                           2019   [#Falcao2019Quantitative]_    `[HTML] <https://dl.acm.org/citation.cfm?id=3297314>`_
Progress in Outlier Detection Techniques: A Survey                                                                      IEEE Access                   2019   [#Wang2019Progress]_          `[PDF] <https://ieeexplore.ieee.org/iel7/6287639/8600701/08786096.pdf>`_
Deep learning for anomaly detection: A survey                                                                           Preprint                      2019   [#Chalapathy2019Deep]_        `[PDF] <https://arxiv.org/pdf/1901.03407.pdf>`_
Anomalous Instance Detection in Deep Learning: A Survey                                                                 Tech Report                   2020   [#Bulusu2020Deep]_            `[PDF] <https://arxiv.org/pdf/2003.06979.pdf>`_
Anomaly detection in univariate time-series: A survey on the state-of-the-art                                           Preprint                      2020   [#Braei2020Anomaly]_          `[PDF] <https://arxiv.org/pdf/2004.00433.pdf>`_
Deep Learning for Anomaly Detection: A Review                                                                           CSUR                          2021   [#Pang2020Deep]_              `[PDF] <https://arxiv.org/pdf/2007.02500.pdf>`_
A Comprehensive Survey on Graph Anomaly Detection with Deep Learning                                                    TKDE                          2021   [#Ma2021A]_                   `[PDF] <https://arxiv.org/pdf/2106.07178.pdf>`_
Revisiting Time Series Outlier Detection: Definitions and Benchmarks                                                    NeurIPS                       2021   [#Lai2021Revisiting]_         `[PDF] <https://openreview.net/pdf?id=r8IvOsnHchr>`_, `[Code] <https://github.com/datamllab/tods/tree/benchmark>`_
A Unified Survey on Anomaly, Novelty, Open-Set, and Out-of-Distribution Detection: Solutions and Future Challenges      Preprint                      2021   [#Salehi2021A]_               `[PDF] <https://arxiv.org/pdf/2110.14051.pdf>`_
Self-Supervised Anomaly Detection: A Survey and Outlook                                                                 Preprint                      2022   [#Hojjati2022Self]_           `[PDF] <https://arxiv.org/pdf/2205.05173.pdf>`_
Weakly supervised anomaly detection: A survey                                                                           Preprint                      2023   [#Jiang2023weakly]_           `[PDF] <https://arxiv.org/abs/2302.04549>`_, `[PDF] <https://github.com/yzhao062/wsad>`_
======================================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================

4.2. Key Algorithms
^^^^^^^^^^^^^^^^^^^

All these algorithms are available in `Python Outlier Detection (PyOD) <https://github.com/yzhao062/pyod>`_.

====================  =================================================================================================  =================================  =====  ===========================  ==============================================================================================================================================================================================
Abbreviation          Paper Title                                                                                        Venue                              Year   Ref                          Materials
====================  =================================================================================================  =================================  =====  ===========================  ==============================================================================================================================================================================================
kNN                   Efficient algorithms for mining outliers from large data sets                                      ACM SIGMOD Record                  2000   [#Ramaswamy2000Efficient]_   `[PDF] <https://webdocs.cs.ualberta.ca/~zaiane/pub/check/ramaswamy.pdf>`_
KNN                   Fast outlier detection in high dimensional spaces                                                  PKDD                               2002   [#Angiulli2002Fast]_         `[PDF] <https://www.researchgate.net/profile/Clara_Pizzuti/publication/220699183_Fast_Outlier_Detection_in_High_Dimensional_Spaces/links/542ea6a60cf27e39fa9635c6.pdf>`_
LOF                   LOF: identifying density-based local outliers                                                      ACM SIGMOD Record                  2000   [#Breunig2000LOF]_           `[PDF] <http://www.dbs.ifi.lmu.de/Publikationen/Papers/LOF.pdf>`_
IForest               Isolation forest                                                                                   ICDM                               2008   [#Liu2008Isolation]_         `[PDF] <https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf>`_
OCSVM                 Estimating the support of a high-dimensional distribution                                          Neural Computation                 2001   [#Scholkopf2001Estimating]_  `[PDF] <http://users.cecs.anu.edu.au/~williams/papers/P132.pdf>`_
AutoEncoder Ensemble  Outlier detection with autoencoder ensembles                                                       SDM                                2017   [#Chen2017Outlier]_          `[PDF] <http://saketsathe.net/downloads/autoencode.pdf>`_
COPOD                 COPOD: Copula-Based Outlier Detection                                                              ICDM                               2020   [#Li2020COPOD]_              `[PDF] <http://www.andrew.cmu.edu/user/yuezhao2/papers/20-icdm-copod.pdf>`_
ECOD                  Unsupervised Outlier Detection Using Empirical Cumulative Distribution Functions                   TKDE                               2022   [#Li2021ECOD]_               `[PDF] <https://www.andrew.cmu.edu/user/yuezhao2/papers/22-tkde-ecod.pdf>`_
====================  =================================================================================================  =================================  =====  ===========================  ==============================================================================================================================================================================================

4.3. Graph & Network Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================================================================================================  =============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                        Venue                          Year   Ref                           Materials
=================================================================================================  =============================  =====  ============================  ==========================================================================================================================================================================
Graph based anomaly detection and description: a survey                                            DMKD                           2015   [#Akoglu2015Graph]_           `[PDF] <https://arxiv.org/pdf/1404.4679.pdf>`_
Anomaly detection in dynamic networks: a survey                                                    WIREs Computational Statistic  2015   [#Ranshous2015Anomaly]_       `[PDF] <https://onlinelibrary.wiley.com/doi/pdf/10.1002/wics.1347>`_
Outlier detection in graphs: On the impact of multiple graph models                                ComSIS                         2019   [#Campos2019Outlier]_         `[PDF] <http://www.comsis.org/pdf.php?id=wims-8671>`_
A Comprehensive Survey on Graph Anomaly Detection with Deep Learning                               TKDE                           2021   [#Ma2021A]_                   `[PDF] <https://arxiv.org/pdf/2106.07178.pdf>`_
=================================================================================================  =============================  =====  ============================  ==========================================================================================================================================================================


4.4. Time Series Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=====================================================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                                                            Venue                         Year   Ref                           Materials
=====================================================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Outlier detection for temporal data: A survey                                                                                          TKDE                          2014   [#Gupta2014Outlier]_          `[PDF] <https://www.microsoft.com/en-us/research/wp-content/uploads/2014/01/gupta14_tkde.pdf>`_
Detecting spacecraft anomalies using lstms and nonparametric dynamic thresholding                                                      KDD                           2018   [#Hundman2018Detecting]_      `[PDF] <https://arxiv.org/pdf/1802.04431.pdf>`_, `[Code] <https://github.com/khundman/telemanom>`_
Time-Series Anomaly Detection Service at Microsoft                                                                                     KDD                           2019   [#Ren2019Time]_               `[PDF] <https://arxiv.org/pdf/1906.03821.pdf>`_
Revisiting Time Series Outlier Detection: Definitions and Benchmarks                                                                   NeurIPS                       2021   [#Lai2021Revisiting]_         `[PDF] <https://openreview.net/pdf?id=r8IvOsnHchr>`_, `[Code] <https://github.com/datamllab/tods/tree/benchmark>`_
Graph-Augmented Normalizing Flows for Anomaly Detection of Multiple Time Series                                                        ICLR                          2022   [#Dai2022Graph]_              `[PDF] <https://openreview.net/pdf?id=45L_dgP48Vd>`_, `[Code] <https://github.com/EnyanDai/GANF>`_
Drift doesn't matter: dynamic decomposition with diffusion reconstruction for unstable multivariate time series anomaly detection      NeurIPS                       2023   [#Wang2023Drift]_             `[PDF] <https://openreview.net/pdf?id=aW5bSuduF1>`_, `[Code] <https://github.com/ForestsKing/D3R>`_
=====================================================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.5. Feature Selection in Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

================================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                                       Venue                         Year   Ref                           Materials
================================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Unsupervised feature selection for outlier detection by modelling hierarchical value-feature couplings            ICDM                          2016   [#Pang2016Unsupervised]_      `[PDF] <https://opus.lib.uts.edu.au/bitstream/10453/107356/4/DSFS_ICDM2016.pdf>`_
Learning homophily couplings from non-iid data for joint feature selection and noise-resilient outlier detection  IJCAI                         2017   [#Pang2017Learning]_          `[PDF] <https://www.ijcai.org/proceedings/2017/0360.pdf>`_
================================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.6. High-dimensional & Subspace Outliers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================================================================================================  ============================  =====  ============================  =======================================================================================================================================================================================================
Paper Title                                                                                         Venue                         Year   Ref                           Materials
==================================================================================================  ============================  =====  ============================  =======================================================================================================================================================================================================
A survey on unsupervised outlier detection in high-dimensional numerical data                       Stat Anal Data Min            2012   [#Zimek2012A]_                `[HTML] <https://onlinelibrary.wiley.com/doi/abs/10.1002/sam.11161>`_
Learning Representations of Ultrahigh-dimensional Data for Random Distance-based Outlier Detection  SIGKDD                        2018   [#Pang2018Learning]_          `[PDF] <https://arxiv.org/pdf/1806.04808.pdf>`_
Reverse Nearest Neighbors in Unsupervised Distance-Based Outlier Detection                          TKDE                          2015   [#Radovanovic2015Reverse]_    `[PDF] <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.699.9559&rep=rep1&type=pdf>`_, `[SLIDES] <https://pdfs.semanticscholar.org/c8aa/832362422418287ff56793c780b425afa93f.pdf>`_
Outlier detection for high-dimensional data                                                         Biometrika                    2015   [#Ro2015Outlier]_             `[PDF] <http://web.hku.hk/~gyin/materials/2015RoZouWangYinBiometrika.pdf>`_
==================================================================================================  ============================  =====  ============================  =======================================================================================================================================================================================================


4.7. Outlier Ensembles
^^^^^^^^^^^^^^^^^^^^^^

=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                        Venue                         Year   Ref                           Materials
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Outlier ensembles: position paper                                                                  SIGKDD Explorations           2013   [#Aggarwal2013Outlier]_       `[PDF] <https://pdfs.semanticscholar.org/841e/ce7c3812bbf799c99c84c064bbcf77916ba9.pdf>`_
Ensembles for unsupervised outlier detection: challenges and research questions a position paper   SIGKDD Explorations           2014   [#Zimek2014Ensembles]_        `[PDF] <http://www.kdd.org/exploration_files/V15-01-02-Zimek.pdf>`_
An Unsupervised Boosting Strategy for Outlier Detection Ensembles                                  PAKDD                         2018   [#Campos2018An]_              `[HTML] <https://link.springer.com/chapter/10.1007/978-3-319-93034-3_45>`_
LSCP: Locally selective combination in parallel outlier ensembles                                  SDM                           2019   [#Zhao2019LSCP]_              `[PDF] <https://epubs.siam.org/doi/pdf/10.1137/1.9781611975673.66>`_
Adaptive Model Pooling for Online Deep Anomaly Detection from a Complex Evolving Data Stream       KDD                           2022   [#Yoon2022ARCUS]_             `[PDF] <https://dl.acm.org/doi/pdf/10.1145/3534678.3539348>`_, `[Github] <https://github.com/kaist-dmlab/ARCUS>`_, `[Slide] <https://drive.google.com/file/d/1JhrnEj1vScqGy69cfNUpfTjQYZh-vj_D/view>`_
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================

4.8. Outlier Detection in Evolving Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                         Venue                         Year   Ref                           Materials
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
A Survey on Anomaly detection in Evolving Data: [with Application to Forest Fire Risk Prediction]   SIGKDD Explorations           2018   [#Salehi2018A]_               `[PDF] <http://www.kdd.org/exploration_files/20-1-Article2.pdf>`_
Unsupervised real-time anomaly detection for streaming data                                         Neurocomputing                2017   [#Ahmad2017Unsupervised]_     `[PDF] <https://www.researchgate.net/publication/317325599_Unsupervised_real-time_anomaly_detection_for_streaming_data>`_
Outlier Detection in Feature-Evolving Data Streams                                                  SIGKDD                        2018   [#Manzoor2018Outlier]_        `[PDF] <https://www.andrew.cmu.edu/user/lakoglu/pubs/18-kdd-xstream.pdf>`_, `[Github] <https://cmuxstream.github.io/>`_
Evaluating Real-Time Anomaly Detection Algorithms--The Numenta Anomaly Benchmark                    ICMLA                         2015   [#Lavin2015Evaluating]_       `[PDF] <https://arxiv.org/pdf/1510.03336.pdf>`_, `[Github] <https://github.com/numenta/NAB>`_
MIDAS: Microcluster-Based Detector of Anomalies in Edge Streams                                     AAAI                          2020   [#Bhatia2020MIDAS]_           `[PDF] <https://www.comp.nus.edu.sg/~sbhatia/assets/pdf/midas.pdf>`_, `[Github] <https://github.com/bhatiasiddharth/MIDAS>`_
NETS: Extremely Fast Outlier Detection from a Data Stream via Set-Based Processing                  VLDB                          2019   [#Yoon2019NETS]_              `[PDF] <http://www.vldb.org/pvldb/vol12/p1303-yoon.pdf>`_, `[Github] <https://github.com/kaist-dmlab/NETS>`_, `[Slide] <https://drive.google.com/file/d/1wqKJZhEE4nTWe0zODu21ejgPDsDA_xaF/view?usp=sharing>`_
Ultrafast Local Outlier Detection from a Data Stream with Stationary Region Skipping                KDD                           2020   [#Yoon2020STARE]_             `[PDF] <https://dl.acm.org/doi/pdf/10.1145/3394486.3403171>`_, `[Github] <https://github.com/kaist-dmlab/STARE>`_, `[Slide] <https://drive.google.com/file/d/11y7Gs703SKJBkPZ4nKKgua__dHXXMbkV/view?usp=sharing>`_
Multiple Dynamic Outlier-Detection from a Data Stream by Exploiting Duality of Data and Queries     SIGMOD                        2021   [#Yoon2021MDUAL]_             `[PDF] <https://dl.acm.org/doi/pdf/10.1145/3448016.3452810>`_, `[Github] <https://github.com/kaist-dmlab/MDUAL>`_, `[Slide] <https://drive.google.com/file/d/1wmkkKCAcF9Dk8Wg49WnJF4U--lbtWy9J/view>`_
Adaptive Model Pooling for Online Deep Anomaly Detection from a Complex Evolving Data Stream        KDD                           2022   [#Yoon2022ARCUS]_             `[PDF] <https://dl.acm.org/doi/pdf/10.1145/3534678.3539348>`_, `[Github] <https://github.com/kaist-dmlab/ARCUS>`_, `[Slide] <https://drive.google.com/file/d/1JhrnEj1vScqGy69cfNUpfTjQYZh-vj_D/view>`_
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.9. Representation Learning in Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                         Venue                         Year   Ref                           Materials
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Learning Representations of Ultrahigh-dimensional Data for Random Distance-based Outlier Detection  SIGKDD                        2018   [#Pang2018Learning]_          `[PDF] <https://arxiv.org/pdf/1806.04808.pdf>`_
Learning representations for outlier detection on a budget                                          Preprint                      2015   [#Micenkova2015Learning]_     `[PDF] <https://arxiv.org/pdf/1507.08104.pdf>`_
XGBOD: improving supervised outlier detection with unsupervised representation learning             IJCNN                         2018   [#Zhao2018Xgbod]_             `[PDF] <http://www.andrew.cmu.edu/user/yuezhao2/papers/18-ijcnn-xgbod.pdf>`_
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.10. Interpretability
^^^^^^^^^^^^^^^^^^^^^^

=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                        Venue                         Year   Ref                           Materials
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Explaining Anomalies in Groups with Characterizing Subspace Rules                                  DMKD                          2018   [#Macha2018Explaining]_       `[PDF] <https://www.andrew.cmu.edu/user/lakoglu/pubs/18-pkdd-journal-xpacs.pdf>`_
Beyond Outlier Detection: LookOut for Pictorial Explanation                                        ECML-PKDD                     2018   [#Gupta2018Beyond]_           `[PDF] <https://www.andrew.cmu.edu/user/lakoglu/pubs/18-pkdd-lookout.pdf>`_
Contextual outlier interpretation                                                                  IJCAI                         2018   [#Liu2018Contextual]_         `[PDF] <https://arxiv.org/pdf/1711.10589.pdf>`_
Mining multidimensional contextual outliers from categorical relational data                       IDA                           2015   [#Tang2015Mining]_            `[PDF] <http://www.cs.sfu.ca/~jpei/publications/Contextual%20outliers.pdf>`_
Discriminative features for identifying and interpreting outliers                                  ICDE                          2014   [#Dang2014Discriminative]_    `[PDF] <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.706.5744&rep=rep1&type=pdf>`_
Sequential Feature Explanations for Anomaly Detection                                              TKDD                          2019   [#Siddiqui2019Sequential]_    `[HTML] <https://dl.acm.org/citation.cfm?id=3230666>`_
A Survey on Explainable Anomaly Detection                                                          TKDD                          2023   [#Li2023XAD]_                 `[HTML] <https://dl.acm.org/doi/10.1145/3609333>`_
Explainable Contextual Anomaly Detection Using Quantile Regression Forests                         DMKD                          2023   [#Li2023QCAD]_                `[HTML] <https://link.springer.com/article/10.1007/s10618-023-00967-z>`_
Beyond Outlier Detection: Outlier Interpretation by Attention-Guided Triplet Deviation Network     WWW                           2021   [#Xu2021Beyond]_              `[PDF] <https://jiansonglei.github.io/files/21WWW.pdf>`_
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.11. Outlier Detection with Neural Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                         Venue                         Year   Ref                           Materials
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Detecting spacecraft anomalies using lstms and nonparametric dynamic thresholding                   KDD                           2018   [#Hundman2018Detecting]_      `[PDF] <https://arxiv.org/pdf/1802.04431.pdf>`_, `[Code] <https://github.com/khundman/telemanom>`_
MAD-GAN: Multivariate Anomaly Detection for Time Series Data with Generative Adversarial Networks   ICANN                         2019   [#Li2019MAD]_                 `[PDF] <https://arxiv.org/pdf/1901.04997.pdf>`_, `[Code] <https://github.com/LiDan456/MAD-GANs>`_
Generative Adversarial Active Learning for Unsupervised Outlier Detection                           TKDE                          2019   [#Liu2019Generative]_         `[PDF] <https://arxiv.org/pdf/1809.10816.pdf>`_, `[Code] <https://github.com/leibinghe/GAAL-based-outlier-detection>`_
Deep Autoencoding Gaussian Mixture Model for Unsupervised Anomaly Detection                         ICLR                          2018   [#Zong2018Deep]_              `[PDF] <http://www.cs.ucsb.edu/~bzong/doc/iclr18-dagmm.pdf>`_, `[Code] <https://github.com/danieltan07/dagmm>`_
Deep Anomaly Detection with Outlier Exposure                                                        ICLR                          2019   [#Hendrycks2019Deep]_         `[PDF] <https://arxiv.org/pdf/1812.04606.pdf>`_, `[Code] <https://github.com/hendrycks/outlier-exposure>`_
Unsupervised Anomaly Detection With LSTM Neural Networks                                            TNNLS                         2019   [#Ergen2019Unsupervised]_     `[PDF] <https://arxiv.org/pdf/1710.09207.pdf>`_, `[IEEE] <https://ieeexplore.ieee.org/document/8836638>`_,
Effective End-to-end Unsupervised Outlier Detection via Inlier Priority of Discriminative Network   NeurIPS                       2019   [#Wang2019Effective]_         `[PDF] <https://papers.nips.cc/paper/8830-effective-end-to-end-unsupervised-outlier-detection-via-inlier-priority-of-discriminative-network.pdf>`_ `[Code] <https://github.com/demonzyj56/E3Outlier>`_
Fascinating Supervisory Signals and Where to Find Them: Deep Anomaly Detection with Scale Learning  ICML                          2023   [#Xu2023Fascinating]_         `[PDF] <https://arxiv.org/abs/2305.16114>`_, `[Code] <https://github.com/xuhongzuo/scale-learning>`_ 
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.12. Active Anomaly Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                         Venue                         Year   Ref                           Materials
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Active learning for anomaly and rare-category detection                                             NeurIPS                       2005   [#Pelleg2005Active]_          `[PDF] <http://papers.nips.cc/paper/2554-active-learning-for-anomaly-and-rare-category-detection.pdf>`_
Outlier detection by active learning                                                                SIGKDD                        2006   [#Abe2006Outlier]_            `[PDF] <https://www.researchgate.net/profile/Naoki_Abe2/publication/221653343_Outlier_detection_by_active_learning/links/5441464a0cf2e6f0c0f60abb.pdf>`_
Active Anomaly Detection via Ensembles: Insights, Algorithms, and Interpretability                  Preprint                      2019   [#Das2019Active]_             `[PDF] <https://arxiv.org/pdf/1901.08930.pdf>`_
Meta-AAD: Active Anomaly Detection with Deep Reinforcement Learning                                 ICDM                          2020   [#Zha2020Meta]_               `[PDF] <https://arxiv.org/pdf/2009.07415.pdf>`_
A3: Activation Anomaly Analysis                                                                     ECML-PKDD                     2020   [#Sperl2021A3]_               `[PDF] <https://arxiv.org/pdf/2003.01801>`_, `[Code] <https://github.com/Fraunhofer-AISEC/A3>`_
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.13. Interactive Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                        Venue                         Year   Ref                           Materials
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Learning On-the-Job to Re-rank Anomalies from Top-1 Feedback                                       SDM                           2019   [#Lamba2019Learning]_         `[PDF] <https://epubs.siam.org/doi/pdf/10.1137/1.9781611975673.69>`_
Interactive anomaly detection on attributed networks                                               WSDM                          2019   [#Ding2019Interactive]_       `[PDF] <http://www.public.asu.edu/~jundongl/paper/WSDM19_GraphUCB.pdf>`_
eX2: a framework for interactive anomaly detection                                                 IUI Workshop                  2019   [#Arnaldo2019ex2]_            `[PDF] <http://ceur-ws.org/Vol-2327/IUI19WS-ESIDA-2.pdf>`_
Tripartite Active Learning for Interactive Anomaly Discovery                                       IEEE Access                   2019   [#Zhu2019Tripartite]_         `[PDF] <https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8707963>`_
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.14. Outlier Detection in Other fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

============== =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Field          Paper Title                                                                                        Venue                         Year   Ref                           Materials
============== =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
**Text**       Outlier detection for text data                                                                    SDM                           2017   [#Kannan2017Outlier]_         `[PDF] <https://epubs.siam.org/doi/pdf/10.1137/1.9781611974973.55>`_
============== =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.15. Outlier Detection Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========================    =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Field                       Paper Title                                                                                        Venue                         Year   Ref                           Materials
========================    =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
**Security**                A survey of distance and similarity measures used within network intrusion anomaly detection       IEEE Commun. Surv. Tutor.     2015   [#WellerFahy2015A]_           `[PDF] <https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6853338>`_
**Security**                Anomaly-based network intrusion detection: Techniques, systems and challenges                      Computers & Security          2009   [#GarciaTeodoro2009Anomaly]_  `[PDF] <http://dtstc.ugr.es/~jedv/descargas/2009_CoSe09-Anomaly-based-network-intrusion-detection-Techniques,-systems-and-challenges.pdf>`_
**Finance**                 A survey of anomaly detection techniques in financial domain                                       Future Gener Comput Syst      2016   [#Ahmed2016A]_                `[PDF] <http://isiarticles.com/bundles/Article/pre/pdf/76882.pdf>`_
**Traffic**                 Outlier Detection in Urban Traffic Data                                                            WIMS                          2018   [#Djenouri2018Outlier]_       `[PDF] <http://dss.sdu.dk/assets/fpd-lof/outlier-detection-urban.pdf>`_
**Social Media**            A survey on social media anomaly detection                                                         SIGKDD Explorations           2016   [#Yu2016A]_                   `[PDF] <https://arxiv.org/pdf/1601.01102.pdf>`_
**Social Media**            GLAD: group anomaly detection in social media analysis                                             TKDD                          2015   [#Yu2015Glad]_                `[PDF] <https://arxiv.org/pdf/1410.1940.pdf>`_
**Machine Failure**         Detecting the Onset of Machine Failure Using Anomaly Detection Methods                             DAWAK                         2019   [#Riazi2019Detecting]_        `[PDF] <https://webdocs.cs.ualberta.ca/~zaiane/postscript/DAWAK19.pdf>`_
**Video Surveillance**      AnomalyNet: An anomaly detection network for video surveillance                                    TIFS                          2019   [#Zhou2019AnomalyNet]_        `[IEEE] <https://ieeexplore.ieee.org/document/8649753>`_, `Code <https://github.com/joeyzhouty/AnomalyNet>`_
========================    =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.16. Automated Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                        Venue                         Year   Ref                           Materials
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
AutoML: state of the art with a focus on anomaly detection, challenges, and research directions    Int J Data Sci Anal           2022   [#Bahri2022automl]_           `[PDF] <https://www.researchgate.net/publication/358364044_AutoML_state_of_the_art_with_a_focus_on_anomaly_detection_challenges_and_research_directions>`_
AutoOD: Automated Outlier Detection via Curiosity-guided Search and Self-imitation Learning        ICDE                          2020   [#Li2020AutoOD]_              `[PDF] <https://arxiv.org/pdf/2006.11321.pdf>`_
Automatic Unsupervised Outlier Model Selection                                                     NeurIPS                       2021   [#Zhao2020Automating]_        `[PDF] <https://www.andrew.cmu.edu/user/yuezhao2/papers/21-neurips-metaod.pdf>`_, `[Code] <https://github.com/yzhao062/MetaOD>`_
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.17. Machine Learning Systems for Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section summarizes a list of systems for outlier detection, which may
overlap with the section of tools and libraries.

=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                        Venue                         Year   Ref                           Materials
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
PyOD: A Python Toolbox for Scalable Outlier Detection                                              JMLR                          2019   [#Zhao2019PYOD]_              `[PDF] <https://www.jmlr.org/papers/volume20/19-011/19-011.pdf>`_, `[Code] <https://github.com/yzhao062/pyod>`_
SUOD: Accelerating Large-Scale Unsupervised Heterogeneous Outlier Detection                        MLSys                         2021   [#Zhao2021SUOD]_              `[PDF] <https://arxiv.org/pdf/2003.05731.pdf>`_, `[Code] <https://github.com/yzhao062/suod>`_
TOD: Tensor-based Outlier Detection                                                                Preprint                      2021   [#Zhao2021TOD]_               `[PDF] <https://arxiv.org/pdf/2110.14007.pdf>`_, `[Code] <https://github.com/yzhao062/pytod>`_
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================



4.18. Fairness and Bias in Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                        Venue                         Year   Ref                           Materials
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
A Framework for Determining the Fairness of Outlier Detection                                      ECAI                          2020   [#Davidson2020A]_             `[PDF] <https://web.cs.ucdavis.edu/~davidson/Publications/TR.pdf>`_
FAIROD: Fairness-aware Outlier Detection                                                           AIES                          2021   [#Shekhar2021FAIROD]_         `[PDF] <https://arxiv.org/pdf/2012.03063.pdf>`_
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================



4.19. Isolation-Based Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================================================================================================  ============================  =====  =============================  ==============================================================================================================================================================================================
Paper Title                                                                                        Venue                         Year   Ref                            Materials
=================================================================================================  ============================  =====  =============================  ==============================================================================================================================================================================================
Isolation forest                                                                                   ICDM                          2008   [#Liu2008Isolation]_           `[PDF] <https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf>`_
Isolation‐based anomaly detection using nearest‐neighbor ensembles                                  Computational Intelligence    2018   [#Bandaragoda2018Isolation]_   `[PDF] <https://www.researchgate.net/publication/322359651_Isolation-based_anomaly_detection_using_nearest-neighbor_ensembles_iNNE>`_, `[Code] <https://github.com/zhuye88/iNNE>`_
Extended Isolation Forest                                                                          TKDE                          2019   [#Hariri2019Extended]_         `[PDF] <https://arxiv.org/pdf/1811.02141.pdf>`_, `[Code] <https://github.com/sahandha/eif>`_
Isolation Distributional Kernel: A New Tool for Kernel based Anomaly Detection                     KDD                           2020   [#Ting2020Isolation]_          `[PDF] <https://arxiv.org/pdf/2009.12196.pdf>`_, `[Code] <https://github.com/IsolationKernel/Codes/tree/main/IDK>`_
Deep Isolation Forest for Anomaly Detection                                                        TKDE                          2023   [#Xu2023Deep]_                 `[PDF] <https://arxiv.org/abs/2206.06602>`_, `[Code] <https://github.com/xuhongzuo/deep-iforest>`_
=================================================================================================  ============================  =====  =============================  ==============================================================================================================================================================================================



4.20. Emerging and Interesting Topics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                        Venue                         Year   Ref                           Materials
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Clustering with Outlier Removal                                                                    TKDE                          2019   [#Liu2018Clustering]_         `[PDF] <https://arxiv.org/pdf/1801.01899.pdf>`_
Real-World Anomaly Detection by using Digital Twin Systems and Weakly-Supervised Learning          IEEE Trans. Ind. Informat.    2020   [#Castellani2020Siamese]_     `[PDF] <https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9179030>`_
SSD: A Unified Framework for Self-Supervised Outlier Detection                                     ICLR                          2021   [#Sehwag2021SSD]_             `[PDF] <https://openreview.net/pdf?id=v5gjXpmR8J>`_, `[Code] <https://github.com/inspire-group/SSD>`_
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


----

5. Key Conferences/Workshops/Journals
-------------------------------------

5.1. Conferences & Workshops
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Key data mining conference **deadlines**, **historical acceptance rates**, and more
can be found `data-mining-conferences <https://github.com/yzhao062/data-mining-conferences>`_.


`ACM International Conference on Knowledge Discovery and Data Mining (SIGKDD) <http://www.kdd.org/conferences>`_. **Note**: SIGKDD usually has an Outlier Detection Workshop (ODD), see `ODD 2021 <https://oddworkshop.github.io/>`_.

`ACM International Conference on Management of Data (SIGMOD) <https://sigmod.org/>`_

`The Web Conference (WWW) <https://www2018.thewebconf.org/>`_

`IEEE International Conference on Data Mining (ICDM) <http://icdm2018.org/>`_

`SIAM International Conference on Data Mining (SDM) <https://www.siam.org/Conferences/CM/Main/sdm19>`_

`IEEE International Conference on Data Engineering (ICDE) <https://icde2018.org/>`_

`ACM InternationalConference on Information and Knowledge Management (CIKM) <http://www.cikmconference.org/>`_

`ACM International Conference on Web Search and Data Mining (WSDM) <http://www.wsdm-conference.org/2018/>`_

`The European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML-PKDD) <http://www.ecmlpkdd2018.org/>`_

`The Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD) <http://pakdd2019.medmeeting.org>`_

5.2. Journals
^^^^^^^^^^^^^

`ACM Transactions on Knowledge Discovery from Data (TKDD) <https://tkdd.acm.org/>`_

`IEEE Transactions on Knowledge and Data Engineering (TKDE) <https://www.computer.org/web/tkde>`_

`ACM SIGKDD Explorations Newsletter <http://www.kdd.org/explorations>`_

`Data Mining and Knowledge Discovery <https://link.springer.com/journal/10618>`_

`Knowledge and Information Systems (KAIS) <https://link.springer.com/journal/10115>`_

----

References
----------

.. [#Abe2006Outlier] Abe, N., Zadrozny, B. and Langford, J., 2006, August. Outlier detection by active learning. In *Proceedings of the 12th ACM SIGKDD international conference on Knowledge discovery and data mining*, pp. 504-509, ACM.

.. [#Aggarwal2013Outlier] Aggarwal, C.C., 2013. Outlier ensembles: position paper. *ACM SIGKDD Explorations Newsletter*\ , 14(2), pp.49-58.

.. [#Ahmed2016A] Ahmed, M., Mahmood, A.N. and Islam, M.R., 2016. A survey of anomaly detection techniques in financial domain. *Future Generation Computer Systems*\ , 55, pp.278-288.

.. [#Ahmad2017Unsupervised] Ahmad, S., Lavin, A., Purdy, S. and Agha, Z., 2017. Unsupervised real-time anomaly detection for streaming data. *Neurocomputing*, 262, pp.134-147.

.. [#Akoglu2015Graph] Akoglu, L., Tong, H. and Koutra, D., 2015. Graph based anomaly detection and description: a survey. *Data Mining and Knowledge Discovery*\ , 29(3), pp.626-688.

.. [#Angiulli2002Fast] Angiulli, F. and Pizzuti, C., 2002, August. Fast outlier detection in high dimensional spaces. In *European Conference on Principles of Data Mining and Knowledge Discovery*, pp. 15-27.

.. [#Arnaldo2019ex2] Arnaldo, I., Veeramachaneni, K. and Lam, M., 2019. ex2: a framework for interactive anomaly detection. In *ACM IUI Workshop on Exploratory Search and Interactive Data Analytics (ESIDA)*.

.. [#Bahri2022automl] Bahri, M., Salutari, F., Putina, A. et al. AutoML: state of the art with a focus on anomaly detection, challenges, and research directions. *International Journal of Data Science and Analytics*  (2022).

.. [#Bandaragoda2018Isolation] Bandaragoda, Tharindu R., Kai Ming Ting, David Albrecht, Fei Tony Liu, Ye Zhu, and Jonathan R. Wells. "Isolation‐based anomaly detection using nearest‐neighbor ensembles." *Computational Intelligence* 34, no. 4 (2018): 968-998.

.. [#Bhatia2020MIDAS] Bhatia, S., Hooi, B., Yoon, M., Shin, K. and Faloutsos. C., 2020. MIDAS: Microcluster-Based Detector of Anomalies in Edge Streams. In *AAAI Conference on Artificial Intelligence (AAAI)*.

.. [#Braei2020Anomaly] Braei, M. and Wagner, S., 2020. Anomaly detection in univariate time-series: A survey on the state-of-the-art. arXiv preprint arXiv:2004.00433.

.. [#Breunig2000LOF] Breunig, M.M., Kriegel, H.P., Ng, R.T. and Sander, J., 2000, May. LOF: identifying density-based local outliers. *ACM SIGMOD Record*\ , 29(2), pp. 93-104.

.. [#Bulusu2020Deep] Bulusu, S., Kailkhura, B., Li, B., Varshney, P. and Song, D., 2020. Anomalous instance detection in deep learning: A survey (No. LLNL-CONF-808677). Lawrence Livermore National Lab.(LLNL), Livermore, CA (United States).

.. [#Campos2016On] Campos, G.O., Zimek, A., Sander, J., Campello, R.J., Micenková, B., Schubert, E., Assent, I. and Houle, M.E., 2016. On the evaluation of unsupervised outlier detection: measures, datasets, and an empirical study. *Data Mining and Knowledge Discovery*\ , 30(4), pp.891-927.

.. [#Campos2018An] Campos, G.O., Zimek, A. and Meira, W., 2018, June. An Unsupervised Boosting Strategy for Outlier Detection Ensembles. In *Pacific-Asia Conference on Knowledge Discovery and Data Mining (pp. 564-576)*. Springer, Cham.

.. [#Campos2019Outlier] Campos, G.O., Moreira, E., Meira Jr, W. and Zimek, A., 2019. Outlier Detection in Graphs: A Study on the Impact of Multiple Graph Models. *Computer Science & Information Systems*, 16(2).

.. [#Castellani2020Siamese] Castellani, A., Schmitt, S., Squartini, S., 2020. Real-World Anomaly Detection by using Digital Twin Systems and Weakly-Supervised Learning. In *IEEE Transactions on Industrial Informatics*.

.. [#Chalapathy2019Deep] Chalapathy, R. and Chawla, S., 2019. Deep learning for anomaly detection: A survey. arXiv preprint arXiv:1901.03407.

.. [#Chandola2009Anomaly] Chandola, V., Banerjee, A. and Kumar, V., 2009. Anomaly detection: A survey. *ACM computing surveys* , 41(3), p.15.

.. [#Chawla2011Anomaly] Chawla, S. and Chandola, V., 2011, Anomaly Detection: A Tutorial. *Tutorial at ICDM 2011*.

.. [#Chen2017Outlier] Chen, J., Sathe, S., Aggarwal, C. and Turaga, D., 2017, June. Outlier detection with autoencoder ensembles. *SIAM International Conference on Data Mining*, pp. 90-98. Society for Industrial and Applied Mathematics.

.. [#Dai2022Graph] Dai, E. and Chen, J., 2022. Graph-Augmented Normalizing Flows for Anomaly Detection of Multiple Time Series. International Conference on Learning Representations (ICLR).

.. [#Dang2014Discriminative] Dang, X.H., Assent, I., Ng, R.T., Zimek, A. and Schubert, E., 2014, March. Discriminative features for identifying and interpreting outliers. In *International Conference on Data Engineering (ICDE)*. IEEE.

.. [#Das2019Active] Das, S., Islam, M.R., Jayakodi, N.K. and Doppa, J.R., 2019. Active Anomaly Detection via Ensembles: Insights, Algorithms, and Interpretability. arXiv preprint arXiv:1901.08930.

.. [#Davidson2020A] Davidson, I. and Ravi, S.S., 2020. A framework for determining the fairness of outlier detection. In Proceedings of the 24th European Conference on Artificial Intelligence (ECAI2020) (Vol. 2029).

.. [#Ding2019Interactive] Ding, K., Li, J. and Liu, H., 2019, January. Interactive anomaly detection on attributed networks. In *Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining*, pp. 357-365. ACM.

.. [#Djenouri2018Outlier] Djenouri, Y. and Zimek, A., 2018, June. Outlier detection in urban traffic data. In *Proceedings of the 8th International Conference on Web Intelligence, Mining and Semantics*. ACM.

.. [#Domingues2018A] Domingues, R., Filippone, M., Michiardi, P. and Zouaoui, J., 2018. A comparative evaluation of outlier detection algorithms: Experiments and analyses. *Pattern Recognition*, 74, pp.406-421.

.. [#Emmott2015A] Emmott, A., Das, S., Dietterich, T., Fern, A. and Wong, W.K., 2015. A meta-analysis of the anomaly detection problem. arXiv preprint arXiv:1503.01158.

.. [#Ergen2019Unsupervised] Ergen, T. and Kozat, S.S., 2019. Unsupervised Anomaly Detection With LSTM Neural Networks. *IEEE transactions on neural networks and learning systems*.

.. [#Falcao2019Quantitative] Falcão, F., Zoppi, T., Silva, C.B.V., Santos, A., Fonseca, B., Ceccarelli, A. and Bondavalli, A., 2019, April. Quantitative comparison of unsupervised anomaly detection algorithms for intrusion detection. In *Proceedings of the 34th ACM/SIGAPP Symposium on Applied Computing*, (pp. 318-327). ACM.

.. [#GarciaTeodoro2009Anomaly] Garcia-Teodoro, P., Diaz-Verdejo, J., Maciá-Fernández, G. and Vázquez, E., 2009. Anomaly-based network intrusion detection: Techniques, systems and challenges. *Computers & Security*\ , 28(1-2), pp.18-28.

.. [#Goldstein2016A] Goldstein, M. and Uchida, S., 2016. A comparative evaluation of unsupervised anomaly detection algorithms for multivariate data. *PloS one*\ , 11(4), p.e0152173.

.. [#Gupta2014Outlier] Gupta, M., Gao, J., Aggarwal, C.C. and Han, J., 2014. Outlier detection for temporal data: A survey. *IEEE Transactions on Knowledge and Data Engineering*\ , 26(9), pp.2250-2267.

.. [#Hariri2019Extended] Hariri, S., Kind, M.C. and Brunner, R.J., 2019. Extended Isolation Forest. *IEEE Transactions on Knowledge and Data Engineering*.

.. [#Hendrycks2019Deep] Hendrycks, D., Mazeika, M. and Dietterich, T.G., 2019. Deep Anomaly Detection with Outlier Exposure. International Conference on Learning Representations (ICLR).

.. [#Hodge2004A] Hodge, V. and Austin, J., 2004. A survey of outlier detection methodologies. *Artificial intelligence review*\ , 22(2), pp.85-126.

.. [#Hojjati2022Self] Hojjati, H., Ho, T.K.K. and Armanfard, N., 2022. Self-Supervised Anomaly Detection: A Survey and Outlook. arXiv preprint arXiv:2205.05173.

.. [#Hundman2018Detecting] Hundman, K., Constantinou, V., Laporte, C., Colwell, I. and Soderstrom, T., 2018, July. Detecting spacecraft anomalies using lstms and nonparametric dynamic thresholding. In *Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, (pp. 387-395). ACM.

.. [#Kannan2017Outlier] Kannan, R., Woo, H., Aggarwal, C.C. and Park, H., 2017, June. Outlier detection for text data. In *Proceedings of the 2017 SIAM International Conference on Data Mining*, pp. 489-497. Society for Industrial and Applied Mathematics. 

.. [#Kriegel2010Outlier] Kriegel, H.P., Kröger, P. and Zimek, A., 2010. Outlier detection techniques. *Tutorial at ACM SIGKDD 2010*.

.. [#Jiang2023adgym] Jiang, M., Hou, C., Zheng, A., Han, S., Huang, H., Wen, Q., Hu, X. and Zhao, Y., 2023. ADGym: Design Choices for Deep Anomaly Detection. *NeurIPS*, Datasets and Benchmarks Track.

.. [#Jiang2023weakly] Jiang, M., Hou, C., Zheng, A., Hu, X., Han, S., Huang, H., He, X., Yu, P.S. and Zhao, Y., 2023. Weakly supervised anomaly detection: A survey. arXiv preprint arXiv:2302.04549.

.. [#Lai2021Revisiting] Lai, K.H., Zha, D., Xu, J., Zhao, Y., Wang, G. and Hu, X., 2021. Revisiting Time Series Outlier Detection: Definitions and Benchmarks. *NeurIPS*, Datasets and Benchmarks Track.

.. [#Lamba2019Learning] Lamba, H. and Akoglu, L., 2019, May. Learning On-the-Job to Re-rank Anomalies from Top-1 Feedback. In *Proceedings of the 2019 SIAM International Conference on Data Mining (SDM)*, pp. 612-620. Society for Industrial and Applied Mathematics.

.. [#Lavin2015Evaluating] Lavin, A. and Ahmad, S., 2015, December. Evaluating Real-Time Anomaly Detection Algorithms--The Numenta Anomaly Benchmark. In *2015 IEEE 14th International Conference on Machine Learning and Applications (ICMLA)* (pp. 38-44). IEEE.

.. [#Lazarevic2008Data] Lazarevic, A., Banerjee, A., Chandola, V., Kumar, V. and Srivastava, J., 2008, September. Data mining for anomaly detection. *Tutorial at ECML PKDD 2008*.

.. [#Li2019MAD] Li, D., Chen, D., Jin, B., Shi, L., Goh, J. and Ng, S.K., 2019, September. MAD-GAN: Multivariate anomaly detection for time series data with generative adversarial networks. In *International Conference on Artificial Neural Networks* (pp. 703-716). Springer, Cham.

.. [#Li2020COPOD] Li, Z., Zhao, Y., Botta, N., Ionescu, C. and Hu, X. COPOD: Copula-Based Outlier Detection. *IEEE International Conference on Data Mining (ICDM)*, 2020.

.. [#Li2021ECOD] Li, Z., Zhao, Y., Hu, X., Botta, N., Ionescu, C. and Chen, H. G. ECOD: Unsupervised Outlier Detection Using Empirical Cumulative Distribution Functions. *IEEE Transactions on Knowledge and Data Engineering (TKDE)*, 2022.

.. [#Li2023XAD] Li, Z., Zhu, Y. and Van Leeuwen, M., 2023. A survey on explainable anomaly detection. *ACM Transactions on Knowledge Discovery from Data*, 18(1), pp.1-54.

.. [#Li2023QCAD] Li, Z. and Van Leeuwen, M., 2023. Explainable contextual anomaly detection using quantile regression forests. *Data Mining and Knowledge Discovery*, 37(6), pp.2517-2563.

.. [#Liu2008Isolation] Liu, F.T., Ting, K.M. and Zhou, Z.H., 2008, December. Isolation forest. In *International Conference on Data Mining*\ , pp. 413-422. IEEE.

.. [#Liu2018Clustering] Liu, H., Li, J., Wu, Y. and Fu, Y., 2019. Clustering with outlier removal. *IEEE transactions on knowledge and data engineering*.

.. [#Liu2018Contextual] Liu, N., Shin, D. and Hu, X., 2017. Contextual outlier interpretation. In *International Joint Conference on Artificial Intelligence (IJCAI-18)*, pp.2461-2467.

.. [#Liu2019Generative] Liu, Y., Li, Z., Zhou, C., Jiang, Y., Sun, J., Wang, M. and He, X., 2019. Generative Adversarial Active Learning for Unsupervised Outlier Detection. *IEEE transactions on knowledge and data engineering*.

.. [#Li2020AutoOD] Li, Y., Chen, Z., Zha, D., Zhou, K., Jin, H., Chen, H. and Hu, X., 2020. AutoOD: Automated Outlier Detection via Curiosity-guided Search and Self-imitation Learning. *ICDE*.

.. [#Liu2022Benchmarking] Liu, K., Dou, Y., Zhao, Y., Ding, X., Hu, X., Zhang, R., Ding, K., Chen, C., Peng, H., Shu, K., Sun, L., Li, J., Chen, G.H., Jia, Z., and Yu, P.S. 2022. Benchmarking Node Outlier Detection on Graphs. arXiv preprint arXiv:2206.10071.

.. [#Ma2021A] Ma, X., Wu, J., Xue, S., Yang, J., Zhou, C., Sheng, Q.Z., Xiong, H. and Akoglu, L., 2021. A comprehensive survey on graph anomaly detection with deep learning. *IEEE Transactions on Knowledge and Data Engineering*.

.. [#Macha2018Explaining] Macha, M. and Akoglu, L., 2018. Explaining anomalies in groups with characterizing subspace rules. Data Mining and Knowledge Discovery, 32(5), pp.1444-1480.

.. [#Manzoor2018Outlier] Manzoor, E., Lamba, H. and Akoglu, L. Outlier Detection in Feature-Evolving Data Streams. In *24th ACM SIGKDD International Conference on Knowledge Discovery and Data mining (KDD)*. 2018.

.. [#Mendiratta2017Anomaly] Mendiratta, B.V., 2017. Anomaly Detection in Networks. *Tutorial at ACM SIGKDD 2017*.

.. [#Micenkova2015Learning] Micenková, B., McWilliams, B. and Assent, I., 2015. Learning representations for outlier detection on a budget. arXiv preprint arXiv:1507.08104.

.. [#Gupta2018Beyond] Gupta, N., Eswaran, D., Shah, N., Akoglu, L. and Faloutsos, C., Beyond Outlier Detection: LookOut for Pictorial Explanation. *ECML PKDD 2018*.

.. [#Han2022Adbench] Han, S., Hu, X., Huang, H., Jiang, M. and Zhao, Y., 2022. ADBench: Anomaly Detection Benchmark. arXiv preprint arXiv:2206.09426.

.. [#Pang2016Unsupervised] Pang, G., Cao, L., Chen, L. and Liu, H., 2016, December. Unsupervised feature selection for outlier detection by modelling hierarchical value-feature couplings. In Data Mining (ICDM), 2016 IEEE 16th International Conference on (pp. 410-419). IEEE.

.. [#Pang2017Learning] Pang, G., Cao, L., Chen, L. and Liu, H., 2017, August. Learning homophily couplings from non-iid data for joint feature selection and noise-resilient outlier detection. In Proceedings of the 26th International Joint Conference on Artificial Intelligence (pp. 2585-2591). AAAI Press.

.. [#Pang2018Learning] Pang, G., Cao, L., Chen, L. and Liu, H., 2018. Learning Representations of Ultrahigh-dimensional Data for Random Distance-based Outlier Detection. In *24th ACM SIGKDD International Conference on Knowledge Discovery and Data mining (KDD)*. 2018.

.. [#Pang2020Deep] Pang, G., Shen, C., Cao, L. and Hengel, A.V.D., 2021. Deep Learning for Anomaly Detection: A Review. ACM Computing Surveys (CSUR), 54(2), pp.1-38.

.. [#Pang2021Deep] Pang, G., Cao, L. and Aggarwal, C., 2021. Deep Learning for Anomaly Detection. *Tutorial at WSDM 2021*.

.. [#Pang2021Toward] Pang, G. and Aggarwal, C., 2021, August. Toward explainable deep anomaly detection. In *KDD* (pp. 4056-4057).

.. [#Pang2023recent] Guansong Pang, Joey Tianyi Zhou, Radu Tudor Ionescu, Yu Tian, and Kihyuk Sohn. "Recent Advances in Anomaly Detection". In: *CVPR'23*. Vancouver, Canada.

.. [#Pelleg2005Active] Pelleg, D. and Moore, A.W., 2005. Active learning for anomaly and rare-category detection. In *Advances in neural information processing systems*\, pp. 1073-1080.

.. [#Radovanovic2015Reverse] Radovanović, M., Nanopoulos, A. and Ivanović, M., 2015. Reverse nearest neighbors in unsupervised distance-based outlier detection. *IEEE transactions on knowledge and data engineering*, 27(5), pp.1369-1382.

.. [#Ramaswamy2000Efficient] Ramaswamy, S., Rastogi, R. and Shim, K., 2000, May. Efficient algorithms for mining outliers from large data sets. *ACM SIGMOD Record*\ , 29(2), pp. 427-438.

.. [#Ranshous2015Anomaly] Ranshous, S., Shen, S., Koutra, D., Harenberg, S., Faloutsos, C. and Samatova, N.F., 2015. Anomaly detection in dynamic networks: a survey. Wiley Interdisciplinary Reviews: Computational Statistics, 7(3), pp.223-247.

.. [#Ren2019Time] Ren, H., Xu, B., Wang, Y., Yi, C., Huang, C., Kou, X., Xing, T., Yang, M., Tong, J. and Zhang, Q., 2019. Time-Series Anomaly Detection Service at Microsoft. In *Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*. ACM.

.. [#Riazi2019Detecting] Riazi, M., Zaiane, O., Takeuchi, T., Maltais, A., Günther, J. and Lipsett, M., Detecting the Onset of Machine Failure Using Anomaly Detection Methods.

.. [#Ro2015Outlier] Ro, K., Zou, C., Wang, Z. and Yin, G., 2015. Outlier detection for high-dimensional data. *Biometrika*, 102(3), pp.589-599.

.. [#Salehi2018A] Salehi, Mahsa & Rashidi, Lida. (2018). A Survey on Anomaly detection in Evolving Data: [with Application to Forest Fire Risk Prediction]. *ACM SIGKDD Explorations Newsletter*. 20. 13-23.

.. [#Salehi2021A] Salehi, M., Mirzaei, H., Hendrycks, D., Li, Y., Rohban, M.H., Sabokrou, M., 2021. A Unified Survey on Anomaly, Novelty, Open-Set, and Out-of-Distribution Detection: Solutions and Future Challenges. arXiv preprint arXiv:2110.14051.

.. [#Scholkopf2001Estimating] Schölkopf, B., Platt, J.C., Shawe-Taylor, J., Smola, A.J. and Williamson, R.C., 2001. Estimating the support of a high-dimensional distribution. *Neural Computation*, 13(7), pp.1443-1471.

.. [#Sehwag2021SSD] Sehwag, V., Chiang, M., Mittal, P., 2021. SSD: A Unified Framework for Self-Supervised Outlier Detection. *International Conference on Learning Representations (ICLR)*.

.. [#Shekhar2021FAIROD] Shekhar, S., Shah, N. and Akoglu, L., 2021. FAIROD: Fairness-aware Outlier Detection. AAAI/ACM Conference on AI, Ethics, and Society (AIES).

.. [#Siddiqui2019Sequential] Siddiqui, M.A., Fern, A., Dietterich, T.G. and Wong, W.K., 2019. Sequential Feature Explanations for Anomaly Detection. *ACM Transactions on Knowledge Discovery from Data (TKDD)*, 13(1), p.1.

.. [#Sperl2021A3] Sperl, P., Schulze, J.-P., and Böttinger, K., 2021. Activation Anomaly Analysis. *European Conference on Machine Learning and Data Mining (ECML-PKDD) 2020*.

.. [#Suri2019Research] Suri, N.R. and Athithan, G., 2019. Research Issues in Outlier Detection. In *Outlier Detection: Techniques and Applications*, pp. 29-51. Springer, Cham.

.. [#Tang2015Mining] Tang, G., Pei, J., Bailey, J. and Dong, G., 2015. Mining multidimensional contextual outliers from categorical relational data. *Intelligent Data Analysis*, 19(5), pp.1171-1192.

.. [#Tang2023GADBench] Tang, J., Hua, F., Gao, Z., Zhao, P. and Li, J., 2023. GADBench: Revisiting and Benchmarking Supervised Graph Anomaly Detection. *NeurIPS*, Datasets and Benchmarks Track.

.. [#Ting2018Which] Ting, KM., Aryal, S. and Washio, T., 2018, Which Anomaly Detector should I use? *Tutorial at ICDM 2018*.

.. [#Ting2020Isolation] Ting, Kai Ming, Bi-Cun Xu, Takashi Washio, and Zhi-Hua Zhou. "Isolation Distributional Kernel: A New Tool for Kernel based Anomaly Detection." In *Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, pp. 198-206. 2020.

.. [#Wang2019Effective] Wang, S., Zeng, Y., Liu, X., Zhu, E., Yin, J., Xu, C. and Kloft, M., 2019. Effective End-to-end Unsupervised Outlier Detection via Inlier Priority of Discriminative Network. In *33rd Conference on Neural Information Processing Systems*.

.. [#Wang2019Progress] Wang, H., Bah, M.J. and Hammad, M., 2019. Progress in Outlier Detection Techniques: A Survey. *IEEE Access*, 7, pp.107964-108000.

.. [#Wang2020Deep] Wang, R., Nie, K., Chang, Y. J., Gong, X., Wang, T., Yang, Y., Long, B.,  2020. Deep Learning for Anomaly Detection. *Tutorial at KDD 2020*.

.. [#WellerFahy2015A] Weller-Fahy, D.J., Borghetti, B.J. and Sodemann, A.A., 2015. A survey of distance and similarity measures used within network intrusion anomaly detection. *IEEE Communications Surveys & Tutorials*\ , 17(1), pp.70-91.

.. [#Xu2021Beyond] Xu, H., Wang, Y., Jian, S., Huang, Z., Wang, Y., Liu, N. and Li, F., 2021, April. Beyond Outlier Detection: Outlier Interpretation by Attention-Guided Triplet Deviation Network. In *Proceedings of the Web Conference* 2021 (pp. 1328-1339).

.. [#Xu2023Deep] Xu, H., Pang, G., Wang, Y., Wang, Y., 2023. Deep Isolation Forest for Anomaly Detection. *IEEE Transactions on Knowledge and Data Engineering*. 

.. [#Xu2023Fascinating] Xu, H., Wang, Y., Wei, J., Jian, S., Li, Y., Liu, N., 2023. Fascinating Supervisory Signals and Where to Find Them: Deep Anomaly Detection with Scale Learning. *International Conference on Machine Learning (ICML)*.

.. [#Yoon2019NETS] Yoon, S., Lee, J. G., & Lee, B. S., 2019. NETS: extremely fast outlier detection from a data stream via set-based processing. Proceedings of the VLDB Endowment, 12(11), 1303-1315.

.. [#Yoon2020STARE] Yoon, S., Lee, J. G., & Lee, B. S., 2020. Ultrafast local outlier detection from a data stream with stationary region skipping. In Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (pp. 1181-1191)

.. [#Yoon2021MDUAL] Yoon, S., Shin, Y., Lee, J. G., & Lee, B. S. (2021, June). Multiple dynamic outlier-detection from a data stream by exploiting duality of data and queries. In Proceedings of the 2021 International Conference on Management of Data (SIGMOD).

.. [#Yoon2022ARCUS] Yoon, S., Lee, Y., Lee, J.G. and Lee, B.S., 2022, August. Adaptive Model Pooling for Online Deep Anomaly Detection from a Complex Evolving Data Stream. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (pp. 2347-2357).

.. [#Yu2015Glad] Yu, R., He, X. and Liu, Y., 2015. GLAD: group anomaly detection in social media analysis. *ACM Transactions on Knowledge Discovery from Data (TKDD)*\ , 10(2), p.18.

.. [#Yu2016A] Yu, R., Qiu, H., Wen, Z., Lin, C. and Liu, Y., 2016. A survey on social media anomaly detection. *ACM SIGKDD Explorations Newsletter*\ , 18(1), pp.1-14.

.. [#Yuan2024Trustworthy] Yuan, S., Xu, D. and Wu, X., 2024  Trustworthy Anomaly Detection. *Tutorial at SDM 2024*.

.. [#Zha2020Meta] Zha, D., Lai, K.H., Wan, M. and Hu, X., 2020. Meta-AAD: Active Anomaly Detection with Deep Reinforcement Learning. *ICDM*.

.. [#Zhao2018Xgbod] Zhao, Y. and Hryniewicki, M.K., 2018, July. XGBOD: improving supervised outlier detection with unsupervised representation learning. In *2018 International Joint Conference on Neural Networks (IJCNN)*. IEEE.

.. [#Zhao2019LSCP] Zhao, Y., Nasrullah, Z., Hryniewicki, M.K. and Li, Z., 2019, May. LSCP: Locally selective combination in parallel outlier ensembles. In *Proceedings of the 2019 SIAM International Conference on Data Mining (SDM)*, pp. 585-593. Society for Industrial and Applied Mathematics.

.. [#Zhao2019PYOD] Zhao, Y., Nasrullah, Z. and Li, Z., PyOD: A Python Toolbox for Scalable Outlier Detection. *Journal of Machine Learning Research*, 20, pp.1-7.

.. [#Zhao2020Automating] Zhao, Y., Rossi, R.A. and Akoglu, L., 2021. Automatic Unsupervised Outlier Model Selection. *Advances in Neural Information Processing Systems*.

.. [#Zhao2021SUOD] Zhao, Y., Hu, X., Cheng, C., Wang, C., Wan, C., Wang, W., Yang, J., Bai, H., Li, Z., Xiao, C. and Wang, Y., 2021. SUOD: Accelerating Large-scale Unsupervised Heterogeneous Outlier Detection. *Proceedings of Machine Learning and Systems (MLSys)*.

.. [#Zhao2021TOD] Zhao, Y., Chen, G.H. and Jia, Z., 2021. TOD: Tensor-based Outlier Detection. arXiv preprint arXiv:2110.14007.

.. [#Zhou2019AnomalyNet] Zhou, J.T., Du, J., Zhu, H., Peng, X., Liu, Y. and Goh, R.S.M., 2019. AnomalyNet: An anomaly detection network for video surveillance. *IEEE Transactions on Information Forensics and Security*.

.. [#Zhu2019Tripartite] Zhu, Y. and Yang, K., 2019. Tripartite Active Learning for Interactive Anomaly Discovery. *IEEE Access*.

.. [#Zimek2012A] Zimek, A., Schubert, E. and Kriegel, H.P., 2012. A survey on unsupervised outlier detection in high‐dimensional numerical data. *Statistical Analysis and Data Mining: The ASA Data Science Journal*\ , 5(5), pp.363-387.

.. [#Zimek2014Ensembles] Zimek, A., Campello, R.J. and Sander, J., 2014. Ensembles for unsupervised outlier detection: challenges and research questions a position paper. *ACM Sigkdd Explorations Newsletter*\ , 15(1), pp.11-22.

.. [#Zong2018Deep] Zong, B., Song, Q., Min, M.R., Cheng, W., Lumezanu, C., Cho, D. and Chen, H., 2018. Deep autoencoding gaussian mixture model for unsupervised anomaly detection. International Conference on Learning Representations (ICLR).

.. [#Wang2023Drift] Wang, C., Zhuang, Z., Qi, Q., Wang, J., Wang, X., Sun, H., & Liao, J. (2023). Drift doesn't matter: dynamic decomposition with diffusion reconstruction for unstable multivariate time series anomaly detection. Advances in Neural Information Processing Systems, 36.