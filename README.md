# 3000classify
根据公司描述和标签进行学习，然后分类新的描述

1 代表 供应链
2 代表 流通链
3 代表 服务链

按八二的比例分为训练集和测试集



实验结果：
LogisticRegression：
特征bigram：0.721843003413（去除停顿词后0.713310580205）
特征unigram：0.749146757679（去除停顿词之后0.750853242321）
特征unigram+bigram：0.755972696246(去除停顿词之后0.766211604096)
TFIDF 特征unigram+bigram removeStopwords:0.762798634812（没remove stopwords 0.754266211604）
TFIDF 特征unigram removeStopwords:0.767918088737（没remove stopwords 0.761092150171）
TFIDF 特征bigram removeStopwords:0.721843003413（没remove stopwords 0.757679180887）


SVM：
unigram and don't removeStopwords and don't use tfidf
clf_linear 正确率: 0.701365187713
clf_another_linear 正确率: 0.699658703072
clf_poly 正确率: 0.343003412969
clf_rbf 正确率: 0.59385665529
clf_sigmoid 正确率: 0.344709897611

移除stopwords
SVM clf_linear正确率: 0.721843003413(2gram0.694539249147,12gram0.737201365188)
SVM clf_another_linear正确率: 0.732081911263(2gram0.709897610922,12gram0.747440273038)
移除stopwords and using tfidf
SVM clf_linear正确率: 0.769624573379(12gram0.769624573379,1gram0.735494880546)
SVM clf_another_linear正确率: 0.762798634812(12gram0.764505119454,1gram0.730375426621)
using tfidf
SVM clf_linear正确率: 0.752559726962(12gram0.77133105802,2gram0.745733788396)
SVM clf_another_linear正确率: 0.761092150171(12gram0.78156996587,2gram0.745733788396)

Naive Bayes:
去除停顿词 and tfidf：1gram0.733788395904，2gram0.709897610922，12gram0.738907849829
tfidf：1gram0.723549488055，2gram0.725255972696，12gram0.733788395904
去除停顿词：1gram0.721843003413，2gram0.725255972696，12gram0.725255972696