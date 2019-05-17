%load('Summaryfull.mat');
load('chromaticscale250summary05172019.mat');
Summaryfull=chromaticscale250summary05172019;

conf=Summaryfull.Confidence(:,:);
timestep=Summaryfull.Timestepms(:,:);
ave_error=Summaryfull.AveErrorcents(:,:);

mat=[conf timestep ave_error];

% for i=1:5
%     scatter3(mat(1+20*(i-1):20*i,1),mat(1+20*(i-1):20*i,2),mat(1+20*(i-1):20*i,3));
%     hold on; grid on;
% end

scatter3(mat(:,1),mat(:,2),mat(:,3))
title('Full Model CREPE Output')
xlabel('Confidence'); 
ylabel('Timestep (ms)');
zlabel('Ave. Error (cents)');
%legend('Timestep=1ms','Timestep=5ms','Timestep=10ms','Timestep=20ms','Timestep=50ms','Location','EastOutside');
