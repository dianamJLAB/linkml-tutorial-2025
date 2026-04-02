

# Slot: instrument_type_signals 


_Instrument-type-specific signal definition groups keyed by device type._





URI: [https://w3id.org/narad_linkml/schema/narad/schema/instrument_type_signals](https://w3id.org/narad_linkml/schema/narad/schema/instrument_type_signals)
Alias: instrument_type_signals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SignalDefinitions](SignalDefinitions.md) | Grouped EPICS signal suffix templates by semantic category |  no  |






## Properties

* Range: [DeviceTypeSignalSet](DeviceTypeSignalSet.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/instrument_type_signals |
| native | https://w3id.org/narad_linkml/schema/narad/schema/instrument_type_signals |




## LinkML Source

<details>
```yaml
name: instrument_type_signals
description: Instrument-type-specific signal definition groups keyed by device type.
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
rank: 1000
alias: instrument_type_signals
domain_of:
- SignalDefinitions
range: DeviceTypeSignalSet
multivalued: true
inlined: true

```
</details>