load('seeme.mat');

test_target = double(test_target');
train_target = double(train_target');
test_data = double(test_data);
train_data = double(train_data);

[Weights,Bias,SVs,Weights_size,Bias_size]=RankSVM_train(train_data,train_target,'Linear');
[HammingLoss,RankingLoss,OneError,Coverage,Average_Precision,Outputs,Threshold,Pre_Labels]=RankSVM_test(test_data,test_target,Weights,Bias,SVs,Wegihts_sizepre,Bias_sizepre);