import FreeCAD as App
import Part

try:
    import FreeCADGui as Gui
except Exception:
    Gui = None


# ============================================================
# WAREHOUSE RACK DESIGN - FREECAD PYTHON CONSOLE SCRIPT
# Units: millimeters
#
# Paste this entire file into the FreeCAD Python console.
# It creates three warehouse pallet racks, each with three storage
# levels. The model is intentionally structural/visual only.
# ============================================================


DOC_NAME = "FreeCAD_WHRackDesing_3_Racks_3_Levels"


# -----------------------------
# Rack dimensions
# -----------------------------

RACK_COUNT = 3
LEVEL_COUNT = 3

RACK_WIDTH = 3600.0
RACK_DEPTH = 1100.0
RACK_HEIGHT = 4200.0
RACK_GAP = 700.0

UPRIGHT_SIZE = 90.0
BEAM_HEIGHT = 140.0
BEAM_DEPTH = 90.0
SIDE_BRACE_SIZE = 45.0
DECK_THICKNESS = 55.0

LEVEL_ELEVATIONS = [900.0, 2300.0, 3700.0]

BASE_PLATE_SIZE = 220.0
BASE_PLATE_THICKNESS = 18.0


# -----------------------------
# Colors
# -----------------------------

UPRIGHT_COLOR = (0.05, 0.22, 0.65)
BEAM_COLOR = (0.95, 0.52, 0.08)
BRACE_COLOR = (0.15, 0.15, 0.15)
DECK_COLOR = (0.55, 0.58, 0.60)
BASE_COLOR = (0.08, 0.08, 0.08)
AISLE_COLOR = (0.25, 0.25, 0.25)


def add_box(doc, name, x, y, z, length, width, height, color, transparency=0):
    obj = doc.addObject("Part::Box", name)
    obj.Length = length
    obj.Width = width
    obj.Height = height
    obj.Placement.Base = App.Vector(x, y, z)

    if Gui is not None and getattr(obj, "ViewObject", None) is not None:
        obj.ViewObject.ShapeColor = color
        obj.ViewObject.Transparency = transparency

    return obj


def add_cylinder_between_points(doc, name, start, end, radius, color):
    direction = end.sub(start)
    length = direction.Length
    if length <= 0:
        raise RuntimeError("Brace length must be greater than zero.")

    cylinder = Part.makeCylinder(radius, length)
    z_axis = App.Vector(0, 0, 1)
    rotation = App.Rotation(z_axis, direction)
    cylinder.Placement = App.Placement(start, rotation)

    obj = doc.addObject("Part::Feature", name)
    obj.Shape = cylinder

    if Gui is not None and getattr(obj, "ViewObject", None) is not None:
        obj.ViewObject.ShapeColor = color

    return obj


def create_upright(doc, rack_name, x, y):
    add_box(
        doc,
        rack_name + "_Upright",
        x - UPRIGHT_SIZE / 2.0,
        y - UPRIGHT_SIZE / 2.0,
        0.0,
        UPRIGHT_SIZE,
        UPRIGHT_SIZE,
        RACK_HEIGHT,
        UPRIGHT_COLOR,
    )
    add_box(
        doc,
        rack_name + "_BasePlate",
        x - BASE_PLATE_SIZE / 2.0,
        y - BASE_PLATE_SIZE / 2.0,
        0.0,
        BASE_PLATE_SIZE,
        BASE_PLATE_SIZE,
        BASE_PLATE_THICKNESS,
        BASE_COLOR,
    )


def create_beam_level(doc, rack_name, origin_x, origin_y, level_z, level_index):
    front_y = origin_y
    back_y = origin_y + RACK_DEPTH
    left_x = origin_x
    right_x = origin_x + RACK_WIDTH

    beam_z = level_z
    beam_length = RACK_WIDTH + UPRIGHT_SIZE

    add_box(
        doc,
        "%s_Level_%d_Front_Beam" % (rack_name, level_index),
        left_x - UPRIGHT_SIZE / 2.0,
        front_y - BEAM_DEPTH / 2.0,
        beam_z,
        beam_length,
        BEAM_DEPTH,
        BEAM_HEIGHT,
        BEAM_COLOR,
    )
    add_box(
        doc,
        "%s_Level_%d_Back_Beam" % (rack_name, level_index),
        left_x - UPRIGHT_SIZE / 2.0,
        back_y - BEAM_DEPTH / 2.0,
        beam_z,
        beam_length,
        BEAM_DEPTH,
        BEAM_HEIGHT,
        BEAM_COLOR,
    )

    add_box(
        doc,
        "%s_Level_%d_Left_Depth_Beam" % (rack_name, level_index),
        left_x - BEAM_DEPTH / 2.0,
        front_y,
        beam_z,
        BEAM_DEPTH,
        RACK_DEPTH,
        BEAM_HEIGHT,
        BEAM_COLOR,
    )
    add_box(
        doc,
        "%s_Level_%d_Right_Depth_Beam" % (rack_name, level_index),
        right_x - BEAM_DEPTH / 2.0,
        front_y,
        beam_z,
        BEAM_DEPTH,
        RACK_DEPTH,
        BEAM_HEIGHT,
        BEAM_COLOR,
    )

    deck_margin = 140.0
    add_box(
        doc,
        "%s_Level_%d_WireDeck_Visual" % (rack_name, level_index),
        left_x + deck_margin,
        front_y + deck_margin,
        beam_z + BEAM_HEIGHT,
        RACK_WIDTH - deck_margin * 2.0,
        RACK_DEPTH - deck_margin * 2.0,
        DECK_THICKNESS,
        DECK_COLOR,
        transparency=35,
    )


def create_side_braces(doc, rack_name, origin_x, origin_y):
    front_y = origin_y
    back_y = origin_y + RACK_DEPTH
    left_x = origin_x
    right_x = origin_x + RACK_WIDTH

    brace_pairs = [
        (left_x, front_y, left_x, back_y),
        (right_x, front_y, right_x, back_y),
    ]

    brace_index = 1
    for x1, y1, x2, y2 in brace_pairs:
        for bottom_z, top_z in [(200.0, 2100.0), (2100.0, 4000.0)]:
            add_cylinder_between_points(
                doc,
                "%s_SideBrace_%02d_A" % (rack_name, brace_index),
                App.Vector(x1, y1, bottom_z),
                App.Vector(x2, y2, top_z),
                SIDE_BRACE_SIZE / 2.0,
                BRACE_COLOR,
            )
            brace_index += 1
            add_cylinder_between_points(
                doc,
                "%s_SideBrace_%02d_B" % (rack_name, brace_index),
                App.Vector(x1, y2, bottom_z),
                App.Vector(x2, y1, top_z),
                SIDE_BRACE_SIZE / 2.0,
                BRACE_COLOR,
            )
            brace_index += 1


def create_rack(doc, rack_number, origin_x, origin_y):
    rack_name = "Rack_%02d" % rack_number

    upright_points = [
        (origin_x, origin_y),
        (origin_x + RACK_WIDTH, origin_y),
        (origin_x, origin_y + RACK_DEPTH),
        (origin_x + RACK_WIDTH, origin_y + RACK_DEPTH),
    ]

    for x, y in upright_points:
        create_upright(doc, rack_name, x, y)

    for level_index, level_z in enumerate(LEVEL_ELEVATIONS, start=1):
        create_beam_level(doc, rack_name, origin_x, origin_y, level_z, level_index)

    create_side_braces(doc, rack_name, origin_x, origin_y)


def create_floor_reference(doc):
    total_width = RACK_COUNT * RACK_WIDTH + (RACK_COUNT - 1) * RACK_GAP
    floor_margin = 600.0

    add_box(
        doc,
        "Floor_Aisle_Reference",
        -floor_margin,
        -floor_margin,
        -12.0,
        total_width + floor_margin * 2.0,
        RACK_DEPTH + floor_margin * 2.0,
        12.0,
        AISLE_COLOR,
        transparency=80,
    )


def rebuild_document():
    for name in list(App.listDocuments().keys()):
        if name.startswith(DOC_NAME):
            App.closeDocument(name)

    doc = App.newDocument(DOC_NAME)
    create_floor_reference(doc)

    for rack_index in range(RACK_COUNT):
        origin_x = rack_index * (RACK_WIDTH + RACK_GAP)
        create_rack(doc, rack_index + 1, origin_x, 0.0)

    doc.recompute()

    if Gui is not None and getattr(Gui, "ActiveDocument", None) is not None:
        Gui.ActiveDocument.ActiveView.viewAxometric()
        Gui.SendMsgToActiveView("ViewFit")

    expected_rack_objects = RACK_COUNT * (
        8 + LEVEL_COUNT * 5 + 8
    )
    print("")
    print("Warehouse rack model created.")
    print("Racks: %d" % RACK_COUNT)
    print("Levels per rack: %d" % LEVEL_COUNT)
    print("Rack width: %.0f mm" % RACK_WIDTH)
    print("Rack depth: %.0f mm" % RACK_DEPTH)
    print("Rack height: %.0f mm" % RACK_HEIGHT)
    print("Expected rack structural objects: %d" % expected_rack_objects)
    print("Total document objects: %d" % len(doc.Objects))

    return doc


rebuild_document()
