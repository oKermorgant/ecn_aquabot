from simple_launch import SimpleLauncher


def generate_launch_description():

    sl = SimpleLauncher(use_sim_time=True)
    sl.declare_arg('rviz', True)
    sl.declare_arg('manual', True)

    with sl.group(if_arg = 'rviz'):
        sl.rviz(sl.find('ecn_aquabot', 'config.rviz'))

    # TODO run gps2pose from aquabot_ekf pkg
    # and robot_localization with config file aquabot_ekf/ekf.yaml

    with sl.group(if_arg='manual'):
        sl.node('slider_publisher',
                arguments = [sl.find('ecn_aquabot', 'props.yaml')])

    return sl.launch_description()
