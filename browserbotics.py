import time, math
import browserbotics as bb

bb.setGravity(0, 0, -9.8)
bb.addGroundPlane()

body_count = 0
def safe_body(shape, halfExtent, position, color, mass=0):
    global body_count
    b = bb.createBody(shape=shape, halfExtent=halfExtent,
                      position=position, color=color, mass=mass)
    body_count += 1
    if body_count % 4 == 0:
        time.sleep(0.3)
    return b

# ═══════════════════════════════════════
# ONE BIG OPEN ROOM
# ═══════════════════════════════════════
safe_body('box',[3.5,8.0,0.05],[0,-4.5,-0.05],0xE8E8E8)
safe_body('box',[0.1,8.0,1.5],[-3.5,-4.5,1.5],0xDDEEFF)
safe_body('box',[0.1,8.0,1.5],[3.5,-4.5,1.5],0xDDEEFF)
safe_body('box',[3.5,0.1,1.5],[0,3.0,1.5],0xDDEEFF)
safe_body('box',[3.5,0.1,1.5],[0,-12.0,1.5],0xDDEEFF)
safe_body('box',[1.0,0.1,1.5],[-2.5,-3.0,1.5],0xDDEEFF)
safe_body('box',[1.0,0.1,1.5],[2.5,-3.0,1.5],0xDDEEFF)
safe_body('box',[1.0,0.1,0.4],[0,-3.0,2.6],0xDDEEFF)
safe_body('box',[0.06,0.08,1.0],[-1.0,-2.95,1.0],0xC8A870)
safe_body('box',[0.06,0.08,1.0],[1.0,-2.95,1.0],0xC8A870)
safe_body('box',[1.06,0.08,0.06],[0,-2.95,2.06],0xC8A870)
safe_body('box',[3.5,0.04,0.01],[0,-6.0,0.0],0xAAAAAA)

# lights
light1  = safe_body('box',[1.2,0.1,0.02],[0,0,2.98],0xFFFBCC)
safe_body('box',[0.02,0.02,0.25],[0,0,2.75],0x888888)
light2  = safe_body('box',[1.2,0.1,0.02],[0,-9.0,2.98],0xFFFBCC)
safe_body('box',[0.02,0.02,0.25],[0,-9.0,2.75],0x888888)
light3  = safe_body('box',[0.40,0.40,0.05],[0.5,0.2,2.85],0xCCCCCC)
light3s = safe_body('box',[0.35,0.35,0.02],[0.5,0.2,2.80],0xFFFFDD)
safe_body('box',[0.02,0.02,0.20],[0.5,0.2,2.70],0x888888)

# wall monitor
safe_body('box',[0.5,0.05,0.35],[3.4,2.5,1.8],0x111122)
safe_body('box',[0.45,0.02,0.30],[3.4,2.5,1.8],0x00CCFF)
safe_body('box',[0.02,0.02,0.40],[3.4,2.5,1.2],0x888888)
time.sleep(0.5)
print("open room ok")

# ═══════════════════════════════════════
# OXYGEN CYLINDER
# ═══════════════════════════════════════
OX,OY = -3.0, 1.5
safe_body('box',[0.14,0.14,0.03],[OX,OY,0.03],0x333333)
safe_body('box',[0.09,0.09,0.55],[OX,OY,0.58],0x226622)
safe_body('box',[0.07,0.07,0.10],[OX,OY,1.16],0x226622)
safe_body('box',[0.04,0.04,0.07],[OX,OY,1.29],0x444444)
safe_body('box',[0.07,0.07,0.05],[OX,OY,1.38],0xBB2222)
safe_body('box',[0.10,0.015,0.015],[OX,OY,1.44],0x888888)
safe_body('box',[0.04,0.04,0.04],[OX+0.07,OY,1.35],0xCCCCCC)
safe_body('box',[0.05,0.05,0.06],[OX,OY-0.06,1.25],0x555555)
safe_body('box',[0.012,0.012,0.40],[OX+0.04,OY-0.04,0.85],0x44BB44)
safe_body('box',[0.015,0.10,0.03],[OX-0.10,OY,0.80],0x444444)
safe_body('box',[0.015,0.10,0.03],[OX-0.10,OY,1.10],0x444444)
time.sleep(0.4)
print("oxygen ok")

# ═══════════════════════════════════════
# BED — adjustable
# ═══════════════════════════════════════
BED_X, BED_Y = 0.5, 0.0
bed_parts     = []
patient_parts = []

def build_bed(bz):
    global bed_parts
    for b in bed_parts:
        try: bb.resetBasePose(b,[99,99,-5],[0,0,0,1])
        except: pass
    bed_parts = []
    lh = bz/2.0
    bed_parts.append(safe_body('box',[0.04,0.04,lh],[BED_X+0.60,-0.60,lh],0x777788))
    bed_parts.append(safe_body('box',[0.04,0.04,lh],[BED_X+0.60, 0.60,lh],0x777788))
    bed_parts.append(safe_body('box',[0.04,0.04,lh],[BED_X-0.60,-0.60,lh],0x777788))
    bed_parts.append(safe_body('box',[0.04,0.04,lh],[BED_X-0.60, 0.60,lh],0x777788))
    bed_parts.append(safe_body('box',[0.06,0.06,0.04],[BED_X+0.60,-0.60,0.04],0x222222))
    bed_parts.append(safe_body('box',[0.06,0.06,0.04],[BED_X+0.60, 0.60,0.04],0x222222))
    bed_parts.append(safe_body('box',[0.06,0.06,0.04],[BED_X-0.60,-0.60,0.04],0x222222))
    bed_parts.append(safe_body('box',[0.06,0.06,0.04],[BED_X-0.60, 0.60,0.04],0x222222))
    bed_parts.append(safe_body('box',[0.65,0.65,0.04],[BED_X,BED_Y,bz+0.02],0x555566))
    bed_parts.append(safe_body('box',[0.60,0.62,0.07],[BED_X,BED_Y,bz+0.09],0x1A1A2A))
    bed_parts.append(safe_body('box',[0.58,0.60,0.015],[BED_X,BED_Y,bz+0.175],0xF5F5F5))
    bed_parts.append(safe_body('box',[0.22,0.26,0.045],[BED_X,BED_Y+0.52,bz+0.205],0xFFFFFF))
    bed_parts.append(safe_body('box',[0.65,0.04,0.28],[BED_X,BED_Y+0.68,bz+0.24],0x333344))
    bed_parts.append(safe_body('box',[0.65,0.04,0.18],[BED_X,BED_Y-0.68,bz+0.14],0x333344))
    bed_parts.append(safe_body('box',[0.55,0.015,0.08],[BED_X,BED_Y+0.63,bz+0.22],0x888899))
    bed_parts.append(safe_body('box',[0.55,0.015,0.08],[BED_X,BED_Y-0.63,bz+0.22],0x888899))

def build_patient(bz):
    global patient_parts
    for b in patient_parts:
        try: bb.resetBasePose(b,[99,99,-5],[0,0,0,1])
        except: pass
    patient_parts = []
    pz = bz + 0.19
    patient_parts.append(safe_body('box',[0.14,0.38,0.06],[BED_X,-0.12,pz+0.04],0xF5F5F5))
    patient_parts.append(safe_body('box',[0.13,0.15,0.07],[BED_X, 0.20,pz+0.05],0xF5C5A0))
    patient_parts.append(safe_body('box',[0.13,0.15,0.02],[BED_X, 0.20,pz+0.13],0x88BBEE))
    patient_parts.append(safe_body('box',[0.04,0.20,0.03],[BED_X, 0.10,pz+0.02],0xF5C5A0))
    patient_parts.append(safe_body('box',[0.04,0.04,0.055],[BED_X,0.39,pz+0.09],0xF5C5A0))
    patient_parts.append(safe_body('box',[0.09,0.09,0.09],[BED_X, 0.50,pz+0.14],0xF5C5A0))
    patient_parts.append(safe_body('box',[0.09,0.09,0.02],[BED_X, 0.50,pz+0.24],0x221100))
    patient_parts.append(safe_body('box',[0.02,0.01,0.02],[BED_X-0.09,0.44,pz+0.17],0x222222))
    patient_parts.append(safe_body('box',[0.02,0.01,0.02],[BED_X+0.09,0.44,pz+0.17],0x222222))

current_bz = 0.45
last_bz    = current_bz
build_bed(current_bz)
time.sleep(0.5)

# IV stand
safe_body('box',[0.02,0.02,0.90],[-0.4,0.55,0.90],0xCCCCCC)
safe_body('box',[0.13,0.02,0.02],[-0.4,0.55,1.75],0xCCCCCC)
safe_body('box',[0.04,0.02,0.08],[-0.29,0.55,1.83],0x44DDF0)
# medicine table
safe_body('box',[0.22,0.18,0.33],[1.55,0.75,0.33],0x7AAEDD)
safe_body('box',[0.22,0.18,0.02],[1.55,0.75,0.68],0xF5F5F5)
medicine_drop_pos = [1.55,0.75,0.76]
build_patient(current_bz)
time.sleep(0.5)
print("bed + patient ok")

# ═══════════════════════════════════════
# HUMAN OPERATOR
# ═══════════════════════════════════════
safe_body('box',[0.22,0.22,0.02],[-2.2,-1.5,0.44],0x222222)
safe_body('box',[0.22,0.04,0.28],[-2.2,-1.28,0.72],0x222222)
for cx,cy in [(-2.38,-1.68),(-2.02,-1.68),(-2.38,-1.32),(-2.02,-1.32)]:
    safe_body('box',[0.03,0.03,0.44],[cx,cy,0.22],0x111111)
safe_body('box',[0.40,0.25,0.02],[-2.2,-1.0,0.75],0x886644)
safe_body('box',[0.03,0.03,0.75],[-2.5,-1.2,0.37],0x664422)
safe_body('box',[0.03,0.03,0.75],[-1.9,-1.2,0.37],0x664422)
safe_body('box',[0.28,0.03,0.20],[-2.2,-0.77,1.05],0x111111)
safe_body('box',[0.25,0.01,0.17],[-2.2,-0.76,1.05],0x0088FF)
safe_body('box',[0.15,0.08,0.01],[-2.2,-0.95,0.77],0x222222)
safe_body('box',[0.14,0.10,0.22],[-2.2,-1.45,0.78],0x3355AA)
safe_body('box',[0.14,0.18,0.06],[-2.2,-1.55,0.53],0x223388)
safe_body('box',[0.04,0.04,0.07],[-2.2,-1.45,1.07],0xF5C5A0)
safe_body('box',[0.10,0.10,0.12],[-2.2,-1.42,1.24],0xF5C5A0)
safe_body('box',[0.10,0.10,0.03],[-2.2,-1.42,1.37],0x221100)
safe_body('box',[0.04,0.18,0.04],[-2.32,-1.16,0.82],0x3355AA)
safe_body('box',[0.04,0.18,0.04],[-2.08,-1.16,0.82],0x3355AA)
safe_body('box',[0.05,0.06,0.02],[-2.32,-0.97,0.78],0xF5C5A0)
safe_body('box',[0.05,0.06,0.02],[-2.08,-0.97,0.78],0xF5C5A0)
time.sleep(0.5)
print("operator ok")

# ═══════════════════════════════════════
# PHARMACY ROOM
# ═══════════════════════════════════════
R2X,R2Y = 0.0,-9.0
safe_body('box',[3.4,3.0,0.02],[R2X,R2Y,-0.03],0xC8D4B0)
safe_body('box',[0.1,1.2,0.9],[R2X+3.0,R2Y,0.9],0xAA8855)
safe_body('box',[0.1,1.2,0.02],[R2X+3.0,R2Y,0.45],0xAA8855)
safe_body('box',[0.1,1.2,0.02],[R2X+3.0,R2Y,0.90],0xAA8855)
safe_body('box',[0.1,1.2,0.02],[R2X+3.0,R2Y,1.35],0xAA8855)
for i,c in enumerate([0xFF4444,0x4444FF,0x44CC44,0xFFAA00,0xFF44AA,0x00CCFF]):
    sy=R2Y-0.5+(i%3)*0.5; sz=0.56 if i<3 else 1.01
    safe_body('box',[0.04,0.04,0.08],[R2X+2.88,sy,sz],c)
PH_X,PH_Y = R2X,R2Y-1.5
safe_body('box',[0.4,0.3,0.38],[PH_X,PH_Y,0.38],0x6688AA)
safe_body('box',[0.4,0.3,0.02],[PH_X,PH_Y,0.78],0xF0F0F0)
time.sleep(0.5)
print("pharmacy ok")

# ═══════════════════════════════════════
# OBJECTS
# ═══════════════════════════════════════
medicine = safe_body('box',[0.09,0.07,0.05],[PH_X,PH_Y,0.86],0x00CC88)
syringe  = safe_body('box',[0.015,0.015,0.09],[-0.5,-1.2,1.5],0xCCEEFF)
time.sleep(0.3)

# ═══════════════════════════════════════
# VACUUM ROBOT
# ═══════════════════════════════════════
vac_body  = safe_body('box',[0.20,0.20,0.06],[-2.5,-2.5,0.06],0x111111,mass=1)
safe_body('box',[0.14,0.14,0.04],[-2.5,-2.5,0.14],0x333333)
safe_body('box',[0.04,0.03,0.03],[-2.5,-2.7,0.09],0x0088FF)
vac_brush = safe_body('box',[0.18,0.02,0.01],[-2.5,-2.5,0.01],0x00CC44)
time.sleep(0.3)
print("vacuum ok")

# ═══════════════════════════════════════
# DA VINCI SURGICAL ROBOT
# full 3-axis movement: X side, Y forward, Z height
# ═══════════════════════════════════════
DV_X, DV_Y_BASE = -1.4, 0.0

# fixed base (never moves)
safe_body('box',[0.25,0.25,0.05],[DV_X,DV_Y_BASE,0.05],0x222233)
safe_body('box',[0.14,0.14,0.80],[DV_X,DV_Y_BASE,0.85],0x334455)

# movable upper body — all tracked
dv_col_upper = safe_body('box',[0.12,0.12,0.60],[DV_X,DV_Y_BASE,1.70],0x445566)
dv_col_cap   = safe_body('box',[0.18,0.18,0.06],[DV_X,DV_Y_BASE,2.33],0x334455)
dv_boom      = safe_body('box',[0.55,0.08,0.06],[-0.85,DV_Y_BASE,2.28],0x445566)
dv_drop      = safe_body('box',[0.06,0.06,0.30],[-0.30,DV_Y_BASE,2.10],0x556677)
dv_hub       = safe_body('box',[0.16,0.16,0.08],[-0.30,DV_Y_BASE,1.82],0x667788)
dv_arm1s     = safe_body('box',[0.04,0.04,0.35],[-0.45,-0.28,1.60],0x778899)
dv_arm1e     = safe_body('box',[0.03,0.10,0.03],[-0.45,-0.28,1.26],0x778899)
scalpel      = safe_body('box',[0.007,0.007,0.08],[-0.45,-0.30,1.14],0xEEEEFF)
dv_arm2s     = safe_body('box',[0.04,0.04,0.35],[-0.15,-0.28,1.60],0x778899)
dv_arm2e     = safe_body('box',[0.03,0.10,0.03],[-0.15,-0.28,1.26],0x778899)
cauterizer   = safe_body('box',[0.012,0.012,0.07],[-0.15,-0.30,1.14],0xFF7700)
dv_arm3s     = safe_body('box',[0.04,0.04,0.40],[-0.30, 0.10,1.60],0x778899)
dv_arm3e     = safe_body('box',[0.06,0.06,0.06],[-0.30, 0.10,1.22],0x1133BB)
cam_arm      = safe_body('box',[0.04,0.04,0.05],[-0.30, 0.10,1.14],0x2244CC)
dv_arm4s     = safe_body('box',[0.04,0.04,0.32],[-0.15, 0.28,1.63],0x778899)
dv_arm4e     = safe_body('box',[0.03,0.10,0.03],[-0.15, 0.28,1.33],0x778899)
retractor    = safe_body('box',[0.014,0.014,0.06],[-0.15, 0.30,1.20],0x88FF44)
time.sleep(0.4)

# surgeon console
safe_body('box',[0.45,0.30,0.55],[-2.0,2.0,0.55],0x1A1A2E)
safe_body('box',[0.38,0.03,0.28],[-2.0,1.72,1.45],0x0033AA)
safe_body('box',[0.36,0.01,0.26],[-2.0,1.73,1.45],0x00AAFF)
safe_body('box',[0.08,0.06,0.06],[-2.12,1.75,1.22],0x111111)
safe_body('box',[0.08,0.06,0.06],[-1.88,1.75,1.22],0x111111)
safe_body('box',[0.06,0.06,0.14],[-2.22,1.85,1.08],0x333344)
safe_body('box',[0.06,0.06,0.14],[-1.78,1.85,1.08],0x333344)
time.sleep(0.5)
print("da vinci ok")

# reference positions for all movable upper parts
DV_UPPER_PARTS = [
    (dv_col_upper, [DV_X,   0.00, 1.70]),
    (dv_col_cap,   [DV_X,   0.00, 2.33]),
    (dv_boom,      [-0.85,  0.00, 2.28]),
    (dv_drop,      [-0.30,  0.00, 2.10]),
    (dv_hub,       [-0.30,  0.00, 1.82]),
    (dv_arm1s,     [-0.45, -0.28, 1.60]),
    (dv_arm1e,     [-0.45, -0.28, 1.26]),
    (dv_arm2s,     [-0.15, -0.28, 1.60]),
    (dv_arm2e,     [-0.15, -0.28, 1.26]),
    (dv_arm3s,     [-0.30,  0.10, 1.60]),
    (dv_arm3e,     [-0.30,  0.10, 1.22]),
    (dv_arm4s,     [-0.15,  0.28, 1.63]),
    (dv_arm4e,     [-0.15,  0.28, 1.33]),
]
DV_TIPS = [
    (scalpel,    [-0.45, -0.30, 1.14]),
    (cauterizer, [-0.15, -0.30, 1.14]),
    (cam_arm,    [-0.30,  0.10, 1.14]),
    (retractor,  [-0.15,  0.30, 1.20]),
]

last_dv_x = 0.0
last_dv_y = 0.0
last_dv_z = 0.0

def update_davinci(dx, dy, dz):
    """Move entire da Vinci upper body: dx=side, dy=forward, dz=height."""
    for body,(ox,oy,oz) in DV_UPPER_PARTS:
        bb.resetBasePose(body,[ox+dx, oy+dy, oz+dz],[0,0,0,1])
    for body,(ox,oy,oz) in DV_TIPS:
        bb.resetBasePose(body,[ox+dx, oy+dy, oz+dz],[0,0,0,1])

# ═══════════════════════════════════════
# PANDA ARM
# ═══════════════════════════════════════
time.sleep(2.0)
robot = bb.loadURDF("panda.urdf", position=[-0.5,-1.1,0], fixedBase=True)
time.sleep(2.5)
for i,jp in enumerate([0,-0.5,0,-1.5,0,1.0,0]):
    bb.resetJointState(robot,i,jp)
time.sleep(0.5)
print("panda ok")

last_px = -0.5
last_py = -1.1

# ═══════════════════════════════════════
# HUMANOID ROBOT
# ═══════════════════════════════════════
HX,HY = PH_X, PH_Y+1.2
h_torso    = safe_body('box',[0.13,0.09,0.20],[HX,HY,0.78],0x224488)
safe_body('box',[0.13,0.09,0.06],[HX,HY,0.54],0x1A3366)
h_head     = safe_body('box',[0.09,0.09,0.10],[HX,HY,1.12],0xDDDDEE)
h_eye_l    = safe_body('box',[0.02,0.01,0.02],[HX-0.04,HY-0.09,1.15],0x0044FF)
h_eye_r    = safe_body('box',[0.02,0.01,0.02],[HX+0.04,HY-0.09,1.15],0x0044FF)
h_larm     = safe_body('box',[0.03,0.03,0.16],[HX-0.17,HY,0.78],0x224488)
h_rarm     = safe_body('box',[0.03,0.03,0.16],[HX+0.17,HY,0.78],0x224488)
h_lforearm = safe_body('box',[0.025,0.025,0.13],[HX-0.17,HY,0.52],0xDDDDEE)
h_rforearm = safe_body('box',[0.025,0.025,0.13],[HX+0.17,HY,0.52],0xDDDDEE)
h_lleg     = safe_body('box',[0.05,0.05,0.22],[HX-0.07,HY,0.22],0x1A3366)
h_rleg     = safe_body('box',[0.05,0.05,0.22],[HX+0.07,HY,0.22],0x1A3366)
h_lfoot    = safe_body('box',[0.05,0.09,0.03],[HX-0.07,HY-0.04,0.03],0x111111)
h_rfoot    = safe_body('box',[0.05,0.09,0.03],[HX+0.07,HY-0.04,0.03],0x111111)
time.sleep(0.5)
print("humanoid ok — bodies:", body_count)

# ═══════════════════════════════════════
# CONTROLS
# ═══════════════════════════════════════
bb.addDebugSlider('bed_height',     0.45, 0.25, 0.80)
bb.addDebugSlider('surgery_side',   0.0, -1.50, 1.50)
bb.addDebugSlider('surgery_fwd',    0.0, -1.50, 1.50)
bb.addDebugSlider('surgery_height', 0.0, -0.40, 0.60)
bb.addDebugSlider('panda_x',       -0.5, -2.50, 2.50)
bb.addDebugSlider('panda_y',       -1.1, -2.50, 1.50)
bb.addDebugSlider('panda_j0',       0.0, -2.8,  2.8)
bb.addDebugSlider('panda_j1',      -0.5, -1.7,  1.7)
bb.addDebugSlider('panda_j2',       0.0, -2.8,  2.8)
bb.addDebugSlider('panda_j3',      -1.5, -3.0,  0.0)
bb.addDebugSlider('panda_j4',       0.0, -2.8,  2.8)
bb.addDebugSlider('panda_j5',       1.0,  0.0,  3.7)
bb.addDebugSlider('panda_j6',       0.0, -2.8,  2.8)
bb.addDebugSlider('vac_speed',      0.04, 0.01, 0.15)
bb.addDebugSlider('surgery_spd',    0.04, 0.01, 0.12)
bb.addDebugSlider('humanoid_spd',   0.04, 0.01, 0.10)

bb.addDebugToggle('light_on')
bb.addDebugToggle('panda_manual')
bb.addDebugToggle('panda_inject')
bb.addDebugToggle('panda_medicine')
bb.addDebugToggle('vacuum_on')
bb.addDebugToggle('surgery_on')
bb.addDebugToggle('humanoid_run')
bb.addDebugToggle('humanoid_return')

# ═══════════════════════════════════════
# STATE
# ═══════════════════════════════════════
vac_pos      = [-2.5,-2.5,0.06]
vac_idx      = 0
vac_angle    = 0.0
VAC_WPS      = [
    [-2.5,-2.5,0.06],[ 2.5,-2.5,0.06],
    [ 2.5, 0.0,0.06],[-2.5, 0.0,0.06],
    [-2.5, 2.5,0.06],[ 2.5, 2.5,0.06],
    [ 0.0, 0.0,0.06],[-2.5,-2.5,0.06],
]
surgery_t     = 0.0
inject_frame  = 0
medicine_frame= 0
lights_on     = True
last_light    = True

DELIVER_WPS = [
    [PH_X-0.5, PH_Y+0.5],
    [R2X-0.5,  R2Y+1.5],
    [R2X-0.5,  R2Y+2.5],
    [-0.5,    -5.8],
    [-0.5,    -4.8],
    [-0.5,    -3.5],
    [-0.5,    -2.5],
    [-0.5,    -1.0],
    [-0.5,     0.5],
    [ 1.0,     0.8],
    [ 1.55,    0.75],
]
RETURN_WPS = [
    [ 1.0,     0.8],
    [-0.5,     0.5],
    [-0.5,    -1.0],
    [-0.5,    -2.5],
    [-0.5,    -3.5],
    [-0.5,    -4.8],
    [-0.5,    -5.8],
    [R2X-0.5, R2Y+2.5],
    [R2X-0.5, R2Y+1.5],
    [PH_X-0.5,PH_Y+0.5],
    [HX,      HY],
]
h_pos         = [HX, HY]
h_wp_idx      = 0
h_walk_i      = 0
h_carrying    = False
h_delivered   = False
h_ret_idx     = 0
h_pickup_done = False

# ═══════════════════════════════════════
# HUMANOID MOVE
# ═══════════════════════════════════════
def move_humanoid_simple(pos, target, speed, wi, carrying):
    cx,cy = pos
    tx,ty = target
    dx=tx-cx; dy=ty-cy
    dist=math.sqrt(dx*dx+dy*dy)
    if dist < 0.10:
        return pos, wi, True
    cx += speed*dx/dist
    cy += speed*dy/dist
    heading = math.atan2(dy,dx)
    q       = bb.getQuaternionFromEuler([0,0,heading])
    cos_h   = math.cos(heading)
    sin_h   = math.sin(heading)
    ls      =  math.sin(wi*0.45)*0.04
    rs      = -math.sin(wi*0.45)*0.04
    nod     =  math.sin(wi*0.9)*0.015
    bb.resetBasePose(h_torso,   [cx,cy,0.78], q)
    bb.resetBasePose(h_head,    [cx,cy,1.12+nod], q)
    bb.resetBasePose(h_eye_l,
        [cx-0.04*cos_h+0.09*sin_h,
         cy-0.04*sin_h-0.09*cos_h, 1.15+nod], q)
    bb.resetBasePose(h_eye_r,
        [cx+0.04*cos_h+0.09*sin_h,
         cy+0.04*sin_h-0.09*cos_h, 1.15+nod], q)
    bb.resetBasePose(h_larm,
        [cx-0.17*cos_h, cy-0.17*sin_h, 0.78+ls], q)
    bb.resetBasePose(h_rarm,
        [cx+0.17*cos_h, cy+0.17*sin_h, 0.78+rs], q)
    bb.resetBasePose(h_lforearm,
        [cx-0.17*cos_h, cy-0.17*sin_h, 0.52+ls], q)
    bb.resetBasePose(h_rforearm,
        [cx+0.17*cos_h, cy+0.17*sin_h, 0.52+rs], q)
    bb.resetBasePose(h_lleg,
        [cx-0.07*cos_h, cy-0.07*sin_h, 0.22+ls*0.5], q)
    bb.resetBasePose(h_rleg,
        [cx+0.07*cos_h, cy+0.07*sin_h, 0.22+rs*0.5], q)
    bb.resetBasePose(h_lfoot,
        [cx-0.07*cos_h, cy-0.07*sin_h, 0.03], q)
    bb.resetBasePose(h_rfoot,
        [cx+0.07*cos_h, cy+0.07*sin_h, 0.03], q)
    if carrying:
        bb.resetBasePose(medicine,[cx,cy,0.60],[0,0,0,1])
    return [cx,cy], wi+1, False

print("ALL READY")

# ═══════════════════════════════════════
# MAIN LOOP
# ═══════════════════════════════════════
while True:
    try:
        # ── LIGHTS ON / OFF ─────────────────────
        light_state = bb.readDebugParameter('light_on')
        if light_state != last_light:
            if light_state:
                bb.resetBasePose(light1, [0,    0,    2.98],[0,0,0,1])
                bb.resetBasePose(light2, [0,   -9.0,  2.98],[0,0,0,1])
                bb.resetBasePose(light3s,[0.5,  0.2,  2.80],[0,0,0,1])
            else:
                bb.resetBasePose(light1, [0,    0,    -5  ],[0,0,0,1])
                bb.resetBasePose(light2, [0,   -9.0,  -5  ],[0,0,0,1])
                bb.resetBasePose(light3s,[0.5,  0.2,  -5  ],[0,0,0,1])
            last_light = light_state

        # ── BED HEIGHT ──────────────────────────
        new_bz = bb.readDebugParameter('bed_height')
        if abs(new_bz - last_bz) > 0.005:
            build_bed(new_bz)
            build_patient(new_bz)
            last_bz = new_bz

        # ── DA VINCI — SIDE + FORWARD + HEIGHT ──
        new_dx = bb.readDebugParameter('surgery_side')
        new_dy = bb.readDebugParameter('surgery_fwd')
        new_dz = bb.readDebugParameter('surgery_height')
        if (abs(new_dx-last_dv_x) > 0.005 or
            abs(new_dy-last_dv_y) > 0.005 or
            abs(new_dz-last_dv_z) > 0.005):
            update_davinci(new_dx, new_dy, new_dz)
            last_dv_x = new_dx
            last_dv_y = new_dy
            last_dv_z = new_dz

        # ── PANDA POSITION ──────────────────────
        new_px = bb.readDebugParameter('panda_x')
        new_py = bb.readDebugParameter('panda_y')
        if abs(new_px-last_px) > 0.01 or abs(new_py-last_py) > 0.01:
            bb.resetBasePose(robot,[new_px,new_py,0],[0,0,0,1])
            last_px = new_px
            last_py = new_py

        # ── PANDA MANUAL JOINTS ─────────────────
        if bb.readDebugParameter('panda_manual'):
            for ji in range(7):
                val = bb.readDebugParameter(f'panda_j{ji}')
                bb.setJointMotorControl(robot,ji,targetPosition=val)

        # ── PANDA INJECT ────────────────────────
        elif bb.readDebugParameter('panda_inject'):
            inject_frame += 1
            c = inject_frame % 320
            if c < 80:
                t = c/80.0
                bb.setJointMotorControl(robot,0,targetPosition=0.5)
                bb.setJointMotorControl(robot,1,targetPosition=-0.3-t*0.3)
                bb.setJointMotorControl(robot,2,targetPosition=0.1)
                bb.setJointMotorControl(robot,3,targetPosition=-1.5+t*0.3)
                bb.setJointMotorControl(robot,5,targetPosition=1.2-t*0.4)
                bb.setJointMotorControl(robot,6,targetPosition=0.4)
            elif c < 140:
                push = math.sin((c-80)/60.0*math.pi)*0.05
                bb.setJointMotorControl(robot,3,targetPosition=-1.2+push)
            elif c < 220:
                bb.setJointMotorControl(robot,1,targetPosition=-0.5)
                bb.setJointMotorControl(robot,3,targetPosition=-1.5)
                bb.setJointMotorControl(robot,5,targetPosition=1.0)
            else:
                for i,jp in enumerate([0,-0.5,0,-1.5,0,1.0,0]):
                    bb.setJointMotorControl(robot,i,targetPosition=jp)
            lp = bb.getLinkPose(robot,10)
            if lp:
                ep = lp[0]
                bb.resetBasePose(syringe,
                    [ep[0],ep[1],ep[2]-0.08],[0,0,0,1])

        # ── PANDA MEDICINE DELIVERY ──────────────
        elif bb.readDebugParameter('panda_medicine'):
            medicine_frame += 1
            c = medicine_frame % 400
            if c < 60:
                t = c/60.0
                bb.setJointMotorControl(robot,0,targetPosition=-0.3)
                bb.setJointMotorControl(robot,1,targetPosition=-0.5+t*0.2)
                bb.setJointMotorControl(robot,2,targetPosition=0.2)
                bb.setJointMotorControl(robot,3,targetPosition=-1.8+t*0.3)
                bb.setJointMotorControl(robot,5,targetPosition=1.4)
                bb.setJointMotorControl(robot,6,targetPosition=0.0)
            elif c < 100:
                bb.setJointMotorControl(robot,1,targetPosition=-0.3)
                bb.setJointMotorControl(robot,3,targetPosition=-1.5)
            elif c < 180:
                t = (c-100)/80.0
                bb.setJointMotorControl(robot,0,targetPosition=-0.3+t*0.5)
                bb.setJointMotorControl(robot,1,targetPosition=-0.3-t*0.2)
                bb.setJointMotorControl(robot,3,targetPosition=-1.5+t*0.1)
                bb.setJointMotorControl(robot,5,targetPosition=1.4-t*0.4)
                lp = bb.getLinkPose(robot,10)
                if lp:
                    ep = lp[0]
                    bb.resetBasePose(medicine,
                        [ep[0],ep[1],ep[2]-0.06],[0,0,0,1])
            elif c < 260:
                t = (c-180)/80.0
                bb.setJointMotorControl(robot,1,targetPosition=-0.5-t*0.2)
                bb.setJointMotorControl(robot,3,targetPosition=-1.4+t*0.2)
                lp = bb.getLinkPose(robot,10)
                if lp:
                    ep = lp[0]
                    bb.resetBasePose(medicine,
                        [ep[0],ep[1],ep[2]-0.06],[0,0,0,1])
            elif c < 300:
                bb.resetBasePose(medicine,
                    [BED_X+0.05,BED_Y+0.10,last_bz+0.30],[0,0,0,1])
                bb.setJointMotorControl(robot,1,targetPosition=-0.4)
                bb.setJointMotorControl(robot,3,targetPosition=-1.6)
            elif c < 400:
                for i,jp in enumerate([0,-0.5,0,-1.5,0,1.0,0]):
                    bb.setJointMotorControl(robot,i,targetPosition=jp)
                if c > 380:
                    bb.resetBasePose(medicine,
                        medicine_drop_pos,[0,0,0,1])

        # ── VACUUM ──────────────────────────────
        if bb.readDebugParameter('vacuum_on'):
            spd = bb.readDebugParameter('vac_speed')
            tgt = VAC_WPS[vac_idx]
            dx  = tgt[0]-vac_pos[0]
            dy  = tgt[1]-vac_pos[1]
            d   = math.sqrt(dx*dx+dy*dy)
            if d < 0.10:
                vac_idx=(vac_idx+1)%len(VAC_WPS)
            else:
                vac_pos[0]+=spd*dx/d
                vac_pos[1]+=spd*dy/d
            vac_angle+=0.18
            bb.resetBasePose(vac_body,
                [vac_pos[0],vac_pos[1],0.06],
                bb.getQuaternionFromEuler([0,0,vac_angle]))
            bb.resetBasePose(vac_brush,
                [vac_pos[0],vac_pos[1],0.01],
                bb.getQuaternionFromEuler([0,0,vac_angle]))

        # ── DA VINCI SURGERY ANIMATION ───────────
        if bb.readDebugParameter('surgery_on'):
            spd = bb.readDebugParameter('surgery_spd')
            surgery_t += spd
            bz = last_bz + last_dv_z + 0.06
            dx = last_dv_x
            dy = last_dv_y
            bb.resetBasePose(scalpel,
                [0.5+dx+0.08*math.sin(surgery_t*0.85),
                 -0.06+dy+0.04*math.sin(surgery_t*1.3),
                 bz+0.02*math.cos(surgery_t*1.6)],
                bb.getQuaternionFromEuler(
                    [0,math.pi/10*math.sin(surgery_t),0]))
            bb.resetBasePose(cauterizer,
                [0.5+dx+0.06*math.sin(surgery_t*1.0+1.2),
                 0.04+dy+0.04*math.cos(surgery_t*1.2),
                 bz+0.05+0.025*abs(math.sin(surgery_t*2.0))],
                bb.getQuaternionFromEuler([0,0,surgery_t*0.35]))
            bb.resetBasePose(cam_arm,
                [0.5+dx+0.20*math.cos(surgery_t*0.20),
                 0.15*math.sin(surgery_t*0.20)+dy,
                 bz+0.38+0.03*math.sin(surgery_t*0.4)],
                bb.getQuaternionFromEuler(
                    [math.pi/10,0,surgery_t*0.10]))
            bb.resetBasePose(retractor,
                [0.5+dx+0.04*math.cos(surgery_t*0.65+1.8),
                 -0.14+dy+0.025*math.sin(surgery_t*0.85),
                 bz+0.015*math.sin(surgery_t*1.0)],
                bb.getQuaternionFromEuler([0,0,surgery_t*0.22]))
        else:
            dx = last_dv_x; dy = last_dv_y; dz = last_dv_z
            bb.resetBasePose(scalpel,
                [-0.45+dx,-0.30+dy,1.14+dz],[0,0,0,1])
            bb.resetBasePose(cauterizer,
                [-0.15+dx,-0.30+dy,1.14+dz],[0,0,0,1])
            bb.resetBasePose(cam_arm,
                [-0.30+dx, 0.10+dy,1.14+dz],[0,0,0,1])
            bb.resetBasePose(retractor,
                [-0.15+dx, 0.30+dy,1.20+dz],[0,0,0,1])

        # ── HUMANOID DELIVER ────────────────────
        if bb.readDebugParameter('humanoid_run') and not h_delivered:
            spd = bb.readDebugParameter('humanoid_spd')
            if not h_pickup_done:
                bb.resetBasePose(medicine,
                    [h_pos[0],h_pos[1],0.60],[0,0,0,1])
                h_carrying=True; h_pickup_done=True
            if h_wp_idx < len(DELIVER_WPS):
                target = DELIVER_WPS[h_wp_idx]
                h_pos,h_walk_i,reached = move_humanoid_simple(
                    h_pos,target,spd,h_walk_i,h_carrying)
                if reached:
                    h_wp_idx += 1
            else:
                bb.resetBasePose(medicine,
                    medicine_drop_pos,[0,0,0,1])
                h_carrying=False; h_delivered=True
                print("Humanoid: medicine delivered!")

        # ── HUMANOID RETURN ─────────────────────
        if bb.readDebugParameter('humanoid_return') and h_delivered:
            spd = bb.readDebugParameter('humanoid_spd')
            if h_ret_idx < len(RETURN_WPS):
                target = RETURN_WPS[h_ret_idx]
                h_pos,h_walk_i,reached = move_humanoid_simple(
                    h_pos,target,spd,h_walk_i,False)
                if reached:
                    h_ret_idx += 1
            else:
                h_delivered=False; h_wp_idx=0
                h_ret_idx=0; h_pickup_done=False
                bb.resetBasePose(medicine,
                    [PH_X,PH_Y,0.86],[0,0,0,1])
                print("Humanoid: back in pharmacy — ready!")

    except Exception as e:
        print("err:",e)

    time.sleep(0.01)
