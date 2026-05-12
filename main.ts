//  When your Player (grey heart) overlaps with a Cupid (red heart), the Cupid disappears and your Player heart grows
sprites.onOverlap(SpriteKind.Player, SpriteKind.Valentine, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy(effects.coolRadial, 1000)
    scaling.scaleByPixels(sprite, 120, ScaleDirection.Uniformly, ScaleAnchor.Middle)
})
//  When your Player (grey heart) overlaps with an Arrow, the Arrow disappears and your Player heart shrinks
sprites.onOverlap(SpriteKind.Player, SpriteKind.Arrow, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    music.play(music.melodyPlayable(music.wawawawaa), music.PlaybackMode.InBackground)
    otherSprite2.destroy(effects.coolRadial, 5000)
    scaling.scaleByPixels(sprite2, -1, ScaleDirection.Uniformly, ScaleAnchor.Middle)
})
//  Every 1.8 seconds a red heart appears on the screen shooting this number of arrows
game.onUpdateInterval(1800, function on_update_interval() {
    valentine.check_win_or_lose()
    valentine.set_win_lose_size(1200, -90)
    valentine.send_valentine(assets.image`
            cupid hearts
            `, 5, assets.image`
            arrow
            `)
})
