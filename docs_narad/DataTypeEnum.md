# Enum: DataTypeEnum 




_Allowed data types for signal values._



URI: [https://w3id.org/narad_linkml/schema/narad/schema/DataTypeEnum](https://w3id.org/narad_linkml/schema/narad/schema/DataTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| None | ncit:C45255 | A special value that may represent an unknown, missing, not applicable, or un... |
| int | ncit:C47840 | A data type comprised of numbers with no fractional part, including negative ... |
| float | ncit:C48150 | A number that can have its decimal point in any position |
| double | ncit:C48870 | A 64-bit floating-point value |
| string | ncit:C45253 | A sequence of characters used to represent text |
| boolean | ncit:C45254 | A data type with two possible values: true and false |
| boolean_non_null | ncit:C95630 | A two-value boolean data type that does not include null flavor |
| date | ncit:C48871 | A calendar date (year, month, day) |
| coded_value | ncit:C95637 | A code value referenced from an external coding system or ontology |




## Slots

| Name | Description |
| ---  | --- |
| [data_type](data_type.md) | The data type of the signal's value |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema






## LinkML Source

<details>
```yaml
name: DataTypeEnum
description: Allowed data types for signal values.
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
rank: 1000
permissible_values:
  None:
    text: None
    description: A special value that may represent an unknown, missing, not applicable,
      or undefined value.
    meaning: ncit:C45255
  int:
    text: int
    description: A data type comprised of numbers with no fractional part, including
      negative and positive values.
    meaning: ncit:C47840
  float:
    text: float
    description: A number that can have its decimal point in any position.
    meaning: ncit:C48150
  double:
    text: double
    description: A 64-bit floating-point value.
    meaning: ncit:C48870
  string:
    text: string
    description: A sequence of characters used to represent text.
    meaning: ncit:C45253
  boolean:
    text: boolean
    description: 'A data type with two possible values: true and false.'
    meaning: ncit:C45254
  boolean_non_null:
    text: boolean_non_null
    description: A two-value boolean data type that does not include null flavor.
    meaning: ncit:C95630
  date:
    text: date
    description: A calendar date (year, month, day).
    meaning: ncit:C48871
  coded_value:
    text: coded_value
    description: A code value referenced from an external coding system or ontology.
    meaning: ncit:C95637

```
</details>