

# Slot: signal_bindings 


_Signal definitions keyed by signal name within a device type._





URI: [https://w3id.org/narad_linkml/schema/narad/schema/signal_bindings](https://w3id.org/narad_linkml/schema/narad/schema/signal_bindings)
Alias: signal_bindings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeviceTypeSignalSet](DeviceTypeSignalSet.md) | Signal binding set scoped to a device type (for example, Quadrupole or BPM) |  no  |
| [ElementNaradRef](ElementNaradRef.md) | NARAD semantic reference block attached to a beamline element |  yes  |






## Properties

* Range: [SignalBinding](SignalBinding.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/signal_bindings |
| native | https://w3id.org/narad_linkml/schema/narad/schema/signal_bindings |




## LinkML Source

<details>
```yaml
name: signal_bindings
description: Signal definitions keyed by signal name within a device type.
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
rank: 1000
alias: signal_bindings
domain_of:
- DeviceTypeSignalSet
- ElementNaradRef
range: SignalBinding
multivalued: true
inlined: true

```
</details>