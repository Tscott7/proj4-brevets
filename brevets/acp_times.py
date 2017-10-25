"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """

    minimum_speed =[(0, 15), (200, 15), (400, 15), (600, 11.428), (1000, 13.333)]
    maximum_speed = [(200, 34), (400, 32), (600, 30), (1000, 28)]
    total_time = 0
    total_distance = 0
    for max_distance, max_speed in maximum_speed:
        if control_dist_km <= max_distance:
            leftovers = control_dist_km - total_distance
            total_time += (leftovers / max_speed)
            break
        else:
            total_time += (max_distance / max_speed)
            total_distance = max_distance
    total_time = round(total_time * 60)
    arw = arrow.get(brevet_start_time)
    arw = arw.shift(minutes=+total_time)
    return arw.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    minimum_speed =[(0, 15), (200, 15), (400, 15), (600, 11.428), (1000, 13.333)]
    maximum_speed = [(200, 34), (400, 32), (600, 30), (1000, 28)]
    overall_time = {200:13.5, 300:20, 400:27, 600:40, 1000:75}
    overall_time_tup = [[200, 13.5], [300, 20], [400, 27], [600, 40], [1000, 75]]
    total_time = 0
    total_distance = 0
    for min_distance, min_speed in minimum_speed:
        if control_dist_km <= min_distance:
            leftovers = control_dist_km - total_distance
            total_time += (leftovers / min_speed)
            break
        else:
            total_time += (min_distance / min_speed)
            total_distance = min_distance
    if control_dist_km in overall_time:
        total_time = overall_time[brevet_dist_km]
    for i in range(len(overall_time_tup)):
        if overall_time_tup[i][1] < total_time < (overall_time_tup[i][1] * 1.1):
            total_time = overall_time[brevet_dist_km]
    arw = arrow.get(brevet_start_time)
    arw = arw.shift(hours=+total_time)
    return arw.isoformat()
