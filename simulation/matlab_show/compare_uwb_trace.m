 clear all
 close all

 kf_path = '/home/yong/workspace/2_project_files/A_single_anchor_imu_ekf/awesome-uwb-RangeTracker/simulation/kf_res.txt'
 kf_data = load(kf_path);

 figure
 plot(kf_data(:,1),kf_data(:,2),'b*');
 title('lab data')
 saveas(gcf,'lab_data','png');

 uwb_pose_path = '/home/yong/workspace/2_project_files/A_single_anchor_imu_ekf/awesome-uwb-RangeTracker/simulation/matlab_show/uwb_location_data.txt'
 uwb_localization_data = load(uwb_pose_path);
 figure
 plot(uwb_localization_data(:,2),uwb_localization_data(:,3),'r-');
 title('uwb_localization')
 saveas(gcf,'uwb_localization_data','png');
 
 wheel_path = '/home/yong/workspace/2_project_files/A_single_anchor_imu_ekf/awesome-uwb-RangeTracker/simulation/matlab_show/imu_wheel.txt'
 wheel_data = load(wheel_path);
 figure
 plot(wheel_data(:,2),wheel_data(:,3),'g.');
 title('wheel_trace');
 saveas(gcf,'wheel_data','png');
% 
% wheel_path_align_uwb_path = '/home/yong/workspace/2_project_files/A_single_anchor_imu_ekf/awesome-uwb-RangeTracker/simulation/matlab_show/one_anchor_distance_wheel_trace.txt';
% wheel_data_new = load(wheel_path_align_uwb_path);
% figure(4)
% plot(wheel_data_new(:,4),wheel_data_new(:,5));
% saveas(gcf,'wheel_data_new','png');
% 
 rtk_path = '/home/yong/workspace/2_project_files/A_single_anchor_imu_ekf/awesome-uwb-RangeTracker/simulation/matlab_show/rtk_converted_z_0_data.txt'
 rtk_data = load(rtk_path);
 figure
 plot(rtk_data(:,2),rtk_data(:,3),'k-');
 title('rtk_trace');
 saveas(gcf,'rtk_data','png');








