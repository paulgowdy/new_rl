import numpy as np


def process_obs_dict(obs_dict):

	obs = []

	obs.extend(obs_dict['misc']['mass_center_pos']) # x, y, z
	obs.extend(obs_dict['misc']['mass_center_vel']) # x, y, z
	obs.extend(obs_dict['misc']['mass_center_acc']) # x, y, z

	# Absolute Joint Positions
	obs.extend(obs_dict['joint_pos']['ground_pelvis'])

	obs.extend(obs_dict['joint_pos']['hip_r'])
	obs.extend(obs_dict['joint_pos']['knee_r'])
	obs.extend(obs_dict['joint_pos']['ankle_r'])

	obs.extend(obs_dict['joint_pos']['hip_l'])
	obs.extend(obs_dict['joint_pos']['knee_l'])
	obs.extend(obs_dict['joint_pos']['ankle_l'])

	obs.extend(obs_dict['joint_vel']['ground_pelvis'])

	obs.extend(obs_dict['joint_vel']['hip_r'])
	obs.extend(obs_dict['joint_vel']['knee_r'])
	obs.extend(obs_dict['joint_vel']['ankle_r'])

	obs.extend(obs_dict['joint_vel']['hip_l'])
	obs.extend(obs_dict['joint_vel']['knee_l'])
	obs.extend(obs_dict['joint_vel']['ankle_l'])

	# Absolute Joint Acc

	obs.extend(obs_dict['joint_acc']['ground_pelvis'])

	obs.extend(obs_dict['joint_acc']['hip_r'])
	obs.extend(obs_dict['joint_acc']['knee_r'])
	obs.extend(obs_dict['joint_acc']['ankle_r'])

	obs.extend(obs_dict['joint_acc']['hip_l'])
	obs.extend(obs_dict['joint_acc']['knee_l'])
	obs.extend(obs_dict['joint_acc']['ankle_l'])

	b = ['body_pos', 'body_vel', 'body_acc']
	parts = ['pelvis', 'femur_r', 'pros_tibia_r', 'pros_foot_r', 'femur_l', 'tibia_l', 'talus_l', 'calcn_l', 'toes_l', 'torso', 'head']

	for i in b:

		for j in parts:

			obs.extend(obs_dict[i][j])











	return np.array(obs)