.. role:: raw-html-m2r(raw)
   :format: html


Anomaly Detection Learning Resources
====================================

----

`\Outlier Detection <https://en.wikipedia.org/wiki/Anomaly_detection>`_
(also known as `Anomaly Detection <https://en.wikipedia.org/wiki/Anomaly_detection>`_) is a fascinating and useful technique to identify outlying data objects. It has been proven critical in many fields, such as credit card fraud analytics and mechanical unit defect detection.

In this repository, you could find:


#. Books & Academic Papers 
#. Learning Materials, e.g., online courses and videos 
#. Outlier Datasets
#. Open-source Libraries & Demo Codes
#. **Paper Downloader**: a Python 3 script to download the open access papers listed in this repository (under development).

**I would continue adding more items to the repository**. 
Please feel free to suggest some critical materials by opening an issue, submitting a pull request, or
dropping me an email @(yuezhao@cs.toronto.edu). Enjoy reading!

----

Table of Contents
-----------------

.. raw:: html

   <!-- TOC -->

* `Anomaly Detection Learning Resources <#anomaly-detection-learning-resources>`_

  * `1. Books & Tutorials <#1-books--tutorials>`_

    * `1.1. Books <#11-books>`_
    * `1.2. Tutorials <#12-tutorials>`_

  * `2. Courses/Seminars/Videos <#2-coursesseminarsvideos>`_
  * `3. Toolbox & Datasets <#3-toolbox--datasets>`_

    * `3.1. Python <#31-python>`_
    * `3.2. Matlab <#32-matlab>`_
    * `3.3. Java <#33-java>`_
    * `3.4. Time series outlier detection <#34-time-series-outlier-detection>`_
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
    * `4.11. Social Media Anomaly Detection <#411-social-media-anomaly-detection>`_
    * `4.12. Outlier Detection in Other fields <#412-outlier-detection-in-other-fields>`_
    * `4.13. Outlier Detection Applications <#413-outlier-detection-applications>`_

  * `5. Key Conferences/Workshops/Journals <#5-key-conferencesworkshopsjournals>`_

    * `5.1. Conferences & Workshops <#51-conferences--workshops>`_
    * `5.2. Journals <#52-journals>`_

:raw-html-m2r:`<!-- /TOC -->`

----

1. Books & Tutorials
--------------------

1.1. Books
^^^^^^^^^^

`Outlier Analysis <https://www.springer.com/gp/book/9781461463955>`_ 
by Charu Aggarwal: Classical text book covering most of the outlier analysis techniques. 
A must-read for people in outlier detection. `[Preview.pdf] <http://charuaggarwal.net/outlierbook.pdf>`_

`Outlier Ensembles: An Introduction <https://www.springer.com/gp/book/9783319547640>`_ 
by Charu Aggarwal and Saket Sathe: Great intro book for ensemble learning in outlier analysis.

`Data Mining: Concepts and Techniques (3rd) <https://www.elsevier.com/books/data-mining-concepts-and-techniques/han/978-0-12-381479-1>`_ 
by Jiawei Han Micheline Kamber Jian Pei: Chapter 12 discusses outlier detection with many important points. `[Google Search] <https://www.google.ca/search?&q=data+mining+jiawei+han&oq=data+ming+jiawei>`_

1.2. Tutorials
^^^^^^^^^^^^^^

Kriegel, H.P., Kröger, P. and Zimek, A., 2010. Outlier detection techniques. *Tutorial at ACM SIGKDD*\ , 10. `[Download PDF] <https://imada.sdu.dk/~zimek/publications/KDD2010/kdd10-outlier-tutorial.pdf>`_

Chawla, S. and Chandola, V., 2011, Anomaly Detection: A Tutorial. *Tutorial at ICDM 2011*.  `[Download PDF] <http://webdocs.cs.ualberta.ca/~icdm2011/downloads/ICDM2011_anomaly_detection_tutorial.pdf>`_

Lazarevic, A., Banerjee, A., Chandola, V., Kumar, V. and Srivastava, J., 2008, September. Data mining for anomaly detection. In *Tutorial at ECML PKDD 2008*. `[See Video] <http://videolectures.net/ecmlpkdd08_lazarevic_dmfa/>`_

2. Courses/Seminars/Videos
--------------------------

**Coursera Introduction to Anomaly Detection (by IBM)**\ :
https://www.coursera.org/learn/ai/lecture/ASPv0/introduction-to-anomaly-detection

**Coursera Machine Learning by Andrew Ng also partly covers the topic**\ :


* `Anomaly Detection vs. Supervised Learning <https://www.coursera.org/learn/machine-learning/lecture/Rkc5x/anomaly-detection-vs-supervised-learning>`_
* `Developing and Evaluating an Anomaly Detection System <https://www.coursera.org/learn/machine-learning/lecture/Mwrni/developing-and-evaluating-an-anomaly-detection-system>`_

**Udemy Outlier Detection Algorithms in Data Mining and Data Science**\ : https://www.udemy.com/outlier-detection-techniques/

**Stanford Data Mining for Cyber Security** also covers part of anomaly detection techniques. http://web.stanford.edu/class/cs259d/

3. Toolbox & Datasets
---------------------

3.1. Python
^^^^^^^^^^^

`Scikit-learn Novelty and Outlier Detection <http://scikit-learn.org/stable/modules/outlier_detection.html>`_. It supports some popular algorithms like LOF, Isolation Forest and One-class SVM

`Python Outlier Detection (PyOD) <https://github.com/yzhao062/Pyod>`_\ : It supports a series of outlier detection algorithms and combination frameworks. It is now released on PyPI and can be installed with "pip install pyod".

3.2. Matlab
^^^^^^^^^^^

`Anomaly Detection Toolbox - Beta <http://dsmi-lab-ntust.github.io/AnomalyDetectionToolbox/>`_\ : A collection of popular outlier detection algorithms in Matlab.

3.3. Java
^^^^^^^^^

`ELKI: Environment for Developing KDD-Applications Supported by Index-Structures <https://elki-project.github.io/>`_\ : 
ELKI is an open source (AGPLv3) data mining software written in Java. The focus of ELKI is research in algorithms, with an emphasis on unsupervised methods in cluster analysis and outlier detection. 

`RapidMiner Anomaly Detection Extension <https://github.com/Markus-Go/rapidminer-anomalydetection>`_\ : The Anomaly Detection Extension for RapidMiner comprises the most well know unsupervised anomaly detection algorithms, assigning individual anomaly scores to data rows of example sets. It allows you to find data, which is significantly different from the normal, without the need for the data being labeled.

3.4. Time series outlier detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* `datastream.io <https://github.com/MentatInnovations/datastream.io>`_
* `skyline <https://github.com/earthgecko/skyline>`_
* `banpei <https://github.com/tsurubee/banpei>`_
* `AnomalyDetection <https://github.com/twitter/AnomalyDetection>`_

3.5. Datasets
^^^^^^^^^^^^^

**ELKI Outlier Datasets**\ : https://elki-project.github.io/datasets/outlier

**Outlier Detection DataSets (ODDS)**\ : http://odds.cs.stonybrook.edu/#table1

**Unsupervised Anomaly Detection Dataverse**\ : https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OPQMVF

**Anomaly Detection Meta-Analysis Benchmarks**\ : https://ir.library.oregonstate.edu/concern/datasets/47429f155

4. Papers
---------

4.1. Overview & Survey Papers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Chandola, V., Banerjee, A. and Kumar, V., 2009. Anomaly detection: A survey. *ACM computing surveys* , 41(3), p.15. `[Download PDF] <https://www.vs.inf.ethz.ch/edu/HS2011/CPS/papers/chandola09_anomaly-detection-survey.pdf>`_

Hodge, V. and Austin, J., 2004. A survey of outlier detection methodologies. *Artificial intelligence review*\ , 22(2), pp.85-126. `[Download PDF] <https://www-users.cs.york.ac.uk/vicky/myPapers/Hodge+Austin_OutlierDetection_AIRE381.pdf>`_

Campos, G.O., Zimek, A., Sander, J., Campello, R.J., Micenková, B., Schubert, E., Assent, I. and Houle, M.E., 2016. On the evaluation of unsupervised outlier detection: measures, datasets, and an empirical study. *Data Mining and Knowledge Discovery*\ , 30(4), pp.891-927. `[HTML] <https://link.springer.com/article/10.1007/s10618-015-0444-8>`_ 
`[SLIDES] <https://imada.sdu.dk/~zimek/InvitedTalks/TUVienna-2016-05-18-outlier-evaluation.pdf>`_

Singh, K., & Upadhyaya, S. (2012). Outlier detection: applications and techniques. International Journal of Computer Science Issues (IJCSI), 9(1), 307. `[Download PDF] <https://pdfs.semanticscholar.org/4f58/44c9e7db68af7c2c5b918082636c3307cef9.pdf>`_

Goldstein, M. and Uchida, S., 2016. A comparative evaluation of unsupervised anomaly detection algorithms for multivariate data. *PloS one*\ , 11(4), p.e0152173.  `[Download PDF] <http://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0152173&type=printable>`_

4.2. Key Algorithms
^^^^^^^^^^^^^^^^^^^

**k Nearst Neighbors (kNN) Outlier Detector**.


* Ramaswamy, S., Rastogi, R. and Shim, K., 2000, May. Efficient algorithms for mining outliers from large data sets. *ACM Sigmod Record*\ , 29(2), pp. 427-438). `[Download PDF] <https://webdocs.cs.ualberta.ca/~zaiane/pub/check/ramaswamy.pdf>`_
* Angiulli, F. and Pizzuti, C., 2002, August. Fast outlier detection in high dimensional spaces. In *European Conference on Principles of Data Mining and Knowledge Discovery* pp. 15-27. `[HTML] <https://link.springer.com/chapter/10.1007/3-540-45681-3_2>`_

**Local Outlier Factor (LOF)**. Breunig, M.M., Kriegel, H.P., Ng, R.T. and Sander, J., 2000, May. LOF: identifying density-based local outliers. *ACM Sigmod Record*\ , 29(2), pp. 93-104. `[Download PDF] <http://www.dbs.ifi.lmu.de/Publikationen/Papers/LOF.pdf>`_

**Isolation Forest**. Liu, F.T., Ting, K.M. and Zhou, Z.H., 2008, December. Isolation forest. In *ICDM '08*\ , pp. 413-422. IEEE. `[Download PDF] <https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf>`_

**One-class Support Vector Machine**. Ma, J. and Perkins, S., 2003, July. Time-series novelty detection using one-class support vector machines. In *IJCNN' 03*\ , pp. 1741-1745. IEEE. `[Download PDF] <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.653.2440&rep=rep1&type=pdf>`_

4.3. Graph & Network Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Akoglu, L., Tong, H. and Koutra, D., 2015. Graph based anomaly detection and description: a survey. *Data Mining and Knowledge Discovery*\ , 29(3), pp.626-688. `[Download PDF] <https://arxiv.org/pdf/1404.4679.pdf>`_

Ranshous, S., Shen, S., Koutra, D., Harenberg, S., Faloutsos, C. and Samatova, N.F., 2015. Anomaly detection in dynamic networks: a survey. Wiley Interdisciplinary Reviews: Computational Statistics, 7(3), pp.223-247. `[Download PDF] <https://onlinelibrary.wiley.com/doi/pdf/10.1002/wics.1347>`_

4.4. Time Series Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gupta, M., Gao, J., Aggarwal, C.C. and Han, J., 2014. Outlier detection for temporal data: A survey. *IEEE Transactions on Knowledge and Data Engineering*\ , 26(9), pp.2250-2267. `[Download PDF] <https://www.microsoft.com/en-us/research/wp-content/uploads/2014/01/gupta14_tkde.pdf>`_

4.5. Feature Selection in Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pang, G., Cao, L., Chen, L. and Liu, H., 2016, December. Unsupervised feature selection for outlier detection by modelling hierarchical value-feature couplings. In Data Mining (ICDM), 2016 IEEE 16th International Conference on (pp. 410-419). IEEE. `[Download PDF] <https://opus.lib.uts.edu.au/bitstream/10453/107356/4/DSFS_ICDM2016.pdf>`_

Pang, G., Cao, L., Chen, L. and Liu, H., 2017, August. Learning homophily couplings from non-iid data for joint feature selection and noise-resilient outlier detection. In Proceedings of the 26th International Joint Conference on Artificial Intelligence (pp. 2585-2591). AAAI Press. `[Download PDF] <https://www.ijcai.org/proceedings/2017/0360.pdf>`_

4.6. High-dimensional & Subspace Outliers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zimek, A., Schubert, E. and Kriegel, H.P., 2012. A survey on unsupervised outlier detection in high‐dimensional numerical data. *Statistical Analysis and Data Mining: The ASA Data Science Journal*\ , 5(5), pp.363-387. `[Downloadable Link] <https://onlinelibrary.wiley.com/doi/abs/10.1002/sam.11161>`_

Pang, G., Cao, L., Chen, L. and Liu, H., 2018. Learning Representations of Ultrahigh-dimensional Data for Random Distance-based Outlier Detection. In *24th ACM SIGKDD International Conference on Knowledge Discovery and Data mining (KDD)*. 2018. `[Download PDF] <https://arxiv.org/pdf/1806.04808.pdf>`_

4.7. Outlier Ensembles
^^^^^^^^^^^^^^^^^^^^^^

Aggarwal, C.C., 2013. Outlier ensembles: position paper. *ACM SIGKDD Explorations Newsletter*\ , 14(2), pp.49-58. `[Download PDF] <https://pdfs.semanticscholar.org/841e/ce7c3812bbf799c99c84c064bbcf77916ba9.pdf>`_

Zimek, A., Campello, R.J. and Sander, J., 2014. Ensembles for unsupervised outlier detection: challenges and research questions a position paper. *ACM Sigkdd Explorations Newsletter*\ , 15(1), pp.11-22. `[Download PDF] <http://www.kdd.org/exploration_files/V15-01-02-Zimek.pdf>`_

Campos, G.O., Zimek, A. and Meira, W., 2018, June. An Unsupervised Boosting Strategy for Outlier Detection Ensembles. In Pacific-Asia Conference on Knowledge Discovery and Data Mining (pp. 564-576). Springer, Cham. `[HTML] <https://link.springer.com/chapter/10.1007/978-3-319-93034-3_45>`_

4.8. Outlier Detection in Evolving Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Salehi, Mahsa & Rashidi, Lida. (2018). A Survey on Anomaly detection in Evolving Data: [with Application to Forest Fire Risk Prediction]. *ACM SIGKDD Explorations Newsletter*. 20. 13-23. `[Download PDF] <http://www.kdd.org/exploration_files/20-1-Article2.pdf>`_

Emaad Manzoor, Hemank Lamba, Leman Akoglu. Outlier Detection in Feature-Evolving Data Streams. In *24th ACM SIGKDD International Conference on Knowledge Discovery and Data mining (KDD)*. 2018. `[Download PDF] <https://www.andrew.cmu.edu/user/lakoglu/pubs/18-kdd-xstream.pdf>`_ 
`[Github] <https://cmuxstream.github.io/>`_

4.9. Representation Learning in Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pang, G., Cao, L., Chen, L. and Liu, H., 2018. Learning Representations of Ultrahigh-dimensional Data for Random Distance-based Outlier Detection. In *24th ACM SIGKDD International Conference on Knowledge Discovery and Data mining (KDD)*. 2018. `[Download PDF] <https://arxiv.org/pdf/1806.04808.pdf>`_

Micenková, B., McWilliams, B. and Assent, I., 2015. Learning representations for outlier detection on a budget. arXiv preprint arXiv:1507.08104. `[Download PDF] <https://arxiv.org/pdf/1507.08104.pdf>`_

Zhao, Y., Hryniewicki, M.K. and PricewaterhouseCoopers, A., 2018. XGBOD: Improving Supervised Outlier Detection with Unsupervised Representation Learning. *International Joint Conference on Neural Networks*. `[Download PDF] <https://www.cs.toronto.edu/~yuezhao/s/edited_XGBOD.pdf>`_

4.10. Interpretability
^^^^^^^^^^^^^^^^^^^^^^

Nikhil Gupta, Dhivya Eswaran, Neil Shah, Leman Akoglu, Christos Faloutsos. Beyond Outlier Detection: LookOut for Pictorial Explanation. *ECML PKDD 2018*. `[Download PDF] <https://www.andrew.cmu.edu/user/lakoglu/pubs/18-pkdd-lookout.pdf>`_

Liu, N., Shin, D. and Hu, X., 2017. Contextual outlier interpretation. arXiv preprint arXiv:1711.10589. `[Download PDF] <https://arxiv.org/pdf/1711.10589.pdf>`_

Tang, G., Pei, J., Bailey, J. and Dong, G., 2015. Mining multidimensional contextual outliers from categorical relational data. Intelligent Data Analysis, 19(5), pp.1171-1192.  `[Download PDF] <http://www.cs.sfu.ca/~jpei/publications/Contextual%20outliers.pdf>`_

Dang, X.H., Assent, I., Ng, R.T., Zimek, A. and Schubert, E., 2014, March. Discriminative features for identifying and interpreting outliers. In *International Conference on Data Engineering (ICDE)*. IEEE. `[Download PDF] <http://cs.au.dk/~dang/icde2014.pdf>`_

4.11. Social Media Anomaly Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yu, R., Qiu, H., Wen, Z., Lin, C. and Liu, Y., 2016. A survey on social media anomaly detection. *ACM SIGKDD Explorations Newsletter*\ , 18(1), pp.1-14. `[Download PDF] <https://arxiv.org/pdf/1601.01102.pdf>`_

Yu, R., He, X. and Liu, Y., 2015. Glad: group anomaly detection in social media analysis. *ACM Transactions on Knowledge Discovery from Data (TKDD)*\ , 10(2), p.18. `[Download PDF] <https://arxiv.org/pdf/1410.1940.pdf>`_

4.12. Outlier Detection in Other fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kannan, R., Woo, H., Aggarwal, C.C. and Park, H., 2017, June. Outlier detection for text data. In Proceedings of the 2017 SIAM International Conference on Data Mining (pp. 489-497). Society for Industrial and Applied Mathematics. `[Download PDF] <https://epubs.siam.org/doi/pdf/10.1137/1.9781611974973.55>`_

4.13. Outlier Detection Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Security**:

* Weller-Fahy, D.J., Borghetti, B.J. and Sodemann, A.A., 2015. A survey of distance and similarity measures used within network intrusion anomaly detection. *IEEE Communications Surveys & Tutorials*\ , 17(1), pp.70-91. `[Download PDF] <https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6853338>`_
* Garcia-Teodoro, P., Diaz-Verdejo, J., Maciá-Fernández, G. and Vázquez, E., 2009. Anomaly-based network intrusion detection: Techniques, systems and challenges. *computers & security*\ , 28(1-2), pp.18-28. `[Download PDF] <http://dtstc.ugr.es/~jedv/descargas/2009_CoSe09-Anomaly-based-network-intrusion-detection-Techniques,-systems-and-challenges.pdf>`_

**Finance**:

* Ahmed, M., Mahmood, A.N. and Islam, M.R., 2016. A survey of anomaly detection techniques in financial domain. Future Generation Computer Systems, 55, pp.278-288. `[Download PDF] <http://isiarticles.com/bundles/Article/pre/pdf/76882.pdf>`_

5. Key Conferences/Workshops/Journals
-------------------------------------

5.1. Conferences & Workshops
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`ACM International Conference on Knowledge Discovery and Data Mining (SIGKDD) <http://www.kdd.org/conferences>`_
 **Note: SIGKDD usually has an Outlier Detection Workshop (ODD), see `ODD 2018 <https://www.andrew.cmu.edu/user/lakoglu/odd/index.html>`_\ **.

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
