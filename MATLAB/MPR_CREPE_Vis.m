%load('Summaryfull.mat');
clear all; close all; clc;
load('chromaticscale250summary05172019.mat');
data=chromaticscale250summary05172019;

%Collect data from file
conf=data.Confidence(:,:);
timestep=data.Timestepms(:,:);
ave_error=data.AveErrorcents(:,:);
percent_orig_data=data.PercentofOriginalData(:,:);
timegap=data.LargestTimeGapms(:,:);

mat=[conf timestep ave_error];

%Graph Error, % of Original Data, and Max. Timestep for each model
n=1;
for model=1:5
    switch model
        case 1
            name='tiny'; start_idx=1; end_idx=399;
        case 2
            name='small'; start_idx=400; end_idx=798;
        case 3
            name='medium'; start_idx=799; end_idx=1218;
        case 4
            name='large'; start_idx=1219; end_idx=1638;
        case 5
            name='full'; start_idx=1639; end_idx=2058;
    end
    
    figure(n);
    scatter3(mat(start_idx:end_idx,1),mat(start_idx:end_idx,2),mat(start_idx:end_idx,3))
    title(strcat('CREPE Output, Error, Model: ',name))
    xlabel('Confidence'); 
    ylabel('Timestep (ms)');
    zlabel('Ave. Error (cents)');

    figure(n+1);
    scatter3(mat(start_idx:end_idx,1),mat(start_idx:end_idx,2),percent_orig_data(start_idx:end_idx))
    title(strcat('CREPE Output, % of Original Data, Model: ',name))
    xlabel('Confidence'); 
    ylabel('Timestep (ms)');
    zlabel('% of Original Data');

    figure(n+2);
    scatter3(mat(start_idx:end_idx,1),mat(start_idx:end_idx,2),timegap(start_idx:end_idx))
    title(strcat('CREPE Output, Max. Time Gap, Model: ',name))
    xlabel('Confidence'); 
    ylabel('Timestep (ms)');
    zlabel('Max. Time Gap (ms)');
    n=n+3;
end
