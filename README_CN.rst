异常检测学习资源（Anomaly Detection Learning Resources）
====================================================

.. image:: https://img.shields.io/github/stars/yzhao062/anomaly-detection-resources.svg
   :target: https://github.com/yzhao062/anomaly-detection-resources/stargazers
   :alt: GitHub stars


.. image:: https://img.shields.io/github/forks/yzhao062/anomaly-detection-resources.svg?color=blue
   :target: https://github.com/yzhao062/anomaly-detection-resources/network
   :alt: GitHub forks


.. image:: https://img.shields.io/github/license/yzhao062/anomaly-detection-resources.svg?color=blue
   :target: https://github.com/yzhao062/anomaly-detection-resources/blob/master/LICENSE
   :alt: License


.. image:: https://img.shields.io/badge/link-996.icu-red.svg
   :target: https://github.com/996icu/996.ICU
   :alt: 996.ICU


----

`异常检测 (anomaly detection) <https://zh.wikipedia.org/wiki/%E5%BC%82%E5%B8%B8%E6%A3%80%E6%B5%8B>`_
(又名 Outlier Detection) 是一个重要但非常有挑战性的领域。异常检测的目标主要是找到数据中
偏离于主要分布的案例--它在很多领域都有重要意义，包括「信用卡诈骗检测」、「网络入侵检测」、
「机械故障检测」等。

这个仓库中收藏了关于异常检测的：


#. 专业书籍与学术论文
#. 在线课程与视频
#. 异常检测数据集
#. 开源与商业工具库
#. 重要的会议与期刊


**更多内容会被陆续添加到当前仓库中来**。
请建议/推荐相关资源，你可以选择提交issue report、pull request或者给我发邮件 (zhaoy@cmu.edu)。
Enjoy reading！

----

目录
-----------------


* `1. 书籍 & 教程 <#1-书籍--教程>`_

  * `1.1. 书籍 <#11-书籍>`_
  * `1.2. 教程 <#12-教程>`_

* `2. Courses/Seminars/Videos <#2-coursesseminarsvideos>`_
* `3. Toolbox & Datasets <#3-toolbox--datasets>`_

  * `3.1. Multivariate data outlier detection <#31-multivariate-data>`_
  * `3.2. Time series outlier detection <#32-time-series-outlier-detection>`_
  * `3.3. Datasets <#33-datasets>`_

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

* `5. Key Conferences/Workshops/Journals <#5-key-conferencesworkshopsjournals>`_

  * `5.1. Conferences & Workshops <#51-conferences--workshops>`_
  * `5.2. Journals <#52-journals>`_


----

1. 书籍 & 教程
-------------

1.1. 书籍
^^^^^^^^

`Outlier Analysis <https://www.springer.com/gp/book/9781461463955>`_
作者: Charu Aggarwal: 经典异常检测教科书，内容涵盖了大部分相关算法与应用。异常检测领域人士必读。
`[预览.pdf] <http://charuaggarwal.net/outlierbook.pdf>`_

`Outlier Ensembles: An Introduction <https://www.springer.com/gp/book/9783319547640>`_
作者: Charu Aggarwal and Saket Sathe: 非常权威的集成异常检测教科书。

`Data Mining: Concepts and Techniques (3rd) <https://www.elsevier.com/books/data-mining-concepts-and-techniques/han/978-0-12-381479-1>`_
作者: 韩家炜 (Jiawei Han) and Micheline Kamber and Jian Pei (裴健): 该书第十二章讨论了异常检测技术。 `[Google Search] <https://www.google.com/search?&q=data+mining+jiawei+han&oq=data+ming+jiawei>`_

1.2. 教程
^^^^^^^^

===================================================== ============================================  =====  ============================  ==========================================================================================================================================================================
Tutorial Title                                        Venue                                         Year   Ref                           Materials
===================================================== ============================================  =====  ============================  ==========================================================================================================================================================================
Outlier detection techniques                          ACM SIGKDD                                    2010   [#Kriegel2010Outlier]_        `[PDF] <https://imada.sdu.dk/~zimek/publications/KDD2010/kdd10-outlier-tutorial.pdf>`_
Anomaly Detection: A Tutorial                         ICDM                                          2011   [#Chawla2011Anomaly]_         `[PDF] <http://webdocs.cs.ualberta.ca/~icdm2011/downloads/ICDM2011_anomaly_detection_tutorial.pdf>`_
Data mining for anomaly detection                     PKDD                                          2008   [#Lazarevic2008Data]_         `[Video] <http://videolectures.net/ecmlpkdd08_lazarevic_dmfa/>`_
===================================================== ============================================  =====  ============================  ==========================================================================================================================================================================

----

2. Courses/Seminars/Videos
--------------------------

**Coursera Introduction to Anomaly Detection (by IBM)**\ :
`[See Video] <https://www.coursera.org/learn/ai/lecture/ASPv0/introduction-to-anomaly-detection>`_

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

[**Python**] `Python Outlier Detection (PyOD) <https://github.com/yzhao062/Pyod>`_\ : PyOD is a comprehensive and scalable Python toolkit for detecting outlying objects in multivariate data. It contains more than 20 detection algorithms, including emerging deep learning models and outlier ensembles.

[**Python**] `Scikit-learn Novelty and Outlier Detection <http://scikit-learn.org/stable/modules/outlier_detection.html>`_. It supports some popular algorithms like LOF, Isolation Forest, and One-class SVM.

[**Java**] `ELKI: Environment for Developing KDD-Applications Supported by Index-Structures <https://elki-project.github.io/>`_\ :
ELKI is an open source (AGPLv3) data mining software written in Java. The focus of ELKI is research in algorithms, with an emphasis on unsupervised methods in cluster analysis and outlier detection.

[**Java**] `RapidMiner Anomaly Detection Extension <https://github.com/Markus-Go/rapidminer-anomalydetection>`_\ : The Anomaly Detection Extension for RapidMiner comprises the most well know unsupervised anomaly detection algorithms, assigning individual anomaly scores to data rows of example sets. It allows you to find data, which is significantly different from the normal, without the need for the data being labeled.

[**R**] `outliers package <https://cran.r-project.org/web/packages/outliers/index.html>`_\ : A collection of some tests commonly used for identifying outliers in R.

[**Matlab**] `Anomaly Detection Toolbox - Beta <http://dsmi-lab-ntust.github.io/AnomalyDetectionToolbox/>`_\ : A collection of popular outlier detection algorithms in Matlab.


3.2. Time series outlier detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


[**Python**] `datastream.io <https://github.com/MentatInnovations/datastream.io>`_\ : An open-source framework for real-time anomaly detection using Python, Elasticsearch and Kibana.

[**Python**] `skyline <https://github.com/earthgecko/skyline>`_\ : Skyline is a near real time anomaly detection system.

[**Python**] `banpei <https://github.com/tsurubee/banpei>`_\ : Banpei is a Python package of the anomaly detection.

[**Python**] `telemanom <https://github.com/khundman/telemanom>`_\ : A framework for using LSTMs to detect anomalies in multivariate time series data.

[**Python**] `DeepADoTS <https://github.com/KDD-OpenSource/DeepADoTS>`_\ : A benchmarking pipeline for anomaly detection on time series data for multiple state-of-the-art deep learning methods.

[**R**] `AnomalyDetection <https://github.com/twitter/AnomalyDetection>`_\ : AnomalyDetection is an open-source R package to detect anomalies which is robust, from a statistical standpoint, in the presence of seasonality and an underlying trend.


3.3. Datasets
^^^^^^^^^^^^^

**ELKI Outlier Datasets**\ : https://elki-project.github.io/datasets/outlier

**Outlier Detection DataSets (ODDS)**\ : http://odds.cs.stonybrook.edu/#table1

**Unsupervised Anomaly Detection Dataverse**\ : https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OPQMVF

**Anomaly Detection Meta-Analysis Benchmarks**\ : https://ir.library.oregonstate.edu/concern/datasets/47429f155

----

4. Papers
---------

4.1. Overview & Survey Papers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                        Venue                         Year   Ref                           Materials
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
A survey of outlier detection methodologies                                                        ARTIF INTELL REV              2004   [#Hodge2004A]_                `[PDF] <https://www-users.cs.york.ac.uk/vicky/myPapers/Hodge+Austin_OutlierDetection_AIRE381.pdf>`_
Anomaly detection: A survey                                                                        CSUR                          2009   [#Chandola2009Anomaly]_       `[PDF] <https://www.vs.inf.ethz.ch/edu/HS2011/CPS/papers/chandola09_anomaly-detection-survey.pdf>`_
A meta-analysis of the anomaly detection problem                                                   Preprint                      2015   [#Emmott2015A]_               `[PDF] <https://arxiv.org/pdf/1503.01158.pdf>`_
On the evaluation of unsupervised outlier detection: measures, datasets, and an empirical study    DMKD                          2016   [#Campos2016On]_              `[HTML] <https://link.springer.com/article/10.1007/s10618-015-0444-8>`_, `[SLIDES] <https://imada.sdu.dk/~zimek/InvitedTalks/TUVienna-2016-05-18-outlier-evaluation.pdf>`_
A comparative evaluation of unsupervised anomaly detection algorithms for multivariate data        PLOS ONE                      2016   [#Goldstein2016A]_            `[PDF] <http://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0152173&type=printable>`_
A comparative evaluation of outlier detection algorithms: Experiments and analyses                 Pattern Recognition           2018   [#Domingues2018A]_            `[PDF] <https://www.researchgate.net/publication/320025854_A_comparative_evaluation_of_outlier_detection_algorithms_Experiments_and_analyses>`_
Research Issues in Outlier Detection                                                               Book Chapter                  2019   [#Suri2019Research]_          `[HTML] <https://link.springer.com/chapter/10.1007/978-3-030-05127-3_3>`_
Quantitative comparison of unsupervised anomaly detection algorithms for intrusion detection       SAC                           2019   [#Falcao2019Quantitative]_    `[HTML] <https://dl.acm.org/citation.cfm?id=3297314>`_
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================

4.2. Key Algorithms
^^^^^^^^^^^^^^^^^^^

====================  =================================================================================================  =================================  =====  ===========================  ==============================================================================================================================================================================================
Abbreviation          Paper Title                                                                                        Venue                              Year   Ref                          Materials
====================  =================================================================================================  =================================  =====  ===========================  ==============================================================================================================================================================================================
kNN                   Efficient algorithms for mining outliers from large data sets                                      ACM SIGMOD Record                  2000   [#Ramaswamy2000Efficient]_   `[PDF] <https://webdocs.cs.ualberta.ca/~zaiane/pub/check/ramaswamy.pdf>`_
KNN                   Fast outlier detection in high dimensional spaces                                                  PKDD                               2002   [#Angiulli2002Fast]_         `[PDF] <https://www.researchgate.net/profile/Clara_Pizzuti/publication/220699183_Fast_Outlier_Detection_in_High_Dimensional_Spaces/links/542ea6a60cf27e39fa9635c6.pdf>`_
LOF                   LOF: identifying density-based local outliers                                                      ACM SIGMOD Record                  2000   [#Breunig2000LOF]_           `[PDF] <http://www.dbs.ifi.lmu.de/Publikationen/Papers/LOF.pdf>`_
IForest               Isolation forest                                                                                   ICDM                               2008   [#Liu2008Isolation]_         `[PDF] <https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf>`_
OCSVM                 Estimating the support of a high-dimensional distribution                                          Neural Computation                 2001   [#Scholkopf2001Estimating]_  `[PDF] <http://users.cecs.anu.edu.au/~williams/papers/P132.pdf>`_
AutoEncoder Ensemble  Outlier detection with autoencoder ensembles                                                       SDM                                2017   [#Chen2017Outlier]_          `[PDF] <http://saketsathe.net/downloads/autoencode.pdf>`_
====================  =================================================================================================  =================================  =====  ===========================  ==============================================================================================================================================================================================

4.3. Graph & Network Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================================================================================================  =============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                        Venue                          Year   Ref                           Materials
=================================================================================================  =============================  =====  ============================  ==========================================================================================================================================================================
Graph based anomaly detection and description: a survey                                            DMKD                           2015   [#Akoglu2015Graph]_           `[PDF] <https://arxiv.org/pdf/1404.4679.pdf>`_
Anomaly detection in dynamic networks: a survey                                                    WIREs Computational Statistic  2015   [#Ranshous2015Anomaly]_       `[PDF] <https://onlinelibrary.wiley.com/doi/pdf/10.1002/wics.1347>`_
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
A survey on unsupervised outlier detection in high-dimensional numerical data                        Stat Anal Data Min            2012   [#Zimek2012A]_                `[HTML] <https://onlinelibrary.wiley.com/doi/abs/10.1002/sam.11161>`_
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
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================

4.8. Outlier Detection in Evolving Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                         Venue                         Year   Ref                           Materials
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
A Survey on Anomaly detection in Evolving Data: [with Application to Forest Fire Risk Prediction]   SIGKDD Explorations           2018   [#Salehi2018A]_               `[PDF] <http://www.kdd.org/exploration_files/20-1-Article2.pdf>`_
Unsupervised real-time anomaly detection for streaming data                                         Neurocomputing                2017   [#Ahmad2017Unsupervised]_     `[PDF] <https://www.researchgate.net/publication/317325599_Unsupervised_real-time_anomaly_detection_for_streaming_data>`_
Outlier Detection in Feature-Evolving Data Streams                                                  SIGKDD                        2018   [#Manzoor2018Outlier]_        `[PDF] <https://www.andrew.cmu.edu/user/lakoglu/pubs/18-kdd-xstream.pdf>`_, `[Github] <https://cmuxstream.github.io/>`_
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.9. Representation Learning in Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                         Venue                         Year   Ref                           Materials
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Learning Representations of Ultrahigh-dimensional Data for Random Distance-based Outlier Detection  SIGKDD                        2018   [#Pang2018Learning]_          `[PDF] <https://arxiv.org/pdf/1806.04808.pdf>`_
Learning representations for outlier detection on a budget                                          Preprint                      2015   [#Micenkova2015Learning]_     `[PDF] <https://arxiv.org/pdf/1507.08104.pdf>`_
XGBOD: improving supervised outlier detection with unsupervised representation learning             IJCNN                         2018   [#Zhao2018Xgbod]_             `[PDF] <https://www.yuezhao.me/s/edited_XGBOD.pdf>`_
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
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.11. Outlier Detection with Neural Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                        Venue                         Year   Ref                           Materials
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Detecting spacecraft anomalies using lstms and nonparametric dynamic thresholding                  KDD                           2018   [#Hundman2018Detecting]_      `[PDF] <https://arxiv.org/pdf/1802.04431.pdf>`_, `[Code] <https://github.com/khundman/telemanom>`_
MAD-GAN: Multivariate Anomaly Detection for Time Series Data with Generative Adversarial Networks  Preprint                      2019   [#Li2019MAD]_                 `[PDF] <https://arxiv.org/pdf/1901.04997.pdf>`_, `[Code] <https://github.com/LiDan456/MAD-GANs>`_
Generative Adversarial Active Learning for Unsupervised Outlier Detection                          TKDE                          2019   [#Liu2019Generative]_         `[PDF] <https://arxiv.org/pdf/1809.10816.pdf>`_, `[Code] <https://github.com/leibinghe/GAAL-based-outlier-detection>`_
Deep Autoencoding Gaussian Mixture Model for Unsupervised Anomaly Detection                        ICLR                          2018   [#Zong2018Deep]_              `[PDF] <http://www.cs.ucsb.edu/~bzong/doc/iclr18-dagmm.pdf>`_, `[Code] <https://github.com/danieltan07/dagmm>`_
=================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


4.12. Active Anomaly Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Paper Title                                                                                         Venue                         Year   Ref                           Materials
==================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Active learning for anomaly and rare-category detection                                             NeurIPS                       2005   [#Pelleg2005Active]_          `[PDF] <http://papers.nips.cc/paper/2554-active-learning-for-anomaly-and-rare-category-detection.pdf>`_
Outlier detection by active learning                                                                SIGKDD                        2006   [#Abe2006Outlier]_            `[PDF] <https://www.researchgate.net/profile/Naoki_Abe2/publication/221653343_Outlier_detection_by_active_learning/links/5441464a0cf2e6f0c0f60abb.pdf>`_
Active Anomaly Detection via Ensembles: Insights, Algorithms, and Interpretability                  Preprint                      2019   [#Das2019Active]_             `[PDF] <https://arxiv.org/pdf/1901.08930.pdf>`_
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

===================    =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
Field                  Paper Title                                                                                        Venue                         Year   Ref                           Materials
===================    =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================
**Security**           A survey of distance and similarity measures used within network intrusion anomaly detection       IEEE Commun. Surv. Tutor.     2015   [#WellerFahy2015A]_           `[PDF] <https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6853338>`_
**Security**           Anomaly-based network intrusion detection: Techniques, systems and challenges                      Computers & Security          2009   [#GarciaTeodoro2009Anomaly]_  `[PDF] <http://dtstc.ugr.es/~jedv/descargas/2009_CoSe09-Anomaly-based-network-intrusion-detection-Techniques,-systems-and-challenges.pdf>`_
**Finance**            A survey of anomaly detection techniques in financial domain                                       Future Gener Comput Syst      2016   [#Ahmed2016A]_                `[PDF] <http://isiarticles.com/bundles/Article/pre/pdf/76882.pdf>`_
**Traffic**            Outlier Detection in Urban Traffic Data                                                            WIMS                          2018   [#Djenouri2018Outlier]_       `[PDF] <http://dss.sdu.dk/assets/fpd-lof/outlier-detection-urban.pdf>`_
**Social Media**       A survey on social media anomaly detection                                                         SIGKDD Explorations           2016   [#Yu2016A]_                   `[PDF] <https://arxiv.org/pdf/1601.01102.pdf>`_
**Social Media**       GLAD: group anomaly detection in social media analysis                                             TKDD                          2015   [#Yu2015Glad]_                `[PDF] <https://arxiv.org/pdf/1410.1940.pdf>`_
**Machine Failure**    Detecting the Onset of Machine Failure Using Anomaly Detection Methods                             DAWAK                         2019   [#Riazi2019Detecting]_        `[PDF] <https://webdocs.cs.ualberta.ca/~zaiane/postscript/DAWAK19.pdf>`_
===================    =================================================================================================  ============================  =====  ============================  ==========================================================================================================================================================================


----

5. Key Conferences/Workshops/Journals
-------------------------------------

5.1. Conferences & Workshops
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Key data mining conference **deadlines**, **historical acceptance rates**, and more
can be found `data-mining-conferences <https://github.com/yzhao062/data-mining-conferences>`_.


`ACM International Conference on Knowledge Discovery and Data Mining (SIGKDD) <http://www.kdd.org/conferences>`_. **Note**: SIGKDD usually has an Outlier Detection Workshop (ODD), see `ODD 2018 <https://www.andrew.cmu.edu/user/lakoglu/odd/index.html>`_.

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

.. [#Breunig2000LOF] Breunig, M.M., Kriegel, H.P., Ng, R.T. and Sander, J., 2000, May. LOF: identifying density-based local outliers. *ACM SIGMOD Record*\ , 29(2), pp. 93-104.

.. [#Campos2016On] Campos, G.O., Zimek, A., Sander, J., Campello, R.J., Micenková, B., Schubert, E., Assent, I. and Houle, M.E., 2016. On the evaluation of unsupervised outlier detection: measures, datasets, and an empirical study. *Data Mining and Knowledge Discovery*\ , 30(4), pp.891-927.

.. [#Campos2018An] Campos, G.O., Zimek, A. and Meira, W., 2018, June. An Unsupervised Boosting Strategy for Outlier Detection Ensembles. In *Pacific-Asia Conference on Knowledge Discovery and Data Mining (pp. 564-576)*. Springer, Cham.

.. [#Chandola2009Anomaly] Chandola, V., Banerjee, A. and Kumar, V., 2009. Anomaly detection: A survey. *ACM computing surveys* , 41(3), p.15.

.. [#Chawla2011Anomaly] Chawla, S. and Chandola, V., 2011, Anomaly Detection: A Tutorial. *Tutorial at ICDM 2011*.

.. [#Chen2017Outlier] Chen, J., Sathe, S., Aggarwal, C. and Turaga, D., 2017, June. Outlier detection with autoencoder ensembles. *SIAM International Conference on Data Mining*, pp. 90-98. Society for Industrial and Applied Mathematics.

.. [#Dang2014Discriminative] Dang, X.H., Assent, I., Ng, R.T., Zimek, A. and Schubert, E., 2014, March. Discriminative features for identifying and interpreting outliers. In *International Conference on Data Engineering (ICDE)*. IEEE.

.. [#Das2019Active] Das, S., Islam, M.R., Jayakodi, N.K. and Doppa, J.R., 2019. Active Anomaly Detection via Ensembles: Insights, Algorithms, and Interpretability. arXiv preprint arXiv:1901.08930.

.. [#Ding2019Interactive] Ding, K., Li, J. and Liu, H., 2019, January. Interactive anomaly detection on attributed networks. In *Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining*, pp. 357-365. ACM.

.. [#Djenouri2018Outlier] Djenouri, Y. and Zimek, A., 2018, June. Outlier detection in urban traffic data. In *Proceedings of the 8th International Conference on Web Intelligence, Mining and Semantics*. ACM.

.. [#Domingues2018A] Domingues, R., Filippone, M., Michiardi, P. and Zouaoui, J., 2018. A comparative evaluation of outlier detection algorithms: Experiments and analyses. *Pattern Recognition*, 74, pp.406-421.

.. [#Emmott2015A] Emmott, A., Das, S., Dietterich, T., Fern, A. and Wong, W.K., 2015. A meta-analysis of the anomaly detection problem. arXiv preprint arXiv:1503.01158.

.. [#Falcao2019Quantitative] Falcão, F., Zoppi, T., Silva, C.B.V., Santos, A., Fonseca, B., Ceccarelli, A. and Bondavalli, A., 2019, April. Quantitative comparison of unsupervised anomaly detection algorithms for intrusion detection. In *Proceedings of the 34th ACM/SIGAPP Symposium on Applied Computing*, (pp. 318-327). ACM.

.. [#GarciaTeodoro2009Anomaly] Garcia-Teodoro, P., Diaz-Verdejo, J., Maciá-Fernández, G. and Vázquez, E., 2009. Anomaly-based network intrusion detection: Techniques, systems and challenges. *Computers & Security*\ , 28(1-2), pp.18-28.

.. [#Goldstein2016A] Goldstein, M. and Uchida, S., 2016. A comparative evaluation of unsupervised anomaly detection algorithms for multivariate data. *PloS one*\ , 11(4), p.e0152173.

.. [#Gupta2014Outlier] Gupta, M., Gao, J., Aggarwal, C.C. and Han, J., 2014. Outlier detection for temporal data: A survey. *IEEE Transactions on Knowledge and Data Engineering*\ , 26(9), pp.2250-2267.

.. [#Hodge2004A] Hodge, V. and Austin, J., 2004. A survey of outlier detection methodologies. *Artificial intelligence review*\ , 22(2), pp.85-126.

.. [#Hundman2018Detecting] Hundman, K., Constantinou, V., Laporte, C., Colwell, I. and Soderstrom, T., 2018, July. Detecting spacecraft anomalies using lstms and nonparametric dynamic thresholding. In *Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, (pp. 387-395). ACM.

.. [#Kannan2017Outlier] Kannan, R., Woo, H., Aggarwal, C.C. and Park, H., 2017, June. Outlier detection for text data. In *Proceedings of the 2017 SIAM International Conference on Data Mining*, pp. 489-497. Society for Industrial and Applied Mathematics.

.. [#Kriegel2010Outlier] Kriegel, H.P., Kröger, P. and Zimek, A., 2010. Outlier detection techniques. *Tutorial at ACM SIGKDD 2010*.

.. [#Lazarevic2008Data] Lazarevic, A., Banerjee, A., Chandola, V., Kumar, V. and Srivastava, J., 2008, September. Data mining for anomaly detection. *Tutorial at ECML PKDD 2008*.

.. [#Lamba2019Learning] Lamba, H. and Akoglu, L., 2019, May. Learning On-the-Job to Re-rank Anomalies from Top-1 Feedback. In *Proceedings of the 2019 SIAM International Conference on Data Mining (SDM)*, pp. 612-620. Society for Industrial and Applied Mathematics.

.. [#Li2019MAD] Li, D., Chen, D., Shi, L., Jin, B., Goh, J. and Ng, S.K., 2019. MAD-GAN: Multivariate Anomaly Detection for Time Series Data with Generative Adversarial Networks. arXiv preprint arXiv:1901.04997.

.. [#Liu2008Isolation] Liu, F.T., Ting, K.M. and Zhou, Z.H., 2008, December. Isolation forest. In *International Conference on Data Mining*\ , pp. 413-422. IEEE.

.. [#Liu2018Contextual] Liu, N., Shin, D. and Hu, X., 2017. Contextual outlier interpretation. In *International Joint Conference on Artificial Intelligence (IJCAI-18)*, pp.2461-2467.

.. [#Liu2019Generative] Liu, Y., Li, Z., Zhou, C., Jiang, Y., Sun, J., Wang, M. and He, X., 2019. Generative Adversarial Active Learning for Unsupervised Outlier Detection. *IEEE transactions on knowledge and data engineering*.

.. [#Macha2018Explaining] Macha, M. and Akoglu, L., 2018. Explaining anomalies in groups with characterizing subspace rules. Data Mining and Knowledge Discovery, 32(5), pp.1444-1480.

.. [#Manzoor2018Outlier] Manzoor, E., Lamba, H. and Akoglu, L. Outlier Detection in Feature-Evolving Data Streams. In *24th ACM SIGKDD International Conference on Knowledge Discovery and Data mining (KDD)*. 2018.

.. [#Micenkova2015Learning] Micenková, B., McWilliams, B. and Assent, I., 2015. Learning representations for outlier detection on a budget. arXiv preprint arXiv:1507.08104.

.. [#Gupta2018Beyond] Gupta, N., Eswaran, D., Shah, N., Akoglu, L. and Faloutsos, C., Beyond Outlier Detection: LookOut for Pictorial Explanation. *ECML PKDD 2018*.

.. [#Pang2016Unsupervised] Pang, G., Cao, L., Chen, L. and Liu, H., 2016, December. Unsupervised feature selection for outlier detection by modelling hierarchical value-feature couplings. In Data Mining (ICDM), 2016 IEEE 16th International Conference on (pp. 410-419). IEEE.

.. [#Pang2017Learning] Pang, G., Cao, L., Chen, L. and Liu, H., 2017, August. Learning homophily couplings from non-iid data for joint feature selection and noise-resilient outlier detection. In Proceedings of the 26th International Joint Conference on Artificial Intelligence (pp. 2585-2591). AAAI Press.

.. [#Pang2018Learning] Pang, G., Cao, L., Chen, L. and Liu, H., 2018. Learning Representations of Ultrahigh-dimensional Data for Random Distance-based Outlier Detection. In *24th ACM SIGKDD International Conference on Knowledge Discovery and Data mining (KDD)*. 2018.

.. [#Pelleg2005Active] Pelleg, D. and Moore, A.W., 2005. Active learning for anomaly and rare-category detection. In *Advances in neural information processing systems*\, pp. 1073-1080.

.. [#Radovanovic2015Reverse] Radovanović, M., Nanopoulos, A. and Ivanović, M., 2015. Reverse nearest neighbors in unsupervised distance-based outlier detection. *IEEE transactions on knowledge and data engineering*, 27(5), pp.1369-1382.

.. [#Ramaswamy2000Efficient] Ramaswamy, S., Rastogi, R. and Shim, K., 2000, May. Efficient algorithms for mining outliers from large data sets. *ACM SIGMOD Record*\ , 29(2), pp. 427-438.

.. [#Ranshous2015Anomaly] Ranshous, S., Shen, S., Koutra, D., Harenberg, S., Faloutsos, C. and Samatova, N.F., 2015. Anomaly detection in dynamic networks: a survey. Wiley Interdisciplinary Reviews: Computational Statistics, 7(3), pp.223-247.

.. [#Riazi2019Detecting] Riazi, M., Zaiane, O., Takeuchi, T., Maltais, A., Günther, J. and Lipsett, M., Detecting the Onset of Machine Failure Using Anomaly Detection Methods.

.. [#Ro2015Outlier] Ro, K., Zou, C., Wang, Z. and Yin, G., 2015. Outlier detection for high-dimensional data. *Biometrika*, 102(3), pp.589-599.

.. [#Salehi2018A] Salehi, Mahsa & Rashidi, Lida. (2018). A Survey on Anomaly detection in Evolving Data: [with Application to Forest Fire Risk Prediction]. *ACM SIGKDD Explorations Newsletter*. 20. 13-23.

.. [#Scholkopf2001Estimating] Schölkopf, B., Platt, J.C., Shawe-Taylor, J., Smola, A.J. and Williamson, R.C., 2001. Estimating the support of a high-dimensional distribution. *Neural Computation*, 13(7), pp.1443-1471.

.. [#Siddiqui2019Sequential] Siddiqui, M.A., Fern, A., Dietterich, T.G. and Wong, W.K., 2019. Sequential Feature Explanations for Anomaly Detection. *ACM Transactions on Knowledge Discovery from Data (TKDD)*, 13(1), p.1.

.. [#Suri2019Research] Suri, N.R. and Athithan, G., 2019. Research Issues in Outlier Detection. In *Outlier Detection: Techniques and Applications*, pp. 29-51. Springer, Cham.

.. [#Tang2015Mining] Tang, G., Pei, J., Bailey, J. and Dong, G., 2015. Mining multidimensional contextual outliers from categorical relational data. *Intelligent Data Analysis*, 19(5), pp.1171-1192.

.. [#WellerFahy2015A] Weller-Fahy, D.J., Borghetti, B.J. and Sodemann, A.A., 2015. A survey of distance and similarity measures used within network intrusion anomaly detection. *IEEE Communications Surveys & Tutorials*\ , 17(1), pp.70-91.

.. [#Yu2015Glad] Yu, R., He, X. and Liu, Y., 2015. GLAD: group anomaly detection in social media analysis. *ACM Transactions on Knowledge Discovery from Data (TKDD)*\ , 10(2), p.18.

.. [#Yu2016A] Yu, R., Qiu, H., Wen, Z., Lin, C. and Liu, Y., 2016. A survey on social media anomaly detection. *ACM SIGKDD Explorations Newsletter*\ , 18(1), pp.1-14.

.. [#Zhao2018Xgbod] Zhao, Y. and Hryniewicki, M.K., 2018, July. XGBOD: improving supervised outlier detection with unsupervised representation learning. In *2018 International Joint Conference on Neural Networks (IJCNN)*. IEEE.

.. [#Zhao2019LSCP] Zhao, Y., Nasrullah, Z., Hryniewicki, M.K. and Li, Z., 2019, May. LSCP: Locally selective combination in parallel outlier ensembles. In *Proceedings of the 2019 SIAM International Conference on Data Mining (SDM)*, pp. 585-593. Society for Industrial and Applied Mathematics.

.. [#Zhu2019Tripartite] Zhu, Y. and Yang, K., 2019. Tripartite Active Learning for Interactive Anomaly Discovery. *IEEE Access*.

.. [#Zimek2012A] Zimek, A., Schubert, E. and Kriegel, H.P., 2012. A survey on unsupervised outlier detection in high‐dimensional numerical data. *Statistical Analysis and Data Mining: The ASA Data Science Journal*\ , 5(5), pp.363-387.

.. [#Zimek2014Ensembles] Zimek, A., Campello, R.J. and Sander, J., 2014. Ensembles for unsupervised outlier detection: challenges and research questions a position paper. *ACM Sigkdd Explorations Newsletter*\ , 15(1), pp.11-22.

.. [#Zong2018Deep] Zong, B., Song, Q., Min, M.R., Cheng, W., Lumezanu, C., Cho, D. and Chen, H., 2018. Deep autoencoding gaussian mixture model for unsupervised anomaly detection. International Conference on Learning Representations (ICLR).

.. [#Wang2023Drift] Wang, C., Zhuang, Z., Qi, Q., Wang, J., Wang, X., Sun, H., & Liao, J. (2023). Drift doesn't matter: dynamic decomposition with diffusion reconstruction for unstable multivariate time series anomaly detection. Advances in Neural Information Processing Systems, 36.