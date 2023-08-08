"""
Add spectators table
"""

from yoyo import step

__depends__ = {'20230801_01_3K32i'}

steps = [
    step(
        (
            'CREATE TABLE spectators(\n'
            '    guild_id BIGINT REFERENCES guilds (id) ON DELETE CASCADE,\n'
            '    user_id BIGINT REFERENCES users (discord_id) ON DELETE CASCADE,\n'
            '    CONSTRAINT spectator_pkey PRIMARY KEY (guild_id, user_id)\n'
            ');'
        ),
        'DROP TABLE spectators;'
    )
]
