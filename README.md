# ff7chthonicharmony

Chthonic Harmony is a "compatibility pack" mod for Final Fantasy 7 + 7th Heaven. Its main purpose is to resolve compatibility problems so that other mods play together nicely. It also adjusts some textures in popular mods to display correctly in the revised NTSC-J mode available in [this FFNx test build](https://github.com/ChthonVII/FFNx-NTSCJ/releases). How it works is:

- Chthonic Harmony contains a few files taken from other mods, modified as necessary; and
- You must set Chthonic Harmony to the highest priority in 7th Heaven so its versions of these files override those of all other mods.

**Changelog**

Version 1.0: Initial release

**Major Features at a Glance**

- 60fps fixes for Shinra Archaeology Cut
- 30fps FMVs from SYW Unified FMV with subtitles from Shinra Archaeology Cut
- Ninostyle chibi FMVs from CosmosFMV to force compatibility with SYW Unified FMV.
- SNES-style ESUI button glyphs for SNES-style xinput controllers like 8bitdo
- A new set of materia icons.
- Some avatars from ESUI and Finishing Touch color corrected to display correctly in NTSC-J mode.
- Some upscales and "traditional-style" backgrounds and intro videos, mostly borrowed from AavockESUI, to override other mods that change these too much in my opinion.

**Content Details and Credits**

- **Note:** Everything is optional. You can always choose to not use any feature of Chthonic Harmony that you don't like.
- **Note:** Assets that specify "NTSC-J mode" mean the revised NTSC-J mode that is presently only available in [this FFNx test build](https://github.com/ChthonVII/FFNx-NTSCJ/releases).
- Backgrounds
     - Prelude and Game Over upscales from AavockESUI by Aavock & Bonez.
     - Start Screen with Remake-style buster sword adapted by ChthonVII. Eight versions, selectable by SD or HD, with or without logo, and NTSC-J mode or uncorrected sRGB mode.
- FMVs
     - Traditional-style Eidos Logo from Grimmy's FMV Replacements. I'm unsure because it's not well documented, but the creator of this file might Shankifer. It appears to have been ripped/adapted from another Eidos game.
     - Traditional-style SquareSoft Logo from SYW Unified FMV by Satsuki Yatoshi.
     - 30fps FMVs from SYW Unified FMV by Satsuki Yatoshi with retranslated subtitles from Shinra Archaeology Cut by Odysseus, TurquioseHammer, Thestrifeisrife, *et al*. (Video subtitling and reencoding done by ChthonVII.)
          - Beta and demo versions of Opening FMV with SAC-translated text crawls.
          - Jenova E FMV with SAC-translated subtitles
          - Three versions of Ending2 FMV:
               - SAC retranslation of final release subtitles.
               - SAC translation of storyboard dialogue. (Upon reflection, I recommend this as the best option.)
               - A mix-n-match of both done by ChthonVII, with a one word added.
          - Ninostyle Chibi FMVs from CosmosFMV by Cosmos. (Overrides incompatibility with SYW Unified FMV.)
          - Upscaled "Five hundred years later..." overlay from AavockESUI by Aavock & Bonez.
- UI
     - "Potraits Borderless Cropped" avatars, adapting Tetsuya Nomura concept art, from Finishing Touch by Bonez. Two versions, NTSC-J mode or uncorrected sRGB mode.
     - NTSC-J mode color correction of mini-avatars from ESUI by Chrysalis, *et al*. (Same options as ESUI.)
     - SNES-style button glyphs for SNES-style xinput controllers like 8bitdo. Requires controller support enabled in ESUI. (Any choice will do, since the glyphs will be overridden.) Eight versions, selectable by bright/gradient ESUI font, NTSC-J mode or uncorrected sRGB mode, and normal or inverted A ↔ B buttons. (Only the button glyphs are color corrected for NTSC-J mode, the font glyphs are not.) Glyphs by Nintendo, adapted by ChthonVII.
     - "Crystal" materia icons by ChthonVII. For NTSC-J mode or sRGB mode. Must be used with ESUI (because the sprite sheet is shared with other things). The choice of materia icons in ESUI still affects the slot graphics -- "shiny materia" is recommended.
- SAC Fixes
     - Harmonize 60/30 FPS Gameplay by Vertex2995, Obesebear, and Kaldrasha with Shinra Archaeology Cut by Odysseus, TurquioseHammer, Thestrifeisrife, *et al*.
          - 60FPS fixes for field maps with FPS-sensitive puzzles/animations:
               - Fix incorrect train animation in Train Graveyard (mds7st2).
               - Fix timing for Cloud and Barret turning to face other characters on Shinra Building Floor 70 (blin70_2).
               - Reduce speed of gear animation in Nibel Reactor (nvmkin1). (Slightly wrong. The slowed down animation is effectively 20fps because there's no good way to do 30fps. Looks OK at 20fps.)
               - Slow down Shinra Mansion (sinin2_1) safe dial to 1 number per 3 frames, increase time limit to 1.5x. (Slightly wrong. 1 number per 2 frames would be correct, but there's no good way to do that.)
               - Halve clock move step size in Temple of the Ancients (kuro_4).
               - Fix the full-screen wind wall in Whirlwind Maze 1, 2, and 3 (woa_1, woa_2, and woa_3) to wax and wane at the correct pace.
               - Fix the cyclone in Whirlwind Maze 2 and 3 (woa_2 and woa_3) to display correctly, move at correct pace, and in sync graphics with its logical position. (As a side-effect of this fix, the cyclone no longer resets to its initial position if you mess up the puzzle and have to fight the battle. Instead it will continue on from the spot you collided with it.)
               - Fix the lightning strikes in Whirlwind Maze 3 (woa_3) to occur at the correct pace.
               - Note that you need a version of FFNx with [commit 3ab025d](https://github.com/julianxhokaxhiu/FFNx/commit/3ab025d91e6d5ba3e2407c5bb93754dfff700b7a) to fix a vanilla bug with the Whirlwind Maze puzzles. Without this fix, the graphics for the puzzles go out of sync with their logical positions whenever you fail the puzzle and have to fight a battle or enter the menu.
          - 60/30 FPS animations for the "Test" monster series restored in SAC.
     - Ninostyle battle models from Ninosyle Battle by NinoStyle, Tsunamix, and Shiniboy for Test 0 and Test 1 monsters restored in SAC.

