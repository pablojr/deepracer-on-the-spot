# Racing line using Waypoints

def reward_function(params):
    left = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 43, 44, 45, 46, 47, 48, 49, 50,
            51, 52, 53, 73, 74, 75, 76, 77, 78, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]
            
    centerleft = [34, 35, 36, 37, 38, 39, 40, 41, 42, 54, 71, 72, 79, 80, 86, 98, 99]
    
    centerright = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 26, 33, 55, 56, 70, 81, 100,
                   101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]

    right = [27, 28, 29, 30, 31, 32, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 82, 83, 84, 85]

# #####

    slow = [17, 18, 19, 20, 21, 22, 23, 24, 33, 47, 48, 49, 50, 51, 52, 53,
            54, 55, 63, 64, 65, 66, 67, 68, 69, 70, 76, 77, 78, 79, 80, 81,
            91, 92, 93, 94, 95, 96, 97, 98]

    medium = [14, 15, 16, 25, 26, 27, 28, 29, 31, 32, 34, 35, 36, 44, 45, 46,
              56, 57, 60, 61, 62, 71, 72, 73, 75, 82, 83, 84, 85, 86, 87, 89, 90, 99, 100, 101, 102]

    fast = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 30, 37, 38, 39, 40, 41,
            42, 43, 58, 59, 74, 88, 103, 104, 105, 106, 107, 108, 109, 110, 111]

    closest = params['closest_waypoints']
    nextwaypoint = max(closest[0], closest[1])

    if params['all_wheels_on_track'] == True:
        delta = params['distance_from_center']/params['track_width']

        if (nextwaypoint in centerleft):
            if (delta <= 0.25):
                reward = 14 if params['is_left_of_center'] else 0
            else:
                reward = -7
                
        elif (nextwaypoint in centerright):
            if (delta <= 0.25): 
                reward = 0 if params['is_left_of_center'] else 14
            else:
                reward = -7

        elif (nextwaypoint in left):
            if (params['is_left_of_center']) and (delta > 0.25 and delta < 0.48):
                reward = 14
            else:
                reward = -7
        elif (nextwaypoint in right):
            if (not params['is_left_of_center']) and (delta > 0.25 and delta < 0.48):
                reward = 14
            else:
                reward = -7

        if nextwaypoint in fast:
            if (params['speed'] == 3):
                reward += 14
            else:
                reward -= (5-params['speed'])**2
        elif nextwaypoint in medium:
            if (params['speed'] == 2):
                reward += 14
            else:
                reward -= 7
        elif nextwaypoint in slow:
            if (params['speed'] == 1):
                reward += 14
            else:
                reward -= (2 + params['speed'])**2
                
    else:
        reward = 0.001
    
    return float(reward)
