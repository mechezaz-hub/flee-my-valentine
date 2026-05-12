# When your Player (grey heart) overlaps with a Cupid (red heart), the Cupid disappears and your Player heart grows

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.cool_radial, 1000)
    scaling.scale_by_pixels(sprite, 120, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
sprites.on_overlap(SpriteKind.player, SpriteKind.valentine, on_on_overlap)

# When your Player (grey heart) overlaps with an Arrow, the Arrow disappears and your Player heart shrinks

def on_on_overlap2(sprite2, otherSprite2):
    music.play(music.melody_playable(music.wawawawaa),
        music.PlaybackMode.IN_BACKGROUND)
    otherSprite2.destroy(effects.cool_radial, 5000)
    scaling.scale_by_pixels(sprite2, -1, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
sprites.on_overlap(SpriteKind.player, SpriteKind.arrow, on_on_overlap2)

# Every 1.8 seconds a red heart appears on the screen shooting this number of arrows

def on_update_interval():
    valentine.check_win_or_lose()
    valentine.set_win_lose_size(1200, -90)
    valentine.send_valentine(assets.image("""
            cupid hearts
            """),
        5,
        assets.image("""
            arrow
            """))
game.on_update_interval(1800, on_update_interval)
