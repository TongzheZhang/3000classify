%This is my file on how the MLNB program could be used (The main function is "MLNB.m")
%
%Type 'help MLNB' under Matlab prompt for more detailed information


% Loading the file containing the necessary inputs for calling the MLNB function
load('seeme.mat'); 

test_target = double(test_target');
train_target = double(train_target');
test_data = double(test_data);
train_data = double(train_data);

%Set the number of remained features after PCA
dim=size(train_data,2);
result = zeros(2, 13);

for i = 0:12
    ratio = 0.05+i*0.02;
    disp(ratio)
    %ratio=0.1;
    pca_remained=ceil(ratio*dim); % Set the number of reamined features after PCA to 30% of the original dimensionality, as suggested in the literature
    % Calling the main function MLNB
    [HammingLoss,RankingLoss,OneError,Coverage,Average_Precision,Outputs,Pre_Labels]=MLNB(train_data,train_target,test_data,test_target,pca_remained);
    result(1,i+1) = ratio;
    result(2,i+1) = Average_Precision;
end
