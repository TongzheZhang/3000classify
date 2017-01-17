[odrIdx,FisherRatio] = rankingFisher(array_x,array_y');
num = 500;

% for i = FisherRatio
%     if i > 0.005
%         num = num+1;
%     end
% end
final_fests_idx = odrIdx(1:num);
final_fests_idx = final_fests_idx - 1;
save 1feats_idx final_fests_idx
