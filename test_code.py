def maneuver(veh_dist_feet):
	if veh_dist_feet >= 50:
		turn_left()
	else:
		wait()
