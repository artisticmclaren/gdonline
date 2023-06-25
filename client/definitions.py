import pygame
import levelgenerator

# blocks
id0="objs/0.png" # easter egg
id1="objs/1.png"
id2="objs/2.png" #waffle top block
id3="objs/3.png" #waffle corner block
id4="objs/4.png" #waffle corner fill
id5="objs/5.png" #waffle
id6="objs/6.png" #waffle pillar top
id7="objs/7.png" # waffle pillar sides
id8="objs/8.png" #default spike
id9="objs/9.png" #ground spike 1
id10="objs/10.png" #normal gravity portal
id11="objs/11.png" #upside down gravity portal
id12="objs/12.png" #cube portal
id13="objs/13.png" #ship portal
id16="objs/16.png" #pulse line deco
id18="objs/18.png" #fake ground spike 1
id19="objs/19.png" #fake ground spike 2
id20="objs/20.png" #fake ground spike 3
id21="objs/21.png" #fake ground spike 4
id29="objs/29.png" #bg trigger
id30="objs/30.png" #ground tigger
id35="objs/35.png" #yellow pad
id36="objs/36.png" #yellow orb
id39="objs/39.png" #squished spike
id40="objs/40.png" #slab
id41="objs/41.png" #chain deco
id45="objs/45.png" #mirror portal
id46="objs/46.png" # unmirror portal
id47="objs/47.png" # ball portal
id67="objs/67.png" # blue pad
id84="objs/84.png" #blue orb
id99="objs/99.png" #big portal
id101="objs/101.png" # mini portal
id111="objs/111.png" #ufo portal
id140="objs/140.png" #pink pad
id141="objs/141.png" #pink orb
id191="objs/191.png" #fake spike
id200="objs/200.png" #slow speed
id201="objs/201.png" # 1x speed
id202="objs/202.png" #2x speed
id203="objs/203.png" #3x speed
id286="objs/286.png" #dual portal
id287="objs/287.png" #normal portal
id660="objs/660.png" #wave portal

# bgs
bg1="bgs/game_bg_01_001-uhd.png"
bg2="bgs/game_bg_02_001-uhd.png"
bg3="bgs/game_bg_03_001-uhd.png"
bg4="bgs/game_bg_04_001-uhd.png"
bg5="bgs/game_bg_05_001-uhd.png"
bg6="bgs/game_bg_06_001-uhd.png"
bg7="bgs/game_bg_07_001-uhd.png"
bg8="bgs/game_bg_08_001-uhd.png"
bg9="bgs/game_bg_09_001-uhd.png"
bg10="bgs/game_bg_10_001-uhd.png"
bg11="bgs/game_bg_11_001-uhd.png"
bg12="bgs/game_bg_12_001-uhd.png"
bg13="bgs/game_bg_13_001-uhd.png"
bg14="bgs/game_bg_14_001-uhd.png"
bg15="bgs/game_bg_15_001-uhd.png"
bg16="bgs/game_bg_16_001-uhd.png"
bg17="bgs/game_bg_17_001-uhd.png"
bg18="bgs/game_bg_18_001-uhd.png"
bg19="bgs/game_bg_19_001-uhd.png"
bg20="bgs/game_bg_20_001-uhd.png"

# other
wico='icon.png'

# ui buttons
b1="ui/object selection/1.png"
b2="ui/object selection/2.png"
b3="ui/object selection/3.png"
b4="ui/object selection/4.png"
b5="ui/object selection/5.png"
b6="ui/object selection/6.png"
b7="ui/object selection/7.png"
b8="ui/object selection/8.png"
b9="ui/object selection/9.png"
b10="ui/object selection/10.png"
b11="ui/object selection/11.png"
b12="ui/object selection/12.png"
b13="ui/object selection/13.png"
b16="ui/object selection/16.png"
b18="ui/object selection/18.png"
b19="ui/object selection/19.png"
b20="ui/object selection/20.png"
b21="ui/object selection/21.png"
b29="ui/object selection/29.png"
b30="ui/object selection/30.png"
b35="ui/object selection/35.png"
b36="ui/object selection/36.png"
b39="ui/object selection/39.png"
b40="ui/object selection/40.png"
b41="ui/object selection/41.png"
b45="ui/object selection/45.png"
b46="ui/object selection/46.png"
b47="ui/object selection/47.png"
b67="ui/object selection/67.png"
b84="ui/object selection/84.png"
b99="ui/object selection/99.png"
b101="ui/object selection/101.png"
b111="ui/object selection/111.png"
b140="ui/object selection/140.png"
b141="ui/object selection/141.png"
b191="ui/object selection/191.png"
b200="ui/object selection/200.png"
b201="ui/object selection/201.png"
b202="ui/object selection/202.png"
b203="ui/object selection/203.png"
b286="ui/object selection/286.png"
b287="ui/object selection/287.png"

generate="ui/generate.png"
rl="ui/rleft.png"
rr="ui/rright.png"
lls="ui/lls.png"
help="ui/help.png"
ok="ui/ok.png"
empty="ui/emptybtn.png"
message="ui/message.png"

# add players
add="ui/addPlayer/add.png"
remove="ui/addPlayer/remove.png"
apbtn="ui/addPlayer/menubtn.png"


# ui other
triggerbg="ui/triggermenu.png"
triggerblack="ui/triggerunderlay.png"

# colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)