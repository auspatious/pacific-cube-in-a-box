# OWS CFG refactored

Goal: Split mega single file ows_cfg.py into multiple manageable/maintainable config files.

## Structure

### root config

This file will act as an assembler which include all the layers required for the ows service. `maynooth_ows.py`

### Resuable

- legend definition
- resource limit definition
- custom functions

### deployment Groups

- ???

### Best practices

#### individual style

Each style definition for layers is to be declared following naming convention `style_*`

#### Grouping of styles

Some layers share common style definitions and in the configuration file they should be declared following naming convention `styles_*`

#### bands

Each product's bands definition is to be declared following naming convention `bands_*`

#### abstract

If several layers have long abstract move them to `abstract_*_cfg.py` and declared following naming convention `abstract_*`

### Resource Limit

Any unique resource limiting configuration should be declared in `ows_reslim_cfg.py` and be declared following naming convention `reslim_*`

### common legend definition

Reusable legend definition should be declared in `ows_legend_cfg.py` and be declared following naming convention `legend_*`
