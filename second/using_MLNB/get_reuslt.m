%循环分开，然后的到平均后的结果
%1002,919,1010
%801,735,808
%201,180,202
%共2344个训练集，587个测试集
high_precision = 0;
hp1= zeros(1,1002);
hp2= zeros(1,919);
hp3= zeros(1,1010);
total = 0.0;
num = 150; % 循环次数
for i = 1:num
    
    disp(i);
    %产生了三个随机排列的数列，用于分训练集和测试集
    p1 = randperm(1002);
    p1_train = p1(1:801);
    p1_test = p1(802:end);
    
    p2 = randperm(919);
    p2_train = p2(1:735);
    p2_test = p2(736:end);
    
    p3 = randperm(1010);
    p3_train = p3(1:808);
    p3_test = p3(809:end);
    %根据随机排列数得到三个分别的标签或者特征
    label1_train = label1(p1_train,:);
    label2_train = label2(p2_train,:);
    label3_train = label3(p3_train,:);
    
    label1_test = label1(p1_test,:);
    label2_test = label2(p2_test,:);
    label3_test = label3(p3_test,:);
    
    features1_train = features1(p1_train,:);
    features2_train = features2(p2_train,:);
    features3_train = features3(p3_train,:);
    
    features1_test = features1(p1_test,:);
    features2_test = features2(p2_test,:);
    features3_test = features3(p3_test,:);
    %合并特征和标签，得到test_data,test_target,train_data,train_target
    train_data = [features1_train;features2_train;features3_train];
    test_data = [features1_test;features2_test;features3_test];
    train_target = [label1_train;label2_train;label3_train];
    test_target = [label1_test;label2_test;label3_test];
    %进行多分类，得到结果
    test_target = double(test_target');
    train_target = double(train_target');
    test_data = double(test_data);
    train_data = double(train_data);
    %Set the number of remained features after PCA
    dim=size(train_data,2);
    ratio = 0.10;
    pca_remained=ceil(ratio*dim); % Set the number of reamined features after PCA to 30% of the original dimensionality, as suggested in the literature
    % Calling the main function MLNB
    [HammingLoss,RankingLoss,OneError,Coverage,Average_Precision,Outputs,Pre_Labels]=MLNB(train_data,train_target,test_data,test_target,pca_remained);
    
    if Average_Precision > high_precision
        high_precision = Average_Precision;
        hp1 = p1;
        hp2 = p2;
        hp3 = p3;
    end
    total = total + Average_Precision;
end
average_result = total/num;
save p1 hp1;
save p2 hp2;
save p3 hp3;