PERMISSIONS = {
    'Create Instant Invite':    0x1,
    'Kick Members':             0x2,
    'Ban Members':              0x4,
    'Administrator':            0x8,

    'Manage Channels':          0x10,
    'Manage Server':            0x20,
    'Add Reactions':            0x40,
    'View Audit Log':           0x80,

    'Read Messages':            0x400, # Both 'Read Messages' and 'View Channel'
    'View Channel':             0x400, # are the same permission.
    'Send Messages':            0x800,

    'Send TTS Messages':        0x1000,
    'Manage Messages':          0x2000,
    'Embed Links':              0x4000,
    'Attach Files':             0x8000,

    'Read Message History':     0x10000,
    'Mention @everyone':        0x20000,
    'Use External Emojis':      0x40000,

    'Connect':                  0x100000,
    'Speak':                    0x200000,
    'Mute Members':             0x400000,
    'Defean Members':           0x800000,

    'Move Members':             0x1000000,
    'Use Voice Activity':       0x2000000,
    'Change Nickname':          0x4000000,
    'Manage Nicknames':         0x8000000,

    'Manage Roles':             0x10000000,
    'Manage Webhooks':          0x20000000,
    'Manage Emojis':            0x40000000,
}

def translate(value):
    """converts 32-bit integer value to list of permission names"""
    plist = []
    for key in PERMISSIONS:
        if value & PERMISSIONS[key]:
            plist.append(key)
    return plist
