# pure pursuit - scottpletcher

def reward_function(params):
    reward = 1e-3

    rabbit = [0,0]
    pointing = [0,0]

    # Reward when yaw (car_orientation) is pointed to the next waypoint IN FRONT.
    # Find nearest waypoint coordinates
    waypoints = params['waypoints']
    closest_waypoint_front = params['closest_waypoints'][1]

    rabbit = [waypoints[closest_waypoint_front][0], waypoints[closest_waypoint_front][1]]
    radius = math.hypot(x - rabbit[0], y - rabbit[1])

    car_orientation = params['heading']
    pointing[0] = x + (radius * math.cos(car_orientation))
    pointing[1] = y + (radius * math.sin(car_orientation))

    vector_delta = math.hypot(pointing[0] - rabbit[0], pointing[1] - rabbit[1])
                                                                                                                                             if vector_delta == 0:
        reward += 1
    else:
        reward += ( 1 - ( vector_delta / (radius * 2)))

    return reward

