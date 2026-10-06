"""Which sibling themes become Style Settings variants of this one."""

ID = "borozdov-palette"  # Style Settings section id and the body-class prefix
NAME = "Borozdov Palette"
DEFAULT_LABEL = "Palette"

# (repository folder next to this one, label in the Variant menu)
MEMBERS = [
    ("recess", "Recess"),
    ("doodle", "Doodle"),
    ("swatch", "Swatch"),
    ("cirrus", "Cirrus"),
    ("pop", "Pop"),
    ("agenda", "Agenda"),
    ("cork", "Cork"),
    ("clipboard", "Clipboard"),
    ("keepsake", "Keepsake"),
    ("copybook", "Copybook"),
    ("sonnet", "Sonnet"),
    ("flashcard", "Flashcard"),
    ("almanac", "Almanac"),
    ("crayon", "Crayon"),
    ("marker", "Marker"),
    ("passport", "Passport"),
    ("hush", "Hush"),
    ("hive", "Hive"),
    ("whiteboard", "Whiteboard"),
]

# Palette names of this theme that no Obsidian variable reads in section 3:
# which of the sibling's resolved variables to take for them instead.
ALIASES = {
    "--highlight-text": "--text-normal",
}

# The palette name the highlight rule colours its text with: the generator
# picks whichever of the sibling's text and canvas reads on its highlight.
MARK_TEXT = "--highlight-text"
