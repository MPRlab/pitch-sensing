load('Summaryfull.mat');

conf=Summaryfull(:,3);
timestep=Summaryfull(:,4);
ave_error=Summaryfull(:,1);

mat=[conf timestep ave_error];

scatter3(mat(1:20,1),mat(1:20,2),mat(1:20,3));
hold on; grid on;
scatter3(mat(21:40,1),mat(21:40,2),mat(21:40,3));
scatter3(mat(41:60,1),mat(41:60,2),mat(41:60,3));
scatter3(mat(61:80,1),mat(61:80,2),mat(61:80,3));
scatter3(mat(81:100,1),mat(81:100,2),mat(81:100,3));
title('Tiny Model CREPE Ouput')
xlabel('Confidence'); 
ylabel('Timestep (ms)');
zlabel('Ave. Error (cents)');
legend('Timestep=1ms','Timestep=5ms','Timestep=10ms','Timestep=20ms','Timestep=50ms','Location','EastOutside');