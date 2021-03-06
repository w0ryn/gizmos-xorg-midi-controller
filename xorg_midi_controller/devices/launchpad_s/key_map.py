from xorg_midi_controller.devices.binding import create_action_binding

from xorg_midi_controller.devices.launchpad_s.byte_map import ByteMap
C = ByteMap.Values.Colors


def set_key_map(Device):
    XORG = Device.XORG
    XKEYS = XORG.Keys
    PA = Device.PULSE_AUDIO

    action_callback = Device.color_button

    def bind(action, ignore_keyup=False, ignore_callback=False, **kwargs):
        return create_action_binding(
                action = action,
                action_condition = lambda b: not ignore_keyup or XORG.is_keydown(b),
                callback = None if ignore_callback else action_callback,
                **kwargs,
                )

    def bind_volume_slider(level, pulse_device_index):
        return bind(
                action=Device.level_volume_control,
                level=level,
                pulse_device_index=pulse_device_index,
                ignore_keyup=True,
                ignore_callback=True,
                )

    def bind_toggle_mute(pulse_device_index):
        signal_handler = lambda _b, pulse_device_index: PA.toggle_mute(pulse_device_index=pulse_device_index)
        return bind(
                action=signal_handler,
                pulse_device_index=pulse_device_index,
                ignore_keyup=True,
                ignore_callback=True,
                )

    Device.KEY_BINDINGS = {
            # --- misc. bindings --------------------------------------------
            # col 1
            '0'   : bind(XORG.bind_mouse),
            '16'  : bind(XORG.bind_mouse),
            '32'  : bind(XORG.bind_mouse),
            '48'  : bind(XORG.bind_mouse),
            # col 2
            '1'   : bind(XORG.bind_mouse, mouse_key='3'),
            '17'  : bind(XORG.bind_mouse, mouse_key='3'),
            '33'  : bind(XORG.bind_mouse, mouse_key='3'),
            '49'  : bind(XORG.bind_mouse, mouse_key='3'),
            # col 3
            #'2'   : ,
            #'18'  : ,
            #'34'  : ,
            #'50'  : ,
            # col 4
            #'3'   : ,
            #'19'  : ,
            #'35'  : ,
            #'51'  : ,
            # col 5
            #'4'   : ,
            #'20'  : ,
            #'36'  : ,
            #'52'  : ,
            # col 6
            #'5'   : ,
            #'21'  : ,
            #'37'  : ,
            #'53'  : ,
            # col 7
            #'6'   : ,
            #'22'  : ,
            #'38'  : ,
            #'54'  : ,
            # col 8
            #'7'   : ,
            #'23'  : ,
            #'39'  : ,
            #'55'  : ,
            # col 9
            '8'   : bind(XORG.bind_mouse, ignore_keyup=True),
            '24'  : bind(XORG.bind_mouse, ignore_keyup=True, mouse_key='3'),
            '40'  : bind(XORG.bind_key, key_name='w', ignore_keyup=True),
            #'56'  : ,
            # --- default source volume slider ------------------------------
            '80'  : bind_volume_slider(level=0, pulse_device_index=1),
            '64'  : bind_volume_slider(level=0, pulse_device_index=1),
            '81'  : bind_volume_slider(level=1, pulse_device_index=1),
            '65'  : bind_volume_slider(level=1, pulse_device_index=1),
            '82'  : bind_volume_slider(level=2, pulse_device_index=1),
            '66'  : bind_volume_slider(level=2, pulse_device_index=1),
            '83'  : bind_volume_slider(level=3, pulse_device_index=1),
            '67'  : bind_volume_slider(level=3, pulse_device_index=1),
            '84'  : bind_volume_slider(level=4, pulse_device_index=1),
            '68'  : bind_volume_slider(level=4, pulse_device_index=1),
            '85'  : bind_volume_slider(level=5, pulse_device_index=1),
            '69'  : bind_volume_slider(level=5, pulse_device_index=1),
            '86'  : bind_volume_slider(level=6, pulse_device_index=1),
            '70'  : bind_volume_slider(level=6, pulse_device_index=1),
            '87'  : bind_volume_slider(level=7, pulse_device_index=1),
            '71'  : bind_volume_slider(level=7, pulse_device_index=1),
            '88'  : bind_volume_slider(level=8, pulse_device_index=1),
            '72'  : bind_toggle_mute(pulse_device_index=1),
            # --- default sink volume slider --------------------------------
            '96'  : bind_volume_slider(level=0, pulse_device_index=0),
            '112' : bind_volume_slider(level=0, pulse_device_index=0),
            '97'  : bind_volume_slider(level=1, pulse_device_index=0),
            '113' : bind_volume_slider(level=1, pulse_device_index=0),
            '98'  : bind_volume_slider(level=2, pulse_device_index=0),
            '114' : bind_volume_slider(level=2, pulse_device_index=0),
            '99'  : bind_volume_slider(level=3, pulse_device_index=0),
            '115' : bind_volume_slider(level=3, pulse_device_index=0),
            '100' : bind_volume_slider(level=4, pulse_device_index=0),
            '116' : bind_volume_slider(level=4, pulse_device_index=0),
            '101' : bind_volume_slider(level=5, pulse_device_index=0),
            '117' : bind_volume_slider(level=5, pulse_device_index=0),
            '102' : bind_volume_slider(level=6, pulse_device_index=0),
            '118' : bind_volume_slider(level=6, pulse_device_index=0),
            '103' : bind_volume_slider(level=7, pulse_device_index=0),
            '119' : bind_volume_slider(level=7, pulse_device_index=0),
            '104' : bind_volume_slider(level=8, pulse_device_index=0),
            '120' : bind_toggle_mute(pulse_device_index=0),
            }

    Device.AUTOMAP_BINDINGS = {
            'default' : action_callback,
            '104' : bind(XORG.bind_key, key_name=XKEYS.NUM_LOCK, ignore_callback=True),
            '105' : bind(XORG.bind_key, key_name=XKEYS.CAPS_LOCK, ignore_callback=True),
            #'106' :,
            '107' : bind(XORG.bind_key, key_name=XKEYS.MEDIA_PREV),
            '108' : bind(XORG.bind_key, key_name=XKEYS.MEDIA_PLAY),
            '109' : bind(XORG.bind_key, key_name=XKEYS.MEDIA_NEXT),
            #'110' :,
            '111' : bind(lambda _b: PA.restart(), ignore_keyup=True),
            }

    Device.FLASH_MAP = {
            '72': True,
            }

    Device.COLOR_MAP = {
        'default': [C.BRIGHT_RED, C.DIM_RED],

        '0'   : [C.BRIGHT_ORANGE, C.MEDIUM_ORANGE],
        '16'  : [C.BRIGHT_ORANGE, C.MEDIUM_ORANGE],
        '32'  : [C.BRIGHT_ORANGE, C.MEDIUM_ORANGE],
        '48'  : [C.BRIGHT_ORANGE, C.MEDIUM_ORANGE],
        '1'   : [C.BRIGHT_ORANGE, C.MEDIUM_RED],
        '17'  : [C.BRIGHT_ORANGE, C.MEDIUM_RED],
        '33'  : [C.BRIGHT_ORANGE, C.MEDIUM_RED],
        '49'  : [C.BRIGHT_ORANGE, C.MEDIUM_RED],

        '8'   : [C.BRIGHT_RED, C.MEDIUM_GREEN],
        '24'  : [C.BRIGHT_RED, C.MEDIUM_AMBER],
        '40'  : [C.BRIGHT_RED, C.MEDIUM_RED],

        'automap' : {
            'default': [C.YELLOW_GREEN, C.DIM_GREEN],

            '104': [C.BRIGHT_GREEN, C.MEDIUM_YELLOW],
            '105': [C.BRIGHT_AMBER, C.MEDIUM_YELLOW],

            '107': [C.BRIGHT_ORANGE, C.MEDIUM_AMBER],
            '108': [C.BRIGHT_ORANGE, C.MEDIUM_YELLOW],
            '109': [C.BRIGHT_ORANGE, C.MEDIUM_AMBER],

            '111': [C.BRIGHT_RED, C.MEDIUM_ORANGE],
            },

        'source' : {
            'no-volume': C.BRIGHT_AMBER,
            'toggle': [C.BRIGHT_RED, C.DIM_AMBER],
            'levels': [
                C.MEDIUM_RED, C.MEDIUM_RED,
                C.MEDIUM_AMBER, C.MEDIUM_AMBER, C.MEDIUM_AMBER,
                C.BRIGHT_AMBER, C.BRIGHT_AMBER,
                C.BRIGHT_YELLOW, C.BRIGHT_YELLOW,
                ],
            },

        'sink' : {
            'no-volume': C.BRIGHT_RED,
            'toggle': [C.BRIGHT_GREEN, C.DIM_GREEN],
            'levels': [
                C.BRIGHT_GREEN, C.BRIGHT_GREEN, C.BRIGHT_GREEN,
                C.YELLOW_GREEN, C.YELLOW_GREEN,
                C.BRIGHT_YELLOW,
                C.BRIGHT_RED, C.BRIGHT_RED, C.BRIGHT_RED,
                ],
            },
        }
