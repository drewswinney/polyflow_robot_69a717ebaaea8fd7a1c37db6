import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69a71ac6aaea8fd7a1c37dfb",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a71ac6aaea8fd7a1c37dfb",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a71b07aaea8fd7a1c37e50","source_node_id":"69a71adbaaea8fd7a1c37e12","source_pin_id":"rear_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69a71acdaaea8fd7a1c37e05",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a71acdaaea8fd7a1c37e05",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a71b06aaea8fd7a1c37e4d","source_node_id":"69a71adbaaea8fd7a1c37e12","source_pin_id":"front_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69a71ac7aaea8fd7a1c37e00",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a71ac7aaea8fd7a1c37e00",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a71b09aaea8fd7a1c37e53","source_node_id":"69a71adbaaea8fd7a1c37e12","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69a71ad8aaea8fd7a1c37e0c",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a71ad8aaea8fd7a1c37e0c",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a71b04aaea8fd7a1c37e4a","source_node_id":"69a71adbaaea8fd7a1c37e12","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="differential_drive",
            executable="differential_drive_node",
            name="differential_drive_n69a71adbaaea8fd7a1c37e12",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a71adbaaea8fd7a1c37e12",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"wheel_radius":0.05,"wheel_separation":0.3,"max_wheel_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c8e4b3f393789aad6f84:cmd_vel","name":"cmd_vel","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3c8e4b3f393789aad6f84:mode","name":"mode","direction":"input","msg_type":"polyflow_msgs/ModeState"},{"pin_id":"69a3c8e4b3f393789aad6f84:encoder_left","name":"encoder_left","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3c8e4b3f393789aad6f84:encoder_right","name":"encoder_right","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_left_motor","name":"front_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_left_motor","name":"rear_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_right_motor","name":"front_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_right_motor","name":"rear_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:odometry","name":"odometry","direction":"output","msg_type":"nav_msgs/Odometry"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a71af9aaea8fd7a1c37e3b","source_node_id":"69a71ae6aaea8fd7a1c37e24","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"},{"connection_id":"69a71afbaaea8fd7a1c37e3e","source_node_id":"69a71af3aaea8fd7a1c37e36","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"},{"connection_id":"69a71afdaaea8fd7a1c37e41","source_node_id":"69a71ae0aaea8fd7a1c37e1d","source_pin_id":"mode","target_pin_id":"mode"},{"connection_id":"69a71affaaea8fd7a1c37e44","source_node_id":"69a71aeaaaea8fd7a1c37e2a","source_pin_id":"encoder_state","target_pin_id":"encoder_left"},{"connection_id":"69a71b01aaea8fd7a1c37e47","source_node_id":"69a71aeeaaea8fd7a1c37e30","source_pin_id":"encoder_state","target_pin_id":"encoder_right"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a71b04aaea8fd7a1c37e4a","target_node_id":"69a71ad8aaea8fd7a1c37e0c","source_pin_id":"rear_right_motor","target_pin_id":"command"},{"connection_id":"69a71b06aaea8fd7a1c37e4d","target_node_id":"69a71acdaaea8fd7a1c37e05","source_pin_id":"front_right_motor","target_pin_id":"command"},{"connection_id":"69a71b07aaea8fd7a1c37e50","target_node_id":"69a71ac6aaea8fd7a1c37dfb","source_pin_id":"rear_left_motor","target_pin_id":"command"},{"connection_id":"69a71b09aaea8fd7a1c37e53","target_node_id":"69a71ac7aaea8fd7a1c37e00","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
            }
        ),
        Node(
            package="logger",
            executable="logger_node",
            name="logger_n69a71adeaaea8fd7a1c37e18",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a71adeaaea8fd7a1c37e18",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"log_file":"","log_to_stdout":true}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="mode_switcher",
            executable="mode_switcher_node",
            name="mode_switcher_n69a71ae0aaea8fd7a1c37e1d",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a71ae0aaea8fd7a1c37e1d",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"default_mode":"stopped","allowed_modes":["teleop","automated","stopped"]}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd36b3f393789aad7079:set_mode","name":"set_mode","direction":"input","msg_type":"polyflow_msgs/ModeCommand"},{"pin_id":"69a3cd36b3f393789aad7079:mode","name":"mode","direction":"output","msg_type":"polyflow_msgs/ModeState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a71afdaaea8fd7a1c37e41","target_node_id":"69a71adbaaea8fd7a1c37e12","source_pin_id":"mode","target_pin_id":"mode"}]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_n69a71aeaaaea8fd7a1c37e2a",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a71aeaaaea8fd7a1c37e2a",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c932b3f393789aad6fbc:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3c932b3f393789aad6fbc:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a71affaaea8fd7a1c37e44","target_node_id":"69a71adbaaea8fd7a1c37e12","source_pin_id":"encoder_state","target_pin_id":"encoder_left"}]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_n69a71aeeaaea8fd7a1c37e30",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a71aeeaaea8fd7a1c37e30",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c932b3f393789aad6fbc:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3c932b3f393789aad6fbc:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a71b01aaea8fd7a1c37e47","target_node_id":"69a71adbaaea8fd7a1c37e12","source_pin_id":"encoder_state","target_pin_id":"encoder_right"}]')),
            }
        ),
        Node(
            package="mission_runner",
            executable="mission_runner_node",
            name="mission_runner_n69a71af3aaea8fd7a1c37e36",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a71af3aaea8fd7a1c37e36",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"mission":[],"linear_speed":0.5,"angular_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":10,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a477bcc85549d8e55e27db:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a477bcc85549d8e55e27db:status","name":"status","direction":"output","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a71afbaaea8fd7a1c37e3e","target_node_id":"69a71adbaaea8fd7a1c37e12","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="gamepad",
            executable="gamepad_node",
            name="gamepad_n69a71ae6aaea8fd7a1c37e24",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a71ae6aaea8fd7a1c37e24",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"device_index":0,"poll_rate_hz":60,"deadzone":0.05,"max_linear_speed":1,"max_angular_speed":2}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":60,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c77bb3f393789aad6f62:axes","name":"axes","direction":"output","msg_type":"polyflow_msgs/GamepadAxes"},{"pin_id":"69a3c77bb3f393789aad6f62:buttons","name":"buttons","direction":"output","msg_type":"polyflow_msgs/GamepadButtons"},{"pin_id":"69a3c77bb3f393789aad6f62:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a71af9aaea8fd7a1c37e3b","target_node_id":"69a71adbaaea8fd7a1c37e12","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
    ])