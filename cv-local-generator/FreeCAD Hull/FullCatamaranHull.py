import math

import FreeCAD as App
import Part

try:
    import FreeCADGui as Gui
except Exception:
    Gui = None


# ============================================================
# CATAMARAN HULL ONLY - FREECAD PYTHON CONSOLE SCRIPT
# Units: millimeters
#
# Paste this entire file into the FreeCAD Python console.
# It creates two closed lofted hulls, no bridge deck, no rigging,
# no cabin, no furniture, no non-hull structure.
# ============================================================


# -----------------------------
# Main dimensions
# -----------------------------

DOC_NAME = "Catamaran_Hull_Only"

LENGTH = 12000.0
HULL_BEAM = 1200.0
OVERALL_BEAM = 6000.0
MAX_DRAFT = 1200.0

STATION_COUNT = 19
SHOW_STATION_FRAMES = True
SHOW_LONGITUDINAL_GUIDES = True

HULL_CENTER_SPACING = OVERALL_BEAM - HULL_BEAM
PORT_CENTER_Y = -HULL_CENTER_SPACING / 2.0
STARBOARD_CENTER_Y = HULL_CENTER_SPACING / 2.0


# -----------------------------
# Utility functions
# -----------------------------

def clamp(value, low, high):
    return max(low, min(high, value))


def station_t(index):
    return index / float(STATION_COUNT - 1)


def longitudinal_fullness(t):
    """
    Smooth fullness curve: narrow at bow/stern and fuller near midship.
    The minimum prevents the loft from collapsing into a numerical point.
    """
    wave = math.sin(math.pi * clamp(t, 0.0, 1.0))
    return 0.10 + 0.90 * (wave ** 0.72)


def beam_at(t):
    return HULL_BEAM * longitudinal_fullness(t)


def draft_at(t):
    wave = math.sin(math.pi * clamp(t, 0.0, 1.0))
    return MAX_DRAFT * (0.16 + 0.84 * (wave ** 0.92))


def keel_z_at(t):
    """
    Rockered keel: shallow at bow/stern, deepest around midship.
    Z is negative below the waterline/sheer reference plane.
    """
    return -draft_at(t)


def sheer_z_at(t):
    """
    Slight sheer rise toward the ends.
    Keeps the top edge from looking mechanically flat.
    """
    end_lift = abs(2.0 * t - 1.0)
    return 70.0 * (end_lift ** 1.6)


def x_at(t):
    return LENGTH * t


def make_bspline_edge(points, closed=False):
    curve = Part.BSplineCurve()
    curve.interpolate(points, closed)
    return curve.toShape()


def make_open_bspline(points):
    return make_bspline_edge(points, closed=False)


def make_closed_profile(points):
    edge = make_bspline_edge(points, closed=True)
    wire = Part.Wire([edge])
    if not wire.isClosed():
        raise RuntimeError("Generated station profile is not closed.")
    return wire


def add_shape(doc, name, shape, color, transparency=0, line_width=2):
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = shape

    if Gui is not None and getattr(obj, "ViewObject", None) is not None:
        obj.ViewObject.ShapeColor = color
        obj.ViewObject.LineColor = color
        obj.ViewObject.LineWidth = line_width
        obj.ViewObject.Transparency = transparency

    return obj


# -----------------------------
# Hull geometry
# -----------------------------

def station_profile_points(center_y, t):
    """
    Returns one closed transverse section in the Y/Z plane at a station.

    The points run port-side sheer -> keel -> starboard-side sheer -> top
    closure. The top closure exists only to make the hull a valid closed
    lofted solid.
    """
    x = x_at(t)
    half_beam = beam_at(t) / 2.0
    draft = draft_at(t)
    keel_z = keel_z_at(t)
    sheer_z = sheer_z_at(t)

    return [
        App.Vector(x, center_y - half_beam * 0.95, sheer_z),
        App.Vector(x, center_y - half_beam * 0.82, -draft * 0.10),
        App.Vector(x, center_y - half_beam * 0.56, -draft * 0.42),
        App.Vector(x, center_y - half_beam * 0.26, -draft * 0.78),
        App.Vector(x, center_y, keel_z),
        App.Vector(x, center_y + half_beam * 0.26, -draft * 0.78),
        App.Vector(x, center_y + half_beam * 0.56, -draft * 0.42),
        App.Vector(x, center_y + half_beam * 0.82, -draft * 0.10),
        App.Vector(x, center_y + half_beam * 0.95, sheer_z),
        App.Vector(x, center_y + half_beam * 0.45, sheer_z + 55.0),
        App.Vector(x, center_y, sheer_z + 85.0),
        App.Vector(x, center_y - half_beam * 0.45, sheer_z + 55.0),
    ]


def create_hull(doc, center_y, name, hull_color):
    station_wires = []
    station_shapes = []

    keel_points = []
    port_sheer_points = []
    starboard_sheer_points = []
    port_chine_points = []
    starboard_chine_points = []

    for index in range(STATION_COUNT):
        t = station_t(index)
        profile_points = station_profile_points(center_y, t)
        wire = make_closed_profile(profile_points)
        station_wires.append(wire)

        half_beam = beam_at(t) / 2.0
        draft = draft_at(t)
        x = x_at(t)

        keel_points.append(App.Vector(x, center_y, keel_z_at(t)))
        port_sheer_points.append(App.Vector(x, center_y - half_beam * 0.95, sheer_z_at(t)))
        starboard_sheer_points.append(App.Vector(x, center_y + half_beam * 0.95, sheer_z_at(t)))
        port_chine_points.append(App.Vector(x, center_y - half_beam * 0.48, -draft * 0.56))
        starboard_chine_points.append(App.Vector(x, center_y + half_beam * 0.48, -draft * 0.56))

        if SHOW_STATION_FRAMES:
            station_shapes.append(wire)

    loft_shape = Part.makeLoft(station_wires, True, False, False, 5)
    hull = add_shape(doc, name, loft_shape, hull_color, transparency=12, line_width=1)

    if SHOW_STATION_FRAMES:
        compound = Part.Compound(station_shapes)
        add_shape(doc, name + "_Station_Frames", compound, (0.05, 0.20, 0.85), transparency=0, line_width=2)

    if SHOW_LONGITUDINAL_GUIDES:
        guides = [
            make_open_bspline(keel_points),
            make_open_bspline(port_sheer_points),
            make_open_bspline(starboard_sheer_points),
            make_open_bspline(port_chine_points),
            make_open_bspline(starboard_chine_points),
        ]
        guide_compound = Part.Compound(guides)
        add_shape(doc, name + "_Guide_Lines", guide_compound, (0.90, 0.10, 0.05), transparency=0, line_width=3)

    return hull


def create_centerline_reference(doc):
    points = [
        App.Vector(0.0, 0.0, 250.0),
        App.Vector(LENGTH, 0.0, 250.0),
    ]
    add_shape(
        doc,
        "Catamaran_Centerline_Reference",
        make_open_bspline(points),
        (0.45, 0.45, 0.45),
        transparency=0,
        line_width=1,
    )


def rebuild_document():
    for name in list(App.listDocuments().keys()):
        if name.startswith(DOC_NAME):
            App.closeDocument(name)

    doc = App.newDocument(DOC_NAME)

    port_hull = create_hull(doc, PORT_CENTER_Y, "Port_Hull", (0.10, 0.38, 0.95))
    starboard_hull = create_hull(doc, STARBOARD_CENTER_Y, "Starboard_Hull", (0.10, 0.38, 0.95))
    create_centerline_reference(doc)

    doc.recompute()

    if Gui is not None and getattr(Gui, "ActiveDocument", None) is not None:
        Gui.ActiveDocument.ActiveView.viewAxometric()
        Gui.SendMsgToActiveView("ViewFit")

    print("")
    print("Catamaran hull-only model created.")
    print("Length: %.0f mm" % LENGTH)
    print("Single hull beam: %.0f mm" % HULL_BEAM)
    print("Overall beam: %.0f mm" % OVERALL_BEAM)
    print("Center spacing: %.0f mm" % HULL_CENTER_SPACING)
    print("Max draft: %.0f mm" % MAX_DRAFT)
    print("Stations per hull: %d" % STATION_COUNT)
    print("Port hull valid: %s, solids: %d" % (port_hull.Shape.isValid(), len(port_hull.Shape.Solids)))
    print("Starboard hull valid: %s, solids: %d" % (starboard_hull.Shape.isValid(), len(starboard_hull.Shape.Solids)))
    print("Objects: two lofted closed hull solids plus optional hull guide curves.")

    return doc


rebuild_document()
