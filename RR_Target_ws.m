load('RR.mat');
SIM_G=G;
SIM_INITAL_ALT=0; %ft
SIM_INITAL_VEL=15; %ft/s
SIM_INITAL_PITCH=90; %deg
% SIM_LAUNCH=2000; %ft
% SIM_CRUISE=0.5; % mach
SIM_TARGET_ALT=-20000; %ft
SIM_TARGET_X=5000; %ft
SIM_TARGET_VEL=convvel(290,'kts','ft/s'); %/ft/s