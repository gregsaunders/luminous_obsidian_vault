---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 4.8: Map Component

**Required By:** [[../../Luminous/LUM-EPIC-02-Unified-Water-Quality-Data-Model/00-Unified-Water-Quality-Data-Model|LUM-EPIC-02]] - Water Quality Dashboard Views

## Outcome

A reusable map component for displaying geographic data with markers, layers, and interactive features.

## What Success Looks Like

- Developer can add a map widget with minimal code
- Map supports marker layers from GeoJSON data sources
- Users can pan, zoom, and click markers to see details
- Map handles loading states and error conditions gracefully
- Works across desktop, mobile, and web platforms

## Context

Geographic visualization is needed across multiple Platform Groups:
- **Luminous**: Water quality monitoring station locations
- **Operations**: Asset locations, service territories
- **Field Services**: Work order locations, route planning

This is a platform-level component to avoid duplicating map implementations.

**Used By:**
- [[../../Luminous/LUM-EPIC-02-Unified-Water-Quality-Data-Model/00-Unified-Water-Quality-Data-Model|LUM-EPIC-02]] Feature 2.6 - Station map visualization

## Technology Options

| Option | Pros | Cons |
|--------|------|------|
| **flutter_map** | Open source, Leaflet-based, active community | Requires tile provider setup |
| **google_maps_flutter** | Feature-rich, familiar UX | API key required, usage costs |
| **mapbox_gl** | Beautiful styling, offline support | API key required, commercial license |

**Recommendation:** Start with `flutter_map` + OpenStreetMap tiles for cost-free development; evaluate Mapbox for production if styling needs exceed OSM capabilities.

## Scope: Owned Files

- `frontend/flutter/packages/ui/lib/components/map/`
- `frontend/flutter/packages/ui/lib/components/map/map_widget.dart`
- `frontend/flutter/packages/ui/lib/components/map/map_marker.dart`
- `frontend/flutter/packages/ui/lib/components/map/map_layer.dart`
- `frontend/flutter/packages/ui/lib/components/map/map_controls.dart`
- `frontend/flutter/packages/ui/lib/components/map/geojson_layer.dart`

## Requirements

**Core Map:**
- Map widget accepts configurable tile provider
- Initial center/zoom can be set via props or auto-fits to markers
- Pan and zoom interactions work with mouse, touch, and scroll
- Loading state shows placeholder while tiles load
- Error state displays when tile loading fails

**Markers:**
- Marker component accepts customizable icons
- Dense point data clusters automatically
- Marker popup/tooltip appears on tap
- Selected markers show highlighted state
- Markers can bind arbitrary data for popup display

**Layers:**
- GeoJSON layer renders polygon/line/point data
- Layer toggle controls show/hide individual layers
- Layers are styleable (fill color, stroke, opacity)
- Choropleth coloring reflects data values
- Layer legend component explains symbology

**Controls:**
- Zoom in/out buttons are accessible
- Fit-to-bounds button resets view to show all data
- Layer switcher panel manages layer visibility
- Scale bar shows distance reference
- Attribution displays tile provider credits

**Data Integration:**
- GeoJSON data sources bind to layers
- Markers update dynamically without full re-render
- Markers can be filtered by data attributes
- Bounds-based loading fetches only visible area data

**Responsive Behavior:**
- Mobile touch gestures work (pinch zoom, two-finger pan)
- Controls are compact on mobile viewport
- Full-screen toggle expands map to fill screen
