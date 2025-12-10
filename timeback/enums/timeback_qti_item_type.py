"""QTI assessment item interaction type enum.

Used by:
- timeback/models/request/timeback_search_assessment_items_request.py
- timeback/models/timeback_qti_assessment_item.py
"""

from enum import Enum


class TimebackQTIItemType(str, Enum):
    """QTI assessment item interaction types.
    
    These types define the kind of interaction/question format
    that an assessment item uses.
    """
    
    CHOICE = "choice"
    TEXT_ENTRY = "text-entry"
    EXTENDED_TEXT = "extended-text"
    INLINE_CHOICE = "inline-choice"
    MATCH = "match"
    ORDER = "order"
    ASSOCIATE = "associate"
    SELECT_POINT = "select-point"
    GRAPHIC_ORDER = "graphic-order"
    GRAPHIC_ASSOCIATE = "graphic-associate"
    GRAPHIC_GAP_MATCH = "graphic-gap-match"
    HOTSPOT = "hotspot"
    HOTTEXT = "hottext"
    SLIDER = "slider"
    DRAWING = "drawing"
    MEDIA = "media"
    UPLOAD = "upload"

